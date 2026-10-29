import numpy as np
import matplotlib.pyplot as plt

diasx=["lun","mar","mie","jue","vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(diasx,califa_va_y)
plt.title("califas en VS con Iker Montoya NC 0105")
plt.xlabel("dias de la semana habil")
plt.ylabel("calificaciones en VS")
plt.grid()
plt.show()