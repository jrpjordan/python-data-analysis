# try/except block

def attemp_float(x):
    try:
        return float(x)
    except (TypeError, ValueError): 
        return x
    
print(attemp_float("1.234"))
print(attemp_float("something"))