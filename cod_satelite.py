G=6.67e-11
m_T=5.97e24
R_T=6371e3
pi=3.1416
T=float(input("Ingrese el periodo en segundos T para un día(24 hrs): "))
T1=float(input("Ingrese el segundo periodo en segundos para (23.93 hrs) T1: "))
h=(((G*m_T*T**2)/(4*pi**2))**(1/3))-R_T
h1=(((G*m_T*T1**2)/(4*pi**2))**(1/3))-R_T
print("La altura para el periodo en 24 hrs es: ",h*(1e-3))
print("La altura para un periodo de 23.93 hrs ingresado es: ",h1*(1e-3))
print("La diferencia en la altura para ambos periodos es: ",(h-h1)*(1e-3))

