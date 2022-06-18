def ler():
  n = input('\nDigite um número: ')
  try:
    return int(n)
  except ValueError:
    print('\nPor favor, digite um número válido.')
    return ler()
print(f'{str(ler())[::-1]}')
