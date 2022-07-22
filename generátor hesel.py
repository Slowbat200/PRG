# knihovna random
import random

# pro vygenerování číselného hesla (#uppers, #lowers, #all,)

# zvolíme si velká, malá písmena a čísla
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
# zde se vše co jsme si zvolili spojí dohromady
all = numbers + uppers + lowers
# nastavíme si délku hesla
lenght = 20

# a zde se všechno přes join spojí dohromady a po každým spuštění se vygeneruje jiný heslo
password = "".join(random.sample(all, lenght))
print("Your password is:", password)