def main():
    fraction = input("Cik pilna ir bāka?")
    percentage = convert(fraction)
    atbilde = gauge(percentage)
    print(atbilde)

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x <= y:
        result = round(x/y*100)
    elif y == 0:
        raise ZeroDivisionError # noteikti izsauc kļūdu
    else:
        raise ValueError

    return result 
        
def gauge(percentage):    
    if 1 < percentage < 98:
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"
    else:
        return "F"

if __name__ == "__main__":
    main()