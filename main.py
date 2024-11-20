import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy import array
from numpy import cross
import time
from PrimitiveObjects import PrimitiveObjects
import inputs
from math import cos, sin, pi, radians
from numpy import linalg   

#tela 
width, height = 1600, 1200
#variaveis da camera
camera_pos = array([0.0, 0.0, 3])
camera_front = array([0.0, 0.0, -1.0])
camera_up = array([0.0, 1.0, 0.0])
camera_speed = 0.001
yaw, pitch = -90, 0.0 # rotação eixo y, eixo x para primeira pessoa
keys={}

#variaveis do mouse
first_mouse = True
cursor_disabled  = False
esc_pressed = False
sensibility = 0.1
last_x, last_y = width/2, height/2


#Função Principal
def main():
    glfw.init()
    #criando a janela(largura e altura, nome da janela, monitor, janela compartilhada)
    window = glfw.create_window(width,height,'Coala Engine Ver0.0.1', None, None)
    glfw.make_context_current(window)#cria um contexto atual para a janela 

    #ativando o blend do alpha
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    #limpando o fundo com uma cor predefinida
    glClearColor(0.0, 0.2, 0.4, 0.4)#cores de limpeza de background
    glEnable(GL_DEPTH_TEST) #zDepth , desenha de tras pra frente em relação a camera, corrigindo a orem de desenho
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    gluPerspective( 45, 800 /600, 0.1, 50)#o clip da camera(campo de visao, aspecto ratio, perto, longe)
    glMatrixMode(GL_MODELVIEW) #modelo de visualização
    
    
    
    def camera(cp , cf , cup):
        #global camera_pos, camera_front, camera_up
        camera_pos = cp
        camera_front = cf
        camera_up = cup
        glLoadIdentity()
        camera_target = camera_pos + camera_front
        gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2], camera_target[0], camera_target[1], camera_target[2], camera_up[0], camera_up[1], camera_up[2])# onde a camera se encontra para onde ela olha, e a orientação dela

    # movimentando a camera 
    def key_callback(window, key, scancode, action, mods):
        if action == glfw.PRESS:
            keys[key] = True
        elif action == glfw.RELEASE:
            keys[key] = False
    
    def process_input():
        global camera_pos, camera_front, camera_up, camera_speed, esc_pressed, first_mouse, cursor_disabled
        
        if keys.get(glfw.KEY_W, False):
            camera_pos += camera_speed * camera_front
        if keys.get(glfw.KEY_S, False):
            camera_pos -= camera_speed * camera_front
        if keys.get(glfw.KEY_A, False):
            camera_pos -= cross(camera_front, camera_up) * camera_speed
        if keys.get(glfw.KEY_D, False):
            camera_pos += cross(camera_front, camera_up) * camera_speed

        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS and not esc_pressed:
            cursor_disabled = not cursor_disabled
            mode = glfw.CURSOR_DISABLED if cursor_disabled else glfw.CURSOR_NORMAL 
            glfw.set_input_mode(window, glfw.CURSOR, mode)
            esc_pressed = True
            first_mouse = cursor_disabled
            if not cursor_disabled:
                glfw.set_cursor_pos(window, last_x, last_y)
        elif glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.RELEASE:
            esc_pressed = False

    def mouse_callback(window, xPos, yPos):
        global yaw, pitch, last_x, last_y, first_mouse, camera_front, cursor_disabled, sensibility
        if not cursor_disabled:
             return
        if first_mouse:
            last_x = xPos
            last_y = yPos
            first_mouse = False
        xOffset = xPos - last_x
        yOffset = last_y - yPos
        last_x = xPos
        last_y = yPos
        xOffset *= sensibility
        yOffset *= sensibility
        yaw += xOffset
        pitch += yOffset



        #angulo maxximo de pitch para subir e descer a camera primeira pessoa
        if pitch > 89.0:
            pitch = 89.0
        if pitch < -89.0:
            pitch = -89.0
        
        direction = array([
            cos(radians(yaw)) * cos(radians(pitch)),
            sin(radians(pitch)),
            sin(radians(yaw)) * cos(radians(pitch))
        ])

        camera_front = direction / linalg.norm(direction) 

    #aqui chama os objetos primitivos da classe PrimitiveObjects
    cubo = PrimitiveObjects()

    glClearColor(0.3, 0.3, 0.3, 1.0)
    glfw.set_key_callback(window, key_callback)
    glfw.set_cursor_pos_callback(window, mouse_callback)
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
    angle = 0
    direction = 0
    speed = 1

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
       

    while not glfw.window_should_close(window):#enquanto nao verdadeira o evento do X a janela continua executando em loop
        glfw.poll_events()#trata eventos de cliques de botões, mouse , teclado , essa função interrompe o loop

        process_input()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)#limpa a tela com a cor definida em glClearColor e usa a distacia da camera como profundidade pra desenhar as faces mais procimas por ultimo
        # Calcular FPS
        frame_count, start_time = calculate_fps(frame_count, start_time)
        glLoadIdentity()
        #glTranslatef(0, 0, -direction* speed)#movendo o cubo para dentro no eixo -z

        #glRotatef(angle, 1, 1, 1)#ligando a rotação pra cada eixo

        #criando a camera
        camera(camera_pos, camera_front, camera_up)
        #chamando as figuras bidimensionais
        #quads()#desenhando o quadrado
        #tris()#desenhando o triangulo
        #circle(0.4, -0.3, 0.3, 20)
        cubo.cube(0, 0, 0)
        #piramide()
        #esfera(0.08, 20, 20)
        #fazendo o cubo rotacionar pelo angulo acrescido

        angle +=  0.1
        direction = 3 


        glfw.swap_buffers(window)#2 framebuffers são usados, um pra background e outro pra desenhar 
        

    glfw.terminate()#termina o glfw assim que o loop da janela termina ao apertar o X
if __name__ == '__main__':
    main()