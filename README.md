# 🍽️ Restaurant Demand Forecasting System

### Developed by Sameer Ahmed

Machine Learning Based Restaurant Demand Forecasting and Inventory Recommendation System using Python, Scikit-Learn, Pandas, Matplotlib, and Tkinter.

---

## 📌 About the Project

The Restaurant Demand Forecasting System is a Machine Learning-based application developed to predict future meal demand and recommend optimal inventory stock levels for restaurants.

This system helps restaurant managers improve inventory planning, reduce food wastage, optimize stock management, and make data-driven decisions using historical demand data.

The project combines Data Analysis, Feature Engineering, Machine Learning, Time Series Validation, and GUI Development into a complete forecasting solution.

---

## 🎯 Project Objectives

- Forecast future restaurant meal demand
- Reduce food wastage through accurate predictions
- Improve inventory and stock management
- Support data-driven restaurant operations
- Analyze historical demand trends
- Provide inventory recommendations through a graphical dashboard

---

## ✨ Key Features

✅ Demand Forecasting

✅ Inventory Stock Recommendation

✅ Interactive GUI Dashboard

✅ Category-wise MAPE Analysis

✅ Actual vs Predicted Demand Comparison

✅ Weekly Demand Trend Analysis

✅ Machine Learning Model Training

✅ Data Preprocessing and Feature Engineering

✅ Time Series Cross Validation

✅ Demand Visualization and Reporting

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Data Analysis
- Pandas
- NumPy

### Data Visualization
- Matplotlib

### Machine Learning
- Scikit-Learn
- Random Forest Regressor

### GUI Development
- Tkinter

### Model Storage
- Joblib

---

## 🤖 Machine Learning Model

The forecasting model is built using:

### Random Forest Regressor

Key features used for forecasting:

- Week Number
- Checkout Price
- Base Price
- Discount
- Email Promotions
- Homepage Featured Meals
- Category Information
- Cuisine Information
- Region Information
- City Information
- Operational Area
- Lag Demand Feature

---

## 📊 Project Results

### Model Performance

- Average MAPE: **1.1841%**

### Analysis Performed

- Weekly Demand Trend Analysis
- Category-wise MAPE Report
- Actual vs Predicted Demand Analysis
- Inventory Recommendation Analysis

---

## 📷 Dashboard Preview

Add your dashboard screenshot here.

---

## 📈 Generated Visualizations

### Weekly Demand Trend

Shows changes in customer demand over time.

### Actual vs Predicted Demand

Compares model forecasts with actual order demand.

### Category-wise Analysis

Displays forecasting performance across meal categories.

---

## 📁 Project Structure

```text
Restaurant_Demand_Forecaster
│
├── data
│   ├── train.csv
│   ├── test.csv
│   ├── meal_info.csv
│   ├── fulfilment_center_info.csv
│   └── sample_submission.csv
│
├── gui
│   └── application.py
│
├── models
│   └── demand_forecasting_model.pkl
│
├── results
│   ├── actual_vs_predicted.png
│   └── weekly_demand_trend.png
│
├── src
│   ├── data_preprocessing.py
│   ├── exploratory_data_analysis.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   ├── category_mape.py
│   └── demand_prediction.py
│
├── README.md
└── requirements.txt
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/sameer-ahmed777/Restaurant_Demand_Forecaster.git
```

Move into project directory:

```bash
cd Restaurant_Demand_Forecaster
```

Install dependencies:

```bash
pip install pandas numpy matplotlib scikit-learn joblib
```

Run GUI:

```bash
python gui/application.py
```

---

## 💡 Business Impact

This system helps restaurants:

- Improve inventory planning
- Reduce stock shortages
- Minimize food wastage
- Increase forecasting accuracy
- Improve operational efficiency
- Support strategic decision-making

---

## 🚀 Future Improvements

Planned enhancements include:

- Deep Learning based forecasting
- Real-time demand prediction
- Web-based dashboard
- Automated inventory alerts
- Revenue forecasting
- Cloud deployment

---

## 👨‍💻 Author

### Sameer Ahmed

Machine Learning & Data Science Student

🔗 GitHub:
https://github.com/sameer-ahmed777

---

## 🙏 Acknowledgement

This project was independently designed and developed by **Sameer Ahmed** as an academic Machine Learning project to demonstrate practical skills in Data Analysis, Predictive Analytics, Forecasting, Machine Learning, and GUI Development.

---

## 🏆 Conclusion

The Restaurant Demand Forecasting System successfully applies Machine Learning techniques to forecast meal demand and recommend inventory stock levels. By combining predictive analytics, data visualization, and an interactive dashboard, the project provides a practical solution for restaurant inventory management and operational planning.

---

## © Copyright

© 2026 Sameer Ahmed. All Rights Reserved.
