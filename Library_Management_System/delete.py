import pandas as pd 
import streamlit as st
from database import view_all_data, view_only_book_title, get_book, edit_book_data, delete_data
def delete():
 result = view_all_data()
 df = pd.DataFrame(result, columns=['book_id', 'book_title', 'category_id', 'author', 'book_pub', 'publisher_name', 'isbn', 'date_added','status']) 
 with st.expander("Current data"):
    st.dataframe(df)
 list_of_books = [i[0] for i in view_only_book_title()] 
 selected_book = st.selectbox("Book to Delete", list_of_books) 
 st.warning("Do you want to delete : {}".format(selected_book)) 
 
 if st.button("Delete Book"):
    delete_data(selected_book)
    st.success("Book has been deleted successfully")
    st.balloons()
 new_result = view_all_data()
 df2 = pd.DataFrame(new_result, columns=['book_id', 'book_title', 'category_id', 'author', 'book_pub', 'publisher_name', 'isbn', 'date_added','status']) 
 with st.expander("Updated data"):
    st.dataframe(df2)