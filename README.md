# Hybrid Fraud Detection & Risk Scoring Engine

This project simulates an end-to-end hybrid fraud detection system for transaction monitoring, combining rules-based controls with machine learning to improve fraud detection, alert prioritisation, and decisioning.

It consolidates:
- rules-based detection and scoring
- ML-based fraud probability prediction
- hybrid risk scoring
- operational decisioning (Approve / Review / Block)
- analyst workflow visualisation through a Streamlit dashboard

This reflects how modern fraud detection systems in banks and fintechs balance explainability, predictive power, and operational usability.

## 💼 Project Type

End-to-End Fraud Detection System Simulation (Bank / Fintech Use Case)

---

## 📌 Overview

This project simulates a real-world fraud detection system used in financial institutions by combining rules-based scoring and machine learning.

It demonstrates how hybrid risk scoring improves fraud detection, reduces false positives, and enables more effective alert prioritisation in transaction monitoring workflows.

It reflects how modern fraud detection systems combine explainable rules with probabilistic machine learning models to optimise both detection accuracy and operational efficiency.

This project reflects how production fraud systems integrate detection, scoring, and decisioning into a single operational workflow.

### Key Result

- Reduced false positives and improved alert prioritisation using hybrid scoring  
- Achieved stronger fraud detection recall while maintaining operational efficiency

---

## End-to-End Workflow Coverage

This project demonstrates full fraud detection lifecycle:

- Detection → Rules-based scoring  
- Optimisation → Machine learning refinement  
- Decisioning → Hybrid scoring and action mapping  
- Operations → Analyst dashboard and workflow  

This aligns with real-world fraud risk engines used in financial institutions.

---

## 📊 Dashboard Preview

### 🔹 Overview Dashboard
![Overview](./dashboard_overview.png)

### 🔹 Risk Insights
![Risk Insights](./dashboard_risk_insights.png)

### 🔹 Model Insights
![Model Insights](./dashboard_model_insights.png)

### 🔹 Analyst Workflow
![Analyst Notes](./dashboard_analyst_notes.png)

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

This architecture reflects how modern fraud detection systems integrate rule-based controls with machine learning models to support scalable and risk-based decision making.

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

---

## 🎯 Objectives

- Simulate fraud detection workflows using transaction-level behavioural data
- Implement rules-based risk scoring
- Build a machine learning model to predict fraud
- Combine both approaches into a hybrid scoring engine
- Prioritise alerts using risk levels and recommended actions
- Provide an interactive dashboard to support analyst triage and decision-making

---

## 🧠 Hybrid Scoring Logic

The engine combines:
- Rule-based score for explainable fraud indicators
- ML fraud probability for predictive risk assessment

These are combined into a final hybrid score used to assign:
- final risk level
- recommended action
- analyst review priority

This approach improves operational usability by translating detection signals into decision-ready outputs.

---

## 💼 Business Impact

This project demonstrates how financial institutions can:

- Reduce false positives in transaction monitoring systems
- Improve alert prioritisation for investigators
- Enhance fraud detection recall while maintaining operational efficiency
- Support risk-based decision making using hybrid scoring models
- Bridge the gap between detection models and operational decisioning layers
- Aligns with risk-based approaches expected in regulated AML/CFT and fraud frameworks
  
The approach reflects real-world fraud risk engines used in banks, payment platforms, and fintech companies, where hybrid scoring models are critical for balancing detection accuracy and operational efficiency.

---

## ⭐ Key Features

- Hybrid rules-based and machine learning fraud detection
- Risk scoring and alert prioritisation engine
- Logistic regression model with threshold optimisation
- Streamlit dashboard simulating analyst workflow
- Visual analytics for model performance and risk distribution
  
---

## Key Features Used

The model uses a combination of behavioural and risk-based indicators, including:

- transaction amount
- transaction velocity (1h / 24h)
- new payee indicator
- card present indicator
- account age
- chargeback history
- prior alerts
- merchant category and merchant risk level
- country mismatch between transaction and IP
  
---

## Decisioning Framework

The system translates hybrid risk scores into operational decisions:

- High Risk → Block / Escalate for Investigation
- Medium Risk → Review / Monitor
- Low Risk → Approve

This simulates how fraud engines support downstream analyst and operations workflows.

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

## Why Hybrid Matters

Rules-based systems are transparent but can generate high false positives.
Machine learning improves detection but is less directly explainable.

A hybrid model combines both strengths:
- better fraud detection
- more practical alert prioritisation
- clearer operational actions
- stronger fit for regulated environments

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

## Example Output

The scored output includes:
- ML fraud probability
- normalised rule score
- final hybrid score
- final risk level
- recommended action

Example operational outputs:
- Low → Approve
- Medium → Review / Monitor
- High → Block / Escalate for Investigation

---

## 📈 Model Evaluation

- Precision, Recall, and F1-score used for performance evaluation  
- Recall prioritised to minimise missed fraud cases  
- Threshold tuning applied to balance detection vs false positives  

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

## How to Use This Project

- Explore the notebook to understand model logic and scoring methodology  
- Review the scored dataset to see final risk outputs  
- Run the Streamlit app to simulate analyst workflow and alert prioritisation

--- 

## 👤 Author
Farzean Hassim
