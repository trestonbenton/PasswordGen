# very simple password generator

import random
import string


def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    return password


print(generate_password())