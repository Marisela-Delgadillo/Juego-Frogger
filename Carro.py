from OpenGL.GL import *
from glew_wish import *
import glfw
from Modelo import *

class Carro(Modelo):

    def __init__(self, x, y, z, velocidad, direccion):
        super().__init__(x, y, z, velocidad, direccion)
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior =0.05

    tiempo_anterior = 0.0

    def dibujar(self):
        for i in range(34):
            glPushMatrix()
            glTranslatef(self.posicion_x, self.posicion_y, 0.0)

            if self.direccion == 2:
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

    def actualizar(self, tiempo_delta):
        #global window

        tiempo_actual = glfw.get_time()

        tiempo_delta = tiempo_actual - self.tiempo_anterior
        
        cantidad_movimiento = self.velocidad * tiempo_delta
        if self.direccion == 2.0:
            self.posicion_x = self.posicion_x - cantidad_movimiento
            if self.posicion_x <= -1:
                self.posicion_x = 1
        if self.direccion == 3.0:
            self.posicion_x = self.posicion_x + cantidad_movimiento
            if self.posicion_x >= 1:
                self.posicion_x = -1
        self.tiempo_anterior = tiempo_actual

