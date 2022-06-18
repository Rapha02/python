import os
from random import randint
from time import sleep


class JogoDaVelha_PvB:

    def __init__(self):
        self.a = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.limpar()
        self.jogadas = 0
        self.ganhador = 0
        self.tabela()
        self.vez = 0
        self.vezj()

    def limpar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def tabela(self):

        print(f'\033[1;36m   0   1   2')
        print(f'\033[1;36m0: {self.a[0][0]} | {self.a[0][1]} | {self.a[0][2]}')
        print('\033[1;36m  -----------')
        print(f'\033[1;36m1: {self.a[1][0]} | {self.a[1][1]} | {self.a[1][2]}')
        print('\033[1;36m  -----------')
        print(f'\033[1;36m2: {self.a[2][0]} | {self.a[2][1]} | {self.a[2][2]}')
        print(f'\033[1;97mJogadas: {self.jogadas}')

    def vezj(self):
        if self.vez == 0 and self.ganhador == 0:
            self.player1()
        elif self.vez == 1 and self.ganhador == 0:
            self.bot()

    def jogada(self):
        self.limpar()
        self.tabela()
        self.player1()

    def player1(self):
        print(
            '\033[1;92m\nSua vez! Escolha uma linha e uma coluna para continuar.')
        try:
            coluna = int(input('\033[1;97mColuna: '))
            if 0 > coluna or coluna >= 3:
                print('\033[1;31m\nDigite um valor válido!')
                sleep(1.25)
                self.jogada()
            linha = int(input('\033[1;97mLinha: '))

            if self.a[linha][coluna] == ' ':
                self.a[linha][coluna] = '\033[1;97mX\033[1;36m'
                self.jogadas += 1
            else:
                print('\033[1;31m\nEsta posição já foi ocupada!')
                sleep(1.25)
                self.jogada()
        except ValueError:
            print('\033[1;31m\nDigite um valor válido!')
            sleep(1.25)
            self.jogada()
        except IndexError:
            print('\033[1;31m\nDigite um valor válido!')
            sleep(1.25)
            self.jogada()
        finally:
            if self.ganhador == 0:
                sleep(1)
                self.ganhar()
                if self.ganhador == 0:
                    self.limpar()
                    self.tabela()
                    self.vez = 1
                    self.vezj()
                else:
                    self.jnovamente()
            else:
                pass

    def bot(self):
        print('\n\033[1;92mO bot está jogando...')

        while True:
            coluna = randint(0, 2)
            linha = randint(0, 2)
            if self.a[coluna][linha] == ' ':
                self.a[coluna][linha] = '\033[1;97mO\033[1;36m'
                self.jogadas += 1
                if self.ganhador == 0:
                    sleep(1)
                    self.ganhar()
                    if self.ganhador == 0:
                        self.limpar()
                        self.tabela()
                        self.vez = 0
                        self.vezj()
                    else:
                        self.jnovamente()
                else:
                    pass
                break
            else:
                continue

    def ganhar(self):
        v = ('\033[1;97mX\033[1;36m' if self.vez ==
             0 else '\033[1;97mO\033[1;36m')
        vjogada = ('O bot' if self.vez == 1 else 'Você')
        if self.a[0][0] == v and self.a[0][1] == v and self.a[0][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[1][0] == v and self.a[1][1] == v and self.a[1][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[2][0] == v and self.a[2][1] == v and self.a[2][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][0] == v and self.a[1][0] == v and self.a[2][0] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][1] == v and self.a[2][1] == v and self.a[1][1] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][2] == v and self.a[1][2] == v and self.a[2][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][0] == v and self.a[1][1] == v and self.a[2][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][2] == v and self.a[1][1] == v and self.a[2][0] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.jogadas >= 9:
            self.gn = '\nVelha!'
            self.ganhador = 1
        if self.ganhador == 1:
            self.limpar()
            self.tabela()
            print(f'\033[1;93m{self.gn}')

    def jnovamente(self):
        print(f"\033[1;36m=-=-"*5)
        valor = input(
            '\n\033[1;92mDeseja jogar novamente? <s/n>: \033[1;97m').upper()
        if valor == 'S':
            self.limpar()
            Comecar()
        else:
            self.ganhador = -1
            self.limpar()


class JogoDaVelha_PvP:

    def __init__(self):
        self.a = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.limpar()
        self.jogadas = 0
        self.ganhador = 0
        self.tabela()
        self.vez = 1
        self.player()

    def limpar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def tabela(self):

        print(f'\033[1;36m   0   1   2')
        print(f'\033[1;36m0: {self.a[0][0]} | {self.a[0][1]} | {self.a[0][2]}')
        print('\033[1;36m  -----------')
        print(f'\033[1;36m1: {self.a[1][0]} | {self.a[1][1]} | {self.a[1][2]}')
        print('\033[1;36m  -----------')
        print(f'\033[1;36m2: {self.a[2][0]} | {self.a[2][1]} | {self.a[2][2]}')
        print(f'\033[1;97mJogadas: {self.jogadas}')

    def jogada(self):
        self.limpar()
        self.tabela()
        self.player()

    def player(self):
        print(
            f'\033[1;92m\nPlayer {self.vez}, é sua vez! Escolha uma linha e uma coluna para continuar.')
        try:
            coluna = int(input('\033[1;97mColuna: '))
            if 0 > coluna or coluna >= 3:
                print('\033[1;31m\nDigite um valor válido!')
                sleep(1.25)
                self.jogada()
            linha = int(input('\033[1;97mLinha: '))

            if self.a[linha][coluna] == ' ':
                self.a[linha][coluna] = '\033[1;97mX\033[1;36m' if self.vez == 1 else '\033[1;97mO\033[1;36m'
                self.jogadas += 1
            else:
                print('\033[1;31m\nEsta posição já foi ocupada!')
                sleep(1.25)
                self.jogada()
        except ValueError:
            print('\033[1;31m\nDigite um valor válido!')
            sleep(1.25)
            self.jogada()
        except IndexError:
            print('\033[1;31m\nDigite um valor válido!')
            sleep(1.25)
            self.jogada()
        finally:
            if self.ganhador == 0:
                sleep(1)
                self.ganhar()
                if self.ganhador == 0:
                    self.limpar()
                    self.tabela()
                    self.vez = 1 if self.vez == 2 else 2
                    self.player()
                else:
                    self.jnovamente()

    def ganhar(self):
        v = ('\033[1;97mX\033[1;36m' if self.vez ==
             1 else '\033[1;97mO\033[1;36m')
        vjogada = ('Player 1' if self.vez == 1 else 'Player 2')
        if self.a[0][0] == v and self.a[0][1] == v and self.a[0][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[1][0] == v and self.a[1][1] == v and self.a[1][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[2][0] == v and self.a[2][1] == v and self.a[2][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][0] == v and self.a[1][0] == v and self.a[2][0] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][1] == v and self.a[2][1] == v and self.a[1][1] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][2] == v and self.a[1][2] == v and self.a[2][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][0] == v and self.a[1][1] == v and self.a[2][2] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.a[0][2] == v and self.a[1][1] == v and self.a[2][0] == v and self.jogadas <= 9:
            self.ganhador = 1
            self.gn = f'\n{vjogada} ganhou!'
        elif self.jogadas >= 9:
            self.gn = '\nVelha!'
            self.ganhador = 1
        if self.ganhador == 1:
            self.limpar()
            self.tabela()
            print(f'\033[1;93m{self.gn}')

    def jnovamente(self):
        print(f"\033[1;36m=-=-"*5)
        valor = input(
            '\n\033[1;92mDeseja jogar novamente? <s/n>: \033[1;97m').upper()
        if valor == 'S':
            self.limpar()
            Comecar()
        else:
            self.ganhador = -1
            self.limpar()


class Comecar:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.msg()

    def msg(self):
        print(
            '\033[1;92mOlá! Este programa possui 2 modos de jogo, um deles contra um BOT, e outro contra um Player.')
        print('\033[1;36m=-=-'*4)
        print('BOT = \033[1;97m1\n\033[1;36mPlayer = \033[1;97m2')
        print('\033[1;36m=-=-'*4)
        while True:
            try:
                decide = int(
                    input('\033[1;92mQual deles você quer jogar? \033[1;97m'))
                if decide in [1, 2]:
                    break
                else:
                    print('Por favor, digite um valor válido!')
                    sleep(1.25)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.msg()
            except ValueError:
                print('Por favor, digite um valor válido!')
                sleep(1.25)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.msg()
        if decide == 1:
            JogoDaVelha_PvB()
        else:
            JogoDaVelha_PvP()
            pass


Comecar()
