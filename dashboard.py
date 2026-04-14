import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
#
# --- Metrics ---
#
import os
print(os.getcwd())

import streamlit as st
import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

# Add Weekday column before using it
df['AppointmentDate'] = pd.to_datetime(df['AppointmentDate'])
df['Weekday'] = df['AppointmentDate'].dt.day_name()

st.title("🏥 Medical Clinic Dashboard")

st.metric("Total Patients", df['PatientID'].nunique())
st.metric("No-show Rate", round((df['Status'] == 'No-show').mean()*100, 2))

# Bar chart for appointments by weekday
st.bar_chart(df['Weekday'].value_counts())



#pie chart with animation by weekday
import plotly.express as px

st.subheader("📊 Animated Pie Chart: No-show vs Completed")

fig = px.pie(
    df,
    names="Status",                # Completed / No-show
    title="Appointment Status Distribution",
    hole=0.3,                      # Donut style
    color="Status",                # Different colors
         # Animate by weekday
)

st.plotly_chart(fig)



import plotly.express as px

# Create NoShowFlag column
df['NoShowFlag'] = df['Status'].apply(lambda x: 1 if x == "No-show" else 0)

st.subheader("📊 Bar Chart: No-show by Weekday")

fig2 = px.bar(
    df,
    x="Weekday",
    y="NoShowFlag",
    color="Status",
    title="No-show Trends by Weekday"
)

st.plotly_chart(fig2)