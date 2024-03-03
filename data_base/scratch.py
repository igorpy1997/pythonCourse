import sqlite3

try:
    conn = sqlite3.connect('users.db')
    conn.executescript("""
        DROP TABLE IF EXISTS user;

        CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            language TEXT NOT NULL,
            course TEXT NOT NULL,
            grade TEXT NOT NULL
        );
    """)
    cur = conn.cursor()

    name = 'Jack'
    language = 'Python'

    sql_add_item = f"""
        INSERT INTO user 
        VALUES (1, '{name}', '{language}', 'Pro', '30');
    """

    cur.execute(sql_add_item)
    conn.commit()

    sql = """
            SELECT * FROM user;
        """
    cur.execute(sql)
    print(cur.fetchall())



finally:
    conn.close()