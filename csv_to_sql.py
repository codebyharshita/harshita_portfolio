import pandas as pd
import mysql.connector

# Step 1: CSV path and data load
csv_file = r'C:\Users\Asus\OneDrive\Desktop\E-Commerce\Amazon Sale Report.csv'
df = pd.read_csv(csv_file)

# Step 2: MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Harshu67',    # apna password
    database='e-commerce'     # apni database ka naam
)
cursor = conn.cursor()

# Step 3: Create table from CSV columns if not exists
table_name = 'amazon_sales'
columns = ', '.join([f"`{col}` TEXT" for col in df.columns])
cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")

# Step 4: Insert all data
for row in df.itertuples(index=False):
    placeholders = ','.join(['%s'] * len(df.columns))
    sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.execute(sql, tuple(row))
conn.commit()

cursor.close()
conn.close()
print("Amazon Sale Report uploaded to MySQL successfully!")


