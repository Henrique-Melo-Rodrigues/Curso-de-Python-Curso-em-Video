num = int(input('Informe um número: '))
u = num//1 % 10 #módulo por 10
d = num//10% 10
c = num//100 % 10
m = num//1000 % 10

print(f'Analisando o número {num}...')
print(f'Unidade: {u}')
print(f'Dezeba: {d}')
print(f'centena: {c}')
print(f'Milhar: {m}')

#É possível fatiar um número com matemática.