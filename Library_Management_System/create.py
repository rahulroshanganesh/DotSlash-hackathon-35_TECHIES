import streamlit as st
from database import add_data

def create():
 col1, col2 = st.columns(2)
 with col1:
    book_id = st.number_input("Book ID : ",min_value=10,max_value=100,step=1)
    book_title = st.text_input("Book Title : ")
    category_id = st.number_input("Category ID : ",min_value=1,max_value=10,step=1)
    author = st.text_input("Author : ")
    book_pub = st.text_input("Book Publisher : ")
 with col2:
    publisher_name = st.text_input("Publisher Name : ")
    isbn = st.text_input("ISBN : ")
    date_added = st.date_input("Date added : ")
    status = st.selectbox("Status :",["New","Old","Lost","Damage","Archive"])
 if st.button("Add Book"):
    add_data(book_id, book_title, category_id, author, book_pub, publisher_name, isbn,date_added,status)
    st.success("Successfully added book : {}".format(book_title))
    st.balloons()