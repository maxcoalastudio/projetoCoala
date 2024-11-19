import glfw
from OpenGL.GL import * 

#Função PARA CONFIGURAÇÕES INICIAIS DA MINHA aplicação
def init():
    glClearColor(1, 1, 1, 1)#cor do fundo da janela
#função para atualizar a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)#limpando o buffer dos pixels

    glColor3f(1,0,0)                                                                    #definindo a cor para nossa geometria
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0,1,0)
    glVertex2f(0.5, -0.5)
    glColor3f(0,0,1)
    glVertex2f(0.0, 0.3)
    glEnd()


#Função Principal
def main():
    glfw.init()                                                                         #inicializando a API GLFW
    #criando a janela(largura e altura, nome da janela, monitor, janela compartilhada)
    window = glfw.create_window(500,500, 'Coala Engine Ver0.0.1', None, None)
    glfw.make_context_current(window)                                                   #CRIANDO O CONTEXTO OpenGL da janela
    init()
    while not glfw.window_should_close(window):                                          #Enquanto a janela nao é fechada
        glfw.poll_events()                                                              #tratamento de eventos
        render()	    
        glfw.swap_buffers(window)                                                       #troca de frame buffer(informação de cores dos pixels)
    glfw.terminate()                                                                    #finaliza a API GLFW

if __name__ == '__main__':
    main()