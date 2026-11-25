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
                    codigo = self.convertir(self.vista.pedir_codigo())
                    tanque = self.modelo.buscar(codigo)
                    if tanque is None:
                        self.vista.mensaje("Error: no existe ese código.")
                    else:
                        cantidad = self.convertir(self.vista.pedir_cantidad())
                        if tanque.despachar(cantidad):
                            self.vista.mensaje(
                                f"Listo. Quedan {tanque.galones} galones."
                            )
                        else:
                            self.vista.mensaje(
                                f"Error: solo hay {tanque.galones} galones."
                            )

                elif opcion == "4":
                    self.vista.mensaje("hasta pronto")

                else:
                    self.vista.mensaje("Opcion Invalida, vuelva a ingresar ")

            except ValueError:
                self.vista.mensaje("Ingrese un numero valido")
