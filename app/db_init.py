import pandas as pd
from sqlalchemy import create_engine
import os

# สร้าง connection string
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER','hospital_user')}:{os.getenv('DB_PASS','hospital_pass')}@{os.getenv('DB_HOST','db')}:5432/{os.getenv('DB_NAME','hospital_db')}"
)

# โหลด raw excel
df = pd.read_excel("../data/raw/Adequecy_data.xlsx")
df.to_sql("adequacy_raw", engine, if_exists="replace", index=False)

print("✅ Uploaded raw data to PostgreSQL successfully!")
