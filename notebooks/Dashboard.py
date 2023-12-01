import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Slack Reaction Message')
st.text('Channel Reaction Analysis')
#st.title('Slack Messages for all data in week 8 and 9')
#st.text('Channel Members Analysis')
upload_file = st.file_uploader("Upload your file")

if upload_file:
    df = pd.read_csv(upload_file)
    st.header('Data Header')
    st.write(df.head())

    st.header('Data Statistics')    
    st.write(df.describe())  
    

     # Print column names to check the actual names in the DataFrame
    st.header('Column Names')
    st.write(df.columns)
    st.header('Barchart')
    df = df[1:15]
    fig, ax = plt.subplots(1, 1)
    ax.bar(df['reaction_name'], df['reaction_count'])
    ax.set_xlabel('reaction_name')
    ax.set_ylabel('reaction_count')

    st.pyplot(fig)