from app.mailer import send_verification_email

try:
    send_verification_email("pradyumnasingh2103@gmail.com", "https://example.com/verify/test")
    print("Email sent OK!")
except Exception as e:
    print("FAILED:", e)
