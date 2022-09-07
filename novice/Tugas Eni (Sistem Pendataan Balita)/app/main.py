from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="tugasenimanis",
        user="postgres",
        password="enacantiksekali"
    )

    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        jenis_kelamin = request.form.get("jenis_kelamin")
        tanggal_lahir = request.form.get("tanggal_lahir")
        vitamin_a = request.form.get("vitamin_a")
        berat_badan = request.form.get("berat_badan")
        tinggi_badan = request.form.get("tinggi_badan")
        lingkar_kepala = request.form.get("lingkar_kepala")
        keterangan = request.form.get("keterangan")
        query = f"insert into data_posyandu(nama, jenis_kelamin, tanggal_lahir, vitamin_a, berat_badan, tinggi_badan, lingkar_kepala, keterangan) values ('{nama}', '{jenis_kelamin}', '{tanggal_lahir}', '{vitamin_a}', '{berat_badan}', '{tinggi_badan}', '{lingkar_kepala}', '{keterangan}')"
        curs.execute(query)
        conn.commit()        
        curs.close()
        conn.close()

if __name__== "__main__":
     app.run()