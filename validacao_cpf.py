import validate_cpf
from colorama import Fore, Back, Style

nome = str(input('Qual é o seu nome completo ? '))
cpf = str(input('Qual é o numero do seu CPF ? '))
validacao = validate_cpf.is_valid(cpf)
if validacao == True:
    validacao1 = 'válido.'
    print(Fore.GREEN +'O documento informado é um documento válido.')
    print(Style.RESET_ALL)
else:
    validacao1 = 'inválido.'
    print(Fore.RED + 'O documento informado não é um documento válido.')
    print(Style.RESET_ALL)
print('Olá',nome,'você informou um documento', validacao1)