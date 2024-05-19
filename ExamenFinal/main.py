from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/calculoCompras', methods=['GET', 'POST'])
def compra():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarro = int(request.form['pintura'])
        pintura = 9000
        total = tarro * pintura
        descuento = 0

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        desc = total * descuento
        total_con_desc = total - desc

        return render_template('calculoCompras.html', nombre=nombre, edad=edad,
                               tarro=tarro, total=total, total_con_desc=total_con_desc, desc=desc)
    return render_template('calculoCompras.html')


@app.route('/inicioSesion', methods=['GET', 'POST'])
def sesion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']

        if nombre == 'juan' and password == 'admin':
            mensaje = 'Bienvenido administrador juan'
        elif nombre == 'pepe' and password == 'user':
            mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'usuario o contraseña incorrectos'
        return render_template('inicioSesion.html', nombre=nombre, password=password,
                               mensaje=mensaje)
    return render_template('inicioSesion.html')


if __name__ == '__main__':
    app.run(debug=True)
