#entrada
text = input('input: ')
vowels = ['a', 'e', 'i', 'o', 'u']
omitted = ''

#processamento
for i in text:
    if not i.lower() in vowels:
        omitted += i

#saída
print('Output:', omitted)