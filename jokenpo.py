from random import randint
import os
from time import sleep


class Teste:
    def __init__(self):
        self.limpar()
        self.tabela()
        self.escolher()
        self.processamento()

    def limpar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def tabela(self):
        print('\033[1;36m=-=-\033[1;97m'*4)
        print('\n\033[1;96mPedra = 1\nPapel = 2\nTesoura = 3\033[1;97m\n')
        print('\033[1;36m=-=-\033[1;97m'*4)

    def escolher(self):
        self.true = True
        while self.true:
            try:
                self.escolha = int(
                    input('\033[1;35mDigite um número da lista acima: \033[1;97m'))
                if 1 <= self.escolha <= 3:
                    sleep(1)
                    self.processamento()
                    self.continuar()
                else:
                    print('\033[1;36m=-=-'*4)
                    print(
                        '\n\033[1;31mPor favor, escolha um dos números apresentados na lista.\033[1;97m')
                    sleep(1)
                    self.limpar()
                    self.tabela()
                    continue

            except ValueError:
                print('\033[1;36m=-=-'*4)
                print(
                    '\n\033[1;31mPor favor, escolha um dos números apresentados na lista.\033[1;97m')
                sleep(1)
                self.limpar()
                self.tabela()
                continue

    def processamento(self):
        bot = randint(1, 3)
        if bot == self.escolha:
            self.msg = '\nEmpate!'
        elif bot == 1 and self.escolha == 2:
            self.msg = '\nO bot escolheu PEDRA e você escolheu PAPEL. Você ganhou!'
        elif bot == 2 and self.escolha == 1:
            self.msg = '\nO bot escolheu PAPEL e você escolheu PEDRA. Você perdeu!'
        elif bot == 1 and self.escolha == 3:
            self.msg = '\nO bot escolheu PEDRA e você escolheu TESOURA. Você perdeu!'
        elif bot == 3 and self.escolha == 1:
            self.msg = '\nO bot escolheu TESOURA e você escolheu PEDRA. Você ganhou!'
        elif bot == 3 and self.escolha == 2:
            self.msg = '\nO bot escolheu TESOURA e você escolheu PAPEL. Você perdeu!'
        elif bot == 2 and self.escolha == 3:
            self.msg = '\nO bot escolheu PAPEL e você escolheu TESOURA. Você ganhou!'
        return 0

    def continuar(self):
        print('\033[1;36m=-=-'*4, f'\033[1;33m{self.msg}', sep='\n')
        continua = input(
            '\n\033[1;32mDeseja continuar? <s/n>: \033[1;97m').upper()
        if continua == 'S':
            self.limpar()
            self.tabela()
            self.escolher()
            self.processamento()
        else:
            self.limpar()
            self.true = False


classe = Teste()
