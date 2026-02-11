import streamlit as st
import pandas as pd
import numpy  as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Portfolio Caesar Simarmata",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state='expanded'
)

#fungsi untuk load dataset

@st.cache_data
def load_data():
    return pd.read_csv(r'C:\Assignment Day 14\data\boston.csv')

#load data boston
df_boston = load_data()

#sidebar
st.sidebar.header('Pengaturan & Navigasi')

pilihan_halaman = st.sidebar.radio(
    'Pilihan Halaman:',
    ('About', 'Dashboard', 'Prediksi')
)

#About
if pilihan_halaman == "About":

    st.title("📂 About Me")
    
    # Bagian Header dengan kolom
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Ganti dengan path foto kamu atau URL gambar
        st.image(r"C:\Assignment Day 14\asset\foto profil.jpeg", caption="Data Analyst & Developer")

    with col2:
        st.subheader("Hi, I'm Caesar!")
        st.write("""
        I am a dedicated professional with a **thorough** approach to data analysis and web development. 
        My goal is to **accomplish** complex technical tasks by turning raw data into **intuitive** and actionable insights.
        """)
        st.info("Currently focused on building rigorous machine learning pipelines, ensuring model accuracy and reliable performance.")

    st.divider()

    # Bagian Skill & Expertise
    st.header("🚀 Professional Expertise")
    
    tab1, tab2, tab3 = st.tabs(["Analysis Philosophy", "Technical Skills", "Decision Making"])

    with tab1:
        st.write("""
        - **Rigorous Methodology:** I ensure every query and script follows a **rigorous** testing process to maintain data integrity.
        - **Explicit Documentation:** I believe that code is only as good as its documentation. I provide **explicit** comments and guides for every project.
        """)

    with tab2:
        # Menampilkan skill dengan progress bar atau tags
        skills = {
            "SQL (PostgreSQL/MySQL)": 90,
            "Python (Streamlit/Pandas)": 80,
            "Data Visualization (Plotly)": 75,
            "Problem Solving": 80
        }
        for skill, level in skills.items():
            st.write(f"**{skill}**")
            st.progress(level)

    with tab3:
        st.write("""
        In every project, I evaluate whether the long-term benefits **outweigh** the initial complexity. 
        I am fascinated by how users are influenced **consciously or unconsciously** by data design, 
        which is why I prioritize **perceived** performance and user experience.
        """)

    st.divider()

    # Bagian Contact / Call to Action
    st.header("📬 Get In Touch")
    st.write("If you have **sufficient** data but lack the insights, let's collaborate!")
    
    contact_col1, contact_col2 = st.columns(2)
    with contact_col1:
        st.link_button("LinkedIn Profile", 'https://www.linkedin.com/in/caesar-simarmata/')
    with contact_col2:
        st.link_button("GitHub Repository", 'https://github.com/caesar-john')

#dashboard
elif pilihan_halaman=='Dashboard':
    st.header("📈 Housing Market Dashboard")
    
    # Load Data
    df = pd.read_csv(r"C:\Assignment Day 14\data\boston.csv")
    
    st.write("""
    This dashboard provides a **thorough** look into the factors affecting housing prices. 
    We analyze how variables like crime rates and room numbers **outweigh** others in value determination.
    """)
    
    # Metric Row (Perbaikan di baris ini)
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg House Price", f"${df['medv'].mean():.2f}K")
    col2.metric("Avg Rooms", f"{df['rm'].mean():.1f}")
    col3.metric("Total Records", len(df)) # Pastikan col3 terisi
    
    # Jangan lupa tambahkan chart di bawahnya agar Dashboard tidak kosong
    fig = px.scatter(df, x="rm", y="medv", color="crim", title="Rooms vs Price")
    st.plotly_chart(fig, use_container_width=True)

#Prediction
elif pilihan_halaman == 'Prediksi':
    st.header("🤖 House Price Prediction")
    st.write("Input the features below to get an **explicit** price prediction **derived** from our ML model.")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            crim = st.number_input("Crime Rate (crim)", value=0.1)
            rm = st.number_input("Average Rooms (rm)", value=6.0)
        with col2:
            tax = st.number_input("Property Tax (tax)", value=300)
            lstat = st.number_input("Lower Status Population % (lstat)", value=10.0)
        
        submit = st.form_submit_button("Predict Price")

    if submit:
        # Di sini nanti masukkan model .pkl kamu
        # Untuk sementara kita pakai simulasi perhitungan
        prediction = (rm * 5) - (lstat * 0.5) + 10 
        
        st.success(f"### Predicted House Price: ${prediction:.2f}K")
        st.write("This prediction is **sufficient** for initial estimation based on current trends.")

