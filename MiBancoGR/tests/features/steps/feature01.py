from behave import *
from Banco import *
from CuentaCorriente import *
from CuentaAhorro import *
from PersonaJuridica import *


#use_step_matcher("re")

@step("una persona natural quiera aperturar una cuenta de ahorros en el BGR con {monto:f} USD")
def step_impl(context, monto):
    context.banco = Banco("Pichincha")
    context.persona = PersonaNatural("German")
    context.cuenta = context.banco.abrir_cuenta_ahorro(context.persona, monto)

    assert isinstance(context.cuenta, CuentaAhorro)
    assert context.cuenta.saldo > 0


@step("se asigna un número de cuenta único")
def step_impl(context):
    context.banco.asignar_número_de_cuentaÚnico(context.cuenta)
    assert context.banco.asignar_número_de_cuentaÚnico(context.cuenta) == True


@step("se crea un usuario para acceder a las herramientas financieras")
def step_impl(context):
    context.banco.habilitar_acceso_a_herramientas_financieras(context.cuenta)
    assert context.cuenta.herramientasHabilitadas == True


@step('una persona natural quiera aperturar una cuenta de corriente en el BGR con "{monto_apertura:f}" USD')
def step_impl(context, monto_apertura):
    context.banco = Banco("Pichincha")
    context.persona = PersonaNatural("German")
    context.cuenta = context.banco.abrir_cuenta_corriente(context.persona, monto_apertura)

    assert isinstance(context.cuenta, CuentaCorriente)
    assert context.cuenta.saldo >= 200


@step('una persona jurídica quiera aperturar una cuenta de corriente en el BGR con "{monto_apertura:f}" USD')
def step_impl(context, monto_apertura):
    context.banco = Banco("Pichincha")
    context.persona = PersonaJuridica("La favorita S.A")

    context.cuenta = context.banco.abrir_cuenta_corriente(context.persona, monto_apertura)

    assert isinstance(context.cuenta, CuentaCorriente)
    assert context.cuenta.saldo >= 500
