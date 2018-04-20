import psycopg2
from postgre_example.keys import db_password


def create_table():
    conn = psycopg2.connect(
        'dbname=book_database user=postgres password={} host=localhost port=5432'.format(db_password))
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect(
        'dbname=book_database user=postgres password={} host=localhost port=5432'.format(db_password))
    cur = conn.cursor()
    cur.execute('INSERT INTO store VALUES (%s, %s, %s)', (item, quantity, price))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect(
        'dbname=book_database user=postgres password={} host=localhost port=5432'.format(db_password))
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s', (quantity, price, item))
    conn.commit()
    conn.close()


def delete(item):
    conn = psycopg2.connect(
        'dbname=book_database user=postgres password={} host=localhost port=5432'.format(db_password))
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item=%s', (item,))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(
        'dbname=book_database user=postgres password={} host=localhost port=5432'.format(db_password))
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close()
    return rows


create_table()
delete('Orange')
insert('apple', 15, 3)
print(view())
