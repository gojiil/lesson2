from flask import Flask, render_template, request, make_response, redirect

# Определение Flask-приложения
app = Flask(__name__)

@app.route('/')
def index():
    # Отображение формы для ввода данных
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    # Создание ответа с перенаправлением на страницу приветствия
    resp = make_response(redirect('/welcome'))
    resp.set_cookie('name', name)
    resp.set_cookie('email', email)
    
    return resp

@app.route('/welcome')
def welcome():
    # Получение данных из cookies
    name = request.cookies.get('name', 'Гость')
    return render_template('welcome.html', name=name)

@app.route('/logout')
def logout():
    # Удаление cookies и перенаправление на главную страницу
    resp = make_response(redirect('/'))
    resp.delete_cookie('name')
    resp.delete_cookie('email')
    
    return resp

# Запуск Flask-приложения
if __name__ == '__main__':
    app.run(debug=True)