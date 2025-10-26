"""
Flask Backend API for Customer Churn Prediction Dashboard
"""

from flask import Flask, jsonify, render_template, send_from_directory
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import json

app = Flask(__name__)

# Global variables to store models and data
models = {}
data_cache = {}

def load_and_preprocess_data():
    """Load and preprocess data once"""
    if 'df' in data_cache:
        return data_cache['df'], data_cache['X'], data_cache['y']
    
    print("Loading data...")
    df = pd.read_csv('customer_data.csv')
    
    # Preprocess
    categorical_cols = ['gender', 'city_tier', 'multiple_lines', 'internet_service',
                       'contract_type', 'paperless_billing', 'payment_method',
                       'international_plan', 'voicemail_plan', 'churned']
    
    for col in categorical_cols:
        if col in df.columns:
            le = LabelEncoder()
            df[col + '_encoded'] = le.fit_transform(df[col].astype(str))
    
    df['churn_label'] = (df['churned'] == 'Yes').astype(int)
    
    # Select features
    feature_cols = ['age', 'tenure_months', 'total_day_calls', 'total_eve_calls',
                   'total_night_calls', 'total_day_minutes', 'total_eve_minutes',
                   'total_night_minutes', 'total_day_charge', 'total_eve_charge',
                   'total_night_charge', 'total_monthly_charge', 'customer_service_calls',
                   'international_calls', 'voicemail_messages', 'total_data_usage_gb']
    
    available_features = [col for col in feature_cols if col in df.columns]
    X = df[available_features].copy()
    y = df['churn_label']
    
    # Cache
    data_cache['df'] = df
    data_cache['X'] = X
    data_cache['y'] = y
    
    return df, X, y

def train_models():
    """Train models and cache them"""
    if models:
        return models
    
    print("Training models...")
    df, X, y = load_and_preprocess_data()
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Random Forest
    rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    rf.fit(X_train_scaled, y_train)
    
    # Gradient Boosting
    gb = GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42)
    gb.fit(X_train_scaled, y_train)
    
    # Evaluate
    y_pred_rf = rf.predict(X_test_scaled)
    y_pred_gb = gb.predict(X_test_scaled)
    
    models['rf'] = rf
    models['gb'] = gb
    models['scaler'] = scaler
    models['X_test'] = X_test_scaled
    models['y_test'] = y_test
    
    return models

def get_clusters():
    """Perform clustering"""
    if 'clusters' in data_cache:
        return data_cache['clusters']
    
    df, X, y = load_and_preprocess_data()
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)
    
    data_cache['clusters'] = clusters
    data_cache['kmeans'] = kmeans
    
    return clusters

@app.route('/')
def index():
    """Serve main page"""
    return render_template('index.html')

@app.route('/api/data/overview')
def api_overview():
    """Get data overview"""
    df, X, y = load_and_preprocess_data()
    
    total = len(df)
    churned = df['churn_label'].sum()
    churn_rate = (churned / total) * 100
    
    # Calculate averages
    avg_monthly_charge = df['total_monthly_charge'].mean()
    avg_tenure = df['tenure_months'].mean()
    avg_age = df['age'].mean()
    
    return jsonify({
        'total_customers': total,
        'churned_customers': int(churned),
        'churn_rate': round(churn_rate, 2),
        'avg_monthly_charge': round(avg_monthly_charge, 2),
        'avg_tenure': round(avg_tenure, 1),
        'avg_age': round(avg_age, 1)
    })

@app.route('/api/models/train')
def api_train_models():
    """Train and return model metrics"""
    train_models()
    
    rf = models['rf']
    gb = models['gb']
    y_test = models['y_test']
    X_test = models['X_test']
    
    # Random Forest metrics
    y_pred_rf = rf.predict(X_test)
    y_proba_rf = rf.predict_proba(X_test)[:, 1]
    
    rf_metrics = {
        'accuracy': float(accuracy_score(y_test, y_pred_rf)),
        'precision': float(precision_score(y_test, y_pred_rf)),
        'recall': float(recall_score(y_test, y_pred_rf)),
        'f1_score': float(f1_score(y_test, y_pred_rf)),
        'auc_roc': float(roc_auc_score(y_test, y_proba_rf)),
        'confusion_matrix': confusion_matrix(y_test, y_pred_rf).tolist()
    }
    
    # Gradient Boosting metrics
    y_pred_gb = gb.predict(X_test)
    y_proba_gb = gb.predict_proba(X_test)[:, 1]
    
    gb_metrics = {
        'accuracy': float(accuracy_score(y_test, y_pred_gb)),
        'precision': float(precision_score(y_test, y_pred_gb)),
        'recall': float(recall_score(y_test, y_pred_gb)),
        'f1_score': float(f1_score(y_test, y_pred_gb)),
        'auc_roc': float(roc_auc_score(y_test, y_proba_gb)),
        'confusion_matrix': confusion_matrix(y_test, y_pred_gb).tolist()
    }
    
    return jsonify({
        'random_forest': rf_metrics,
        'gradient_boosting': gb_metrics
    })

@app.route('/api/models/feature-importance')
def api_feature_importance():
    """Get feature importance"""
    models_data = train_models()
    rf = models['rf']
    df, X, y = load_and_preprocess_data()
    
    importance = pd.DataFrame({
        'feature': X.columns,
        'importance': rf.feature_importances_
    }).sort_values('importance', ascending=False)
    
    top_10 = importance.head(10)
    
    return jsonify({
        'features': top_10['feature'].tolist(),
        'importance': top_10['importance'].tolist()
    })

@app.route('/api/clustering/segments')
def api_clustering():
    """Get clustering results"""
    clusters = get_clusters()
    df, X, y = load_and_preprocess_data()
    
    df['cluster'] = clusters
    
    # Get cluster stats
    cluster_stats = []
    for i in range(5):
        cluster_df = df[df['cluster'] == i]
        total = len(cluster_df)
        churned = cluster_df['churn_label'].sum()
        churn_rate = (churned / total * 100) if total > 0 else 0
        
        cluster_stats.append({
            'cluster': i,
            'size': total,
            'percentage': round((total / len(df)) * 100, 2),
            'churn_rate': round(churn_rate, 2),
            'churned': int(churned),
            'avg_tenure': round(cluster_df['tenure_months'].mean(), 1),
            'avg_monthly_charge': round(cluster_df['total_monthly_charge'].mean(), 2),
            'avg_service_calls': round(cluster_df['customer_service_calls'].mean(), 1),
            'avg_age': round(cluster_df['age'].mean(), 1)
        })
    
    return jsonify({'clusters': cluster_stats})

@app.route('/api/pca/results')
def api_pca():
    """Get PCA results"""
    df, X, y = load_and_preprocess_data()
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    pca = PCA(n_components=10)
    X_pca = pca.fit_transform(X_scaled)
    
    explained_variance = pca.explained_variance_ratio_ * 100
    cumulative = np.cumsum(explained_variance)
    
    components = []
    for i in range(10):
        components.append({
            'component': f'PC{i+1}',
            'variance': round(explained_variance[i], 2),
            'cumulative': round(cumulative[i], 2)
        })
    
    return jsonify({
        'components': components,
        'total_variance': round(cumulative[-1], 2)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

