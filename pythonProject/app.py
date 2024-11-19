from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])

        asistencia = float(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3) / 3)


        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        return render_template('resultado.html',
 promedio=promedio, estado=estado)
    else:
        return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        return render_template('resultado2.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)
    else:
        return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)