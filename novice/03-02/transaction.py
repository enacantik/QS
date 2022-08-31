import psycopg2

conn = None
try:
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # execute 1st statement
    cur.execute(statement_1)
    # execute 2nd statement
    cur.execute(statement_1)
    # commit the transaction
    conn.commit()
    # close the database communication
    cur.close()
except psycopg2.DatabaseError as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

import psycopg2
from config import config


def add_part(part_name, vendor_list):
    # statement for inserting a new row into the parts table
    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"
    # statement for inserting a new row into the vendor_parts table
    assign_vendor = "INSERT INTO vendor_parts(vendor_id,part_id) VALUES(%s,%s)"

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # insert a new part
        cur.execute(insert_part, (part_name,))
        # get the part id
        part_id = cur.fetchone()[0]
        # assign parts provided by vendors
        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))

        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Vibrator', (5, 6))
    add_part('Antenna', (6, 7))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))

suppliers=# select * from parts;
 part_id |  part_name
---------+-------------
       1 | SIM Tray
       2 | Speaker
       3 | Vibrator
       4 | Antenna
       5 | Home Button
       6 | LTE Modem
(6 rows)

suppliers=# select * from vendor_parts;
 vendor_id | part_id
-----------+---------
         1 |       1
         2 |       1
         3 |       2
         4 |       2
         5 |       3
         6 |       3
         6 |       4
         7 |       4
         1 |       5
         5 |       5
         1 |       6
         5 |       6
(12 rows)

add_part('Power Amplifier', (99,))

insert or update on table "vendor_parts" violates foreign key constraint "vendor_parts_vendor_id_fkey"
DETAIL:  Key (vendor_id)=(99) is not present in table "vendors".

with psycopg2.connect(dsn) as conn:
    with conn.cursor() as cur:
        cur.execute(sql)

conn = psycopg2.connect(dsn)

# transaction 1
with conn:
    with conn.cursor() as cur:
        cur.execute(sql)

# transaction 2
with conn:
    with conn.cursor() as cur:
        cur.execute(sql)

conn.close()