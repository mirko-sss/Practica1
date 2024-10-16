from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienessoomos')
def about():
    return render_template('quienessoomos.html')

@app.route('/servicios')
def services():
    return render_template('servicios.html')

@app.route('/noticias')
def news():
    return render_template('noticias.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Aquí puedes manejar los datos del formulario, como almacenarlos en una base de datos o enviarlos por correo.
        return f"Gracias, {name}. Tu mensaje ha sido enviado."
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)