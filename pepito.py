import pyautogui as main
from union import union_iterador

from functions import precopy, inicio


# Función y prompt princial

#prueba haciendo merge git


inicio()
revision = main.confirm('REVISION', buttons=['OK', 'CANCELAR'])
precopy()
iterator = union_iterador()

