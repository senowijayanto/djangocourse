import requests
import os

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY", "None")
MAILGUN_API_URL = os.getenv("MAILGUN_URL", "None")
FROM_EMAIL_ADDRESS = os.getenv("MAILGUN_EMAIL", "None")

def send_email(to_address: str, subject: str, body: str):
    resp = requests.post(
        MAILGUN_API_URL, auth=("api", MAILGUN_API_KEY),
        data={
            "from": FROM_EMAIL_ADDRESS,
            "to": to_address,
            "subject": subject,
            "text": body,
        }
    )

    if resp.status_code == 200:
        print("Successfully sent email")

send_email("senowijayanto@gmail.com", "Djangocourse Email", "<h1>Hello, Seno</h1>")