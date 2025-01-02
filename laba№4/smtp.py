import smtplib
from email.mime.text import MIMEText


def main():
    # Конфигурация SMTP сервера
    smtp_server = "smtp.mail.ru"
    smtp_port = 587
    username = 'kiselev99055@mail.ru'
    password = 'xBhpgYeV4Fm7ZhbTyNQ0'

    # Создание содержимого письма
    subject = "Тема письма"
    body = "Это текст письма."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = "kiselev9905@gmail.com"

    server = smtplib.SMTP(smtp_server, smtp_port)
    try:
        # Подключение к SMTP серверу
        server.starttls()  # Начало шифрования
        server.login(username, password)  # Вход в аккаунт
        server.sendmail(username, "kiselev9905@gmail.com", msg.as_string())  # Отправка письма
        print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        server.quit()  # Закрытие соединения


if __name__ == "__main__":
    main()