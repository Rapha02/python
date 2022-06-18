import random
from string import ascii_letters, digits


class Teste:

    def __init__(self, valor):
        self.letra()
        self.x = valor

    def letra(self):

        a = ascii_letters
        n = digits
        s = ')(*&%$#@!?/'
        self.all = a + n + s

    def cal(self):
        self.senha = "".join(random.sample(self.all, self.x))
        return self.senha


ab = Teste(random.randint(8, 12))
print(ab.cal())
