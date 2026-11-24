# SafeRepurpose AI — Hackathon prototype

This mobile-friendly Streamlit prototype demonstrates the UI/workflow using **synthetic demonstration values only**.

## Run locally
1. Install Python 3.10+
2. In this folder run:
   `pip install -r requirements.txt`
3. Run:
   `streamlit run streamlit_app.py`

## Deploy on Streamlit Community Cloud
1. Upload `streamlit_app.py` and `requirements.txt` to a GitHub repository.
2. Go to https://share.streamlit.io and connect GitHub.
3. Choose the repository and `streamlit_app.py` as entrypoint.

## Scope and caveats
- Candidate labels are generic, not real medicines.
- Values and score weights are invented for interface demonstration.
- No external data is fetched and no biological analysis is performed.
- The biosafety checklist is review-awareness only; not a formal assessment or certification.
