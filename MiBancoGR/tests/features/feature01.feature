# Created by Bryan at 12/6/2024
# language:es

Característica: Aperturar cuenta bancaria
  Como cliente del banco
  quiero aperturar una cuenta bancaria de acuerdo a mis proyecciones de ahorro
  para poder realizar operaciones bancarias.

  Esquema del escenario: Persona natural que apertura una cuenta de ahorros
    Cuando una persona natural quiera aperturar una cuenta de ahorros en el BGR con <monto> USD
    Entonces se asigna un número de cuenta único
    Y se crea un usuario para acceder a las herramientas financieras
    Ejemplos:
    |monto|
    |0    |
    |200  |
    |500  |

    
  Escenario: Persona natural que apertura una cuenta corriente
    Cuando una persona natural quiera aperturar una cuenta de corriente en el BGR con "200.0" USD
    Entonces se asigna un número de cuenta único
    Y se crea un usuario para acceder a las herramientas financieras

  Escenario: Persona jurídica que apertura una cuenta corriente
    Cuando una persona jurídica quiera aperturar una cuenta de corriente en el BGR con "500.0" USD
    Entonces se asigna un número de cuenta único
    Y se crea un usuario para acceder a las herramientas financieras

