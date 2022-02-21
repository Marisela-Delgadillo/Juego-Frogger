from argparse import Action
from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from cmath import cos, pi, sin

#nube 
angulo_nube = 0.0
fase = 330.0
velocidad_nube = 0.2
posicion_nube = [-1.0, 0.8, 0.0]

#nube2
angulo_nube2 = 0.0
fase2 = 70.0
velocidad_nube2 = 0.1
posicion_nube2 = [-1.5, -0.8, 0.0]

#unidades por segundo
velocidad = 0.5
posicion_rana = [0.0,-0.95,0.0]
posiciones_cuadrados = [
     [0.3,-0.85, 0.0],
     [0.8, -0.75, 0.0],
     [-0.4, -0.65, 0.0],
     [-0.8, -0.55, 0.0],
     [0.7, -0.45, 0.0],
     [-0.2, -0.55, 0.0],
     [-0.3, -0.25, 0.0],
     [-0.6, -0.15, 0.0],
     [-0.2, -0.05, 0.0],
     [0.5, 0.05, 0.0],
     [0.3, 0.15, 0.0],
     [0.7, 0.25, 0.0],
     [0.9, 0.75, 0.0],
     [0.2, 0.45, 0.0],
     [-0.4, 0.55, 0.0],
     [-0.2, 0.65, 0.0],
     [0.5, 0.75, 0.0],
     [0.2, 0.85, 0.0],
     #mas cuadros
     [0.5,-0.85, 0.0],
     [0.5, -0.75, 0.0],
     [-0.9, -0.65, 0.0],
     [0.8, -0.55, 0.0],
     [0.9, -0.45, 0.0],
     [-0.8, -0.85, 0.0],
     [-0.7, -0.25, 0.0],
     [-0.2, -0.15, 0.0],
     [-0.5, -0.05, 0.0],
     [0.9, 0.05, 0.0],
     [0.7, 0.15, 0.0],
     [0.2, 0.25, 0.0],
     [0.7, 0.65, 0.0],
     [0.5, 0.45, 0.0],
     [-0.5, 0.55, 0.0],
     [-0.3, 0.65, 0.0],
     [0.8, 0.75, 0.0],
     [0.1, 0.85, 0.0]

     
 ]

velocidades_cuadrados=[0.9, 0.4, 0.6, 0.9, 0.5, 1.0, 0.7, 0.9, 1.5, 0.7, 0.9, 0.4, 0.5, 0.8, 0.9, 0.6, 0.5, 1.9, 0.4, 0.6, 1.4, 0.5, 0.6, 0.7, 0.5, 0.9, 0.3, 0.8, 0.9, 0.5, 0.8, 0.9, 0.6, 0.5]
direcciones_cuadrados=[2,3,3,2,3,3,2,2,2,3,3,2,3,3,2,2,3,2,3,3,2,3,3,2,2,2,3,3,2,3,3,2,2,3]

window = None
velocidad_triangulo = 0.1

tiempo_anterior = 0.0

#0 arriba , 1 abajo, 2 izquierda, 3 derecha
direccion_triangulo = 0
angulo_triangulo = 0
angulo_triangulo2 = 0
direccion_derecha = 3
direccion_izquierda = 2


def actualizar():
    global tiempo_anterior
    global window
    global posicion_rana
    global direccion_triangulo
    global angulo_triangulo
    global velocidad_triangulo


    tiempo_actual = glfw.get_time()

    tiempo_delta = tiempo_actual - tiempo_anterior
    
    for i in range(34):
        cantidad_movimiento = velocidades_cuadrados[i] * tiempo_delta
        if direcciones_cuadrados[i] == 2:
            posiciones_cuadrados[i][0] = posiciones_cuadrados[i][0] - cantidad_movimiento
            if posiciones_cuadrados[i][0] <= -1:
                posiciones_cuadrados[i][0] = 1
        if direcciones_cuadrados[i] == 3:
            posiciones_cuadrados[i][0] = posiciones_cuadrados[i][0] + cantidad_movimiento
            if posiciones_cuadrados[i][0] >= 1:
                posiciones_cuadrados[i][0] = -1

    movimiento_nube = velocidad_nube * tiempo_delta
    posicion_nube[0] = posicion_nube[0] + (
            math.cos((angulo_triangulo + fase) * pi / 180.0) * movimiento_nube
        )
    posicion_nube[1] = posicion_nube[1] + (
            math.sin((angulo_triangulo + fase) * pi / 180.0) * movimiento_nube
        )

    movimiento_nube2 = velocidad_nube2 * tiempo_delta
    posicion_nube2[0] = posicion_nube2[0] + (
            math.cos((angulo_triangulo2 + fase2) * pi / 180.0) * movimiento_nube2
        )
    posicion_nube2[1] = posicion_nube[1] + (
            math.sin((angulo_triangulo2 + fase2) * pi / 180.0) * movimiento_nube2
        )


    tiempo_anterior = tiempo_actual

#Movimiento rana
def key_callback(window, key, scancode, action, mods):
    global posicion_rana
    global velocidad_triangulo

    #Que la tecla escape cierre ventana al ser presionada
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window,1)

    #Mover el triangulo
     #IZQUIERDA CON flecha
    if key == glfw.KEY_LEFT and (action == glfw.PRESS):
        if posicion_rana[0] <= -0.9 :
            posicion_rana[0]=posicion_rana[0]
        else:
            posicion_rana[0] =  posicion_rana[0] - velocidad_triangulo
    #DERECHA CON flecha
    if key == glfw.KEY_RIGHT and (action == glfw.PRESS):
        if posicion_rana[0] >= 0.9 :
            posicion_rana[0]=posicion_rana[0]
        else:
            posicion_rana[0] =  posicion_rana[0] + velocidad_triangulo
    #ARRIBA CON flecha
    if key == glfw.KEY_UP and (action == glfw.PRESS):
        if posicion_rana[1] >= 0.9 :
            posicion_rana[1]=posicion_rana[1]
        else:
            posicion_rana[1] =  posicion_rana[1] + velocidad_triangulo
    #ABAJO CON flecha
    if key == glfw.KEY_DOWN and (action == glfw.PRESS):
        if posicion_rana[1] <= -0.9 :
            posicion_rana[1]=posicion_rana[1]
        else:
         posicion_rana[1] =  posicion_rana[1] - velocidad_triangulo

def colisionando():
    colisionando = False

    for i in range(34):
        if (posicion_rana[0] + 0.04 >= posiciones_cuadrados[i][0] - 0.05 
            and posicion_rana[0] - 0.04 <= posiciones_cuadrados[i][0] + 0.05 
            and posicion_rana[1] + 0.04 >= posiciones_cuadrados[i][1] - 0.05 
            and posicion_rana[1] - 0.04 <= posiciones_cuadrados[i][1] + 0.05):
            
            colisionando = True 

    return colisionando

def draw_ranita():
    global posicion_rana
    glPushMatrix()
    glTranslatef(posicion_rana[0], posicion_rana[1],0.0)
    glScalef(0.5,0.5,0.0)  
    #Revisar colision
    if colisionando():
        glfw.set_window_should_close(window)
        glColor3f(1,0,0)
    else:
        glColor3f(13/255,255/255,0/255)

    #RANA
    glTranslatef(0.75,0.2,0.0)
    glBegin(GL_QUADS)

    glVertex3f(-0.76, -0.11, 0.0)
    glVertex3f(-0.76, -0.15, 0.0)
    glVertex3f(-0.80, -0.15, 0.0)
    glVertex3f(-0.80, -0.11, 0.0)

    glVertex3f(-0.74, -0.25, 0.0)
    glVertex3f(-0.74, -0.15, 0.0)
    glVertex3f(-0.82, -0.15, 0.0)
    glVertex3f(-0.82, -0.25, 0.0)

    glVertex3f(-0.72, -0.18, 0.0)
    glVertex3f(-0.72, -0.15, 0.0)
    glVertex3f(-0.84, -0.15, 0.0)
    glVertex3f(-0.84, -0.18, 0.0)

    glVertex3f(-0.72, -0.22, 0.0)
    glVertex3f(-0.72, -0.25, 0.0)
    glVertex3f(-0.84, -0.25, 0.0)
    glVertex3f(-0.84, -0.22, 0.0)

    glVertex3f(-0.72, -0.27, 0.0)
    glVertex3f(-0.72, -0.22, 0.0)
    glVertex3f(-0.74, -0.22, 0.0)
    glVertex3f(-0.74, -0.27, 0.0)

    glVertex3f(-0.82, -0.27, 0.0)
    glVertex3f(-0.82, -0.22, 0.0)
    glVertex3f(-0.84, -0.22, 0.0)
    glVertex3f(-0.84, -0.27, 0.0)

    glVertex3f(-0.82, -0.13, 0.0)
    glVertex3f(-0.82, -0.15, 0.0)
    glVertex3f(-0.84, -0.15, 0.0)
    glVertex3f(-0.84, -0.13, 0.0)

    glVertex3f(-0.72, -0.13, 0.0)
    glVertex3f(-0.72, -0.15, 0.0)
    glVertex3f(-0.74, -0.15, 0.0)
    glVertex3f(-0.74, -0.13, 0.0)
    glEnd()

    glPopMatrix()

def draw_cuadrado():
    global posiciones_cuadrados

    for i in range(34):
        glPushMatrix()
        glTranslatef(posiciones_cuadrados[i][0], posiciones_cuadrados[i][1], 0.0)

        if direcciones_cuadrados[i] == 2:
            glBegin(GL_QUADS)
            glColor3f(255/255,54/255,0/255)
            glVertex3f(-0.03,0.04,0.0)
            glVertex3f(0.05,0.04,0.0)
            glVertex3f(0.05,-0.04,0.0)
            glVertex3f(-0.03,-0.04,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(255/255,143/255,0/255)
            glVertex3f(-0.05,0.04,0.0)
            glVertex3f(0.01,0.04,0.0)
            glVertex3f(0.01,-0.04,0.0)
            glVertex3f(-0.05,-0.04,0.0)
            glEnd()

            #llantas
            glBegin(GL_QUADS)
            glColor3f(0,0,00)
            glVertex3f(-0.05,0.05,0.0)
            glVertex3f(-0.03,0.05,0.0)
            glVertex3f(-0.03,0.04,0.0)
            glVertex3f(-0.05,0.04,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0,0,00)
            glVertex3f(0.05,0.05,0.0)
            glVertex3f(0.03,0.05,0.0)
            glVertex3f(0.03,0.04,0.0)
            glVertex3f(0.05,0.04,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0,0,00)
            glVertex3f(0.05,-0.04,0.0)
            glVertex3f(0.03,-0.04,0.0)
            glVertex3f(0.03,-0.05,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0,0,00)
            glVertex3f(-0.05,-0.04,0.0)
            glVertex3f(-0.03,-0.04,0.0)
            glVertex3f(-0.03,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()

            glPopMatrix()
        else:
            glBegin(GL_QUADS)
            glColor3f(0,122/255,255/255)
            glVertex3f(-0.05,0.04,0.0)
            glVertex3f(0.03,0.04,0.0)
            glVertex3f(0.03,-0.04,0.0)
            glVertex3f(-0.05,-0.04,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(13/255,92/255,165/255)
            glVertex3f(0.05,0.04,0.0)
            glVertex3f(-0.01,0.04,0.0)
            glVertex3f(-0.01,-0.04,0.0)
            glVertex3f(0.05,-0.04,0.0)
            glEnd()

            #llantas
            glBegin(GL_QUADS)
            glColor3f(0,0,00)
            glVertex3f(-0.05,0.05,0.0)
            glVertex3f(-0.03,0.05,0.0)
            glVertex3f(-0.03,0.04,0.0)
            glVertex3f(-0.05,0.04,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0,0,00)
            glVertex3f(0.05,0.05,0.0)
            glVertex3f(0.03,0.05,0.0)
            glVertex3f(0.03,0.04,0.0)
            glVertex3f(0.05,0.04,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0,0,00)
            glVertex3f(0.05,-0.04,0.0)
            glVertex3f(0.03,-0.04,0.0)
            glVertex3f(0.03,-0.05,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0,0,00)
            glVertex3f(-0.05,-0.04,0.0)
            glVertex3f(-0.03,-0.04,0.0)
            glVertex3f(-0.03,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()
            
            glPopMatrix()


def draw():
    draw_ranita()
    draw_cuadrado()

def nube():
    #Nube 1
    glPushMatrix()
    glTranslatef(posicion_nube[0], posicion_nube[1],0.0)
    glScalef(0.5,0.5,0.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.1 * math.cos(angulo * math.pi / 180) -0.1 , 0.12 * math.sin(angulo * math.pi / 180) + 0.65, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.15 * math.cos(angulo * math.pi / 180) -0.15 , 0.09 * math.sin(angulo * math.pi / 180) + 0.61, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.15 * math.cos(angulo * math.pi / 180) + 0.01 , 0.09 * math.sin(angulo * math.pi / 180) + 0.61, 0)
    glEnd()
    glPopMatrix()

    #nube 2
    glPushMatrix()
    glTranslatef(posicion_nube2[1], posicion_nube2[0],0.0)
    glScalef(0.5,0.5,0.0)
    glBegin(GL_POLYGON)
    glColor3f(238/255, 238/255, 238/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.1 * math.cos(angulo * math.pi / 180) -0.1 , 0.12 * math.sin(angulo * math.pi / 180) + 0.65, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(238/255, 238/255, 238/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.15 * math.cos(angulo * math.pi / 180) -0.15 , 0.09 * math.sin(angulo * math.pi / 180) + 0.61, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(238/255, 238/255, 238/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.15 * math.cos(angulo * math.pi / 180) + 0.01 , 0.09 * math.sin(angulo * math.pi / 180) + 0.61, 0)
    glEnd()
    glPopMatrix()




def background():

    #ground
    glBegin(GL_QUADS)
    glColor3f(128/255,128/255,128/255)
    glVertex3f(-1.0,2.0,0.0)
    glVertex3f(1.0,2.0,0.0)
    glVertex3f(1.0,-2.0,0.0)
    glVertex3f(-1.0,-2.0,0.0)
    glEnd()

    #Calle
    glBegin(GL_QUADS)
    glColor3f(84/255,85/255,84/255)
    glVertex3f(-1.0,0.4,0.0)
    glVertex3f(1.0,0.4,0.0)
    glVertex3f(1.0,-0.4,0.0)
    glVertex3f(-1.0,-0.4,0.0)
    glEnd()

    #Banqueta cesped
    glBegin(GL_QUADS)
    glColor3f(125/255, 179/255, 70/255)
    glVertex3f(-1.0,-0.30,0.0)
    glVertex3f(1.0,-0.30,0.0)
    glVertex3f(1.0,-0.40,0.0)
    glVertex3f(-1.0,-0.40,0.0)
    glEnd()

    #banqueta cemento
    glBegin(GL_QUADS)
    glColor3f(179/255, 131/255, 70/255)
    glVertex3f(-1.0,0.30,0.0)
    glVertex3f(1.0,0.30,0.0)
    glVertex3f(1.0,0.40,0.0)
    glVertex3f(-1.0,0.40,0.0)
    glEnd()

    #Roca
    glPushMatrix()
    glScalef(.9,.9,0)
    glTranslatef(0.0,0.6,0.0)
    glBegin(GL_POLYGON)
    glColor3f(93/255, 93/255, 93/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.04 * math.cos(angulo * math.pi / 180) + 0.3 , 0.03 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    glPopMatrix()
    #Roca2
    glPushMatrix()
    glScalef(.7,.7,0)
    glTranslatef(-1.5,0.7,0.0)
    glBegin(GL_POLYGON)
    glColor3f(93/255, 93/255, 93/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.04 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    glPopMatrix()
    #Roca3
    glPushMatrix()
    glScalef(.9,.9,0)
    glTranslatef(-0.5,0.63,0.0)
    glBegin(GL_POLYGON)
    glColor3f(93/255, 93/255, 93/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.04 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    glPopMatrix()

    #Agua inicio
    glBegin(GL_QUADS)
    glColor3f(3/255, 153/255, 185/255)
    glVertex3f(-1.0,-0.9,0.0)
    glVertex3f(1.0,-0.9,0.0)
    glVertex3f(1.0,-1,0.0)
    glVertex3f(-1.0,-1,0.0)
    glEnd()
    
      
    #final
    glBegin(GL_QUADS)
    glColor3f(255/255, 243/255, 1/255)
    glVertex3f(-1.0,0.9,0.0)
    glVertex3f(1.0,0.9,0.0)
    glVertex3f(1.0,1,0.0)
    glVertex3f(-1.0,1,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(-0.8, 1.0,0.0)
    glVertex3f(-0.8,0.9,0.0)
    glVertex3f(-1.0,0.9,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(-0.6,1.0,0.0)
    glVertex3f(-0.4, 1.0,0.0)
    glVertex3f(-0.4,0.9,0.0)
    glVertex3f(-0.6,0.9,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(-0.2,1.0,0.0)
    glVertex3f(0.0, 1.0,0.0)
    glVertex3f(0.0,0.9,0.0)
    glVertex3f(-0.2,0.9,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(0.2,1.0,0.0)
    glVertex3f(0.4, 1.0,0.0)
    glVertex3f(0.4,0.9,0.0)
    glVertex3f(0.2,0.9,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(0.8,1.0,0.0)
    glVertex3f(0.6, 1.0,0.0)
    glVertex3f(0.6,0.9,0.0)
    glVertex3f(0.8,0.9,0.0)
    glEnd()

    #Lienas calle
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0,0.025,0.0)
    glVertex3f(-0.8,0.025,0.0)
    glVertex3f(-0.8,-0.025,0.0)
    glVertex3f(-1.0,-0.025,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.5,0.025,0.0)
    glVertex3f(-0.3,0.025,0.0)
    glVertex3f(-0.3,-0.025,0.0)
    glVertex3f(-0.5,-0.025,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0,0.025,0.0)
    glVertex3f(0.2,0.025,0.0)
    glVertex3f(0.2,-0.025,0.0)
    glVertex3f(0.0,-0.025,0.0)
    glEnd()


    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.5,0.025,0.0)
    glVertex3f(0.7,0.025,0.0)
    glVertex3f(0.7,-0.025,0.0)
    glVertex3f(0.5,-0.025,0.0)
    glEnd()

    #FLOR
    glPushMatrix()
    glScalef(.6,.6,0)
    glTranslatef(-1.08,-0.4,0)

    glBegin(GL_POLYGON)
    glColor3f(186/255, 15/255, 15/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(186/255, 15/255, 15/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.17, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(186/255, 15/255, 15/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.33 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(186/255, 15/255, 15/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.27 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 227/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()
    glPopMatrix()

    #FLOR2
    glPushMatrix()
    glScalef(.6,.6,0)
    glTranslatef(0.9,-0.38,0)

    glBegin(GL_POLYGON)
    glColor3f(248/255, 40/255, 207/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(248/255, 40/255, 207/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.17, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(248/255, 40/255, 207/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.33 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(248/255, 40/255, 207/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.27 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 227/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()
    glPopMatrix()

    #FLOR3
    glPushMatrix()
    glScalef(.6,.6,0)
    glTranslatef(0.5,-0.38,0)

    glBegin(GL_POLYGON)
    glColor3f(126/255, 40/255, 248/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(126/255, 40/255, 248/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.17, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(126/255, 40/255, 248/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.33 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(126/255, 40/255, 248/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.27 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 227/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()
    glPopMatrix()

    	#Neufar
    glPushMatrix()
    glScalef(.9,.9,0)
    glTranslatef(0.33,-0.83,0.0)
    glBegin(GL_POLYGON)
    glColor3f(40/255, 121/255, 17/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.04 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    glPopMatrix() 

	#tronco
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.3, 0.3)
    glVertex3f(-0.9,-0.92,0.0)
    glVertex3f(-0.4, -0.92,0.0)
    glVertex3f(-0.4,-0.98,0.0)
    glVertex3f(-0.9,-0.98,0.0)
    glEnd()

	#Lienas calle & Cruce peatonal
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0,0.025,0.0)
    glVertex3f(-0.8,0.025,0.0)
    glVertex3f(-0.8,-0.025,0.0)
    glVertex3f(-1.0,-0.025,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0,0.125,0.0)
    glVertex3f(-0.8,0.125,0.0)
    glVertex3f(-0.8,0.075,0.0)
    glVertex3f(-1.0,0.075,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0,0.225,0.0)
    glVertex3f(-0.8,0.225,0.0)
    glVertex3f(-0.8,0.175,0.0)
    glVertex3f(-1.0,0.175,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0,-0.075,0.0)
    glVertex3f(-0.8,-0.075,0.0)
    glVertex3f(-0.8,-0.125,0.0)
    glVertex3f(-1.0,-0.125,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0,-0.175,0.0)
    glVertex3f(-0.8,-0.175,0.0)
    glVertex3f(-0.8,-0.225,0.0)
    glVertex3f(-1.0,-0.225,0.0)
    glEnd()


    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.5,0.025,0.0)
    glVertex3f(-0.3,0.025,0.0)
    glVertex3f(-0.3,-0.025,0.0)
    glVertex3f(-0.5,-0.025,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0,0.025,0.0)
    glVertex3f(0.2,0.025,0.0)
    glVertex3f(0.2,-0.025,0.0)
    glVertex3f(0.0,-0.025,0.0)
    glEnd()


    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.5,0.025,0.0)
    glVertex3f(0.7,0.025,0.0)
    glVertex3f(0.7,-0.025,0.0)
    glVertex3f(0.5,-0.025,0.0)
    glEnd()
    #alcantarilla    
    glBegin(GL_POLYGON)
    glColor3f(84/255,85/255,84/255)
    for angulo in range(0,359,5):
        glVertex3f(0.075 * math.cos(angulo * math.pi / 180) + 0.01, 0.075 * math.sin(angulo * math.pi / 180) + 0.65, 0)
    glEnd()


    




def main():
    global window

    width = 700
    height = 700

    if not glfw.init():
        return

    window = glfw.create_window(width, height, "Mi ventana", None, None)

    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glewExperimental = True

    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    version = glGetString(GL_VERSION)
    print(version)

    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        glClearColor(0.7,0.7,0.7,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        background()
        actualizar()
        draw()
        nube()


        glfw.poll_events()

        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()