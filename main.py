import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math
import time
#Função Principal
def main():
    glfw.init()
    #criando a janela(largura e altura, nome da janela, monitor, janela compartilhada)
    window = glfw.create_window(800,600,'Coala Engine Ver0.0.1', None, None)
    glfw.make_context_current(window)#cria um contexto atual para a janela 


    
    #ativando o blend do alpha
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    """
    #Desenhando figuras Bidimensionais
    vertices = [
        [-0.5, 0.5, 0.0],
        [0.5, 0.5, 0.0],
        [0.5, 0.0, 0.0],
        [-0.5, 0.0, 0.0]
        ]
    #função pra desenhar usando os vertices
    def quads():
        glColor4f(1.0, 0.0, 0.5, 0.5)
        glBegin(GL_QUADS)#inicia uma forma geometrica basica
        for vertice in vertices:#agora vamos passar os vertices para o opengl
            glVertex3f(vertice[0], vertice[1], vertice[2])
        glEnd()#sempre que começa com um begin tem que termionar

    def tris():
        glColor4f(0.0, 1.0, 0.5, 0.5)
        glBegin(GL_TRIANGLES)#inicia uma forma geometrica basica
        for vertice in vertices:#agora vamos passar os vertices para o opengl
            glVertex3f(vertice[0]+0.4, vertice[1]+0.3, vertice[2])
        glEnd()#sempre que começa com um begin tem que termionar

    def circle(x, y, raio, segment):#circulo baseado no ponto central
        glColor4f(0.2, 0.3, 0.8, 0.8)
        glBegin(GL_TRIANGLE_FAN)#do ponto inicial ele calcula o angulo de inclinação
        glVertex2f(x, y)
        for i in range(segment + 1):# um loop com a quantidade de segmentos corrigida
            angle = 2* math.pi* i/segment #calculando o angulo de acordo com a quantidade de segmentos 
            glVertex2f(x + math.cos(angle) * raio, y + math.sin(angle) *raio)#desenhando os triangulos usando o angulo 
        glEnd()

    """
    #limpando o fundo com uma cor predefinida
    glClearColor(0.0, 0.2, 0.4, 0.4)#cores de limpeza de background
    glEnable(GL_DEPTH_TEST) #zDepth , desenha de tras pra frente em relação a camera, corrigindo a orem de desenho
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    gluPerspective( 45, 800 /600, 0.1, 50)#o clip da camera(campo de visao, aspecto ratio, perto, longe)
    glMatrixMode(GL_MODELVIEW) #modelo de visualização

    def cube():
        #vertices do cubo
        vertices = [
            [-0.5, -0.5, -0.5],#traseiras (-z) construidos da esquerda pra direita de cima para baixo
            [0.5, -0.5, -0.5],
            [0.5, 0.5, -0.5],
            [-0.5, 0.5, -0.5],
            
            [-0.5, -0.5, 0.5],#frontais (+z)construido de baixo para cima da direita para esquerda
            [0.5,-0.5, 0.5],
            [0.5, 0.5, 0.5],
            [-0.5, 0.5, 0.5],
            
        ]
        #vamos passar as faces por que futuramente vamos passar cores a elas
        faces = [
            [0, 1, 2, 3],#tras
            [4, 5, 6, 7],#frente
            [0, 1, 5 ,4],#topo
            [2, 3, 7, 6],#esquerda
            [0, 3, 7, 4],#base
            [1, 2, 6, 5],#direita
        ]
        colors = [
            [1, 0, 0, 0.6], [0, 1, 0, 0.6], [0, 0, 1, 0.6], [1, 1, 0, 0.6], [1, 0, 1, 0.6], [0, 1, 1,0.6 ], [1, 1, 1, 0.6], [1, 0.5, 0, 0.6]
        ]
        
        #iniciando a contrução dele
        glBegin(GL_QUADS)
        for face in faces:#passando um laço em cada lista(face)
            for vertex in face:#passando um laço em cada valor de de cada lista a cada loop
                glColor4fv(colors[vertex])
                glVertex3fv(vertices[vertex])#desehando as faces usando triangulos, usando os loopes acima
        glEnd()


    def piramide():
        vertices = [
            [1, 1, 1],
            [-1, -1, 1],
            [-1, 1, -1],
            [1, -1, -1]
        ]
        
        faces = [ 
            [0, 1, 2],
            [0, 1, 3],
            [0, 2, 3],
            [1, 2, 3]
        ]
        cores =[
            [1, 0, 0, 0.4], [0, 1, 0, 0.4], [0, 0, 1, 0.4], [1, 1, 0, 0.4]
        ]

        glBegin(GL_TRIANGLES)
        for face in faces:
            for vertex in face:
                glColor4fv(cores[vertex])
                glVertex3fv(vertices[vertex])
        glEnd()

    def esfera(raio, slices, stacks):
        for i in range(stacks):
            lat0 = math.pi *(-0.5 + float(i) / stacks)
            z0 = raio * math.sin(lat0)
            zr0 = raio * math.cos(lat0)

            lat1 = math.pi *(-0.5 + float(i + 1) / stacks)
            z1 = raio * math.sin(lat1)
            zr1 = raio * math.cos(lat1)

            glBegin(GL_QUAD_STRIP)
            for j in range(slices+1):
                lng = 2 * math.pi * float(j)/slices
                x = math.cos(lng)
                y = math.sin(lng)
                glColor4f(j/ slices , i /stacks, 1- (i/stacks), 0.5)
                glVertex3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr1, y * zr1, z1)
            glEnd()





    glClearColor(0.3, 0.3, 0.3, 1.0)
    angle = 0
    direction = 0
    speed = 2

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
        #cube()
        #piramide()
        esfera(1, 10, 6)
        #fazendo o cubo rotacionar pelo angulo acrescido
        angle +=  0.01
        direction += 0.0001 


        glfw.swap_buffers(window)#2 framebuffers são usados, um pra background e outro pra desenhar 
        

    glfw.terminate()#termina o glfw assim que o loop da janela termina ao apertar o X
if __name__ == '__main__':
    main()