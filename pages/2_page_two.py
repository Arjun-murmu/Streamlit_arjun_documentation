import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Data Analysis",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="auto"
)

st.sidebar.markdown("### Page 2 ❄️")
st.title("📄 Page Two")
st.write("This is **Page Two** of the app!")

st.write("## Discuss about pandas and analysis.")

file = st.file_uploader("Upload your file (CSV or Excel format).", type=["csv", "xlsx"])

if file:
    st.subheader("Data Preview")
    
    # Read file into dataframe
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    elif file.name.endswith(".xlsx"):
        df = pd.read_excel(file)
    else:
        st.error("File format not supported.")
        df = None
    
    # Show dataframe only if loaded
    if df is not None:
        st.dataframe(df)

        # Extra: Show basic info
        st.subheader("Basic Analysis")
        st.write("🔹 Shape of data:", df.shape)
        st.write("🔹 Columns:", list(df.columns))
        st.write("🔹 First 5 rows:")
        st.write(df.head())

        # ---- Filter by Product ----
        if "Product" not in df.columns:
            st.error("Dataset must contain a 'Product' column.")
        else:
            product = df["Product"].unique()
            st.write(f"Products available: {product}")
            select_product = st.selectbox("Filter by product : ", product)

            FD = df[df["Product"] == select_product]
            st.dataframe(FD)

            # ---- Detect time column ----
            time_col = None
            for col in ["Date", "Month", "Year"]:
                if col in FD.columns:
                    time_col = col
                    break

            if time_col is None:
                st.error("No time column ('Date', 'Month', or 'Year') found in dataset.")
            else:
                # Convert to datetime and sort
                FD[time_col] = pd.to_datetime(FD[time_col])
                FD = FD.sort_values(time_col)

                # --- Line graph for Price ---
                if "Price" in FD.columns:
                    st.subheader(f"📈 Price Trend for {select_product}")
                    price_chart = (
                        alt.Chart(FD)
                        .mark_line(point=True, color="blue")
                        .encode(
                            x=f"{time_col}:T",   # temporal axis
                            y="Price:Q"
                        )
                    )
                    st.altair_chart(price_chart, use_container_width=True)
                else:
                    st.warning("No 'Price' column found in dataset.")

                # --- Line graph for Total Sales ---
                if "Total Sales" in FD.columns:
                    st.subheader(f"📊 Sales Trend for {select_product}")
                    sales_chart = (
                        alt.Chart(FD)
                        .mark_line(point=True, color="orange")
                        .encode(
                            x=f"{time_col}:T",
                            y="Total Sales:Q"
                        )
                    )
                    st.altair_chart(sales_chart, use_container_width=True)
                else:
                    st.warning("No 'Total Sales' column found in dataset.")

                    # --- Graphs for Total Sales ---
                if "Total Sales" in FD.columns:
                    # --- Bar Graph ---
                    st.markdown("**Bar Graph (Total Sales by Time)**")
                    bar_chart = (
                        alt.Chart(FD)
                        .mark_bar(color="green")
                        .encode(
                            x=f"{time_col}:T",
                            y="Total Sales:Q"
                        )
                    )
                    st.altair_chart(bar_chart, use_container_width=True)

                    # --- Pie Chart ---
                    st.markdown("**Pie Chart (Share of Total Sales)**")
                    pie_chart = (
                        alt.Chart(FD)
                        .mark_arc()
                        .encode(
                            theta="Total Sales:Q",
                            color=alt.Color(f"{time_col}:T", legend=alt.Legend(title="Time Period"),
                                            scale=alt.Scale(scheme="category20"))  # colorful scheme
                        )
                    )
                    st.altair_chart(pie_chart, use_container_width=True)

                else:
                    st.warning("No 'Total Sales' column found in dataset.")


                

