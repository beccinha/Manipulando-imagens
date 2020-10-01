import numpy
import matplotlib.pyplot as plt 

in_array = numpy.linspace(-(2*numpy.pi), 2*numpy.pi, 256) #encontrando os valores de -pi a pi
out_array = numpy.cos(in_array) #encontrando o cosseno de cada valor

print("in_array : ", in_array) 
print("\nout_array : ", out_array) 

# plotagem do grafico
plt.plot(in_array, out_array, color = 'red', marker = "o") 
plt.title("Cosseno") 
plt.xlabel("X") 
plt.ylabel("Y") 
plt.show()