import glfw
from OpenGL.GL import * 

vertices = [
    [-0.5, -0.5],
    [0.5, -0.5],
    [0.0, 0.3]
]
cores = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

#Função PARA CONFIGURAÇÕES INICIAIS DA MINHA aplicação
def init():
    glClearColor(1, 1, 1, 1)#cor do fundo da janela
#função para atualizar a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)                                                        #limpando o buffer dos pixels
    glBegin(GL_TRIANGLES)                                                               #função desenha inicio com um parametro de primitiva
    for v, c in zip(vertices, cores):                                                   #for pela lista de  lista de vertice e cores simuntaneamente e fomando pares com o valor do indice de cada lista
        glColor3fv(c)                                                                   #colore cada vertice em sua sequencia 
        glVertex2fv(v)                                                                  #desenhando cada vertice em seu lugar 
    glEnd()                                                                             #função desenha final

#Função Principal
def main():
    glfw.init()                                                                         #inicializando a API GLFW
    #criando a janela(largura e altura, nome da janela, monitor, janela compartilhada)
    window = glfw.create_window(500,500, 'Coala Engine Ver0.0.1', None, None)
    glfw.make_context_current(window)                                                   #CRIANDO O CONTEXTO OpenGL da janela
    init()
    while not glfw.window_should_close(window):                                         #Enquanto a janela nao é fechada
        glfw.poll_events()                                                              #tratamento de eventos
        render()	    
        glfw.swap_buffers(window)                                                       #troca de frame buffer(informação de cores dos pixels)
    glfw.terminate()                                                                    #finaliza a API GLFW

if __name__ == '__main__':
    main()