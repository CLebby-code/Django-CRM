import psycopg2

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'catposter' 
port_id = 5432 

try:
    conn = psycopg2.connect(
            host = hostname, 
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

    cur = conn.cursor()

    create_script = ''' CREATE TABLE employee (
                           id       int    PRIMARY KEY,
                           name     varchar(30) NOT NULL,
                           department int, 
                           address  varchar(40)) '''

    cur.execute(create_script)

    conn.commit()


   
except Exception as error: 
    print(error)
finally:
     if cur is not None:
         cur.close()
     if cur is not None:
        conn.close()

print('all done')