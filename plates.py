#entrada / saída
import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#processamento
def is_valid(s):

    #Tamanho permitido
    length = len(s)
    if length > 6 or length < 2:
        return False

    alphabet = string.ascii_letters
    numbers = string.digits

    #Começa com pelo menos duas letras
    if not s[:1] in alphabet:
        return False

    last_one = ''
    count_digit = 0
    count_letter = 0

    #Verifica se há pontuação, se p primeiro número = 0 e se tem números entre uma sequência de letras
    for letter in s:

        if letter in alphabet:
            count_letter += 1

            # Verficar se tem uma letra após um número
            if last_one == 'd':
                return False

            last_one = 'l'

        elif letter in numbers:
            count_digit += 1
            last_one = 'd'

            # Verificar se o primeiro número é um zero
            if count_digit == 1 and letter == '0':
                return False

        else:
            return False #Pontuação







    return True

main()