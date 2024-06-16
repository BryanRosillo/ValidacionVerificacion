from CuentaAhorro import *
from PersonaNatural import *
import random

class Banco:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def abrir_cuenta_ahorro(self, personaNatural):
        if not isinstance(personaNatural, PersonaNatural):
            raise TypeError("El titular debe ser una persona natural.")

        cuentaAhorro = CuentaAhorro(personaNatural.nombre)
        self.agregar_cuenta(cuentaAhorro)
        return cuentaAhorro

    def asignar_número_de_cuentaÚnico(self,cuenta):
        numeroCuenta = random.randint(1,100)
        if self.numero_de_cuenta_unico(numeroCuenta):
            cuenta.numeroCuenta = numeroCuenta
            return True
        else:
            return False

    def numero_de_cuenta_unico(self, numeroCuenta):
        for cuenta in self.cuentas:
            if cuenta.numeroCuenta == numeroCuenta:
                return False
        return True

    def habilitar_acceso_a_herramientas_financieras(self, cuenta):
        cuenta.herramientasHabilitadas = True



