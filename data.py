from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = {'username': "Mahaa", 'bio':"I am Maha from KSA  i'm studying in university  and i live  in Riyadh"}
    info = {'phone': '123', 'Email':'A@gmail.com', 'Tel':'999','Address':'424km2' }

    return render_template('index.html', user=user,info=info)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True )
