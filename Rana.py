from OpenGL.GL import *
from glew_wish import *
import glfw
from Carro import *
from Modelo import *

class Rana(Modelo):

    def __init__(self, x, y, z, velocidad, direccion):
        super().__init__(x, y, z, velocidad, direccion)
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.04
        self.extremo_superior =0.04

    #carros = Carro()

        #Movimiento rana
    def key_callback(self,window, key, scancode, action, mods):
        #Que la tecla escape cierre ventana al ser presionada
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window,1)

        #Mover el triangulo
        #IZQUIERDA CON flecha
        if key == glfw.KEY_LEFT and (action == glfw.PRESS):
            if self.posicion_x <= -0.9 :
                self.posicion_x=self.posicion_x
            else:
                self.posicion_x =  self.posicion_x - self.velocidad
        #DERECHA CON flecha
        if key == glfw.KEY_RIGHT and (action == glfw.PRESS):
            if self.posicion_x >= 0.9 :
                self.posicion_x=self.posicion_x
            else:
                self.posicion_x =  self.posicion_x + self.velocidad
        #ARRIBA CON flecha
        if key == glfw.KEY_UP and (action == glfw.PRESS):
            if self.posicion_y >= 0.9 :
                self.posicion_y=self.posicion_y
            else:
                self.posicion_y =  self.posicion_y + self.velocidad
        #ABAJO CON flecha
        if key == glfw.KEY_DOWN and (action == glfw.PRESS):
            if self.posicion_y <= -0.9 :
                self.posicion_y=self.posicion_y
            else:
                self.posicion_y =  self.posicion_y - self.velocidad


    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y,0.0)
        glScalef(0.5,0.5,0.0)  

        #RANA
        glTranslatef(0.75,0.2,0.0)
        glBegin(GL_QUADS)
        glColor3f(13/255,255/255,0/255)

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
