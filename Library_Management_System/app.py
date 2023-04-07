import streamlit as st
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
def main():
 st.title("LIBRARY")
 menu = ["Add books", "View books", "Edit books", "Remove books"]
 choice = st.sidebar.selectbox("Menu", menu)
 create_table()
 if choice == "Add books":
    st.subheader("Enter new book details:")
    create()
 elif choice == "View books":
    st.subheader("View all books")
    read()
 elif choice == "Edit books":
    st.subheader("Update available books")
    update()
 elif choice == "Remove books":
    st.subheader("Delete available books")
    delete()
 else:
    st.subheader("About tasks")
if __name__ == '__main__':
 main()
