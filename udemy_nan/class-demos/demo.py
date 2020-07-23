import psycopg2

connection = psycopg2.connect(host='localhost',database='example2',user='postgres',password='Madara12')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE mytable (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('''
    INSERT INTO mytable (id, completed) VALUES (1, true);
''')

connection.commit()
connection.close()
cursor.close()

# works the same as python sqlite3 library