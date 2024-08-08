from enum import Enum


class EmailSendingStrategy(Enum):
    LOCAL = "local"
    MAILGUN = "anymail"
    MAILPIT = "mailpit"
