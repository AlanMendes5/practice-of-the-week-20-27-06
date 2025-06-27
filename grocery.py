'''
Em um arquivo chamado grocery.py, implemente um programa que solicite itens ao usuário, um por linha,
até que ele digite control-d (uma forma comum de encerrar a entrada de dados em um programa).
Em seguida, exiba a lista de compras do usuário em letras maiúsculas, ordenada alfabeticamente por item,
prefixando cada linha com o número de vezes que o usuário digitou aquele item.
    Não é necessário pluralizar os itens.
    Trate a entrada do usuário sem diferenciação entre maiúsculas e minúsculas.
'''

products = dict()

#Loop infinito
while True:
    try:
        item = input("Item: ").upper()

        if item not in products:
            products[item] = 1
        else:
            products[item] += 1

    except EOFError: #encerra se a entrada for um comando, exemplo: ctrl + D

        products = dict(sorted(products.items())) #ordena o dicionário em ordem alfabética.
        #A função sorted() retorna uma tupla, logo é preciso converte-la de volta para dict.

        for key, value in products.items():
        #product.items() -> converte um dicionário para um tupla. Exemplo: {cave:valor} -> (chave, valor)
        #Utiliado para iterar ou classificar um dicionário pois sort() nem for() suportam essa estrutura de dados.

            print(F"{value} {key}")
        break