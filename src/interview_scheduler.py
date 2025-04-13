import smtplib
from email.mime.text import MIMEText

def send_interview_email(email, name):
    msg = MIMEText(f"Dear {name},\n\nYou have been shortlisted for an interview.")
    msg["Subject"] = "Interview Invitation"
    msg["From"] = "recruitment@company.com"
    msg["To"] = email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        server.sendmail("your_email@gmail.com", email, msg.as_string())

if __name__ == "__main__":
    send_interview_email("candidate@example.com", "John")
