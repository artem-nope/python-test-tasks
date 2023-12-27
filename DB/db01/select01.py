import sqlite3

DB = 'db1.sqlite3'


query1 = '''
    SELECT * 
    FROM languages
    ORDER BY rating DESC;
'''
query2 = '''
    SELECT * 
    FROM languages
    WHERE id = ?;
'''
with sqlite3.connect(DB) as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    # 1
    # for item in cursor.execute(query1):
    #     print(dict(item))
    # 2
    data = [dict(item) for item in cursor.execute(query1).fetchall()]
    for item in data:
        print(item.get('id'), item.get('name'))
    # print(data)
    # 3
    idx = int(input('id: '))
    row = cursor.execute(query2, [idx]).fetchone()
    print(dict(row))
