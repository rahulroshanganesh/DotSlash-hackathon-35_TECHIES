import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data
def read():
 result = view_all_data()
 # st.write(result) 
 df = pd.DataFrame(result, columns=['book_id', 'book_title', 'category_id', 'author', 'book_pub', 'publisher_name', 'isbn', 'date_added','status']) 
 with st.expander("View all Books"):
    st.dataframe(df)
 """
 with st.expander("Source"):
 task_df = df['Dealer City'].value_counts().to_frame()
 task_df = task_df.reset_index()
 st.dataframe(task_df)
 p1 = px.pie(task_df, names='index', values='Dealer City')
 st.plotly_chart(p1)
 """