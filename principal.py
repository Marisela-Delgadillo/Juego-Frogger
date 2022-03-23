from argparse import Action
from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from cmath import cos, pi, sin
from Carro import *
from Rana import *
from Fondo import *
from Nube import *

window = None

tiempo_anterior = 0.0

carros = []
rana = Rana(0.0, -0.95, 0.0, 0.1, 0.0)
fondo = Fondo()
nubes = []


def actualizar():
    global tiempo_anterior
    global window
    global angulo_nube
    global angulo_nube2

    tiempo_actual = glfw.get_time()

    tiempo_delta = tiempo_actual - tiempo_anterior

    for carro in carros:
        carro.actualizar(tiempo_delta)
        if carro.colisionando(rana):
            glfw.set_window_should_close(window)
    for nube in nubes:
        nube.actualizar(tiempo_delta)

    tiempo_anterior = tiempo_actual

def colisionando():
    colisionando = False

    return colisionando    

def draw():
    fondo.dibujar()
    for carro in carros:
        carro.dibujar()
    #carros.dibujar()
    rana.dibujar()
    for nube in nubes:
     nube.dibujar()

def inicializar_carros():
    carros.append(Carro(0.3, -0.85, 0.0, 0.9, 2.0))
    carros.append(Carro(0.8, -0.75, 0.0, 0.4, 3.0))
    carros.append(Carro(-0.4, -0.65, 0.0, 0.6, 3.0))
    carros.append(Carro(-0.8, -0.55, 0.0, 0.9, 2.0))
    carros.append(Carro(0.7, -0.45, 0.0, 0.5, 3.0))
    carros.append(Carro(-0.2, -0.55, 0.0, 1.0, 3.0))
    carros.append(Carro(-0.3, -0.25, 0.0, 0.7, 2.0))
    carros.append(Carro(-0.6, -0.15, 0.0, 0.9, 2.0))
    carros.append(Carro(-0.2, -0.05, 0.0, 1.5, 2.0))
    carros.append(Carro(0.5, 0.05, 0.0, 0.7, 3.0))
    carros.append(Carro(0.3, 0.15, 0.0, 0.9, 3.0))
    carros.append(Carro(0.7, 0.25, 0.0, 0.4, 2.0))
    carros.append(Carro(0.9, 0.75, 0.0, 0.5, 3.0))
    carros.append(Carro(0.2, 0.45, 0.0, 0.8, 3.0))
    carros.append(Carro(-0.4, 0.55, 0.0, 0.9, 2.0))
    carros.append(Carro(0.5, 0.75, 0.0, 0.5, 2.0))
    carros.append(Carro(0.2, 0.85, 0.0, 1.9, 3.0))
    carros.append(Carro(0.5, -0.85, 0.0, 0.4, 2.0))
    carros.append(Carro(0.5, -0.75, 0.0, 0.6, 3.0))
    carros.append(Carro(-0.9, -0.65, 0.0, 1.4, 3.0))
    carros.append(Carro(0.8, -0.55, 0.0, 0.5, 2.0))
    carros.append(Carro(0.9, -0.45, 0.0, 0.6, 3.0))
    carros.append(Carro(-0.8, -0.85, 0.0, 0.7, 3.0))
    carros.append(Carro(-0.2, -0.15, 0.0, 0.5, 2.0))
    carros.append(Carro(-0.5, -0.05, 0.0, 0.9, 2.0))
    carros.append(Carro(0.9, 0.05, 0.0, 0.3, 2.0))
    carros.append(Carro(0.7, 0.15, 0.0, 0.8, 3.0))
    carros.append(Carro(0.2, 0.25, 0.0, 0.9, 3.0))
    carros.append(Carro(0.7, 0.65, 0.0, 0.5, 2.0))
    carros.append(Carro(0.5, 0.45, 0.0, 0.8, 3.0))
    carros.append(Carro(-0.5, 0.55, 0.0, 0.9, 3.0))
    carros.append(Carro(-0.3, 0.65, 0.0, 0.6, 2.0))
    carros.append(Carro(0.8, 0.75, 0.0, 0.5, 2.0))
    carros.append(Carro(0.1, 0.85, 0.0, 0.9, 3.0))

def inicializar_nubes():
    nubes.append(Nube(-1.0, 0.6, 0.0, 0.2, 2.0))
    nubes.append(Nube(-1.2, -0.5, 0.0, 0.1, 3.0))

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

    inicializar_carros()
    inicializar_nubes()

    glfw.set_key_callback(window, rana.key_callback)

    while not glfw.window_should_close(window):
        glClearColor(0.7,0.7,0.7,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #background()
        actualizar()
        draw()
        #nube()

        glfw.poll_events()

        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()