from Modelo import ListaTanques
from vista import VistaTanques
from controlador import controladorTanque

modelo = ListaTanques()
vista = VistaTanques()
controlador = controladorTanque(modelo, vista)
controlador.ejecutar()
