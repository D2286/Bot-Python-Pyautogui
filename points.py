import pyautogui as main
import pymsgbox
from openpyxl import load_workbook

Excel = "GESTION.xlsx"

Wb = load_workbook(Excel, data_only=True)
sheet = Wb["Hoja1"]

r = sheet['B1'].value

pymsgbox.rootWindowPosition = "+700+0"
AN = main.prompt(text=' ', title='Nombre + Sexo', default='').split(" ")
btn_estado = main.confirm('Estado Civil', buttons=['Soltero', 'Unión L.', 'Casado'])
btn_genero = main.confirm('GENERO', buttons=['Femenino', 'Masculino'])
del_file = main.confirm('REVISION', buttons=['OK', 'CANCELAR'])


# Se genera directorio que obtiene data para su elección dependiendo de estado y genero
data = {
    'Soltero': (551,349),
    'Unión L.': (598,350),
    'Casado':(567,352),
    'Masculino':( 692,350),
    'Femenino':(704,351),
    'ACTIVOS': "ACTIVOS.pdf",
    'ATECNO': "ATECNO.pdf",
    'SERVIOLA': "SERVIOLA.pdf",
}

data_usuario = {
    'Names': (424,337),
    'Espacios': (424,337),
    'Names_2': (424,337),
    'First_Name': (499,337),
    'Second_Name':(604,336),
}

fechas = {
    'fecha_Mes_ing': (367,383),
    'fecha_Dia_ing': (382,383),
    'fecha_Mes_nac': (658,354),
    'fecha_Dia_nac': (673,354),
}

position = {
    'Num_cc': (453,351),
    'Fecha_nac': (633,354),
    'Fecha_ing': (344,383),
    'Ingreso': (457,380),  
    'Direccion': (344,394),
    'Num_cel': (513,382),
    'Correo': (348,423),
}


data_fechas = list(fechas.values())
data_espacios = [(648,725)] * 5
data_nombres = list(data_usuario.values())
posiciones = list(position.values())
coordenadas = []

# prompts y función que conecta los datos extraidos de data y las posiciones ya conocidas para recorrer en "Union.py"- 


data_names = {
    "NOMBRE_1": AN[0],
    "Espacio": " ",
    "NOMBRE_2": AN[1],
    "APELLIDO_1": AN[2],
    "APELLIDO_2": AN[3],
}

r = sheet['B1'].value

data_firma = {
    "CEDULA": r,
    "Espacio_l":" ",
    "NOMBRE": AN[0],
    "Espacio_2":" ",
    "APELLIDO": AN[2],

}
data_firmas = list(data_firma.values())
data_names_ = list(data_names.values())

estado = data.get(btn_estado)
genero = data.get(btn_genero)

def fusion(a,b):
    return a.append(b)

def data_position():
    fusion(coordenadas,estado)
    fusion(coordenadas,genero)
    return_ubicacion = coordenadas + posiciones + data_fechas + data_espacios + data_nombres
    return return_ubicacion
