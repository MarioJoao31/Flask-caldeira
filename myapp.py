from flask import Flask, render_template, redirect, request, url_for
from servo import on, off
from subprocess import call
import socket




sw = 1

app = Flask(__name__)

def get_ip_address():
        """ get ip-address of interface being used """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

IP = get_ip_address()


@app.route("/")
@app.route("/home")
def home():
    if sw > 0:
         return render_template("button.html", msg="Desligada",veri=False )
    else:
         return render_template("button.html", msg="Ligada", veri=True)
    return render_template("button.html")   

@app.route("/switch", methods =["POST", "GET"])
def switch():
    global sw 
    if request.method == "POST":
        sw = sw * -1
        if sw > 0:
            on()
            return redirect(url_for("home",msg="Desligada" )) 
        else:
            off()
            return redirect(url_for("home",msg="Ligada" ))

    return render_template("button.html")

if __name__ == "__main__":
    app.run(host=IP, port=5000, debug=False)

