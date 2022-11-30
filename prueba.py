from ctypes import Array
from openpyxl import load_workbook
import datetime
import pyautogui as main
from points import AN


Excel = "GESTION.xlsx"

# Conexión con Openpyxl



""" data_names = {
    "NOMBRE_1": AN[0],
    "Espacio": " ",
    "NOMBRE_2": AN[1],
    "APELLIDO_1": AN[2],
    "APELLIDO_2": AN[3],
}



data_firma = {
    "CEDULA": r,
    "Espacio_l":" ",
    "NOMBRE": AN[0],
    "Espacio_2":" ",
    "APELLIDO": AN[2],

} """

#r = sheet['B1'].value
array = [" ",AN[0]," ",AN[2],AN[0],]

def fusion(a,b):
    return a.append(b)

def sumar(*args):
    for i in args:
       i.append(array)
       return i

sumar(" ",AN[0]," ",AN[2])

print(array)