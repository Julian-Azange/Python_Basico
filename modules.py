# own modules
# thirdy party modules
# python modules

print("---Modulos Preconstruidos---")
print("")

import datetime

print(datetime.date.today()) # muestra la fecha actual
print(datetime.timedelta(minutes=100))  # Calcula cuantas horas, minutos son

print("------")
print("")

import fmath
fmath.sumar(1,2)
fmath.restar(1,2)

print("-------")

from fmath import sumar, restar  # otra forma de importar modulos con sus metodos
sumar(20,10)
restar(20,40)
print("")
print("----COLORAMA----")

from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "Hello World")
print(Fore.WHITE + "Hello World")
print(Fore.CYAN + "Hello World")
print(Fore.YELLOW + "Hello World")
