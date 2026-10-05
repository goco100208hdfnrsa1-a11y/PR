from flask import Flask

app = Flask(__name__)

@app.rute("/", methods=["GET" ,"POST"])
def inicio():
    area = 0
    perimetro = 0
    if request.method == "POST":
       base = float(request.form["base"])
       altura = float(raquest.form["altura"])
       area = (base * altura) / 2
       perimetro = base * 3  
    #Triangulo 

    return
render_template("triangulo.html",area=area, perimetrp=perimetro)

app.run(debug=true)
