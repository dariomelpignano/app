import streamlit as st
import snowflake.connector

st.title("My Streamlit App with Snowflake")

# Connect to Snowflake (using Streamlit secrets)
try:
    conn = snowflake.connector.connect(
        account=st.secrets["snowflake"]["account"],
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"],
        warehouse=st.secrets["snowflake"]["warehouse"]
    )

    # Example: Execute a query
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM your_table_name")  # Replace with your query
        results = cur.fetchall()
        st.dataframe(results)  # Display results in a table

except Exception as e:
    st.error(f"Error connecting to Snowflake: {e}")