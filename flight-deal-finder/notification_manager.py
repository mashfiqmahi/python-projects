import os
import smtplib
from email.message import EmailMessage
from twilio.rest import Client
class NotificationManager:

    def __init__(self):
        # For Twillo
        self.client = Client(
            os.environ["TWILIO_SID"],
            os.environ["TWILIO_AUTH_TOKEN"]
        )

        self.email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_PASSWORD"]
        self.receiver = os.environ["EMAIL_RECEIVER"]

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f"whatsapp:{os.environ['TWILIO_WHATSAPP_NUMBER']}",
            to=f"whatsapp:{os.environ['TWILIO_VERIFIED_NUMBER']}",
            body=message_body
        )
        print("WhatsApp sent:", message.sid)

    def send_email(self, email_list, subject, message_body):
        """
        Sends an email notification using SMTP (Gmail).

        Parameters:
        subject (str): Email subject
        message_body (str): Email body
        """
        email_msg = EmailMessage()
        email_msg["Subject"] = subject
        email_msg["From"] = self.email
        email_msg["To"] = ", ".join(email_list)
        email_msg.set_content(message_body)
        msg = f"Subject:{subject}\n\n{message_body}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            connection.send_message(email_msg)

        print("✅ Email sent successfully to all recipients")