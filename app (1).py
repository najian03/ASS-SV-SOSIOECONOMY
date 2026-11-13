
import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Malaysia Scientific Visualisation",
    page_icon="📊",
    layout="wide"
)

st.title("Malaysia Scientific Visualisation")
st.caption("Socioeconomic and Demographic Statistics of Malaysia (2020–2024)")

# ==========================================
# DOSM DATASET URLS
# ==========================================

URL_MARRIAGES = "https://storage.dosm.gov.my/demography/marriages_age.parquet"

URL_PRISONERS = "https://storage.data.gov.my/publicsafety/prisoners_state.parquet"

URL_INCOME = "https://storage.dosm.gov.my/hies/hies_state_percentile.parquet"


# ==========================================
# LOAD DATA FROM DOSM
# ==========================================

@st.cache_data
def load_data():

    df_marriages = pd.read_parquet(URL_MARRIAGES)
    df_prisoners = pd.read_parquet(URL_PRISONERS)
    df_income = pd.read_parquet(URL_INCOME)

    for df in [df_marriages, df_prisoners, df_income]:
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"])

    return df_marriages, df_prisoners, df_income


# ==========================================
# DISPLAY DATA
# ==========================================

try:

    df_marriages, df_prisoners, df_income = load_data()

    st.success("All three datasets loaded successfully!")

    st.header("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Marriage Records", len(df_marriages))
    col2.metric("Prisoner Records", len(df_prisoners))
    col3.metric("Income Records", len(df_income))

    # Marriage dataset
    with st.expander("Marriage Dataset"):
        st.write(df_marriages.head())

    # Prisoner dataset
    with st.expander("Prisoner Dataset"):
        st.write(df_prisoners.head())

    # Income dataset
    with st.expander("Income Dataset"):
        st.write(df_income.head())

except Exception as e:

    st.error(f"Unable to load dataset: {e}")
