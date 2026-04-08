import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hybrid Fraud Detection Dashboard", layout="wide")

st.title("Hybrid Fraud Detection & Risk Scoring Dashboard")
st.markdown(
    """
    This dashboard simulates how fraud analysts and risk teams can review
    scored transactions, prioritise alerts, and monitor fraud detection performance.
    """
)

@st.cache_data
def load_data():
    return pd.read_csv("df_test_results.csv")

df = load_data()

if "final_score" in df.columns:
    df["final_score"] = df["final_score"].round(4)

if "ml_risk_probability" in df.columns:
    df["ml_risk_probability"] = df["ml_risk_probability"].round(4)

st.sidebar.header("Filter Alerts")

risk_levels = sorted(df["final_risk_level"].dropna().unique().tolist()) if "final_risk_level" in df.columns else []
selected_risk = st.sidebar.multiselect("Select Risk Level", risk_levels, default=risk_levels)

if "ml_risk_probability" in df.columns:
    selected_prob = st.sidebar.slider("Minimum ML Risk Probability", 0.0, 1.0, 0.0, 0.01)
else:
    selected_prob = 0.0

filtered_df = df.copy()

if "final_risk_level" in filtered_df.columns and selected_risk:
    filtered_df = filtered_df[filtered_df["final_risk_level"].isin(selected_risk)]

if "ml_risk_probability" in filtered_df.columns:
    filtered_df = filtered_df[filtered_df["ml_risk_probability"] >= selected_prob]

st.subheader("Overview")

col1, col2, col3, col4 = st.columns(4)

total_txns = len(filtered_df)
high_risk = len(filtered_df[filtered_df["final_risk_level"] == "High"]) if "final_risk_level" in filtered_df.columns else 0
medium_risk = len(filtered_df[filtered_df["final_risk_level"] == "Medium"]) if "final_risk_level" in filtered_df.columns else 0
fraud_flags = int(filtered_df["ml_predicted_flag"].sum()) if "ml_predicted_flag" in filtered_df.columns else 0

col1.metric("Transactions Reviewed", total_txns)
col2.metric("High Risk Alerts", high_risk)
col3.metric("Medium Risk Alerts", medium_risk)
col4.metric("ML Fraud Flags", fraud_flags)

st.subheader("Alert Review Table")

display_columns = [
    col for col in [
        "true_fraud",
        "ml_risk_probability",
        "rule_score_normalized",
        "final_score",
        "final_risk_level",
        "recommended_action"
    ] if col in filtered_df.columns
]

if "final_score" in filtered_df.columns:
    st.dataframe(
        filtered_df[display_columns].sort_values(by="final_score", ascending=False),
        use_container_width=True
    )
else:
    st.dataframe(filtered_df[display_columns], use_container_width=True)

st.subheader("Risk Insights")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    if "final_risk_level" in filtered_df.columns:
        st.markdown("**Risk Level Distribution**")
        risk_counts = filtered_df["final_risk_level"].value_counts()
        fig, ax = plt.subplots()
        risk_counts.plot(kind="bar", ax=ax)
        ax.set_xlabel("Risk Level")
        ax.set_ylabel("Count")
        ax.set_title("Risk Level Distribution")
        plt.xticks(rotation=0)
        st.pyplot(fig)

with chart_col2:
    if "recommended_action" in filtered_df.columns:
        st.markdown("**Recommended Action Distribution**")
        action_counts = filtered_df["recommended_action"].value_counts()
        fig, ax = plt.subplots()
        action_counts.plot(kind="bar", ax=ax)
        ax.set_xlabel("Recommended Action")
        ax.set_ylabel("Count")
        ax.set_title("Recommended Action Distribution")
        plt.xticks(rotation=20)
        st.pyplot(fig)

st.subheader("Model Insights")

insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    if "ml_risk_probability" in filtered_df.columns:
        st.markdown("**ML Risk Probability Distribution**")
        fig, ax = plt.subplots()
        filtered_df["ml_risk_probability"].plot(kind="hist", bins=20, ax=ax)
        ax.set_xlabel("ML Risk Probability")
        ax.set_ylabel("Frequency")
        ax.set_title("Distribution of ML Risk Probability")
        st.pyplot(fig)

with insight_col2:
    if "final_score" in filtered_df.columns and "true_fraud" in filtered_df.columns:
        st.markdown("**Average Final Score by Fraud Label**")
        score_by_label = filtered_df.groupby("true_fraud")["final_score"].mean()
        fig, ax = plt.subplots()
        score_by_label.plot(kind="bar", ax=ax)
        ax.set_xlabel("True Fraud Label")
        ax.set_ylabel("Average Final Score")
        ax.set_title("Average Final Score by Fraud Label")
        plt.xticks(rotation=0)
        st.pyplot(fig)

st.subheader("Analyst Notes")
st.markdown(
    """
    - High-risk alerts are prioritised for immediate review or escalation.
    - Medium-risk alerts may be reviewed or monitored depending on capacity.
    - Low-risk alerts may be approved or deprioritised.
    - This dashboard illustrates how hybrid fraud scoring can support more efficient alert triage.
    """
)