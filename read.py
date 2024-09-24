import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data

def read():
    # Fetch data from the database
    result = view_all_data()
    
    # Convert the data to a DataFrame
    df = pd.DataFrame(result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    
    # Display the DataFrame in an expander
    with st.expander("View all Dealers in table"):
        st.dataframe(df)
    
    # Display Dealer Location data
    with st.expander("Dealer Location"):
        # Create a DataFrame with the count of dealers in each city
        task_df = df['Dealer City'].value_counts().to_frame()
        task_df.columns = ['count']  # Rename the column to 'count' for clarity
        task_df = task_df.reset_index()  # Reset index to make 'Dealer City' a column
        task_df.columns = ['Dealer City', 'count']  # Rename columns
        
        # Display the DataFrame with the dealer city counts
        st.dataframe(task_df)
        
        # Create a pie chart using Plotly
        p1 = px.pie(task_df, names='Dealer City', values='count', title='Dealer Distribution by City')
        
        # Display the pie chart in Streamlit
        st.plotly_chart(p1)

