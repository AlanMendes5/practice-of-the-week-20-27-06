import sys
import random
from pyfiglet import Figlet

'''
Em um arquivo chamado figlet.py, implemente um programa que:
    Espera zero ou dois argumentos de linha de comando:
        - Zero se o usuário quiser gerar o texto em uma fonte aleatória.
        - Dois se o usuário quiser gerar texto em uma fonte específica, nesse caso o primeiro dos dois deve ser -f
        ou --font, e o segundo dos dois deve ser o nome da fonte.
    Solicita ao usuário um tipo str de texto.
    Exibe o texto na fonte desejada.
    
    Se o usuário fornecer dois argumentos de linha de comando e o primeiro não for -fou --fonto segundo não for o nome 
    de uma fonte, o programa deverá sair sys.exitcom uma mensagem de erro.'''

# input
args = sys.argv[1:] #slice the list to not consider the file_name
size = len(args)
fonts = Figlet().getFonts()

#zero args = random font | == 2 font = args[2]
if not(size == 0 or size == 2):
    print('Invalid usage')
    sys.exit(0)

#If the lenght of args == 0, will simulate a comand with append of two args and random font.
if size == 0:
    args.append('-f')
    args.append(random.choice(fonts))

if args[0] not in ['-f', '--font']:
    print('Invalid usage')
    sys.exit(0)

if args[1] not in fonts:
    print('Invalid usage')
    sys.exit(0)

text = input("Input: ")

#output
print(Figlet(font=args[1]).renderText(text))