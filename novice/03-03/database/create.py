try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="enacantiksekali")

    curs = conn.cursor()

    nama = "ifan"
    umur = 12
    query = f"insert into siswa(nama, umur) values('{nama}', {umur})"
    curs.execute(query)
    conn.commit() 
    print("data masuk")  
except Exception as e:
   print(e)

