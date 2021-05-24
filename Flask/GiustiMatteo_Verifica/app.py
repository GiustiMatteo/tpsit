import semaforo
from flask import Flask,request,render_template
import sqlite3
import time

app = Flask(__name__)

s = semaforo.semaforo()


#ESEMPIO di pagina di test
@app.route('/test')
def test(r,g,v,on_off):
    if on_off == "on":
        print("semaforo acceso")
 
        s.rosso(int(r))
        s.verde(int(v))
        s.giallo(int(g))
    else:
        print("semaforo spento")
        for _ in range(3):
            s.giallo(1)
            s.luci_spente(1)
    return 'TEST ESEGUITO!'

@app.route('/configurazione', methods = ["GET","POST"])
def condigurazione():
    if request.method == "POST":
        r =request.form["rosso"]
        g = request.form["giallo"]
        v = request.form["verde"]
        on_off = request.form["on_off"]
        
        test(r,g,v,on_off)

    return render_template("semaforo.html")

@app.route('/db')
def database():
    conn = sqlite3.connect('semaforo.db')

    c = conn.cursor()

    #crete table store
    command1 ="""CREATE TABLE IF NOT EXISTS semaforo(id INTEGER PRIMARY KEY,on_off TEXT,dataora datatime)"""

    c.execute(command1)

    c.execute("INSERT INTO semaforo VALUES(1,'on','23/02/2021 12:23')")

    c.execute("SELECT * FROM semaforo")

    #update
    c.execute("UPDATE semaforo SET on_off = on WHERE id = 2")

    #delete

    c.execute("DELETE FROM semaforo WHERE id = 1")

    results = c.fetchall()
    print(results) 
    conn.commit()
    conn.close() 



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')