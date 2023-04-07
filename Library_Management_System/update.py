import pandas as pd
import streamlit as st
from database import view_all_data, view_only_book_title, get_book, edit_book_data
def update():
 result = view_all_data()
 df = pd.DataFrame(result, columns=['book_id', 'book_title', 'category_id', 'author', 'book_pub', 'publisher_name', 'isbn', 'date_added','status'])
 with st.expander("Current Books"):
    st.dataframe(df)
 list_of_books = [i[0] for i in view_only_book_title()]
 selected_book = st.selectbox("Book to Edit", list_of_books)
 selected_result = get_book(selected_book)
 if selected_result:
    book_id = selected_result[0][0]
    book_title = selected_result[0][1]
    category_id = selected_result[0][2]
    author = selected_result[0][3]
    book_pub = selected_result[0][4]
    publisher_name = selected_result[0][5]
    isbn = selected_result[0][6]
    date_added = selected_result[0][7]
    status = selected_result[0][8]
    col1, col2 = st.columns(2)
    with col1:
        new_book_id = st.number_input("Book ID : ",book_id)
        new_book_title = st.text_input("Book Title : ",book_title)
        new_category_id = st.number_input("Category ID : ",category_id)
        new_author = st.text_input("Author : ",author)
        new_book_pub = st.text_input("Book Publisher : ",book_pub)
    with col2:
        new_publisher_name = st.text_input("Publisher Name : ",publisher_name)
        new_isbn = st.text_input("ISBN : ",isbn)
        new_date_added = st.date_input("Date added : ",date_added)
        new_status = st.text_input("Status : ",status)
    
    if st.button("Update Book"):
        edit_book_data(new_book_id, new_book_title, new_category_id, new_author, new_book_pub, new_publisher_name, new_isbn, new_date_added,new_status,book_id)
        st.success("Successfully updated")
        st.balloons()
 result2 = view_all_data()
 df2 = pd.DataFrame(result2, columns=['book_id', 'book_title', 'category_id', 'author', 'book_pub', 'publisher_name', 'isbn',  'date_added','status'])
 with st.expander("Updated data"):
    st.dataframe(df2)