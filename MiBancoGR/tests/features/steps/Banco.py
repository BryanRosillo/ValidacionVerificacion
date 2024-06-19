from CuentaAhorro import *
from PersonaNatural import *
from CuentaCorriente import *
import random


class Banco:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def abrir_cuenta_ahorro(self, personaNatural, saldo):
        cuentaAhorro = CuentaAhorro(personaNatural, saldo)
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

    def abrir_cuenta_corriente(self, persona, monto_apertura):
        cuentaCorriente = CuentaCorriente(persona, monto_apertura)
        self.agregar_cuenta(cuentaCorriente)
        return cuentaCorriente








