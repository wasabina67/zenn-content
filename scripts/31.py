import smtplib
from email.mime.text import MIMEText


def main():
    pass


if __name__ == "__main__":
    from_email, to_email = "test@example.com", "test@example.com"
    smtp_server, port, password = "", 587, ""
    main(from_email, to_email, smtp_server, port, password)
