'''
Em um arquivo chamado fuel.py, implemente um programa que solicite ao usuário uma fração, formatada como X/Y,
em que cada um de Xe Yé um número inteiro, e então exiba, como uma porcentagem arredondada para o número inteiro
mais próximo, a quantidade de combustível no tanque. Se, no entanto, restar 1% ou menos, exiba Eem vez disso para
 indicar que o tanque está essencialmente vazio. E se restarem 99% ou mais, exiba Fem vez disso para indicar que
 o tanque está essencialmente cheio.

Se, no entanto, X ou Y não for um inteiro, Xfor maior que Y, ou Yfor 0, em vez disso, pergunte ao usuário novamente.
(Não é necessário que Y seja 4).
Certifique-se de capturar quaisquer exceções como ValueErrorou ZeroDivisionError.
'''


def main():
    #entrada-processamento
    z = get_division()

    #Saída
    if z <= 1:
        print('E')

    elif z > 99:
        print('F')

    else:
        print(f'{z}%')

def get_division():
    while True:
        try:
            #Entrada
            fraction = input('Fraction: ') #Entrada 1/4

            fraction = fraction.split('/') #Utilizando a função split para separar x, y tendo como delimitador '/'

            x = int(fraction[0]) # .split() retorna uma lista ['x', 'y'].
            y = int(fraction[1]) # x = int('x') y = int('y')

            #Processamento
            if x > y or y == 0:
                continue

            z = round((x/y) * 100)
            #roud: arredonda para o inteiro mais próximo. Por exemplo: 0.25 * 100 = 25.0 => round(25.0) = 25.

        except (ValueError, ZeroDivisionError):
            pass
            #pass é uma instrução nula, ou seja: ela não faz nada, apenas preenche o espaço!
            #Nessa situação, o pass serve para retornar à pergunta do usuário sem exibir a mesma mensagem de erro repetidamente.
        else:
            return z

main()