import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SafeRepurpose AI", page_icon="🧬", layout="wide")

st.title("🧬 SafeRepurpose AI")
st.caption("AI-inspired research candidate comparison • Biosafety-aware review")

st.warning(
    "Prototype only — all scores and comparison patterns below are synthetic demonstration values. "
    "This app does not analyze real biological datasets, establish efficacy, recommend treatment, "
    "or provide formal biosafety certification."
)

st.header("1. Choose a disease context")
disease = st.selectbox(
    "Disease context",
    ["Alzheimer's disease", "Asthma", "Type 2 diabetes", "Rheumatoid arthritis", "Parkinson's disease"]
)

# Synthetic, illustrative candidate list and scores; not derived from real biological data.
demo = {
    "Alzheimer's disease": [
        ("Metformin", 78, "Illustrative demo score only"),
        ("Dexamethasone", 67, "Illustrative demo score only"),
        ("Atorvastatin", 61, "Illustrative demo score only"),
        ("Losartan", 54, "Illustrative demo score only"),
    ],
    "Asthma": [
        ("Metformin", 74, "Illustrative demo score only"),
        ("Atorvastatin", 69, "Illustrative demo score only"),
        ("Losartan", 58, "Illustrative demo score only"),
        ("Dexamethasone", 52, "Illustrative demo score only"),
    ],
    "Type 2 diabetes": [
        ("Losartan", 80, "Illustrative demo score only"),
        ("Atorvastatin", 72, "Illustrative demo score only"),
        ("Dexamethasone", 64, "Illustrative demo score only"),
        ("Metformin", 56, "Illustrative demo score only"),
    ],
    "Rheumatoid arthritis": [
        ("Dexamethasone", 82, "Illustrative demo score only"),
        ("Metformin", 70, "Illustrative demo score only"),
        ("Losartan", 62, "Illustrative demo score only"),
        ("Atorvastatin", 57, "Illustrative demo score only"),
    ],
    "Parkinson's disease": [
        ("Atorvastatin", 76, "Illustrative demo score only"),
        ("Metformin", 71, "Illustrative demo score only"),
        ("Losartan", 63, "Illustrative demo score only"),
        ("Dexamethasone", 55, "Illustrative demo score only"),
    ],
}

st.header("2. Illustrative medicine-candidate shortlist")
rows = demo[disease]
df = pd.DataFrame(rows, columns=["Medicine name (example)", "Demo score", "Evidence label"])
df = df.sort_values("Demo score", ascending=False).reset_index(drop=True)
df.insert(0, "Demo rank", range(1, len(df) + 1))
st.caption("These medicines are example names for a UI demonstration. The ranking is invented and must not be interpreted as a real research finding.")
st.dataframe(df, use_container_width=True, hide_index=True)
st.bar_chart(df.set_index("Medicine name (example)")["Demo score"])

st.header("3. Review the demo candidate")
chosen = st.selectbox("Select an example medicine to inspect", df["Medicine name (example)"].tolist())
selected_row = df[df["Medicine name (example)"] == chosen].iloc[0]
col1, col2 = st.columns(2)
with col1:
    st.metric("Illustrative score", int(selected_row["Demo score"]), help="Invented demonstration value; not evidence.")
with col2:
    st.metric("Displayed demo rank", int(selected_row["Demo rank"]), help="Rank within this synthetic example only.")

st.subheader("What this result can and cannot tell you")
st.markdown(
    "- **Can show:** how a prototype might display a candidate list, score, rank, and review prompts.\n"
    "- **Cannot show:** real efficacy, clinical suitability, safety, or a validated drug–disease relationship.\n"
    "- **Data status:** no real disease-expression dataset or drug-response dataset is queried in this version."
)

st.header("4. Biosafety-aware review checklist")
checks = [
    "Dataset source and license/usage terms reviewed (when real data are added)",
    "Data completeness and missing values reviewed",
    "Methods, assumptions, and limitations documented",
    "Uncertainty and lack of validation clearly disclosed",
    "Institutional review / expert consultation considered where appropriate",
    "No clinical or laboratory use based on this prototype alone",
]
for item in checks:
    st.checkbox(item, key="review_" + item)

st.header("5. Generate a demo report")
review_status = [st.session_state.get("review_" + item, False) for item in checks]
report = f"""SafeRepurpose AI — Synthetic Demo Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

Disease context: {disease}
Selected example medicine: {chosen}
Illustrative score: {int(selected_row['Demo score'])}
Illustrative rank: {int(selected_row['Demo rank'])}

Synthetic shortlist:
{df.to_string(index=False)}

Checklist:
""" + "\n".join(
    f"- [{'x' if done else ' '}] {item}" for item, done in zip(checks, review_status)
) + """

Limitations:
All scores and rankings are invented demonstration values. No actual biological dataset was analyzed.
This is not medical advice, evidence of efficacy, a validated biosafety assessment, or certification.
"""
st.download_button("⬇️ Download demo report (.txt)", report, file_name="SafeRepurpose_demo_report.txt")

st.divider()
st.caption("SafeRepurpose AI • Hackathon prototype • Synthetic demonstration only")
