print( "\033[H\033[J")

import matplotlib.pyplot as plt
Caba="Caba"
Ushuaia = "Ushuaia"
tempcaba = [9,10,8,7,7,7,7,6,7,9,11,13,14,14,14,14,13,11,10,9,8,8,7,7]
hora = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
tempushuaia = [-2,-2,-1,-1,-1,0,0,0,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,1]

plt.plot(hora,tempcaba,'.-')
plt.plot(hora,tempushuaia,'r.-')
plt.title("Temperatura por hora del 28/06/2023 - CABA - USHUAIA")
plt.xlabel("Horas")
plt.ylabel("Temperatura")
plt.xticks(range(1,25,1))
plt.yticks(range(-2,16,1))
plt.legend(["Caba","Ushuaia"])
plt.show()