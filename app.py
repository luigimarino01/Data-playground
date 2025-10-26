import streamlit as st
from modules.extractor import read_csv, read_excel, read_json
from modules.transformer import drop_nulls, drop_duplicated



st.title("🎡 Data Playground")
st.markdown("""
This is an interactive space to explore your dataset and try out common **Pandas operations**.
Made by **Luigi Marino** for learning and experimentation. 🚀
""")


uploaded_file = st.file_uploader("Upload your data", type=["csv", "xlsx", "json"])
df = None
if not uploaded_file:
    st.markdown("---")  
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>Made by <a href='https://github.com/luigimarino01' target='_blank'>Luigi Marino</a></p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>⚠️ I am currently working on this project, so new functions are being added regularly.</p>",
        unsafe_allow_html=True
    )
if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = read_excel(uploaded_file)
    else:
        df = read_json(uploaded_file)

    st.text(f"Dataset: {uploaded_file.name}")

    operations = {
        "Drop nulls": drop_nulls,
        "Drop duplicates": drop_duplicated,
    }



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

    st.subheader("Transform your data")
    for op_name, op_func in operations.items():
        if st.checkbox(op_name):
            df = op_func(df)
            st.success(f"{op_name} applied. Dataset shape: {df.shape}")


    st.sidebar.header("Dataset Info")
    st.sidebar.write(f"Shape: {df.shape}")
    st.sidebar.write(f"Rows: {df.shape[0]}")
    st.sidebar.write(f"Columns: {df.shape[1]}")
    st.sidebar.write("Missing values per column:")
    st.sidebar.write(df.isnull().sum())
    st.sidebar.write("Numeric columns summary:")
    st.sidebar.write(df.describe())

    st.subheader("Export your transformed dataset")
    if st.button("Export dataset to CSV"):
        df.to_csv("data/processed/exported_data.csv", index=False)
        st.success("Dataset exported to data/processed/exported_data.csv")


    st.markdown("---")  
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>Made by <a href='https://github.com/luigimarino01' target='_blank'>Luigi Marino</a></p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>⚠️ I am currently working on this project, so new functions are being added regularly.</p>",
        unsafe_allow_html=True
    )
