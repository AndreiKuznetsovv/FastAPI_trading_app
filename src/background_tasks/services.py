import smtplib
from email.message import EmailMessage

from src.config import Config
from .config import SMTP_HOST, SMTP_PORT, celery


def get_email_template_dashboard(username: str) -> EmailMessage:
    email = EmailMessage()
    email['Subject'] = 'Натрейдил'
    email['From'] = Config.EMAIL_USER
    email['To'] = Config.EMAIL_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username=username)
    with smtplib.SMTP_SSL(host=SMTP_HOST, port=SMTP_PORT) as server:
        server.login(user=Config.EMAIL_USER, password=Config.EMAIL_PASS)
        server.send_message(email)
