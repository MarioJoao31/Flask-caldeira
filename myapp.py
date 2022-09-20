from flask import Flask, render_template, redirect, request, url_for
import datetime
from servo import on, off
from subprocess import call
import socket




sw = 1

app = Flask(__name__)
lista=["Desligado","Ligado"]
datelist=[]

def get_ip_address():
        """ get ip-address of interface being used """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

IP = get_ip_address()


@app.route("/")
@app.route("/home", methods =["POST", "GET"])
def home():
    #zipped=(lista,datelist)
    if sw > 0:
         return render_template("button.html", msg="Desligada",veri=False ,lista=lista, datelist=datelist)
    else:
         return render_template("button.html", msg="Ligada", veri=True, lista=lista, datelist=datelist)
    return render_template("button.html", lista=lista)   

@app.route("/switch", methods =["POST", "GET"])
def switch():
    
    global sw 
    if request.method == "POST":
        sw = sw * -1
        if sw > 0:
            on()
            dt=datetime.datetime.now()
            datelist.insert(0,dt)
            lista.insert(0,"Desligada")
            print(lista)
            return redirect(url_for("home",msg="Desligada" ,lista=lista), datelist=datelist) 
        else:
            off()
            dt=datetime.datetime.now()
            datelist.insert(0,dt)
            lista.insert(0,"Ligada")
            print(lista)
            return redirect(url_for("home",msg="Ligada" ,lista=lista), datelist=datelist)

    return render_template("button.html")

if __name__ == "__main__":
    app.run(host=IP, port=5000, debug=False)

