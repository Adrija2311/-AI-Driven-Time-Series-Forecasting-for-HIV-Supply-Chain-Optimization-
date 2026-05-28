🚀 AI-Driven Time Series Forecasting & Anomaly Detection for HIV Supply Chain Optimization
📌 Overview

This project focuses on optimizing the global healthcare supply chain for HIV diagnostic kits and Antiretroviral (ARV) drugs using advanced AI, Machine Learning, and Time Series Forecasting techniques.

The system predicts freight costs, detects anomalous logistics transactions, and provides intelligent AI-powered chat support to enable proactive and data-driven supply chain decision-making.

🌍 Problem Statement

Global HIV healthcare logistics face major operational inefficiencies due to:

High freight and transportation costs
Delivery delays and stock shortages
Seasonal demand fluctuations
Dynamic fuel pricing
Lack of real-time forecasting systems
Inefficient routing and shipment planning

Traditional supply chain systems are reactive and struggle to adapt to real-world disruptions. This project introduces an AI-driven predictive framework to improve operational efficiency and cost transparency.

🎯 Objectives
Forecast freight costs and shipment demand using advanced time series models
Detect anomalies and suspicious logistics transactions using AI
Build an intelligent conversational AI support system for supply chain analytics
Improve healthcare logistics planning and cost optimization
🧠 Technologies & Tools Used
📊 Machine Learning & Forecasting
SARIMA
Exponential Smoothing
Prophet
LSTM (Long Short-Term Memory)
XGBoost
Prophet + XGBoost Hybrid Model
Isolation Forest (Anomaly Detection)
🛠️ Tech Stack
Python
Pandas
NumPy
Scikit-learn
TensorFlow / Keras
Prophet
XGBoost
Streamlit
LangChain
Groq API
LLaMA 3-70B
Matplotlib / Seaborn
📂 Dataset

The dataset contains global shipment and pricing information related to HIV and ARV healthcare supply chains, including:

Freight Cost (USD)
Shipment Quantity
Pack Price
Unit Price
Weight (Kilograms)
Vendor Information
Delivery Dates
Shipment Modes
Product Categories

The project utilizes historical logistics and procurement data inspired by global healthcare supply chain datasets such as PEPFAR and Global Fund procurement records.

🔍 Key Features
📈 Freight Cost Forecasting

Implemented multiple forecasting models to predict freight costs and shipping demand patterns.

Models Implemented
Exponential Smoothing
LSTM
Prophet
XGBoost
Hybrid Prophet + XGBoost
🏆 Best Performing Model

The Hybrid Prophet + XGBoost model achieved the highest accuracy:

MAPE: 3.30%
Lowest MAE & MSE
Captured both temporal seasonality and nonlinear relationships
🚨 Anomaly Detection

Implemented Isolation Forest to identify:

Suspicious freight charges
Duplicate transactions
Abnormal shipment patterns
Pricing inconsistencies
Explainable AI

Integrated LIME Explainability to interpret anomaly predictions and identify the strongest contributing features.

🤖 AI Chat Support System

Built an interactive AI-powered chat assistant using:

Streamlit
LangChain
Groq API
LLaMA 3-70B

The chatbot enables users to:

Ask natural language questions
Analyze CSV supply chain datasets
Detect delayed shipments
Explore anomalous costs
Generate operational insights
Example Queries
"What are the monthly average freight costs?"
"Show delayed delivery routes"
"Identify abnormal freight charges"
"Which shipment modes are most expensive?"
📊 Exploratory Data Analysis (EDA)

Performed detailed EDA using:

Histograms
Scatter Plots
Correlation Heatmaps
Boxplots
Boxen Plots
Key Insights
Strong correlation between shipment weight and freight cost
Significant seasonal patterns in shipment demand
High cost variability across shipment modes and vendors
Presence of extreme outliers in freight transactions
⚙️ Data Preprocessing
Missing value imputation
Outlier handling
Feature engineering
Time-series lag generation
Date feature extraction
Encoding categorical variables
Scaling numerical features
📌 Results
Model	Performance
Exponential Smoothing	Baseline
LSTM	Improved temporal learning
Prophet	Better seasonality capture
XGBoost	Strong nonlinear prediction
Prophet + XGBoost	⭐ Best Overall Performance
📈 Major Achievements

✅ 98%+ forecasting improvement over baseline methods
✅ Intelligent anomaly detection system
✅ AI-powered logistics decision support
✅ Real-world healthcare supply chain optimization

💡 Business Impact

This project demonstrates how AI can transform healthcare logistics by:

Reducing freight and operational costs
Improving delivery planning accuracy
Enhancing supply chain transparency
Enabling proactive decision-making
Preventing costly shipment anomalies
