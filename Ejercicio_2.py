print( "\033[H\033[J")

import matplotlib.pyplot as plt

lluvia = [101.3,116.1,114.5,98.6,71.4,54.3,51.9,58.8,72.8,99.8,107.1,94.7]
mes = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.bar(mes, lluvia,color='r')
plt.title("Promedio precipitaciones por mes CABA")
plt.xlabel("Promedio precipitaciones en mm")
plt.ylabel("Meses")
plt.xticks(range(1,13,1))
plt.yticks(range(1,130,10))
plt.savefig("Precipitaciones.jpg")
plt.show()