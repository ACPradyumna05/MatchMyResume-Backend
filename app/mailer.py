import os
import requests
from dotenv import load_dotenv

load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM", "onboarding@resend.dev")

def send_verification_email(to_email: str, verification_link: str):
    if not RESEND_API_KEY:
        raise Exception("Missing RESEND_API_KEY")

    url = "https://api.resend.com/emails"

    data = {
        "from": EMAIL_FROM,  # MUST BE just the email
        "to": [to_email],
        "subject": "Verify your MatchMyResume account",
        "html": f"""
            <h2>Verify your email</h2>
            <p>Click here:</p>
            <a href="{verification_link}">
                Verify Email
            </a>
            <p>If you did not sign up, ignore this email.</p>
        """,
    }

    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        resp = requests.post(url, json=data, headers=headers)
        print("Resend response:", resp.text)
        resp.raise_for_status()
    except Exception as e:
        print("Mailer error:", e)
        raise
