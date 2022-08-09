import time

t = input("Digite o tempo (em segundos): ")

#verificacao de numero
if t.isdigit():
    t = int(t)
else:
    print("Entrada Inválida!")    
    quit()

# t / 60 = sec

while t != 0: 
    min, sec = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(min, sec)
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1
    
print("!!!TEMPO ESGOTADO!!!")