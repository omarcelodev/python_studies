#Mini Log

import time
from datetime import datetime

def log():
    with open("log.txt", "a") as file:
        file.write(f"Programa executado em: {date()}\n")

def date():
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    hour = now.hour
    minutes = now.minute

    return f"{day:02d}/{month:02d}/{year:04d} {hour:02d}:{minutes:02d}"

log()