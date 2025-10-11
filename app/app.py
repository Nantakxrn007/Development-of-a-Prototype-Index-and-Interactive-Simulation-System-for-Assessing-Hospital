import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

st.set_page_config(page_title="Hospital Data Preview", layout="wide")
st.title("🏥 Hospital Adequacy Data (Raw Preview)")

# connect PostgreSQL
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER','hospital_user')}:{os.getenv('DB_PASS','hospital_pass')}@{os.getenv('DB_HOST','db')}:5432/{os.getenv('DB_NAME','hospital_db')}"
)

# ดึงข้อมูลจาก adequacy_raw2
df = pd.read_sql("SELECT * FROM adequacy_raw", engine)

# แสดงข้อมูลบนเว็บ
st.write("### ข้อมูลทั้งหมด (จาก adequacy_raw)")
st.dataframe(df)

# แสดงจำนวนแถวและคอลัมน์
st.write(f"**🧮 Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")

# preview 5 แถวแรก
st.write("### ตัวอย่างข้อมูล 5 แถวแรก")
st.dataframe(df.head())

