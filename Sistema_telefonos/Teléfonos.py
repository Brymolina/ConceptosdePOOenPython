# Clase base: Telefono
class Telefono:
    def __init__(self, numero):
        self._numero = numero  # Encapsulación: atributo protegido

    def llamar(self, destino):
        return f"Llamando al número {destino} desde {self._numero}"

    def mostrar_info(self):
        print(f"Número de teléfono: {self._numero}")


# Clase derivada: Smartphone
class Smartphone(Telefono):
    def __init__(self, numero, marca, sistema_operativo):
        super().__init__(numero)
        self._marca = marca
        self._sistema_operativo = sistema_operativo

    # Polimorfismo: sobrescribimos llamar
    def llamar(self, destino):
        return f"[Smartphone] Videollamada desde {self._numero} a {destino}"

    def mostrar_info(self):
        print(f"Smartphone - Número: {self._numero}, Marca: {self._marca}, SO: {self._sistema_operativo}")


# Clase derivada: Telefonofijo
class TelefonoFijo(Telefono):
    def __init__(self, numero, ubicacion):
        super().__init__(numero)
        self._ubicacion = ubicacion

    # Polimorfismo: sobrescribimos llamar
    def llamar(self, destino):
        return f"[Teléfono Fijo] Llamada desde {self._ubicacion} al {destino}"

    def mostrar_info(self):
        print(f"Teléfono Fijo - Número: {self._numero}, Ubicación: {self._ubicacion}")


# Función que muestra el polimorfismo
def realizar_llamadas(telefonos, destino):
    for tel in telefonos:
        print(tel.llamar(destino))


# Creando instancias que en este caso serian los objetos
telefono1 = Smartphone("0968804359", "Samsung", "Android")
telefono2 = TelefonoFijo("062731927", "Casa")

# Mostrando la información correspondiente
telefono1.mostrar_info()
telefono2.mostrar_info()

# Demostrar polimorfismo
realizar_llamadas([telefono1, telefono2], "0985857660")