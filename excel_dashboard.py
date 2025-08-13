import streamlit as st
import pandas as pd
import plotly.express as px


def main() -> None:
    st.title("Excel Dashboard Builder")
    st.write("Upload an Excel file to explore the data and build charts.")

    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])
    if not uploaded_file:
        return

    df = pd.read_excel(uploaded_file)
    st.subheader("Data preview")
    st.dataframe(df.head())

    if df.empty:
        st.warning("The uploaded file contains no data.")
        return

    chart_type = st.selectbox(
        "Chart type", ["Line", "Bar", "Scatter", "Area"], index=0
    )
    x_axis = st.selectbox("X-axis", options=df.columns)
    numeric_columns = df.select_dtypes(include="number").columns
    y_axis = st.selectbox("Y-axis", options=numeric_columns)

    if st.button("Create chart"):
        if chart_type == "Line":
            fig = px.line(df, x=x_axis, y=y_axis)
        elif chart_type == "Bar":
            fig = px.bar(df, x=x_axis, y=y_axis)
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=x_axis, y=y_axis)
        else:
            fig = px.area(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Summary statistics")
        st.write(df.describe())


if __name__ == "__main__":
    main()
