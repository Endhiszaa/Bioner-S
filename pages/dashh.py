import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Riwayat Produksi Listrik",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Ensure user is logged in
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.error("Please log in to access this page.")
    st.switch_page('Home.py')

if st.sidebar.button("Logout"):
    st.session_state['logged_in'] = False
    st.switch_page('Home.py')

# Read data from CSV
data = pd.read_csv('electricity.csv')

# Split data into production
data_production = data[['Hour', 'Voltage_Production', 'Current_Production']].copy()
data_production.columns = ['Hours', 'Voltage', 'Current']

# Streamlit app
st.title('Bioner-S')
st.subheader('Smart Energy for the Future')

# Function to create line chart for voltage
def create_voltage_chart(data):
    fig = px.line(data, x='Hours', y='Voltage', 
                  labels={'Voltage': 'Voltage (V)', 'Hours': 'Hour'},
                  color_discrete_sequence=['blue'])
    fig.update_layout(title_font_size=20, title_x=0.5, xaxis=dict(tickmode='linear'), yaxis=dict(range=[0, max(data['Voltage'])*1.1]))
    return fig

# Function to create line chart for current
def create_current_chart(data):
    fig = px.line(data, x='Hours', y='Current', 
                  labels={'Current': 'Current (A)', 'Hours': 'Hour'},
                  color_discrete_sequence=['cyan'])
    fig.update_layout(title_font_size=20, title_x=0.5, xaxis=dict(tickmode='linear'), yaxis=dict(range=[0, max(data['Current'])*1.1]))
    return fig

# Production charts side by side
st.markdown('### Riwayat Produksi Listrik')
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(create_voltage_chart(data_production), use_container_width=True)
with col2:
    st.plotly_chart(create_current_chart(data_production), use_container_width=True)
