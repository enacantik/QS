conn = psycopg2.connect(dsn)
cur = conn.cursor()
DELETE FROM table_1 WHERE id = %s;
cur.execute(delete_sql, (value_1,))
conn.commit()
cur.close()
conn.close()

import psycopg2
from config import config

def delete_part(part_id):
    """ delete part by part id """
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM parts WHERE part_id = %s", (part_id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

suppliers=# SELECT * FROM parts;
 part_id |  part_name
---------+-------------
       1 | SIM Tray
       2 | Speaker
       3 | Vibrator
       4 | Antenna
       5 | Home Button
       6 | LTE Modem
(6 rows)

if __name__ == '__main__':
    deleted_rows = delete_part(2)
    print('The number of deleted rows: ', deleted_rows)

suppliers=# SELECT * FROM parts;
 part_id |  part_name
---------+-------------
       2 | Speaker
       3 | Vibrator
       4 | Antenna
       5 | Home Button
       6 | LTE Modem
(5 rows)