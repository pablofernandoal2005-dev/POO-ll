from modelo import *
from vista import VistaTanques
from controlador import ControladorTanques

modelo=ListaTanques()
vista=VistaTanques()
controlador=ControladorTanques(modelo,vista)
controlador.ejecutar()