# Denna fil använder funktionen numeric_derivative, som
# finns defnierad  i filen derivata.py.
# Filen är fullt körbar, men behöver ändras / kompletteras
# för att lösa uppgifterna som hör till den.

from derivata import *
import math as m


def f(x):
    # Här definieras funktionen som ska deriveras
    return m.sin(x)


# Detta värde ska gå mot noll, pröva h = 0.1,
# h = 0.01 och # h= 0.001 och se vad det blir
# för skillnad
h = 0.1

# Deriveringspunkt (i det här fallet x = pi)
x = m.pi

# Derivatans funktion skapas med hjälp av
# funktionen numeric_derivative (som definieras
# i filen derivata.py).
# Filen derivata.py måste ligga i samma
# katalog som denna fil (newton-raphson.py).
fprime = numeric_derivative(f, h)
print(f"f'({x:.2f}) ≈ {fprime(x)}")
