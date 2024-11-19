def dalisana(x, y):
    try:
        atbilde = x / y        
    except ZeroDivisionError:
        return "ar nulli nedali!"
    except TypeError:
        return "nepareizs datu tips"
    else:
        return(atbilde)
    finally:
        print("Šīs ir beigas dalīšanai!")
    

# print(dalisana(4, 2))
# print(dalisana(4, 0))
# print(dalisana("konfekte", 2))
