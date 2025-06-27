'''
Em um arquivo chamado taqueria.py, implemente um programa que permita ao usuário fazer um pedido,
solicitando itens, um por linha, até que o usuário pressione Ctrl-d (uma forma comum de encerrar a
entrada de dados em um programa). Após cada item inserido, exiba o custo total de todos os itens
inseridos até o momento, prefixado com um cifrão ( $) e formatado com duas casas decimais.
    Trate a entrada do usuário sem distinção entre maiúsculas e minúsculas.
    Ignore qualquer entrada que não seja um item.
    Suponha que todos os itens do menu sejam escritos com maiúsculas e minúsculas .
'''

prices = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0

while True:
    try:
        order = input("Item: ").lower()
        total += prices[order]
        print(F"${total:.2f}")
    except EOFError:
        exit(0)
