from flask import Flask, render_template, request

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


if __name__ == "__main__":
    app.run(debug=True)
