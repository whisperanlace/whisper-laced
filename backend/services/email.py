# Stub email sender — replace with real provider (SES/Sendgrid) later.
import logging
logger = logging.getLogger("email")

def send_email(to_email: str, subject: str, body: str):
    logger.info({"event":"email_send","to":to_email,"subject":subject,"body":body})
