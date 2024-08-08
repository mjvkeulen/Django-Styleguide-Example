from bb.emails.enums import EmailSendingStrategy
from config.env import env, env_to_enum

# local | mailtrap
EMAIL_SENDING_STRATEGY = env_to_enum(EmailSendingStrategy, env("EMAIL_SENDING_STRATEGY", default="local"))

EMAIL_SENDING_FAILURE_TRIGGER = env.bool("EMAIL_SENDING_FAILURE_TRIGGER", default=False)
EMAIL_SENDING_FAILURE_RATE = env.float("EMAIL_SENDING_FAILURE_RATE", default=0.2)

if EMAIL_SENDING_STRATEGY == EmailSendingStrategy.LOCAL:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if EMAIL_SENDING_STRATEGY == EmailSendingStrategy.MAILGUN:
    EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
    ANYMAIL = {
        "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
        "MAILGUN_API_URL": "https://api.eu.mailgun.net/v3",
        "MAILGUN_SENDER_DOMAIN": env("MAILGUN_SENDER_DOMAIN"),
    }
    EMAIL_SENDER_DOMAIN = ANYMAIL["MAILGUN_SENDER_DOMAIN"]
    EMAIL_LOCAL_PART_PREFIX = env("EMAIL_LOCAL_PART_PREFIX", default="")
    EMAIL_REPLY_DOMAIN = env("EMAIL_REPLY_DOMAIN")

if EMAIL_SENDING_STRATEGY == EmailSendingStrategy.MAILPIT:
    EMAIL_BACKEND = env(
        "DJANGO_EMAIL_BACKEND",
        default="django.core.mail.backends.smtp.EmailBackend",
    )
    EMAIL_TIMEOUT = 5
    EMAIL_HOST = env("EMAIL_HOST", default="mailpit")
    EMAIL_PORT = 1025
