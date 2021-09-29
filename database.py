import sqlite3
import pandas as pd

# conn = sqllite3.connect(':memory:') this is temp
conn = sqlite3.connect('customer.db')


def create_db(c):
    try:
        # create a Table
        c.execute("""
        CREATE TABLE customers(
            first_name TEXT, 
            last_name TEXT,
            email TEXT
        )

        """)
    except Exception as e:
        print(e)
    return 'Table Created!'


def insert_db(c):
    c.execute(
        "INSERT INTO customers VALUES ('John', 'Elder', 'johnnyboy@gmail.com')")
    print('data inserted!')


def insertmany_db(c):
    many_cust = [
        ('Mary', 'Poppins', 'mary@fairy.com'),
        ('Dr.', 'Who', 'Dr@dr.com')
    ]
    c.executemany("INSERT INTO customers VALUES(?,?,?)", many_cust)
    print('Many data inserted')


def read_db(c):
    c.execute("SELECT * FROM customers")
    # c.fetchone()
    # c.fetchmany(3)
    items = c.fetchall()

    # non formatted
    # print(items)

    # formatted
    data = pd.read_sql_query("SELECT rowid, * FROM customers", conn)
    print(data.to_string(index=False))


def display_db(c):
    for i in c.fetchall():
        print(i)


def search_db(c):
    c.execute('SELECT * from customers WHERE first_name LIKE "Jo%"')
    display_db(c)


def update_db(c):
    c.execute('''UPDATE customers SET first_name="Doctor"
        WHERE rowid=3
    ''')
    conn.commit()
    read_db(c)


def delete_db(c):
    c.execute('DELETE from customers WHERE rowid=3')
    conn.commit()
    read_db(c)


def order_db(c):
    c.execute("SELECT rowid, * from customers ORDER BY last_name DESC")  # ASC
    display_db(c)


def searchandor_db(c):
    # similarly use OR
    c.execute('SELECT rowid, * from customers WHERE rowid > 0 AND first_name="Mary"')
    display_db(c)


def limit_db(c):
    c.execute('SELECT rowid,* from customers LIMIT 1')
    display_db(c)


def dropcol_db(c):
    c.execute('ALTER TABLE customers DROP COLUMN last_name')
    display_db(c)


def drop_db(c):
    c.execute('DROP TABLE customers')
    print('Table deleted')


# create cursor
c = conn.cursor()

# create_db(c)
# insert_db(c)
# insertmany_db(c)
# read_db(c)
# search_db(c)
# update_db(c)
# delete_db(c)
# order_db(c)
# searchandor_db(c)
# limit_db(c)
# dropcol_db(c)
# drop_db(c)


# Datatypes
# NULL INTEGER REAL TEXT BLOB

# commit our command
conn.commit()

# close connection
conn.close()
