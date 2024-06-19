from PersonaNatural import *
class CuentaAhorro:

    def __init__(self, propietario: PersonaNatural, saldo):
        if not isinstance(propietario, PersonaNatural):
            raise TypeError("El titular debe ser una persona natural.")
        else:
            self.propietario = propietario

        self.saldo = saldo
        self.numeroCuenta = 0
        self.herramientasHabilitadas = False
