import random

SecretNumber = random.randint(1,20)
print("Мною загадано число в інтервалі від 1 до 20, Спробуйте його відгадати")

for Attempts in range(1,7):
    print("ваша варіант?")
    attempt =int(input())
    
    if attempt < SecretNumber:
       print("Ваше число менше задуманого")
    elif attempt > SecretNumber: 
       print("Ваше число більше задуманого")
    else:
       break
    
if SecretNumber ==attempt:
       print("Вітаю!!!Ви відгадали число!!")
else:
       print("Ви не вгадали, було задумано число: "+ str(SecretNumber))
      