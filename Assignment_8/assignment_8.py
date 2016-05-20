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
        omega.append(omega[i-1]-(g*theta[i-1]/l+q*omega[i-1]-f*math.sin(omega_D*t[i-1]))*dt)
        theta.append(theta[i-1]+omega[i]*dt)
        t.append(t[i-1]+dt)
        i=i+1
    return 0

initialize(theta,omega,t)
calculate(omega,theta,t,i)

plot(t,theta, label="driven pendium", linestyle='-')
legend(loc='upper center')
xlabel('time (s) ')
ylabel('theta (radians) ')
xlim(0,max(t))
show()
    
