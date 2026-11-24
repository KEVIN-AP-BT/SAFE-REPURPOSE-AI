import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SafeRepurpose AI", page_icon="🧬", layout="wide")

# Styling
st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#081421 0%,#0e1b2c 55%,#102737 100%); color:#e9f2f8;}
[data-testid="stSidebar"] {background:#101e2e;}
div[data-testid="stMetric"] {background:#132a3a;border:1px solid #23475a;padding:14px;border-radius:14px;}
div.stButton>button {border-radius:12px; font-weight:600;}
.small-muted {color:#a7bdcc;}
</style>
""", unsafe_allow_html=True)

st.title("🧬 SafeRepurpose AI")
st.caption("AI-driven research candidate prioritization • Biosafety-aware review")
st.warning("Prototype only — synthetic demonstration data. This is not medical advice, efficacy evidence, or a formal biosafety certification.")

with st.sidebar:
    st.header("Navigation")
    page=st.radio("Go to", ["Overview","Research Analysis","Biosafety Review","Report"])
    st.divider()
    st.caption("Demo uses simulated data, not validated drug-response signatures.")

# Synthetic data explicitly labeled
demo = pd.DataFrame([
    {"Candidate":"Candidate Alpha","Pattern similarity":0.82,"Evidence completeness":0.90,"Uncertainty":0.22,"Review flags":1},
    {"Candidate":"Candidate Beta","Pattern similarity":0.73,"Evidence completeness":0.75,"Uncertainty":0.35,"Review flags":2},
    {"Candidate":"Candidate Gamma","Pattern similarity":0.65,"Evidence completeness":0.88,"Uncertainty":0.28,"Review flags":1},
    {"Candidate":"Candidate Delta","Pattern similarity":0.59,"Evidence completeness":0.62,"Uncertainty":0.48,"Review flags":3},
])
# Demo scoring is illustrative and not biological prediction
demo["Illustrative priority score"] = (demo["Pattern similarity"]*0.55 + demo["Evidence completeness"]*0.30 + (1-demo["Uncertainty"])*0.15)*100
demo=demo.sort_values("Illustrative priority score",ascending=False).reset_index(drop=True)

if page=="Overview":
    st.header("Project overview")
    st.write("A transparent research-support prototype: compare a disease-associated pattern to a hypothetical perturbation pattern, show an illustrative shortlist, and surface review questions.")
    a,b,c=st.columns(3)
    a.metric("Modules","4")
    b.metric("Demo candidates","4")
    c.metric("Mode","Synthetic")
    st.markdown("### Workflow")
    st.markdown("**Disease context → Data review → Candidate shortlist → Biosafety-aware checks → Report**")
    st.info("Ranking in this version is based on invented demonstration values. No actual disease dataset or drug is analyzed.")
    st.markdown("### What this prototype demonstrates")
    st.markdown("- Responsive interface designed for phone and laptop\n- Candidate-ranking visualization with transparent example score\n- Evidence and uncertainty fields\n- Biosafety-awareness checklist\n- Exportable demo report")

elif page=="Research Analysis":
    st.header("Research analysis")
    disease=st.selectbox("Choose a research context",["Alzheimer's disease","Parkinson's disease","Type 2 diabetes","Cancer (general)","Other"])
    st.text_input("Optional study ID / dataset accession",placeholder="e.g., GSEXXXXX (not fetched automatically)")
    st.markdown("#### Candidate shortlist (synthetic example)")
    st.caption("These generic labels are not actual drugs and are not tied to the selected disease.")
    st.dataframe(demo[["Candidate","Pattern similarity","Evidence completeness","Uncertainty","Illustrative priority score"]].style.format({"Pattern similarity":"{:.2f}","Evidence completeness":"{:.2f}","Uncertainty":"{:.2f}","Illustrative priority score":"{:.1f}"}),use_container_width=True,hide_index=True)
    st.bar_chart(demo.set_index("Candidate")["Illustrative priority score"])
    st.markdown("#### How the illustrative score works")
    st.code("score = 55% pattern similarity + 30% evidence completeness + 15% (1 − uncertainty)",language="text")
    st.write("This weighting is an invented demo rule. It is not validated and should not be interpreted as a biological or clinical score.")
    st.download_button("Download demo shortlist CSV",demo.to_csv(index=False).encode("utf-8"),"saferepurpose_demo_shortlist.csv","text/csv")

elif page=="Biosafety Review":
    st.header("Biosafety-aware review")
    st.write("Checklist for responsible interpretation. It does not perform a formal biosafety assessment.")
    checks=[
        "Data source and accession documented",
        "Dataset organism, tissue/cell type and context recorded",
        "Missing values and data quality limitations described",
        "Prediction method and score weights disclosed",
        "Uncertainty and out-of-domain limitations disclosed",
        "No experimental or clinical claims made from ranking alone",
        "Institutional review / biosafety consultation considered where applicable",
        "Privacy, access and responsible-use requirements considered",
    ]
    answers={}
    for item in checks:
        answers[item]=st.checkbox(item)
    completed=sum(answers.values())
    st.metric("Checklist completed",f"{completed} / {len(checks)}")
    if completed==len(checks):
        st.success("All checklist items marked. This is self-attestation only, not a safety approval.")
    else:
        st.info("Review remaining items before presenting the interpretation.")
    st.caption("Checklist status is user-marked and does not certify biosafety, efficacy, or regulatory compliance.")

elif page=="Report":
    st.header("Demo report")
    st.markdown("### SafeRepurpose AI — Prototype Summary")
    st.write("**Mode:** Synthetic demonstration")
    st.write("**Scope:** Research prioritization interface and biosafety-aware checklist")
    st.write("**Candidates:** Generic labels Alpha, Beta, Gamma, Delta")
    st.write("**Interpretation:** Scores are illustrative software behavior only; they are not computed from real biological data.")
    st.write("**Limitations:** No external datasets fetched, no clinical validation, no drug safety certification, no efficacy claim.")
    st.dataframe(demo[["Candidate","Illustrative priority score","Uncertainty","Review flags"]],use_container_width=True,hide_index=True)
    report_text=("SafeRepurpose AI Prototype Report\n\n"
                 "Mode: Synthetic demonstration only.\n"
                 "No real drug or disease dataset was analyzed.\n"
                 "Scores are invented examples to demonstrate UI logic.\n"
                 "Not clinical evidence or a formal biosafety assessment.\n\n"
                 + demo[["Candidate","Illustrative priority score","Uncertainty","Review flags"]].to_string(index=False))
    st.download_button("Download report (TXT)",report_text,"saferepurpose_demo_report.txt","text/plain")
    st.markdown("---")
    st.markdown("**Next development milestone:** Connect a documented public dataset and implement a reproducible, validated analysis workflow with scientific review.")

st.divider()
st.caption("SafeRepurpose AI • Hackathon prototype • Synthetic demo data • Responsible research only")
