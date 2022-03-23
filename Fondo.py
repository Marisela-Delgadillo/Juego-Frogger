from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from cmath import cos, pi, sin

class Fondo:

    def dibujar(self):
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