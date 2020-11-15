from hashlib import sha256
import random
from secret import get_secret_key

SECRET_KEY = get_secret_key()
def make_password(plaintext, app_name):
    salt = get_hexdigest(SECRET_KEY, app_name)[:20]
    hsh = get_hexdigest(salt, plaintext)
    return ''.join((salt, hsh))
        
def get_hexdigest(salt, plaintext):
    return sha256((salt + plaintext).encode('utf-8')).hexdigest()

def password(plaintext, app_name, length):
    raw_hex = make_password(plaintext, app_name)
    ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')

    num = int(raw_hex, 16)

    chars = []

    while len(chars) < length:
        n = random.randint(0, len(ALPHABET)-1)
        alpha = ALPHABET[n]
        n = random.randint(0, len(alpha)-1)
        chars.append(alpha[n])

    return ''.join(chars)
