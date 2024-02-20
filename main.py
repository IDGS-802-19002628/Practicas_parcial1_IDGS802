from flask import Flask, render_template, request
from io import open
import distancia_form
import resistencia_form
import diccionario_form
import math
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/diccionario")
def dco():
    dco = diccionario_form.UseForm(request.form)
    return render_template('diccionario.html', form=dco)


@app.route("/diccionario_guardar",  methods=("GET", "POST"))
def diccionario_guardar():
    dic = diccionario_form.UseForm(request.form)
    ing = ''
    esp = ''
    if request.method == 'POST':
        ing = dic.ing.data
        esp = dic.esp.data
        print(ing)
        print(esp)

        archivo_texto = open("diccionario.txt", 'a')
        archivo_texto.write('\n' + ing + '\n' + esp)
        archivo_texto.close()
    print(dic.validate())

    return render_template('diccionario.html', form=dic)


@app.route("/diccionario_consultar",  methods=("GET", "POST"))
def diccionario_consultar():
    dicr = diccionario_form.UseForm(request.form)
    valor = 0
    valor2 = 0
    valor3 = 0
    d = ''
    f = ''
    msg = ''
    v = ''
    diccionarioE = []
    diccionarioG = []
    diccionarioI = []

    archivo_texto = open("diccionario.txt", 'r')
    for lineas in archivo_texto.readlines():
        valor += 1
        diccionarioE.append(lineas.rstrip())

    print('Completa', diccionarioE)
    for item in range(0, len(diccionarioE), 2):
        diccionarioG.append(diccionarioE[item])
    print('Espanol', diccionarioG)
    for item in range(1, len(diccionarioE), 2):
        diccionarioI.append(diccionarioE[item])
    print('Ingles', diccionarioI)
    op = dicr.radios.data
    spain = dicr.spain.data
    print('Valor radio ', op)
    if op == '2':
        print('ingles')
        if request.method == 'POST':

            archivo_texto = open("diccionario.txt", 'r')

            for item in range(1, len(diccionarioI), 1):
                valor3 += 1
                if spain == diccionarioI[item]:
                    print("match: " + spain)
                    print('index', valor3)
                    v = valor3
                    valor1 = v+1
                    d = diccionarioG[valor1]
                    valor2 = valor1+1
                    f = diccionarioG[valor1]

                    print(valor1)
                    print(valor2)
                    print("valor1 d", d)
                    print("valor2 f", f)
                

            archivo_texto.close()

            print(v)
            if v == '':
                msg = 'Palabra no encontrada {}'.format(spain)

    else:
        print('espanol')
        if request.method == 'POST':

            archivo_texto = open("diccionario.txt", 'r')

            for item in range(1, len(diccionarioG), 1):
                valor2 += 1
                if spain == diccionarioG[item]:
                    print("match: " + spain)
                    print('index', valor2)
                    v = valor2
                    valor1 = v-1
                    d = diccionarioI[valor1]
                    valor2 = valor1-1
                    f = diccionarioI[valor1]

                    print(valor1)
                    print(valor2)
                    print("valor1 d", d)
                    print("valor2 f", f)
                

            archivo_texto.close()

            print(v)
            if v == '':
                msg = 'Palabra no encontrada {}'.format(spain)

    return render_template('diccionario.html', form=dicr, v=valor, ig=f, m=msg)


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


@app.route("/resistencia", methods=("GET", "POST"))
def rt():
    val0 = 0
    val1 = 0
    val2 = 0
    val3 = 0
    val4 = 0
    val5 = 0

    color1 = ''
    color2 = ''
    color3 = ''
    hexs1 = ''
    hexs2 = ''
    hexs3 = ''
    hexs4 = ''
    tolerancia = ''
    rf = resistencia_form.UseForm(request.form)
    r1 = rf.r1.data
    r2 = rf.r2.data
    r3 = rf.r3.data
    val3 = r3
    radios = rf.radios.data

    if r1 == '0':
        color1 = 'Negro'
        hexs1 = "#000000"
    if r1 == '1':
        color1 = 'Cafe'
        hexs1 = "#8B4513"
    if r1 == '2':
        color1 = 'Rojo'
        hexs1 = "#FF0000"
    if r1 == '3':
        color1 = 'Naranja'
        hexs1 = "#FFA500"
    if r1 == '4':
        color1 = 'Amarillo'
        hexs1 = "#FFFF00"
    if r1 == '5':
        color1 = 'Verde'
        hexs1 = "#008000"
    if r1 == '6':
        color1 = 'Azul'
        hexs1 = "#0000FF"
    if r1 == '7':
        color1 = 'Violeta'
        hexs1 = "#8A2BE2"
    if r1 == '8':
        color1 = 'Gris'
        hexs1 = "#808080"
    if r1 == '9':
        color1 = 'Blanco'
        hexs1 = "#FFFFFF"

    if r2 == '0':
        color1 = 'Negro'
        hexs2 = "#000000"
    if r2 == '1':
        color2 = 'Cafe'
        hexs2 = "#8B4513"
    if r2 == '2':
        color2 = 'Rojo'
        hexs2 = "#FF0000"
    if r2 == '3':
        color2 = 'Naranja'
        hexs2 = "#FFA500"
    if r2 == '4':
        color2 = 'Amarillo'
        hexs2 = "#FFFF00"
    if r2 == '5':
        color2 = 'Verde'
        hexs2 = "#008000"
    if r2 == '6':
        color2 = 'Azul'
        hexs2 = "#0000FF"
    if r2 == '7':
        color2 = 'Violeta'
        hexs2 = "#8A2BE2"
    if r2 == '8':
        color2 = 'Gris'
        hexs2 = "#808080"
    if r2 == '9':
        color2 = 'Blanco'
        hexs1 = "#FFFFFF"

    if r3 == '':
        color3 = 'Negro'
        hexs3 = "#000000"
    if r3 == '0':
        color3 = 'Cafe'
        hexs3 = "#8B4513"
    if r3 == '00':
        color3 = 'Rojo'
        hexs3 = "#FF0000"
    if r3 == '000':
        color3 = 'Naranja'
        hexs3 = "#FFA500"
    if r3 == '0000':
        color3 = 'Amarillo'
        hexs3 = "#FFFF00"
    if r3 == '00000':
        color3 = 'Verde'
        hexs3 = "#008000"
    if r3 == '000000':
        color3 = 'Azul'
        hexs3 = "#0000FF"
    if r3 == '0000000':
        color3 = 'Violeta'
        hexs3 = "#8A2BE2"
    if r3 == '00000000':
        color3 = 'Gris'
        hexs3 = "#808080"
    if r3 == '000000000':
        color2 = 'Blanco'
        hexs3 = "#FFFFFF"

    if radios == '0.10':
        tolerancia = 'Plata'
        hexs4 = "#C0C0C0"
    if radios == '0.05':
        tolerancia = 'Oro'
        hexs4 = "#FFD700"

    r1 = "0" if r1 is None else str(r1)
    r2 = "0" if r2 is None else str(r2)
    r3 = "0" if r3 is None else str(r3)
    radios = 0 if radios is None else radios
    val0 = str(r1) + str(r2)
    val1 = str(r1) + str(r2) + str(r3)
    val2 = int(val1)
    val3 = val2 * float(radios)
    val4 = val2 + val3
    val5 = val2 - val3
    print(color1)
    return render_template("resistencia.html", form=rf, co1=color1, col2=color2, col3=color3, valor1=val1, maxima=val4, minima=val5, hex1=hexs1, hex2=hexs2, hex3=hexs3, hex4=hexs4, tr=tolerancia, valtr=radios)


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
