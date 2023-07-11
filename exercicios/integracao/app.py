from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    with open('./fabioindex.html', 'r') as f:
        return f.read()

@app.route("/test", methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        return f"Ola {request.form['name']}"
    else:
        return f"Ola Get {request.args.get('name', '')}"
#como subir flask: flask run
#cd trocar de pasta
# dir: lista o que ta dentro da pasta
# flask run --host=0.0.0.0: roda o flask, permitindo outra maquina se conectar
