import hashlib
import random
from colorama import Fore
import os
os.system("")

# Po ilu probach ma pokazać że udało się wykopać
proby = random.randint(100, 89300)
eth = random.randint(0, 500)  # Ile eth ma być wykopane

for i in range(0, proby):
    print(Fore.RED +
          f"[0x{hashlib.sha1(str(i).encode()).hexdigest()}] Kopanie...  Ilość eth: 0.00ETH" + Fore.RESET)

i = random.randint(0, 9999)
print(Fore.GREEN +
      f"[0x{hashlib.sha1(str(i).encode()).hexdigest()}] ZNALEZIONO!!! Ilość eth: {eth/100}ETH" + Fore.RESET)

input()
