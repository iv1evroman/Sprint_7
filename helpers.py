import random
import string


class Helpers:
    def create_random_login(self):
        letters = string.ascii_lowercase
        random_login = ''.join(random.choice(letters) for i in range(10))
        return random_login
