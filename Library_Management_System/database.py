import mysql.connector 
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Library")
c = mydb.cursor()

def create_table(): 
    c.execute('CREATE TABLE IF NOT EXISTS book(book_id INT, book_title TEXT, category_id INT, author TEXT, book_pub TEXT, publisher_name TEXT, isbn TEXT, date_added TEXT,status TEXT)')
def add_data(book_id , book_title, category_id, author, book_pub, publisher_name, isbn,date_added,status): 
    c.execute('INSERT INTO book VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(book_id, book_title, category_id, author, book_pub, publisher_name, isbn, date_added,status)) 
    mydb.commit()
def view_all_data(): 
    c.execute('SELECT * FROM book') 
    data = c.fetchall()
    return data
def view_only_book_title(): 
    c.execute('SELECT book_title FROM book') 
    data = c.fetchall()
    return data
def get_book(book_title): 
    c.execute('SELECT * FROM book WHERE book_title="{}"'.format(book_title)) 
    data = c.fetchall()
    return data
def edit_book_data(new_book_id, new_book_title, new_category_id, new_author, new_book_pub, new_publisher_name, new_isbn, new_date_added,new_status,book_id): 
    c.execute("UPDATE book SET book_id=%s, book_title=%s, category_id=%s, author=%s, book_pub=%s, publisher_name=%s,isbn=%s,date_added=%s,status=%s WHERE book_id=%s",(new_book_id, new_book_title, new_category_id, new_author, new_book_pub, new_publisher_name, new_isbn, new_date_added,new_status,book_id)) 
    mydb.commit()
def delete_data(book_title): 
    c.execute('DELETE FROM book WHERE book_title="{}"'.format(book_title)) 
    mydb.commit()