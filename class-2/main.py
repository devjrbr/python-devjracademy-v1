# -*- coding: utf-8 -*-
"""DevJrBr-PythonDoInicio-TiposDeDados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WpqQybdfdroY_T8iphNFFMz3JwBgOLWm

# DevJrBr - Python do Início
## Encontro 2 - Tipos de dados embutidos
- `boolean`
- Numéricos
   - `int`: inteiros
   - `float`: ponto flutuante
   - `complex`: números complexos
- Tipos sequências
   - `list`
   - `tuple`
   - `range`
- `string`
- Tipos conjuntos
   - `set`
   - `frozenset`
- Mapa
   - `dict`

## Links úteis

- Documentação Oficial Python 3
  - [Tipos embutidos](https://docs.python.org/pt-br/3/library/stdtypes.html)
  - [Duck Typing](https://docs.python.org/pt-br/3/glossary.html?highlight=duck%20typing#term-duck-typing)
- [Python Data Structures with Primitive & Non-Primitive Examples | DataCamp](https://www.datacamp.com/tutorial/data-structures-python)
- [Tipos de Variáveis disponíveis no Python - python academy](https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python)
- [Tutorial: Why Functions Modify Lists and Dictionaries in Python](https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/)
"""

import platform

platform.python_version()

"""# Boolean

Teste do valor verdade

Qualquer objeto pode ser testado quanto ao valor de verdade, para uso em uma condição if ou while ou como operando das operações booleanas abaixo.

Por padrão, um objeto é considerado verdadeiro, a menos que sua a classe defina um método __bool__() que retorne False ou um método __len__() que retorna zero, quando chamado com o objeto. 1 Aqui estão a maioria dos objetos embutidos considerados falsos:

    constantes definidas para serem falsas: None e False.

    zero de qualquer tipo numérico: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

    sequências e coleções vazias: '', (), [], {}, set(), range(0)

Operações e funções embutidas que têm um resultado Booleano retornam 0 ou False para falso e 1 ou True para verdadeiro, salvo indicações ao contrário. (Exceção importante: as operações Booleanas or e and sempre retornam um de seus operandos.)
"""

resultado = False or 'Fábio é ok'
print(resultado)

# boolean
## e exemplos de operaçoes com boolean
a = True
b = False

print('"or" é OU:')
print('   ', False, 'OU', False, '==', False or False)
print('   ', False, 'OU', True, '==', False or True)
print('   ', False, 'OU', 'Luis', '==', False or 'Luis')
print('   ', True, 'OU', True, '==', True or True)

a_e_b = a and b
print('"and" é E:')
print('   ', False, 'E', False, '==', False and False)
print('   ', False, 'E', True, '==', False and True)
print('   ', True, 'E', True, '==', True and True)

print('"not" é NÃO:')
nao_a = not a
print('   NÃO', False, '==', not False)
nao_b = not b
print('   NÃO', '==', True, not True)

# comparações
## operações de comparação resultam em valores 'boolean' (True, False)
mundiais_inter = 1
mundiais_gremio = 0
inter_mais_mundiais_gremio = mundiais_inter > mundiais_gremio
print('Inter tem mais mundiais do que o Grêmio?', inter_mais_mundiais_gremio)

mundiais_palmeiras = 0
palmeiras_menos_mundiais_inter = mundiais_palmeiras < mundiais_inter
print('Palmeiras tem menos mundiais do que o Inter?', palmeiras_menos_mundiais_inter)

gremio_nao_tem_mundial = mundiais_gremio == 0
print('Grêmio não tem mundial?', gremio_nao_tem_mundial)

palmeiras_tem_mundial = mundiais_palmeiras >= 1
print('Palmeiras tem mundial?', palmeiras_tem_mundial)

"""# Tipos numéricos

Existem três tipos numéricos distintos: inteiros, números de ponto flutuante e números complexos. Além disso, os booleanos são um subtipo de números inteiros. Inteiros têm precisão ilimitada. Números de ponto flutuante são geralmente implementados usando double em C; informações sobre a precisão e representação interna dos números de ponto flutuante para a máquina na qual seu programa está sendo executado estão disponíveis em sys.float_info. Números complexos têm uma parte real e imaginária, cada um com um número de ponto flutuante. Para extrair essas partes de um número complexo z, use z.real e z.imag. (A biblioteca padrão inclui os tipos numéricos adicionais fractions.Fraction, para racionais, e decimal.Decimal, para números de ponto flutuante com precisão definida pelo usuário.)
"""

# Tipos numéricos

inteiro = -100
ponto_flutuante = 0.3
complexo = complex(2, 1)

print(inteiro, ponto_flutuante, complexo, sep=', ')

print(inteiro, '+', ponto_flutuante, '==', inteiro + ponto_flutuante)

print(inteiro, '+', complexo, '==', inteiro + complexo)

print(ponto_flutuante, '+', complexo, '==', ponto_flutuante + complexo)

"""### Problemas da vida real
Mais detalhes em https://docs.python.org/3/tutorial/floatingpoint.html
"""

print('Hehehehehehe', ponto_flutuante, '* 3', '==', ponto_flutuante*3)

"""# Tipos sequências

Existem três tipos básicos de sequência: listas, tuplas e objetos range. Tipos de sequência adicionais adaptados para o processamento de dados binários e strings de texto são descritos em seções dedicadas.
Operações comuns de sequências

As operações nas seguintes tabelas são suportadas pela maioria dos tipos sequências, ambos mutáveis e imutáveis. A classe ABC collections.abc.Sequence é fornecida para tornar fácil a correta implementação desses operadores em tipos sequências personalizados.

"""

# Tipos sequências
# listas
libertadores_inter = [2006, 2010,]
libertadores_gremio = [ 1995, 2017, ]
libertadores_gauchas = libertadores_inter + libertadores_gremio
libertadores_gauchas

# Tipos sequências
# listas (cont)

# esqueci uma libertadores empoeirada do Greminho :D
# podemos adicionar à lista
libertadores_gremio.append(1983)
libertadores_gauchas = libertadores_inter + libertadores_gremio
libertadores_gauchas

libertadores = libertadores_inter - libertadores_gremio
libertadores

lista = [2010, 0.3, complex(2, 1), 'texto', False, None, ['foi que é uma beleza']]

# tamanho = len(lista)
# lista[4]
# lista[tamanho - 1]
lista[8]

# Tipos sequências
# tuplas
libertadores_inter_tupla = ( 2006, 2010, )
libertadores_gremio_tupla = ( 1995, 2017, )
libertadores_gauchas_tupla = libertadores_inter_tupla + libertadores_gremio_tupla
libertadores_gauchas_tupla

# Tipos sequências
# tuplas (cont)
## ops, esqueci mais uma vez aquela libertadores de 1900 e guaraná com rolha
libertadores_gremio_tupla.append(1983)
libertadores_gauchas_tupla = libertadores_inter_tupla + libertadores_gremio_tupla
libertadores_gauchas_tupla

# Tipos sequências
# range

range_simples = range(10)
range_com_inicio = range(1, 10)
range_com_inicio_e_passo = range(1, 10, 3)

print(range_simples, range_com_inicio, range_com_inicio_e_passo, sep=',')

# Tipos sequências
# range (cont.)
print(list(range_simples))
print(3 in range_simples)

print(list(range_com_inicio_e_passo))
print(3 in range_com_inicio_e_passo)

print(list(range_simples[:3]))
print(range_simples[5])

# Tipos sequências
# metodos padrão

titulos_gauchos_inter = (
    1927, 1934, 1940, 1941, 1942, 1943, 1944, 1945, 1947, 1948,
    1950, 1951, 1952, 1953, 1955, 1961, 1969, 1970, 1971, 1972,
    1973, 1974, 1975, 1976, 1978, 1981, 1982, 1983, 1984, 1991,
    1992, 1994, 1997, 2002, 2003, 2004, 2005, 2008, 2009, 2011,
    2012, 2013, 2014, 2015, 2016,
)
titulos_gauchos_gremio = [
    1921, 1922, 1926, 1931, 1932, 1946, 1949, 1956, 1957, 1958,
    1959, 1960, 1962, 1963, 2023, 1964, 1965, 1966, 1967, 1968,
    1979, 1980, 1985, 1986, 1987, 1988, 1989, 1990, 1993, 1995,
    1996, 1999, 2001, 2006, 2007, 2010, 2018, 2019, 2020, 2021,
    2022, 1977,
]

# len - tamanho
print('Quantidade de títulos.', 'Inter:', len(titulos_gauchos_inter), 'Grêmio:', len(titulos_gauchos_gremio))

# min - menor valor
print('Primeiro título.', 'Inter:', min(titulos_gauchos_inter), 'Grêmio:', min(titulos_gauchos_gremio))

# max - maior valor
print('Último título.', 'Inter:', max(titulos_gauchos_inter), 'Grêmio:', max(titulos_gauchos_gremio))

# in - contém elemento X
campeao_de_tudo = 'campeão de tudo'
feitos_do_inter = ('campeão brasileiro invicto', campeao_de_tudo, )
feitos_do_gremio = ['tri rebaixado', 'nenhum chute a gol contra o Real Madrid', ]

print('Inter é campeão de tudo?', campeao_de_tudo in feitos_do_inter)
print('Grêmio é campeão de tudo?', campeao_de_tudo in feitos_do_gremio)

"""# Strings

Os dados textuais em Python são tratados com objetos str, ou strings. Strings são sequências imutáveis de pontos de código Unicode. As strings literais são escritas de diversas maneiras:

    Aspas simples: 'permitem aspas "duplas" internas'

    Aspas duplas: "permitem aspas 'simples' internas"

    Aspas triplas: '''Três aspas simples''', '''Três aspas duplas'''

Strings de aspas triplas podem expandir por várias linhas – todos os espaços em branco associados serão incluídos em literal string.
"""

# string
##    Aspas simples: 'permitem aspas "duplas" internas'
##    Aspas duplas: "permitem aspas 'simples' internas"
##   Aspas triplas: '''Três aspas simples''', """Três aspas duplas"""

("brasil " "brasileiro") == "brasil brasileiro"

(
    'iofhdiouhfsdioufhiufdhfsiouohfduiofhsdiufhsiuufshiufsdhuisfd '
    'uarheiuhaeiouehauiohaeiouhaeiueahoae '
)

print('fábio'.lower().endswith('io'))
print('fábio'.upper().startswith('FÁ'))
'fábio'[-2:] == 'io'
'fábio'[:2].upper() == 'FÁ'

texto = 'um texto bonito'
texto = 'ok  ko'
texto = 'ok  ko'
texto.upper()

print('fábio'.upper())
print('fábio'.upper().endswith('io'))
print('fábio'.upper().startswith('FÁ'))
print('fábio'.upper().split('B'))

"""# Tipos conjuntos (set e frozenset)

Um objeto conjunto é uma coleção não ordenada de objetos hasheáveis distintos. Usos comuns incluem testes de associação, remover duplicatas de uma sequência e computar operações matemáticas tais como interseção, união, diferença e diferença simétrica. (Para outros tipos de contêineres veja as classes embutidas dict, list e tuple, e o módulo collections.)
"""

# Tipos conjuntos
## set
## frozenset

lista = (12, 2, 4, 4, 5, 56 ,765, 687, 876,76 ,987, 'wywiusyrhious', 56, 'wywiusyrhious',876,876,876,876,876,876,)
len(lista)

lista_unicos = frozenset(lista)
len(lista_unicos)

lista_unicos.add(13)
len(lista_unicos)

a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, }

len(a)

a.add(11)
len(a)
type(a)

"""# Tipo mapa (dict)

Um objeto mapeamento mapeia valores hasheáveis para objetos arbitrários. Mapeamentos são objetos mutáveis. Existe no momento apenas um tipo de mapeamento padrão, o dicionário. (Para outros contêineres, veja as classes embutidas list, set e tuple, e o módulo collections.)

As chaves de um dicionário são quase valores arbitrários. Valores que não são hasheáveis, ou seja, valores contendo listas, dicionários ou outros tipos mutáveis (que são comparados por valor e não por identidade de objeto) não podem ser usados como chaves. Valores que comparam iguais (como 1, 1.0 e True) podem ser usados alternadamente para indexar a mesma entrada do dicionário.
"""

# Mapa
## dict

sou_dicionario = {
    100: ('Porto Alegre', 1_500_000),
    1: ('São Paulo', 12_500_000),
}

sou_dicionario['chave_string']

teste = sou_dicionario.get('chave_string')
print(teste)

sou_dicionario[10] = ('Itaquaquicetuba', 1_200_000)
print(sou_dicionario)

sou_dicionario[10] = ('Pindamonhangaba', 1_100_200_000)
print(sou_dicionario)

"""# Duck Typing


"""

# sou_dicionario.items()
for chave, valor in sou_dicionario.items():
  print('Chave', chave, '|', 'Valor', valor)

def imprime_itens(itens):
  cont = 1
  for item in itens:
    print('Item', cont ,'| Valor', item)
    cont += 1

texto_exemplo = "O Internacional é o maior clube do Rio Grande do Sul"

imprime_itens(texto_exemplo)

palavras_texto = texto_exemplo.split(' ')
palavras_texto

imprime_itens(palavras_texto)

1 in sou_dicionario
0 in sou_dicionario

0 in sou_dicionario.values()

texto = 1
texto = 'texto'
['t', 'e', 'x', 't', 'o']

"""# Valores padrão em funções (pegadinha da vida real)

### Problema famoso com valores padrão de funções e dados mutáveis
"""

# Cuidados da vida real

def func_decora_dict(chave, valor, dict_decorar=None):
  dict_decorar = dict_decorar or {}
  dict_decorar[chave] = valor
  return dict_decorar

func_decora_dict('teste', 1)

func_decora_dict('teste2', 2)

def func_decora_dict_corretamente(chave, valor, dict_decorar=None):
  dict_decorar = dict_decorar or {}
  dict_decorar[chave] = valor
  return dict_decorar

func_decora_dict_corretamente('teste', 1)

func_decora_dict_corretamente('teste2', 2)

def func_lista(*args, lista_default=[]):
  lista_default.extend(args)
  return lista_default

func_lista('teste', 1)

func_lista('teste2', 2)

"""## Esse problema ocorre com listas também"""

def func_lista_corretamente(*args, lista_default=None):
  lista_default = lista_default or []
  lista_default.extend(args)
  return lista_default

func_lista_corretamente('teste', 1)

func_lista_corretamente('teste2', 2)

"""### Por que isso acontece?

Algumas classes de coleção são mutáveis. Os métodos que adicionam, subtraem ou reorganizam seus membros no lugar, e não retornam um item específico, nunca retornam a instância da coleção propriamente dita, mas um None.

(fonte: documentação oficial)
"""
