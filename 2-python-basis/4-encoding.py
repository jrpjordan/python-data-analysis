# Unicode has become first-class string type to enable more consistent handling of ASCII and non ASCII

val = "español"

print(val)

val_utf8 = val.encode("utf-8")

print(val_utf8)

print(val_utf8.decode("utf-8"))

print(val.encode("latin1"))