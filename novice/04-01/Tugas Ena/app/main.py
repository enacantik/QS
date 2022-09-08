from flask import Flask, render_template, request, redirect
import psycopg2
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="profilsantriqoryatussalam",
        user="postgres",
        password="enacantiksekali"
    )

    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        jenis_kelamin = request.form.get("jenis_kelamin")
        keterangan = request.form.get("keterangan")
        query = f"insert into profilsantriqoryatussalam(nama, keterangan) values('{nama}', '{keterangan}')"
        curs.execute(query)
        conn.commit()
        print(request.method)        
        curs.close()
        conn.close()
        
    query = f"select * from profilsantriqoryatussalam"
    curs.execute(query)
    data = curs.fetchall()
    return render_template("index.html", context=data)
   
@app.route("/detail/<data_posyandu_id>")
def detail(profilsantriqoryatussalam_id):
    conn = psycopg2.connect(
        host="localhost",
        database="profilsantriqoryatussalam",
        user="postgres",
        password="enacantiksekali"
    )
    curs = conn.cursor()
    query = f"select * from profilsantriqoryatussalam where id = {profilsantriqoryatussalam_id}"
    curs.execute(query)
    data = curs.fetchone()
    conn.commit()        
    curs.close()
    conn.close()
    print (data)
    return render_template("detail.html", context=data)

@app.route("/delete/<profilsantriqoryatussalam_id>")
def delete(profilsantriqoryatussalam_id):
    conn = psycopg2.connect(
        host="localhost",
        database="profilsantriqoryatussalam",
        user="postgres",
        password="enacantiksekali"
    )
    curs = conn.cursor()
    query = f"delete from profilsantriqoryatussalam where id = {daprofilsantriqoryatussalam_id}"
    curs.execute(query)
    conn.commit()        
    curs.close()
    conn.close()
    return redirect ("/")

@app.route("/update/<profilsantriqoryatussalam_id>" ,methods=["GET", "POST"])
def update(profilsantriqoryatussalam_id):
    conn = psycopg2.connect(
        host="localhost",
        database="tugasenimanis",
        user="postgres",
        password="enacantiksekali"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")

        keterangan = request.form.get("keterangan")
        query = f"update data_posyandu set nama='{nama}', keterangan = '{keterangan}' where data_posyandu ='{profilsantriqoryatussalam}'"
        curs.execute(query)
        conn.commit()
        return redirect("/")

    query = f"select * from profilsantriqoryatussalam where id = {profilsantriqoryatussalam_id}"
    curs.execute(query)
    data = curs.fetchone()
    conn.close()
    conn.close()
    # print("data masuk")
    return render_template("update.html", context=data)

if __name__== "__main__":
    app.run()