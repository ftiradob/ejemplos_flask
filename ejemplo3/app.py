from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	nombre = "NADIE"
	return render_template("inicio.html",nombre=nombre)

@app.route('/<cadena>',methods=["GET","POST"])
def saluda(cadena):
	nombre = cadena
	return render_template("inicio.html",nombre=nombre)

@app.route("/articulos/<int:numero>")
def mostrar_ariculo(numero):
    return render_template("articulos.html",id=numero)

app.run(debug=True)