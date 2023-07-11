# -*- coding: utf-8 -*-
"""DevJrBr-PythonDoInicio-Exceptions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18a1nUph4MJ4aTyGHmwwLSgzLpOo7_99U

# Python do Início

## Erros e Exceptions

### Links úteis
- https://docs.python.org/pt-br/3/tutorial/errors.html
- https://realpython.com/python-lbyl-vs-eafp/
"""

# '1' + 1

a = '1'
b = 1

print('INÍCIO')

print(a + b)

print('DEU')

if isinstance(a, int):
  print('a é inteiro')
  print(a + b)
else:
  print('a precisa ser inteiro')

int('1') + 1

operando_1 = '1'
operando_2 = 1

try:
  # 1 / 0
  # ... não executa
  soma = operando_1 + operando_2
  print(operando_1 + operando_2)
  # ...
except TypeError:
  print('TypeError')
  operando_1 = int(operando_1)
  operando_2 = int(operando_2)
  print(operando_1 + operando_2)
# ...
except ZeroDivisionError:
  print('Dã, não divida por zero!')
except Exception as e:
  print(f'Erro desconhecido: {e.__class__.__name__}')

print('DEU')