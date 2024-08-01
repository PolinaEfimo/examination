
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')

# Список пользователей
users = []


# Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            return render_template('error.html', message='Пароль или логин не могут быть пустыми!'), 401
        else:
            with open('users.txt', 'r', encoding='utf-8') as file:
                if username in file.read():
                    return render_template('login.html', message='Вход успешно выполнен')
    return render_template('login.html')



@app.errorhandler(401)
def error_401(e):
    return render_template("error.html", e='Неверное имя пользователя или пароль'), 401


@app.route("/")
def index():
    return render_template("index.html")

# Страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    message=''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.append({'username': username, 'password': password})
        if not username or not password:
            return render_template('register.html', message='Логин и пароль не могут быть пустыми!')
        else:
            with open('users.txt', 'r', encoding='utf-8') as file:
                if username in file.read():
                    return render_template('register.html', message='Этот логин уже занят!')
                else:
                    with open('users.txt', 'a', encoding='utf-8') as f:
                        f.write(f'{username},{password}\n')
                        return render_template('register.html', message='Успешно зарегистрирован логин и пароль!')
    return render_template('register.html', message=message)




@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/transportation')
def transportation():
    return render_template('transportation.html')

def get_phone_number():
    return '+79998887766'

@app.route('/how_to_get')
def how_to_get():
    return render_template('how_to_get.html')



if __name__ == '__main__':
    app.run(debug=True)
