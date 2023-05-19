LED = []
sum = 0

1
Number = input("Enter numbers from 0 to 9: ")
for i in Number:
    if i.isalnum():
        LED.append(int(i))
    else: continue


#while True:
#    number = int(input("0 to 9: LED | -1: Exit  >>"))
#    if number != -1:
#        LED.append(number)
#        sum += 1
#        continue
#    else: break


LED0 = ['###',' # ','###','###','# #','###','###','###','###','###',]
LED1 = ['# #',' # ','  #','  #','# #','#  ','#  ','  #','# #','# #',]
LED2 = ['# #',' # ','###','###','###','###','###','  #','###','###',]
LED3 = ['# #',' # ','# ','   #','  #','  #','# #','  #','# #','  #',]
LED4 = ['###',' # ','###','###','  #','###','###','  #','###','  #',]


for number in LED:
    print(LED0[number], end=' ')
print('')
for number in LED:
    print(LED1[number], end=' ')
print('')
for number in LED:
    print(LED2[number], end=' ')
print('')
for number in LED:
    print(LED3[number], end=' ')
print('')
for number in LED:
    print(LED4[number], end=' ')
print('')