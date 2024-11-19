def dalisana(x, y):
    try:
        rezultats = x / y        
    except ZeroDivisionError:
        return "ar nulli nedali!"
    except TypeError:
        return "šo datu tipu nevar dalīt"
    else:
        return rezultats
    finally:
        print("Šīs ir programmas beigas")
    

print(dalisana(5, 10))
print(dalisana(5, 0))
print(dalisana("konfekte", 2))
