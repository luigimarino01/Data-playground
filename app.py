import streamlit as st
from modules.extractor import read_csv, read_excel, read_json
from modules.transformer import drop_nulls, drop_duplicated
import io
import os
SAMPLE_PATH = "sample_dataset/"



# ------ TITLE: START ------ #
st.set_page_config(layout="wide")
st.title("🎡 Data Playground")
st.markdown("""
This is an interactive space to explore your dataset and try out common **Pandas operations**.
Made by **Luigi Marino** for learning and experimentation. 🚀
""")
# ------ TITLE: END ------ #


#------ SAMPLE FILES: START ------ #
st.subheader("Use a default dataset or upload yours")
for file_name in os.listdir(SAMPLE_PATH):
    file_path = os.path.join(SAMPLE_PATH, file_name)
    
    if st.button(file_name):
        # Carica il file in base all'estensione
        if file_name.endswith(".csv"):
            df = read_csv(file_path)
        elif file_name.endswith(".xlsx"):
            df = read_excel(file_path)
        elif file_name.endswith(".json"):
            df = read_json(file_path)
        
        # Salva il dataset selezionato in session_state
        st.session_state['df'] = df
        st.session_state['uploaded_file_name'] = file_name
        st.rerun()
#------ SAMPLE FILES: END ------ #


# ------ UPLOAD FILE: START ------ #
uploaded_file = st.file_uploader("Upload your data", type=["csv", "xlsx", "json"])

# Controlla prima se c'è un dataset di default selezionato
if 'df' in st.session_state and not uploaded_file:
    df = st.session_state['df']
    file_name = st.session_state['uploaded_file_name']
    st.text(f"Dataset: {file_name}")
elif uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = read_excel(uploaded_file)
    else:
        df = read_json(uploaded_file)
    
    df = df
    file_name = uploaded_file.name
    st.text(f"Dataset: {file_name}")
else:
    df = None

if df is None or df.empty:
    st.markdown("---")  
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>Made by <a href='https://github.com/luigimarino01' target='_blank'>Luigi Marino</a></p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>⚠️ I am currently working on this project, so new functions are being added regularly.</p>",
        unsafe_allow_html=True
    )
# ------ UPLOAD FILE: END ------ #



if df is not None and not df.empty:
    # ------ DATASET SHOWING OPTION: START ------ #
    st.subheader("Choose how to display your dataset")
    show_option = st.radio(
        "Select an option:",
        options=(
            "Show entire dataset",
            "Show first N rows",
            "Show rows from N to M",
            "Show last N rows"
        )
    )
    if show_option == "Show entire dataset":
        st.dataframe(df)

    elif show_option == "Show first N rows":
        n = st.number_input("Enter N:", min_value=1, max_value=len(df), value=5)
        st.dataframe(df.head(n))

    elif show_option == "Show rows from N to M":
        n = st.number_input("Enter start row (N):", min_value=0, max_value=len(df)-1, value=0)
        m = st.number_input("Enter end row (M):", min_value=n+1, max_value=len(df), value=min(n+5, len(df)))
        st.dataframe(df.iloc[n:m])

    elif show_option == "Show last N rows":
        n = st.number_input("Enter N:", min_value=1, max_value=len(df), value=5)
        st.dataframe(df.tail(n))

    # ------ DATASET SHOWING OPTION: END ------ #


    # ------ DATA TRANSFORMS: START ------ #
    st.subheader("Transform your data")

    operations = {
        "Drop nulls": {
            "func": drop_nulls,
            "code": "df = df.dropna()"
        },
        "Drop duplicates": {
            "func": drop_duplicated,
            "code": "df = df.drop_duplicates()"
        },
    }

    for op_name, op_info in operations.items():
        col1, col2 = st.columns([3, 1])

        with col1:
            apply_op = st.checkbox(op_name, key=f"apply_{op_name}")

        with col2:
            show_code_key = f"show_code_{op_name}"
            show_code = st.toggle(
                "Show Code" if not st.session_state.get(show_code_key, False) else "Hide Code",
                key=show_code_key
            )

        if show_code:
            st.code(op_info["code"], language="python")

        if apply_op:
            df = op_info["func"](df)
            st.success(f"{op_name} applied. Dataset shape: {df.shape}")
    # ------ DATA TRANSFORMS: END ------ #




    # ------ SIDEBAR: DATASET STATS: START ------ #
    st.sidebar.header("Dataset Info")
    st.sidebar.write(f"Shape: {df.shape}")
    st.sidebar.write(f"Rows: {df.shape[0]}")
    st.sidebar.write(f"Columns: {df.shape[1]}")
    st.sidebar.write("Missing values per column:")
    st.sidebar.write(df.isnull().sum())
    st.sidebar.write("Numeric columns summary:")
    st.sidebar.write(df.describe())
    # ------ SIDEBAR: DATASET STATS: END ------ #


    # ------ DOWNLOAD YOUR DATA: START ------ #
    st.subheader("Download your transformed dataset")
    csv_buffer = io.StringIO()
    json_buffer = io.StringIO()
    excel_buffer = io.BytesIO()

    df.to_csv(csv_buffer, index=False)
    df.to_json(json_buffer, orient="records", indent=2)
    df.to_excel(excel_buffer, index=False, engine="openpyxl")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            label="📥 Download CSV",
            data=csv_buffer.getvalue(),
            file_name="exported_data.csv",
            mime="text/csv"
        )

    with col2:
        st.download_button(
            label="📥 Download JSON",
            data=json_buffer.getvalue(),
            file_name="exported_data.json",
            mime="application/json"
        )

    with col3:
        st.download_button(
            label="📥 Download XLSX",
            data=excel_buffer.getvalue(),
            file_name="exported_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    # ------ DOWNLOAD YOUR DATA: END ------ #



    # ------ FOOTNOTE: START ------ #
    st.markdown("---")  
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>Made by <a href='https://github.com/luigimarino01' target='_blank'>Luigi Marino</a></p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>⚠️ I am currently working on this project, so new functions are being added regularly.</p>",
        unsafe_allow_html=True
    )
    # ------ FOOTNOTE: END ------ #