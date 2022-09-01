try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="enacantiksekali")

    curs = conn.cursor()

    nama = "ifan"
    query = f"delete from siswa where nama='{nama})"

    curs.execute(query)
    conn.commit() 
    print("data berhasil didelete")  
except Exception:
   pass
