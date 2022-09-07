from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="profilqs2",
        user="postgres",
        password="enacantiksekali"
    )

    curs = conn.cursor()
    if request.method == "POST":
        nama_santri = request.form.get("nama_santri")
        keterangan = request.form.get("keterangan")
        query = f"insert into profilqs2(nama_santri, keterangan) values ('{nama_santri}', '{keterangan}')"
        curs.execute(query)
        conn.commit()        
        curs.close()
        conn.close()

    print(request.method)
    query = f"select * from profilqs2"
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)

if __name__== "__main__":
     app.run()