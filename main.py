import glfw
from OpenGL.GL import *
import math
#Função Principal
def main():
    glfw.init()
    #criando a janela(largura e altura, nome da janela, monitor, janela compartilhada)
    window = glfw.create_window(500,500,'Coala Engine Ver0.0.1', None, None)
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


    #limpando o fundo com uma cor predefinida
    glClearColor(0.0, 0.2, 0.4, 1)#cores de limpeza de background
    """
    while not glfw.window_should_close(window):#enquanto nao verdadeira o evento do X a janela continua executando em loop
        glfw.poll_events()#trata eventos de cliques de botões, mouse , teclado , essa função interrompe o loop

        glClear(GL_COLOR_BUFFER_BIT)#limpa a tela com a cor definida em glClearColor

        #chamando as figuras bidimensionais
        #quads()#desenhando o quadrado
        #tris()#desenhando o triangulo
        #circle(0.4, -0.3, 0.3, 20)
        
        glfw.swap_buffers(window)#2 framebuffers são usados, um pra background e outro pra desenhar 
        

    glfw.terminate()#termina o glfw assim que o loop da janela termina ao apertar o X
if __name__ == '__main__':
    main()