from pathlib import Path
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi import BackgroundTasks
from app.config import Config

config = Config()
TEMPLATE_FOLDER = Path(__file__).parent.parent / "templates"

email_config = ConnectionConfig(
    MAIL_USERNAME=config.MAIL_USERNAME,
    MAIL_FROM=config.MAIL_USERNAME,
    MAIL_PASSWORD=config.MAIL_SECRET,
    MAIL_PORT=config.MAIL_PORT,
    MAIL_SERVER=config.MAIL_SERVER,
    MAIL_SSL_TLS=False,
    MAIL_STARTTLS=True,
    TEMPLATE_FOLDER=TEMPLATE_FOLDER,
)
