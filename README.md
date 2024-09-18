# Singular Website - Contact Form with Flask and SQLite

## Project Overview
This project is a simple, yet functional website template designed with HTML5, CSS, and Bootstrap, integrated with a backend powered by Flask and SQLite. The primary feature of the site is a contact form, which allows users to submit their name, email, and message. Upon submission, the data is stored in an SQLite database, and an email is sent to the administrator. After the form submission, the user is redirected to a thank-you page, which automatically returns to the home page after a few seconds.

## Features
- **Responsive Design**: Built with Bootstrap to ensure the website looks great on all devices.
- **Contact Form**: Users can send their name, email, and a message, which is saved in an SQLite database and emailed to the admin.
- **Email Notifications**: On form submission, the administrator receives an email notification with the details of the message.
- **Flask Backend**: The backend is developed using Flask, which handles form processing and email sending.
- **SQLite Database**: Messages are stored in a local SQLite database for easy management and access.
- **Automatic Redirect**: After form submission, users are thanked on a separate page, and then redirected back to the home page after a short delay.

## Technologies Used
- **Frontend**:
  - HTML5, CSS3, Bootstrap for responsive design.
  - JavaScript and jQuery for interactive features.
  
- **Backend**:
  - Flask: Micro web framework used to handle routing and form processing.
  - Flask-Mail: For sending email notifications.
  - SQLite: Lightweight database for storing submitted form data.

## Getting Started

### Prerequisites
To run this project locally, you need to have the following installed:
- Python 3.x
- Flask
- Flask-Mail
- SQLite (comes pre-installed with Python)
- Any SMTP server (for email functionality, such as Gmail)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/singular-website.git
   ```

2. Navigate to the project directory:

   ```bash
   cd singular-website
   ```

3. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```bash
   pip install Flask Flask-Mail
   ```

### Configuration

1. **Database Setup**: The SQLite database is automatically created when you first run the application.
   
2. **Email Setup**: You need to configure Flask-Mail to send email notifications. Open `app.py` and update the following lines with your SMTP settings (for example, if you're using Gmail):

   ```python
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-email-password'
   ```

   If you're using Gmail, you also need to enable "Less Secure Apps" in your Gmail account.

### Running the Application

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your browser and go to:

   ```
   http://127.0.0.1:5000
   ```

3. You should see the homepage of the website. Fill out the contact form to test the functionality.

### Project Structure

```
singular-website/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   ├── js/
│   │   └── main.js
├── templates/
│   ├── index.html
│   └── thanks.html
├── app.py
├── README.md
└── messages.db
```

- `static/`: Contains static assets such as CSS, JavaScript, and images.
- `templates/`: Contains HTML templates for the website.
- `app.py`: The main Flask application file, which handles routing, form submission, database interaction, and email sending.
- `messages.db`: The SQLite database file where all form submissions are stored.

## Features to be Added
- Add CSRF protection for the form.
- Improve the design of the thank-you page.
- Add the ability to export messages from the database in CSV format.

## License
This project is licensed under the MIT License.


### Описание разделов:
1. **Project Overview** — краткое описание проекта и его функциональности.
2. **Features** — список ключевых возможностей проекта.
3. **Technologies Used** — используемые технологии, как на фронтенде, так и на бэкенде.
4. **Getting Started** — пошаговое руководство по установке и запуску проекта.
5. **Project Structure** — описание файлов и папок в проекте.
6. **Features to be Added** — идеи для будущих улучшений.
