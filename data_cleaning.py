import pandas as pd

df = pd.read_csv("data/raw_data.csv")
df['Age'].fillna(df['Age'].median(), inplace=True)
df.drop_duplicates(inplace=True)
df['AppointmentDate'] = pd.to_datetime(df['AppointmentDate'])
df.to_csv("data/cleaned_data.csv", index=False)
print("✅ Data cleaning complete!")