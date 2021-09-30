import smtplib
import ssl
import os

def email_error_report(message):
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("emo.robot.error.report@gmail.com", os.getenv('ERROR_REPORT_EMAIL'))
        server.sendmail("emo.robot.error.report@gmail.com", "felipeferreiramarra@gmail.com", message)
        server.sendmail("emo.robot.error.report@gmail.com", "dinalifabricio@yahoo.com", message)