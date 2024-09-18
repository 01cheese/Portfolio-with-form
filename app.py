from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message as MailMessage


app = Flask(__name__)

# Настройка пути к базе данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Настройка Flask-Mail для отправки email через Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '**********@gmail.com'  # Замени на твой Gmail
app.config['MAIL_PASSWORD'] = '**** **** **** ****'  # Введи пароль к почте
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


# Инициализация базы данных
db = SQLAlchemy(app)

mail = Mail(app)

# Определяем модель данных для сообщений
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Создаем таблицы базы данных (только один раз)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')  # Загрузка твоего index.html с формой

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    message = request.form['message']

    try:
        # Сохранение данных в базу данных
        new_message = Message(first_name=first_name, last_name=last_name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
    except Exception as e:
        return f"Error saving to the database: {str(e)}"

    msg = MailMessage('New Message from Contact Form',
                      sender='server_email@gmail.com',  # Почта сервера
                      recipients=['admin@gmail.com'],  # Почта админа
                      reply_to=email)  # Email пользователя, на который админ может ответить

    msg.body = f'New message from {first_name} {last_name} ({email}):\n\n{message}'

    try:
        mail.send(msg)
    except Exception as e:
        return f"Error sending email: {str(e)}"

    return render_template('thanks.html', first_name=first_name, last_name=last_name)

if __name__ == '__main__':
    app.run(debug=True)
