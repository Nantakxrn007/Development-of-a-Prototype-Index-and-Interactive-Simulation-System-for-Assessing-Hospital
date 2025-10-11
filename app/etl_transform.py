import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import MinMaxScaler
import os

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER','hospital_user')}:{os.getenv('DB_PASS','hospital_pass')}@{os.getenv('DB_HOST','db')}:5432/{os.getenv('DB_NAME','hospital_db')}"
)

# ดึงข้อมูลดิบ
df = pd.read_sql("SELECT * FROM adequacy_raw", engine)

# # clean
# df = df.fillna(0)

# # normalize
# num_cols = df.select_dtypes("number").columns
# scaler = MinMaxScaler()
# df[num_cols] = scaler.fit_transform(df[num_cols])

# # สร้าง Adequacy Index
# df["Adequacy_Index"] = df[num_cols].mean(axis=1)

# เขียนกลับ DB
df.to_sql("adequacy_processed", engine, if_exists="replace", index=False)
print("✅ ETL completed successfully!")
