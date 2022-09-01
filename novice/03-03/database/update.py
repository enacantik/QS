try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="enacantiksekali")
        curs = conn.cursor()

        namaLama= "imam"

        namaBaru = "zhafar imam"
        umurBaru = 23   
        query = f"update siswa set nama='{namaBaru}', {umurBaru} where nama='{namaLama}'"
        
        curs.execute(query)
        conn.commit() 
        print("data masuk")  
except Exception as e:
   pass