class controladorTanque:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def convertir(self, texto):
        valor = float(texto)
        return int(valor) if valor.is_integer() else valor

    def ejecutar(self):
        opcion = ""
        while opcion != "4":
            opcion = self.vista.menu()
            try:
                if opcion == "1":
                    combustible, precio, galones = self.vista.pedir_datos()
                    codigo = self.modelo.registrar(
                        combustible, self.convertir(precio), self.convertir(galones)
                    )
                    self.vista.mensaje(f"Registrado con el código {codigo}.")

                elif opcion == "2":
                    self.vista.mostrar_tanques(self.modelo.tanques)
                elif opcion == "3":
                    codigo = self.convertir(self.vist.pedir_codigo)
                    if tanque.despachar(cantidad):
                        self.vista.mensaje("no existte se codigo")
                    else:
                        cantidad = self.convertir(self.vista.pedir_cantidad())
                        if tanque.despachar(cantidad):
                            self.vista.mensaje(
                                f"listo quedan {tanque.galones} de galones"
                            )
                        else:
                            self.vista.mensaje(f"solo hay {tanque.galones} de galones")

                elif opcion == "4":
                    self.vista.mensaje("hasta pronto")
                else:
                    self.vista.mensaje("Opcion Invalida, vuelva a ingresar ")
            except ValueError:
                self.vista.mensaje("Ingrese un numero valido")
