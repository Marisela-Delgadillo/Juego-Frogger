from OpenGL.GL import *
from glew_wish import *
import glfw
from Modelo import *
import math
from cmath import cos, pi, sin

angulo_nube = 0
fase = 330.0

class Nube(Modelo):

    global angulo_nube 
    global fase 
    
    def __init__(self, x, y, z, velocidad, direccion):
        super().__init__(x, y, z, velocidad, direccion)

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y,0.0)
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

    def actualizar(self, tiempo_delta):
        movimiento_nube = self.velocidad * tiempo_delta
        self.posicion_x = self.posicion_x + (
                math.cos((angulo_nube + fase) * pi / 180.0) * movimiento_nube
            )
        self.posicion_y = self.posicion_y + (
                math.sin((angulo_nube + fase) * pi / 180.0) * movimiento_nube
            )