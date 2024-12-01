import requests

MAILGUN_API_KEY = "40d978913b67b768accb23322dabf7db-c02fd0ba-a6463f6c"
MAILGUN_API_URL = "https://api.mailgun.net/v3/sandbox2589808390164319bdcaef2cf6459361.mailgun.org/messages"
FROM_EMAIL_ADDRESS = "mailgun@sandbox2589808390164319bdcaef2cf6459361.mailgun.org"

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