import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
R=[4]
T=[5]
a=[0,0,1,0,0,0,0,0,0,0]
t=0
x_ray=range(11)
for i in range(10):
    if a[i]==0:
        R_temp=0.75*R[i]
        R.append(R_temp)

    if a[i]==1:
        t=t+1
        if i==2:
            CV=6
            TA=7
            V=5
        R_temp=R[i]+1.8*t*pow(CV*TA*V,0.5)/(R[i]+V+TA)
        R.append(R_temp)

    if R_temp < 3:
        T_temp = T[i] + pow(0.2, t) * (3 - R_temp)
        T.append(T_temp)
    elif R_temp >= 3:
        T_temp = pow(0.8, t) * T[i] + pow(0.2, t) * (R_temp - 3)
        T.append(T_temp)

x_major_locator = MultipleLocator(1)
plt.figure()
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.plot(T, label='Trust Value')
plt.plot(R, label='Risk Value')
plt.ylim(0,7)
plt.xlim(0,10,1)
plt.grid(alpha=0.3)
plt.legend()
plt.xlabel('Visit times')
plt.ylabel('Values')

plt.show()
