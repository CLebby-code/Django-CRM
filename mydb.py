import psycopg2

hostname = "localhost"
database = "violetflowers"
username = "candacelebby"
pwd = "catposter"
port_id = 5432

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id,  # noqa: E501
    )

    cur = conn.cursor()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()

print("all done")
