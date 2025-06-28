import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os   
import uuid

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# 1. Read the CSV with proper encoding
df = pd.read_csv("coursea_data.csv", encoding="utf-8-sig")

# 2. Drop unnecessary columns (like Unnamed: 0)
df.drop(columns=["Unnamed: 0"], errors="ignore", inplace=True)


# 3. Drop missing or bad titles
df = df[df['course_title'].notnull()]
df = df[df['course_title'].str.strip() != '']
df = df[df['course_title'].str.len() > 5]

# 4. Clean the 'course_students_enrolled' column
def parse_enrollment(x):
    if isinstance(x, str):
        x = x.lower().replace("k", "000").replace(".", "")
        return int(x) if x.isdigit() else None
    return None

df['course_students_enrolled'] = df['course_students_enrolled'].apply(parse_enrollment)

df['course_id'] = [str(uuid.uuid4()) for _ in range(len(df))]

cols = ['course_id'] + [col for col in df.columns if col != 'course_id']
df = df[cols]


# 5. Connect to PostgreSQL
engine = create_engine(DATABASE_URL)

# 6. Insert into PostgreSQL
df.to_sql("courses", engine, if_exists="replace", index=False)

print("✅ Data uploaded successfully.")
