template = "{0:.2f} {1:s} are worth US$ {2:d}"

amount = 10
rate = 88.46
currency = "Pesos"
# .2f floating number with 2 decs
# s string
# d decimal

print(template.format(88.46, "Argentine Pesos", 1))

print(f"{amount} {currency} is worth US$ {amount / rate:.2f}")