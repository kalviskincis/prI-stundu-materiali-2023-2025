# piemēri
saraksts = ["viens", "divi", "trīs"]
cits_saraksts = []

for skaitlis in range(3):
    #print(saraksts[skaitlis])
    cits_saraksts.append(skaitlis)

#print(cits_saraksts)

# 1. uzd.



# 2. uzd.
skaitli = []
skaitlu_kvadrati = []
print(skaitli)
for skaitlis in range(10, 21):
    skaitli.append(skaitlis)
    skaitlu_kvadrati.append(skaitlis**2)

print(skaitli)
print(skaitlu_kvadrati)

# 3. uzd.

fizzbuzz = ["FizzBuzz" if i%3==0 and i%5==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i for i in range(1,22)]
print(fizzbuzz)


# 5. uzd.
t = []
for diena in range(7):
    temp = float(input(f"Kāda temperatūra {diena+1}. dienā?"))
    t.append(temp)
