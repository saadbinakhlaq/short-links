from datetime import datetime
from typing import Optional
import datetime

def verify_expiration_date(expiration_date: datetime.datetime) -> bool:
    return datetime.datetime.now(datetime.timezone.utc) < expiration_date