import secrets
import string

number = string.digits
_pin = "".join(secrets.choice(number) for i in range(4))

intpin = int(_pin)

print(intpin)
