conn = psycopg2.connect(dsn)
cur = conn.cursor()
cur.execute(sql, (value1,value2))
def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_vendors()

The number of parts:  7
(1, '3M Corp')
(2, 'AKM Semiconductor Inc.')
(3, 'Asahi Glass Co Ltd.')
(4, 'Daikin Industries Ltd.')
(5, 'Dynacast International Inc.')
(6, 'Foster Electric Co. Ltd.')
(7, 'Murata Manufacturing Co. Ltd.')

def get_parts():
    """ query parts from the parts table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_parts()

The number of parts:  6
(4, 'Antenna')
(5, 'Home Button')
(6, 'LTE Modem')
(1, 'SIM Tray')
(2, 'Speaker')
(3, 'Vibrator')

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_part_vendors():
    """ query part and vendor data from multiple tables"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("""
            SELECT part_name, vendor_name
            FROM parts
            INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
            INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
            ORDER BY part_name;
        """)
        for row in iter_row(cur, 10):
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_part_vendors()

('Antenna', 'Foster Electric Co. Ltd.')
('Antenna', 'Murata Manufacturing Co. Ltd.')
('Home Button', 'Dynacast International Inc.')
('Home Button', '3M Corp')
('LTE Modem', 'Dynacast International Inc.')
('LTE Modem', '3M Corp')
('SIM Tray', 'AKM Semiconductor Inc.')
('SIM Tray', '3M Corp')
('Speaker', 'Daikin Industries Ltd.')
('Speaker', 'Asahi Glass Co Ltd.')
('Vibrator', 'Dynacast International Inc.')
('Vibrator', 'Foster Electric Co. Ltd.')

