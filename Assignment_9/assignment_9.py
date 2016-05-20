from pylab import * 
import math

g=9.8
q=1.0
l=1.0
f=0.2
omega_D=2.0
dt=0.01
theta=[]
omega=[]
t=[]
i=1
theta1=[]
omega1=[]
t1=[]
f1=0
j=1
theta2=[]
omega2=[]
t2=[]
f2=1.2
k=1

def initialize(_theta, _omega, _t):
    global theta, omega, t
    theta=[]
    omega=[]
    t=[]
    t.append(0.)
    theta.append(0.2)
    omega.append(0.)

def calculate(omega, theta, t,i):
    while t[i-1]<25:
        omega.append(omega[i-1]-(g*math.sin(theta[i-1])/l+q*omega[i-1]-f*math.sin(omega_D*t[i-1]))*dt)
        theta.append(theta[i-1]+omega[i-1]*dt)
        t.append(t[i-1]+dt)
        i=i+1
    return 0

def initialize1(_theta1, _omega1, _t1):
    global theta1, omega1, t1
    theta1=[]
    omega1=[]
    t1=[]
    t1.append(0.)
    theta1.append(0.2)
    omega1.append(0.)

def calculate1(omega1, theta1, t1,j):
    while t1[j-1]<25:
        omega1.append(omega1[j-1]-(g*math.sin(theta1[j-1])/l+q*omega1[j-1]-f1*math.sin(omega_D*t1[j-1]))*dt)
        theta1.append(theta1[j-1]+omega1[j-1]*dt)
        t1.append(t1[j-1]+dt)
        j=j+1
    return 0

def initialize2(_theta2, _omega2, _t2):
    global theta2, omega2, t2
    theta2=[]
    omega2=[]
    t2=[]
    t2.append(0.)
    theta2.append(0.2)
    omega2.append(0.)

def calculate2(omega2, theta2, t2,k):
    while t2[k-1]<25:
        omega2.append(omega2[k-1]-(g*math.sin(theta2[k-1])/l+q*omega2[k-1]-f*math.sin(omega_D*t2[k-1]))*dt)
        theta2.append(theta2[k-1]+omega2[k-1]*dt)
        t2.append(t2[k-1]+dt)
        k=k+1
    return 0

initialize(theta,omega,t)
calculate(omega,theta,t,i)
initialize1(theta1,omega1,t1)
calculate1(omega1,theta1,t1,j)
initialize2(theta2,omega2,t2)
calculate2(omega2,theta2,t2,k)

plot(t,theta, label="driven pendium", linestyle='-')
plot(t1,theta1)
plot(t2,theta2)
legend(loc='upper center')
xlabel('time (s) ')
ylabel('theta (radians) ')
xlim(0,max(t))
show()
    
