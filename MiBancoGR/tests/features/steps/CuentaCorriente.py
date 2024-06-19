from PersonaNatural import *
from PersonaJuridica import *

class CuentaCorriente:

    def __init__(self, propietario, saldo):
        self.propietario = propietario

        if isinstance(propietario, PersonaNatural):
            if saldo < 200:
                raise TypeError("Una persona NATURAL solo puede abrir la cuenta con más de 200 $.")
            else:
                self.saldo = 200

        if isinstance(propietario, PersonaJuridica):
            if saldo < 500:
                raise TypeError("Una persona JURÍDICA solo puede abrir la cuenta con más de 500 $.")
            else:
                self.saldo = 500
        self.numeroCuenta = 0
        self.herramientasHabilitadas = False
