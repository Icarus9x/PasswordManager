from Crypto.Random import get_random_bytes
import string
import random


def password_generator():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|"

    seed_bytes = get_random_bytes(32)
    seed_int = int.from_bytes(seed_bytes, byteorder="big")

    rng = random.Random(seed_int)

    password = [
        rng.choice(lowercase),
        rng.choice(uppercase),
        rng.choice(digits),
        rng.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols


    for i in range(16):
        password.append(rng.choice(all_chars))

    rng.shuffle(password)
    
    return ''.join(password)
