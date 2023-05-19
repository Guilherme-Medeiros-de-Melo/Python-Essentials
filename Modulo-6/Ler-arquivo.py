
try:
    f = open("Modulo-6/teste.txt", 'rt', errors='ignore')
    letter = ""
    number = ""
    aux = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for line in f:
        for ch in line:
            if ch in aux:
                number += ch
            else:
                letter += ch
except Exception as e:
    print(e)

print("\nRead letters:\n\"" + letter + '"\n')
print("Read numbers:\n" + number + "\n")