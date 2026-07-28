import random
import string
from datetime import datetime


def random_email():
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"qa_{suffix}@example.com"


def random_name(prefix="QA_User"):
    suffix = "".join(random.choices(string.ascii_lowercase, k=5))
    return f"{prefix}_{suffix}"


def timestamped_filename(prefix, ext="png"):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{stamp}.{ext}"
