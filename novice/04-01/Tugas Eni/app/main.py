from flask import Flask, render_template, request, redirect
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
        print(request.method)        
        curs.close()
        conn.close()
        
    query = f"select * from data_posyandu"
    curs.execute(query)
    data = curs.fetchall()
    return render_template("index.html", context=data)
   
@app.route("/detail/<data_posyandu_id>")
def detail(data_posyandu_id):
    conn = psycopg2.connect(
        host="localhost",
        database="tugasenimanis",
        user="postgres",
        password="enacantiksekali"
    )
    curs = conn.cursor()
    query = f"select * from data_posyandu where id = {data_posyandu_id}"
    curs.execute(query)
    data = curs.fetchone()
    conn.commit()        
    curs.close()
    conn.close()
    print (data)
    return render_template("detail.html", context=data)

@app.route("/delete/<data_posyandu_id>")
def delete(data_posyandu_id):
    conn = psycopg2.connect(
        host="localhost",
        database="tugasenimanis",
        user="postgres",
        password="enacantiksekali"
    )
    curs = conn.cursor()
    query = f"delete from data_posyandu where id = {data_posyandu_id}"
    curs.execute(query)
    conn.commit()        
    curs.close()
    conn.close()
    return redirect ("/")

@app.route("/update/<data_posyandu_id>" ,methods=["GET", "POST"])
def update(data_posyandu_id):
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
        query = f"update data_posyandu set nama='{nama}', jenis_kelamin='{jenis_kelamin}', tanggal_lahir='{tanggal_lahir}', vitamin_a ='{vitamin_a}', berat_badan = '{berat_badan}', tinggi_badan = '{tinggi_badan}', lingkar_kepala = '{lingkar_kepala}', keterangan = '{keterangan}' where data_posyandu ='{data_posyandu}'"
        

        curs.execute(query)
        conn.commit()
        return redirect("/")

    query = f"select * from data_posyandu where id = {data_posyandy_id}"
    curs.execute(query)
    data = curs.fetchone()
    conn.close()
    conn.close()
    # print("data masuk")
    return render_template("update.html", context=data)

if __name__== "__main__":
    app.run()