chave_api='AIzaSyDL556ldYXgdcIV_q2lDhZMnEABOL4wSyw'

from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bancodadosteste-f88fe-default-rtdb.firebaseio.com/'
})

@app.route('/add_user', methods=['POST'])
def add_user():
    nome = request.form['nome']
    idade = request.form['idade']
    ref = db.reference('/usuarios')
    ref.push({
        'nome': nome,
        'idade': idade
    })
    return 'Usuário adicionado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
