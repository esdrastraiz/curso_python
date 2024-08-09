# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# srt, int, float, bool 
print(1 + 1)
print('a' + 'b')
# print('1' + 1) nesse caso vai dar erro
# porque não pode concatenar string com int
print(int('1'), type('1'))
# nesse caso pode se fazer essa conversão
# de str para int
print(float('1') + 1)
print(float('1.2') + 1)
# aqui ele vai entender que o '1' é uma float
# e vai realizar a soma.
print(bool(''))
print(bool(' '))
# uma str vazia sem espaço dá 'false'
# e uma str vazia com espaço dá 'true'

