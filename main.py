from flask import Flask, render_template, request
import distancia_form
import math
app = Flask(__name__)


@app.route("/resultado", methods=("GET", "POST"))
def multe():
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        operacion = request.form['operacion']
    if operacion == 'suma':
        resultado = num1 + num2
        print(resultado)
    elif operacion == 'resta':
        resultado = num1 - num2
        print(resultado)
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
        print(resultado)
    elif operacion == 'division':
        if num2 != 0:
            resultado = num1 / num2
            print(resultado)
        else:
            return "Error: No se puede dividir por cero."
    else:
        return "Error: Operación no válida."

    return render_template('calculadora.html', resultado=resultado)


@app.route("/calculadora")

def op():
    return render_template('calculadora.html')


@app.route("/distancia", methods=("GET", "POST"))

def dt():
    dts = distancia_form.UseForm(request.form)
    result4 = 0
    if request.method == 'POST':
        num1 = int(dts.x1.data)
        num2 = int(dts.y1.data)
        num3 = int(dts.x2.data)
        num4 = int(dts.y2.data)
        res1 = (num3 - num1)
        res2 = (num4 - num2)
        result1 = (res1 ** 2)
        result2 = (res2 ** 2)
        result3 = result1 + result2
        result4 = math.sqrt(result3)
        print(result4)

        
    return render_template("distancia.html", form=dts, resultado=result4)

if __name__ == "__main__":
    app.run(debug=True)
