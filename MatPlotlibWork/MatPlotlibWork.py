import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#Формирование данных и построение диаграммы



#Бабочка
x1 = np.arange(-9, 0)
y1 = -1/8*(x1+9)**2+8

x2 = np.arange(1, 10)
y2 = -1/8*(x2-9)**2+8

x3 = np.arange(-9, -7)
y3 = 7*(x3+8)**2+1

x4 = np.arange(8, 10)
y4= 7*(x4-8)**2+1

x5 = np.arange(-8, 0)
y5= 1/49*(x5+1)**2

x6 = np.arange(1, 9)
y6= 1/49*(x6-1)**2

x7 = np.arange(-8, 0)
y7= -4/49*(x7+1)**2

x8 = np.arange(1, 9)
y8= -4/49*(x8-1)**2

x9 = np.arange(-8, -1)
y9= 1/3*(x9+5)**2-7

x10 = np.arange(2, 9)
y10= 1/3*(x10-5)**2-7

x11 = np.arange(-2, 0)
y11= -2*(x11+1)**2-2

x12 = np.arange(1, 3)
y12= -2*(x12-1)**2-2#!

x13 = np.arange(-1, 1.1,0.1)
y13= -4*x13**2+2

x14 = np.arange(-1, 1.1,0.1)
y14= 4*x14**2-6

x15 = np.arange(-1, 0,0.1)
y15= -1.5*x15+2

x16 = np.arange(0, 2)
y16= 1.5*x16+2

plt.subplots()
plt.title("Бабочка") #название графика
plt.tick_params(axis="x", direction="in",length=25, width=5,color="blue",labelsize=14, labelrotation=20)
plt.grid(axis="x", color="green", alpha=.3, linewidth=5, linestyle=":")
plt.grid(True)# Отображение сетки на координатной плоскости


plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16,linewidth=5)# График красного цвета

plt.savefig("my_image.png") # Сохранение изображения или
plt.show() # Вывод изображения на экран



#Кит
plt.title("Кит")
x1= np.arange(-1,10) 
y1= 2/27*x1**2-3

x2= np.arange(-10,0.5) 
y2= 0.04*x2**2-3

x3= np.arange(-9,-2) 
y3= 2/9*(x3+6)**2+1

x4= np.arange(-4,10) 
y4= -1/12*(x4-3)**2+6

x5= np.arange(4,8.1) 
y5= 1/9*(x5-5)**2+2

x6= np.arange(5,8.5) 
y6= 1/8*(x6-7)**2+1.5

x7= np.arange(-13,-8) 
y7= -0.75*(x7+11)**2+6

x8= np.arange(-15,-12) 
y8= -0.5*(x8+13)**2+3

x9=np.arange(-15,-9)
y9=[1]*len(x9)

x10=np.arange(3,4)
y10=[3]*len(x10)

plt.tick_params(axis="x", direction="in",length=25, width=5,color="blue",labelsize=14, labelrotation=20)
plt.grid(axis="x", color="green", alpha=.3, linewidth=5, linestyle=":")
plt.grid(True)


plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
plt.savefig("my_image.png")
plt.show()



#Зонтик
plt.title("Зонтик")
x1= np.arange(-12,13) 
y1= -1/18*x1**2+12

x2= np.arange(-4,5) 
y2= -1/8*x2**2+6

x3= np.arange(-12,-3) 
y3= -1/8*(x3+8)**2+6

x4= np.arange(4,13) 
y4= -1/8*(x4-8)**2+6

x5= np.arange(-4,-0.3) 
y5= 2*(x5+3)**2-9

x6= np.arange(-4,0.2) 
y6= 1.75*(x6+3)**2-10

plt.tick_params(axis="x", direction="in",length=25, width=5,color="blue",labelsize=14, labelrotation=20)
plt.grid(axis="x", color="green", alpha=.3, linewidth=5, linestyle=":")
plt.grid(True)


plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
plt.savefig("my_image.png")
plt.show()



#Лягушка
plt.title("Лягушка")
x1 = np.arange(-7, 7)
y1 = -3/49*x1**2+8

x2 = np.arange(-7, 7)
y2 = 4/49*x2**2+1

x3 = np.arange(-6.8, -2)
y3 = -0.75*(x3+4)**2+11

x4 = np.arange(2, 6.8)
y4 = -0.75*(x4-4)**2+11

x5 = np.arange(-5.8, -2.8)
y5= -(x5+2)**2+9

x6 = np.arange(2.8, 5.8)
y6= -(x6-4)**2+9

x7 = np.arange(-4, 4)
y7= 4/9*x7**2+5

x8 = np.arange(-5.2, 5.2)
y8= 4/9*x8**2-9

x9 = np.arange(-7, -2.8)
y9= -1/16*(x9+3)**2-6

x10 = np.arange(2.8, 7)
y10= -1/16*(x10-3)**2-6

x11 = np.arange(-7, 0)
y11= 1/9*(x11+4)**2-11

x12 = np.arange(0, 7)
y12 = 1/9*(x12-4)**2-11

x13 = np.arange(-7,-4.5)
y13 = -(x13+5)**2

x14 = np.arange(4.5,7)
y14 = -(x14-5)**2

x15 = np.arange(-3,3)
y15 = 2/9*x15**2+2

plt.tick_params(axis="x", direction="in",length=25, width=5,color="blue",labelsize=14, labelrotation=20)
plt.grid(axis="x", color="green", alpha=.3, linewidth=5, linestyle=":")
plt.grid(True)


plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15)
plt.savefig("my_image.png")
plt.show()



#Очки
plt.title("Очки")
x1 = np.arange(-9, 0)
y1 = -2/32*(x1+5)**2+2

x2 = np.arange(1, 10)
y2 = -2/32*(x2-5)**2+2

x3 = np.arange(-9, -1)
y3 = 1/4*(x3+5)**2-3

x4 = np.arange(1, 9)
y4 = 1/4*(x4-5)**2-3

x5 = np.arange(-9, -6)
y5 = -(x5+7)**2+5

x6 = np.arange(6, 9)
y6 = -(x6-6)**2+5

x7 = np.arange(-1, 2)
y7 = 0*x7**2+1

plt.tick_params(axis="x", direction="in",length=25, width=5,color="blue",labelsize=14, labelrotation=20)
plt.grid(axis="x", color="green", alpha=.3, linewidth=5, linestyle=":")
plt.grid(True)


plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
plt.savefig("my_image.png")
plt.show()
