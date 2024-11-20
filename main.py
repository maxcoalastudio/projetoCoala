import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
#import numpy as np
import math
import time
from PrimitiveObjects import PrimitiveObjects
#Função Principal
def main():
    glfw.init()
    #criando a janela(largura e altura, nome da janela, monitor, janela compartilhada)
    window = glfw.create_window(800,600,'Coala Engine Ver0.0.1', None, None)
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

    #aqui chama os objetos primitivos da classe PrimitiveObjects
    cubo = PrimitiveObjects()

    glClearColor(0.3, 0.3, 0.3, 1.0)
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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)#limpa a tela com a cor definida em glClearColor e usa a distacia da camera como profundidade pra desenhar as faces mais procimas por ultimo
        # Calcular FPS
        frame_count, start_time = calculate_fps(frame_count, start_time)
        glLoadIdentity()
        glTranslatef(0, 0, -direction* speed)#movendo o cubo para dentro no eixo -z

        glRotatef(angle, 1, 1, 1)

        #chamando as figuras bidimensionais
        #quads()#desenhando o quadrado
        #tris()#desenhando o triangulo
        #circle(0.4, -0.3, 0.3, 20)
        cubo.cube(0, 0, 0)
        #piramide()
        #esfera(0.08, 20, 20)
        #fazendo o cubo rotacionar pelo angulo acrescido
        angle +=  0.1
        direction += 0.0001 


        glfw.swap_buffers(window)#2 framebuffers são usados, um pra background e outro pra desenhar 
        

    glfw.terminate()#termina o glfw assim que o loop da janela termina ao apertar o X
if __name__ == '__main__':
    main()