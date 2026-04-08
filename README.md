# Hybrid Fraud Detection & Risk Scoring Engine

## 💼 Project Type
End-to-End Fraud Detection System Simulation (Bank / Fintech Use Case)

---

## 📌 Overview
This project simulates a real-world fraud detection system used in financial institutions by combining rules-based scoring and machine learning.

It demonstrates how hybrid risk scoring improves fraud detection, reduces false positives, and enables more effective alert prioritisation in transaction monitoring workflows.

---

## 📂 Access Project Files

- 📓 **Notebook (Full Workflow)**  
  👉 [View Notebook](https://github.com/FarzeanHassim/hybrid-fraud-detection-risk-scoring-engine/blob/main/real_time_fraud_detection_engine.ipynb)

- 📊 **Sample Dataset**  
  👉 [View Dataset](https://github.com/FarzeanHassim/hybrid-fraud-detection-risk-scoring-engine/blob/main/sample_transactions.csv)

- 📈 **Scored Results Output**  
  👉 [View Results](https://github.com/FarzeanHassim/hybrid-fraud-detection-risk-scoring-engine/blob/main/df_test_results.csv)

- 📊 **Dashboard Code (Streamlit)**  
  👉 [View App](https://github.com/FarzeanHassim/hybrid-fraud-detection-risk-scoring-engine/blob/main/app.py)

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

---

## 🎯 Objectives
- Simulate fraud detection using transaction data
- Implement rules-based risk scoring
- Build a machine learning model to predict fraud
- Combine both approaches into a hybrid scoring engine
- Prioritise alerts using risk levels and recommended actions
- Provide an interactive dashboard for analyst review

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

## 👤 Author
Farzean Hassim
