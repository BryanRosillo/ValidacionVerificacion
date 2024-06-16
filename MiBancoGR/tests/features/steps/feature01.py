from behave import *
from Banco import *
from PersonaNatural import *
from CuentaAhorro import *

use_step_matcher("re")



@step("una persona natural quiera aperturar una cuenta de ahorros en el BGR con 0 USD")
def step_impl(context):
    context.banco = Banco("Pichincha")
    context.personaNatural = PersonaNatural("German")
    context.cuentaAhorro = context.banco.abrir_cuenta_ahorro(context.personaNatural)

    assert isinstance(context.cuentaAhorro,CuentaAhorro)
    assert context.cuentaAhorro.saldo == 0



@step("se asigna un número de cuenta único")
def step_impl(context):
    context.banco.asignar_número_de_cuentaÚnico(context.cuentaAhorro)
    assert context.banco.asignar_número_de_cuentaÚnico(context.cuentaAhorro) == True



@step("se crea un usuario para acceder a las herramientas financieras")
def step_impl(context):
    context.banco.habilitar_acceso_a_herramientas_financieras(context.cuentaAhorro)
    assert context.cuentaAhorro.herramientasHabilitadas == True

