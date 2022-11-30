from data_excel import fila_excel
from points import data_position
from functions import puntero, function_copy


data_excel_total = fila_excel()
coordenadas = data_position()

# Unión de (coordenadas y data de excel) iteradas

def union_iterador():
    for a, b in zip(coordenadas, data_excel_total):
        puntero(a)
        function_copy(b)

""" def union_iterador():
    for a, b in zip(coordenadas, data_excel_total):
        print(a)
        print(b) """