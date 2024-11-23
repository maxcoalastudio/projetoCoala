import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy import array
import time
from PIL import Image
from PrimitiveObjects import PrimitiveObjects
from Camera import Camera
#from Mesh import Mesh
from Lights import Lights

if not glfw.init():
    raise Exception("Falha ao iniciar")

width, height = 1280, 720
window = glfw.create_window(width, height, "Coala Engine Ver0.0.1", None, None)
if not window:
    raise Exception("Falha ao criar a janela")

icon = "icon.png"
glfw.set_window_icon(window, 1, Image.open(icon))
glfw.make_context_current(window)
glfw.swap_interval(1)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, width / height, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

camera = Camera(width, height)
#aqui chama os objetos primitivos da classe PrimitiveObjects
cubo = PrimitiveObjects()
esfera = PrimitiveObjects()
lights = Lights()
glClearColor(0.5, 0.5, 0.5, 1)
glfw.set_key_callback(window, camera.key_callback)
glfw.set_cursor_pos_callback(window, camera.mouse_callback)



#mesh = Mesh([-5, -5, 0], [5, 5, 0], [0, 0, -1], 10000)
"""
# Variáveis para calcular o FPS
frame_count = 0
start_time = time.time()
def calculate_fps(frame_count, start_time):
    frame_count += 1
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= 1.0:  # Atualizar o FPS a cada segundo
        fps = frame_count / elapsed_time
        print(f"FPS: {fps:.2f}")  # Exibe no console
        frame_count = 0
        start_time = current_time
    return frame_count, start_time
"""
while not glfw.window_should_close(window):
    glfw.poll_events()
    camera.process_input(window)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    camera.updateCamera()
    # Calcular FPS
    #frame_count, start_time = calculate_fps(frame_count, start_time)

    #criando a camera
    
    #chamando as figuras bidimensionais
    #quads()#desenhando o quadrado
    #tris()#desenhando o triangulo
    #circle(0.4, -0.3, 0.3, 20)
    
    cubo.cube(2, 2, 2)
    
    esfera.esfera(0 , 0, 0, 0.5, 10, 10) 
    #piramide()
    #esfera(0.08, 20, 20)
    #fazendo o cubo rotacionar pelo angulo acrescido

    #angle +=  0.1
    #dir+= 0.04
    #lights.configurar_luz_pontual(GL_LIGHT2, [2, 1, 0], [0.6, 0, 0], 0.7)#ponto de luz vermelho

    #lights.configurar_luz_pontual(GL_LIGHT3, [0, 1, 2], [0, 0.6, 0], 0.7)#ponto de luz verde

    lights.configurar_luz_pontual(GL_LIGHT4, [0, 1, -2], [0, 0, 0.6], 0.7)#ponto de luz azul

    #lights.configurar_luz_spot(GL_LIGHT6, [0, 0, -1], [0, -1, 1], [0.1, 0.1, 0.1], 1, 40, 15)#lanterna

    direction = [1, 1, 1]

    lights.configurar_luz_direcional(GL_LIGHT5, direction, [1, 0.4, 0.0], 1 )#sol

    """
    glTranslatef(0, -0.6, 0)
    glRotatef(90, 1, 0, 0)

    mesh.draw()
    """
    

    glfw.swap_buffers(window)
    

glfw.terminate()#termina o glfw assim que o loop da janela termina ao apertar o X