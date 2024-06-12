from behave import *

use_step_matcher("re")


class Banco:


class PersonaNatural:
    pass


@step("una persona natural quiera aperturar una cuenta de ahorros en el BGR con 0 USD")
def step_impl(context):
    context.banco = Banco()
    context.personaNatural = PersonaNatural("German")
    cuenta = banco.abrir_cuenta_ahorro(personaNatural)
    # TODO: comprobación
    # Colocar el assert 


@step("se asigna un número de cuenta único")
def step_impl(context):
    banco.asignar_número_de_cuentaÚnico(cuenta)
    # TODO: comprobación



@step("se crea un usuario para acceder a las herramientas financieras")
def step_impl(context):
    cuenta.habilitar_acceso_a_herramientas_financieras()
    # TODO: comprobación