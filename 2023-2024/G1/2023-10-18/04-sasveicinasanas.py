stunda = int(input("Cik ir pulkstens? Raksti tikai stundu!"))

if stunda >= 6 and stunda < 12:
    print("Labrīt!")
elif (stunda >= 23 and stunda <=24) or (stunda >= 0 and stunda < 6):
    print("Ar labunakti!")
elif stunda >= 18:
    print("Labvakar!")
elif stunda >= 12:
    print("Labdien!")
else:
    print("Pulksteņa laiks nepareizs.")