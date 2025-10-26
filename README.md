# Customer Churn Prediction and Segmentation

## 📊 Project Overview

This project implements a comprehensive **Customer Churn Prediction and Segmentation** system using machine learning. The system predicts customer churn using classification models (Random Forest and Gradient Boosting) and performs customer segmentation using K-Means clustering and PCA for dimensionality reduction.

### Key Features

- ✅ **Churn Prediction**: Uses Random Forest and Gradient Boosting classifiers
- ✅ **Customer Segmentation**: K-Means clustering to identify distinct groups
- ✅ **Dimensionality Reduction**: PCA for feature space optimization
- ✅ **Interactive Dashboard**: Beautiful web interface with HTML/CSS/JavaScript
- ✅ **RESTful API**: Flask backend for data processing
- ✅ **Comprehensive Analysis**: Statistical insights and visualizations

### Dataset

The project uses a **synthetic telecom customer dataset** with 10,000+ records containing:
- Customer demographics (age, gender, city tier)
- Service features (internet, TV, security, support)
- Usage patterns (calls, minutes, data usage)
- Charges and billing information
- Customer service interactions
- Churn status (target variable)

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate dataset** (if not already present):
   ```bash
   python generate_data.py
   ```

3. **Start the web application**:
   ```bash
   python app_flask.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
bdmla/
├── app_flask.py                  # Flask backend API
├── generate_data.py              # Dataset generator
├── customer_data.csv             # Generated dataset
├── churn_analysis_results.png    # Visualization output
├── templates/
│   └── index.html                # Frontend HTML
├── static/
│   ├── style.css                 # Frontend styling
│   └── script.js                 # Frontend JavaScript
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

## 💻 Usage

### Web Application (Recommended)

Run the interactive web dashboard:

```bash
python app_flask.py
```

Then open `http://localhost:5000` in your browser.

**Features:**
- 📊 Interactive dashboard with real-time metrics
- 🤖 Train and evaluate ML models (Random Forest & Gradient Boosting)
- 🎯 Customer segmentation analysis with K-Means clustering
- 📈 PCA dimensionality reduction visualization
- 📉 Feature importance charts
- 🎨 Beautiful responsive UI with gradient designs

### Command Line Analysis (Alternative)

For a quick analysis without the web interface:

```bash
python run_churn_analysis.py
```

This generates:
- Model performance metrics
- Clustering analysis
- PCA results
- Visualization saved as `churn_analysis_results.png`

## 📈 Expected Results

### Model Performance

- **Random Forest**: ~69% accuracy, ~0.77 AUC-ROC
- **Gradient Boosting**: ~69% accuracy, ~0.77 AUC-ROC
- **Precision & Recall**: Balanced metrics for churn prediction

### Customer Segments

The K-Means clustering identifies **5 distinct segments**:

| Cluster | Size | Churn Rate | Characteristics |
|---------|------|------------|-----------------|
| 0 | 2,660 (26.6%) | 52.6% | High service calls, older customers |
| 1 | 1,493 (14.9%) | 50.6% | Medium tenure, average charges |
| 2 | 2,431 (24.3%) | **55.0%** 🔴 | **Highest risk**, highest charges |
| 3 | 2,356 (23.6%) | 48.5% | Lowest risk, fewer service issues |
| 4 | 1,060 (10.6%) | 53.6% | Price-sensitive segment |

### Key Insights

- **Top Churn Predictors**: Customer service calls (21.5%), tenure (14.2%), monthly charges (14.1%)
- **High Churn Contracts**: Month-to-month contracts show 65.6% churn rate
- **Protective Factors**: Longer tenure reduces churn probability
- **PCA Performance**: Retains 64% variance with 10 principal components

## 🎯 Web Dashboard Features

### 1. Dashboard Tab
- Overview metrics (total customers, churn rate, average charges)
- Churn distribution pie chart
- Contract type analysis

### 2. ML Models Tab
- Train Random Forest and Gradient Boosting models
- Real-time performance metrics
- Confusion matrices
- Top 10 feature importance visualization

### 3. Clustering Tab
- Customer segmentation with K-Means
- 5 cluster cards with detailed statistics
- Cluster distribution chart
- Churn rate analysis by cluster

### 4. Analytics Tab
- Principal Component Analysis (PCA)
- Variance explained by components
- Cumulative variance chart
- Key business insights

## 🔧 Technical Details

### Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **ML Libraries**: scikit-learn
- **Charts**: Chart.js
- **Data**: pandas, numpy

### Algorithms

1. **Random Forest**: 100 trees, max depth 10
2. **Gradient Boosting**: 100 estimators, max depth 5
3. **K-Means**: 5 clusters, random state 42
4. **PCA**: 10 principal components

### API Endpoints

- `GET /` - Main dashboard
- `GET /api/data/overview` - Dataset statistics
- `GET /api/models/train` - Train and evaluate models
- `GET /api/models/feature-importance` - Feature rankings
- `GET /api/clustering/segments` - Cluster analysis
- `GET /api/pca/results` - PCA results

## 📊 Sample Output

The web application provides:

1. **Real-time Metrics**: Live updates of key statistics
2. **Interactive Charts**: Hover effects, tooltips, animations
3. **Model Performance**: Detailed evaluation metrics
4. **Cluster Analysis**: Visual representation of segments
5. **Feature Importance**: Bar charts showing top predictors
6. **PCA Visualization**: Variance explained analysis

## 🎓 Project Goals Achieved

✅ Predict customer churn using machine learning  
✅ Segment customers into distinct behavioral groups  
✅ Apply dimensionality reduction techniques  
✅ Provide actionable business insights  
✅ Create interactive visualization dashboard  
✅ Demonstrate end-to-end ML pipeline  
✅ Production-ready web application  

## 📞 Troubleshooting

### Application won't start
```bash
# Check if Flask is installed
pip install flask

# Check if data file exists
python generate_data.py
```

### Port 5000 already in use
```python
# Edit app_flask.py and change the port
app.run(debug=True, port=5001)
```

### Charts not displaying
- Ensure Chart.js CDN is loading (check browser console)
- Clear browser cache and reload
- Check JavaScript console for errors

## 📝 Files Description

| File | Purpose |
|------|---------|
| `app_flask.py` | Flask backend server with API endpoints |
| `generate_data.py` | Creates synthetic customer dataset |
| `run_churn_analysis.py` | Command-line ML analysis script |
| `customer_data.csv` | Generated dataset (10,000 records) |
| `templates/index.html` | Frontend HTML interface |
| `static/style.css` | CSS styling with gradients |
| `static/script.js` | JavaScript for interactivity |
| `requirements.txt` | Python dependencies |

## 🎨 UI Features

- **Modern Gradient Design**: Beautiful purple/blue gradients
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Interactive Charts**: Chart.js with animations and tooltips
- **Real-time Updates**: AJAX-powered dynamic content
- **Smooth Navigation**: Sticky header, smooth scrolling
- **Color-coded Metrics**: Visual indicators for churn rates
- **Professional Cards**: Clean card-based layout

## 🚀 Deployment

For production deployment:

1. Set `debug=False` in `app_flask.py`
2. Use a production WSGI server (Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn -w 4 app_flask:app
   ```
3. Configure reverse proxy (Nginx)
4. Set up SSL certificate for HTTPS

## 📄 License

This project is for educational purposes.

## 🙏 Acknowledgments

- Built for Build and Deploy ML Applications course
- Uses scikit-learn for machine learning
- Chart.js for beautiful visualizations
- Flask for web framework
#   B u i l d - a n d - d e p l o y - m a c h i n e - l e a r n i n g - a p p l i c a t i o n s  
 #   B u i l d - a n d - d e p l o y - m a c h i n e - l e a r n i n g - a p p l i c a t i o n s  
 