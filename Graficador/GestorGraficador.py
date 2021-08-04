import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



funciones = { "sin" : "np.sin" , "cos" : "np.cos" , "tan" : "np.tan" , "log" : "np.log" ,"pi" : "np.pi" , "sqrt" : "np.sqrt" , "exp" : "np.exp",
"sec":"1/np.cos","csc":"1/np.sin","cot":"1/np.tan", "ones":"np.ones", "size":"np.size"}

rango_u1 = "0"
rango_u2 = "2*pi"

rango_v1 = "0"
rango_v2 = "pi"

def reemplazo(a):
    for i in funciones:
        if i in a:
            a=a.replace(i, funciones[i])
    return a

def reemplazoMultiplicacionVectorial(function):
    while True:
        splited = function.split('*')
        flag = len(splited)
        for i in range(1, flag):
            if ('u' in splited[i] or 'v' in splited[i]) and ('u' in splited[i-1] or 'v' in splited[i-1]):
                function = ('*'.join(splited[:i-1]) + '*' if i-1>=0 else '') + 'np.outer(' + splited[i-1] + ',' + splited[i] + ')' + ('*' + '*'.join(splited[i+1:]) if i+1<flag else '')
                i+=1
        splited = function.split('*')
        if len(splited) == flag:
            break
    return function

rango_u1=reemplazo(rango_u1)
rango_u2=reemplazo(rango_u2)
rango_v1=reemplazo(rango_v1)
rango_v2=reemplazo(rango_v2)


u = np.linspace(eval(rango_u1),eval(rango_u2), 100)
v = np.linspace(eval(rango_v1),eval(rango_v2), 100)



funcion_x = "10*cos(u)*sin(v)"
funcion_x = reemplazoMultiplicacionVectorial(reemplazo(funcion_x))

funcion_y = "10*sin(u)*sin(v)"
funcion_y = reemplazoMultiplicacionVectorial(reemplazo(funcion_y))

funcion_z = "10*ones(size(u))*sin(v)"
funcion_z = reemplazoMultiplicacionVectorial(reemplazo(funcion_z))

#funcion_x = "10*np.outer(np.sqrt(u), np.cos(v))"
#funcion_y = "5*np.outer(np.sqrt(u), np.sin(v))"
#funcion_z = "np.outer(np.ones(np.size(u)), u)"




def parametroX(funcion_x):
    x = eval(funcion_x)
    return x

def parametroY(funcion_y):
    y = eval(funcion_y)
    return y

def parametroZ(funcion_z):
    z = eval(funcion_z)
    return z

x= parametroX(funcion_x)
y= parametroY(funcion_y)
z= parametroZ(funcion_z)


ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b')
plt.show()

