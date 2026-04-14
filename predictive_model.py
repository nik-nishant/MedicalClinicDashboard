import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/cleaned_data.csv")

# Add Weekday column before using it
df['AppointmentDate'] = pd.to_datetime(df['AppointmentDate'])
df['Weekday'] = df['AppointmentDate'].dt.day_name()

# Features and target
X = pd.get_dummies(df[['Age','Gender','Weekday']], drop_first=True)
y = df['Status'].apply(lambda x: 1 if x=="No-show" else 0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train,y_train)

# Evaluate
y_pred = model.predict(X_test)
print("✅ Model Accuracy:", accuracy_score(y_test,y_pred))