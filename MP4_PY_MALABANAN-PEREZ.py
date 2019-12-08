# malabanan, angelo - perez, eric
# 2-ece-a
# ece2112 machine problem 4: on projectile motion (python solution)

import matplotlib.pyplot as plt
from math import *

def projectile(Yin, Vin, theta, Ax, Ay):
    
    if Ay == 0:
        print ('Error. Acceleration in Y cannot be zero.')
        return
        
    X = []
    Y = []
        
    Vix = Vin * cos(theta*(3.141/180))
    Viy = Vin * sin(theta*(3.141/180))
        
    time = 0
    Xpos = 0
    Ypos = Yin
    disp = 0.01
        
    X.append(Xpos)
    Y.append(Ypos)
        
    while(True):
        
        time = time + disp
            
        Xpos = (Vix * time) +(0.5) * Ax * (time*time)
        Ypos = (Viy * time) +(0.5) * Ay * (time*time) + Yin
            
        X.append(Xpos)
        Y.append(Ypos)
            
        if Ypos < disp:
            break
            
    plt.plot(X, Y)
    
    plt.grid()
    plt.xlabel('Position in X')
    plt.ylabel('Position in Y')
    plt.title('Projectile Motion')
    