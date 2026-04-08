# Hybrid Fraud Detection & Risk Scoring Engine

Designed and implemented a hybrid fraud detection framework inspired by real-world systems used in financial institutions, combining rules-based logic and machine learning for transaction monitoring and risk scoring.

## 💼 Project Type
End-to-End Fraud Detection System Simulation (Bank / Fintech Use Case)

---

## 📌 Overview
This project simulates a real-world fraud detection system used in financial institutions by combining rules-based scoring and machine learning.

It demonstrates how hybrid risk scoring improves fraud detection, reduces false positives, and enables more effective alert prioritisation in transaction monitoring workflows.

It reflects how modern fraud detection systems combine explainable rules with probabilistic machine learning models to optimise both detection accuracy and operational efficiency.

---

## 📊 Dashboard Preview

### 🔹 Overview Dashboard
![Overview](images/dashboard_overview.png)

### 🔹 Risk Insights
![Risk Insights](images/dashboard_risk_insights.png)

### 🔹 Model Insights
![Model Insights](images/dashboard_model_insights.png)

### 🔹 Analyst Workflow
![Analyst Notes](images/dashboard_analyst_notes.png)

---

## 📂 Access Project Files

- 📓 **Notebook (Full Workflow)**  
  👉 [View Notebook](./real_time_fraud_detection_engine.ipynb)

- 📊 **Sample Dataset**  
  👉 [View Dataset](./sample_transactions.csv)

- 📈 **Scored Results Output**  
  👉 [View Results](./df_test_results.csv)

- 📊 **Dashboard Code (Streamlit App)**  
  👉 [View App](./app.py)
  
---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🏗️ System Architecture

```
Transaction Data 
    ↓
Rules-Based Engine
    ↓
Machine Learning Model
    ↓
Hybrid Risk Scoring
    ↓
Risk Classification (High / Medium / Low)
    ↓
Recommended Action (Block / Review / Approve)
```

This architecture reflects how modern fraud detection systems integrate rule-based controls with machine learning models to support scalable and risk-based decision making.

---

## 🎯 Objectives
- Simulate fraud detection using transaction data
- Implement rules-based risk scoring
- Build a machine learning model to predict fraud
- Combine both approaches into a hybrid scoring engine
- Prioritise alerts using risk levels and recommended actions
- Provide an interactive dashboard for analyst review

---

## 💼 Business Impact

This project demonstrates how financial institutions can:

- Reduce false positives in transaction monitoring systems
- Improve alert prioritisation for investigators
- Enhance fraud detection recall while maintaining operational efficiency
- Support risk-based decision making using hybrid scoring models

The approach reflects real-world fraud risk engines used in banks, payment platforms, and fintech companies, where hybrid scoring models are critical for balancing detection accuracy and operational efficiency.

---

## ⭐ Key Features

- Hybrid rules-based and machine learning fraud detection
- Risk scoring and alert prioritisation engine
- Logistic regression model with threshold optimisation
- Streamlit dashboard simulating analyst workflow
- Visual analytics for model performance and risk distribution

---

## ⚡ Tech Stack

- **Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn (Logistic Regression)  
- **Visualisation:** Matplotlib  
- **Dashboard:** Streamlit

---

## ⚙️ Methodology

### 1. Data Simulation
Synthetic dataset representing:
- Transaction amount
- Merchant category risk
- Country mismatch
- Velocity patterns
- Behavioural indicators

### 2. Rules-Based Detection
- Defined fraud rules (amount, velocity, country mismatch, etc.)
- Generated explainable scores
- Captured triggered rules

### 3. Machine Learning Model
- Logistic Regression
- Class imbalance handling
- Threshold tuning (recall prioritised)

### 4. Hybrid Risk Scoring Engine
- Combined:
  - Normalised rule score
  - ML fraud probability
- Produced:
  - Final risk score
  - Risk classification
  - Recommended action

---

## 📊 Results & Comparison

| Approach | Strength | Limitation |
|----------|----------|------------|
| Rules-Based | Explainable | High false positives |
| Machine Learning | Better detection | Less interpretable |
| Hybrid Model | Balanced performance | Requires calibration |

### Key Outcome
- Improved fraud detection (higher recall)
- Structured alert prioritisation
- Better alignment with real-world fraud workflows

---

## 📈 Model Evaluation

- Precision, Recall, and F1-score used for performance evaluation  
- Recall prioritised to minimise missed fraud cases  
- Threshold tuning applied to balance detection vs false positives  

---

## 📊 Sample Output
- Final risk score per transaction
- Risk classification (High / Medium / Low)
- Recommended action (Block / Review / Approve)

---

## 📊 Dashboard (Streamlit)

Interactive dashboard simulating fraud analyst workflow.

### Features
- Alert filtering by risk level
- Risk metrics overview
- Alert review table
- Risk distribution charts
- ML probability insights

---

## 🧠 Key Insights
- Accuracy alone is insufficient in fraud detection
- Recall is critical to minimise missed fraud
- Rules and ML serve complementary roles
- Hybrid models improve both detection and usability

---

## 🏦 Real-World Applications
- Banking transaction monitoring systems
- Fintech payment risk engines
- Fraud detection platforms
- Compliance and AML workflows

---

## 🛠️ Tools Used
- Python
- Pandas / NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## 🚀 Future Improvements
- Real-time scoring pipeline
- Advanced ML models (XGBoost, Random Forest)
- SHAP explainability
- AI-assisted alert narratives
- Integration with external data sources

---

## ⚠️ Limitations

- Synthetic dataset may not reflect real-world complexity  
- Model performance may vary on real production data  
- Further validation required with larger datasets  

---

## 🎯 Target Users

- Fraud analysts and investigators  
- AML / transaction monitoring teams  
- Risk and compliance professionals  
- Fintech and payment risk teams

--- 

## 👤 Author
Farzean Hassim
