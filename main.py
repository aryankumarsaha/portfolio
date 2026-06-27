from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import datetime
import os
import smtplib
from email.mime.text import MIMEText

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")


class ContactMessage(BaseModel):
    name: str
    email: str
    message: str


def send_notification_email(contact: ContactMessage):
    # Configuration using Environment Variables
    SMTP_SERVER = "smtp.gmail.com"  # Defaulting to Gmail
    SMTP_PORT = 587
    SENDER_EMAIL = os.environ.get("PORTFOLIO_EMAIL")       # e.g., your_email@gmail.com
    SENDER_PASSWORD = os.environ.get("PORTFOLIO_EMAIL_PASSWORD") # e.g., your 16-digit App Password
    
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("WARNING: Email credentials (PORTFOLIO_EMAIL, PORTFOLIO_EMAIL_PASSWORD) not set. Email not sent.")
        return

    # Create the email message
    msg = MIMEText(f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}")
    msg['Subject'] = f"New Portfolio Contact from {contact.name}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = SENDER_EMAIL   # You will receive the email at your own address
    msg['Reply-To'] = contact.email  # This allows you to hit "Reply" and respond directly to the sender

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Successfully sent email notification.")
    except Exception as e:
        print(f"Failed to send email: {e}")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/api/contact")
async def receive_contact(message: ContactMessage):
    log_entry = (
        f"Timestamp: {datetime.datetime.now().isoformat()}\n"
        f"Name: {message.name}\n"
        f"Email: {message.email}\n"
        f"Message: {message.message}\n"
        f"{'-' * 40}\n"
    )
    # Log to local file
    with open("contacts_log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    # Print to console for server logs
    print(f"\n[CONTACT FORM SUBMISSION]\n{log_entry}")
    
    # Attempt to send the email notification
    send_notification_email(message)
    
    return {"status": "success", "message": f"Thanks, {message.name}! Your message has been received successfully."}