import glfw
from OpenGL.GL import * 

width, height = 1920, 1080

vertices = [
    [-0.8, -0.4],
    [-0.8, 0.4],
    [-0.4, -0.8],
    [-0.4, 0.8],
    [0.4, -0.8],
    [0.4, 0.8],
    [0.8, -0.4],
    [0.8, 0.4],
    
    
    
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
    
    glColor3f(1,0,0)     
    glPointSize(10)                                       
    glBegin(GL_POINTS)                                                                  #função desenha inicio com um parametro de primitiva
    for v in vertices:
        glVertex2fv(v)                                                                 #desenhando cada vertice em seu lugar 
    glEnd() 
    
    glLineWidth(5)
    """
    glBegin(GL_LINES)
    for l in vertices:
        glVertex2fv(l)
    glEnd()      
    
    glBegin(GL_LINE_STRIP)
    for ls in vertices:
        glVertex2fv(ls)
    glEnd()      
    
    glBegin(GL_LINE_LOOP)
    for lP in vertices:
        glVertex2fv(lP)
    glEnd()     
    """

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_STRIP)
    for lP in vertices:
        glVertex2fv(lP)
    glEnd() 
    """
    glPolygonMode(GL_FRONT, GL_LINE)
    glColor3f(0, 0, 0)
    glBegin(GL_TRIANGLES)
    for lP in vertices:
        glVertex2fv(lP)
    glEnd()       
    """
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glColor3f(0, 0, 0)
    glBegin(GL_TRIANGLE_STRIP)
    for lP in vertices:
        glVertex2fv(lP)
    glEnd()                                                     #função desenha final

#Função Principal
def main():
    glfw.init()                                                                         #inicializando a API GLFW
    #criando a janela(largura e altura, nome da janela, monitor, janela compartilhada)
    window = glfw.create_window(width, height, 'Coala Engine Ver0.0.1', None, None)
    glfw.make_context_current(window)                                                   #CRIANDO O CONTEXTO OpenGL da janela
    init()
    while not glfw.window_should_close(window):                                         #Enquanto a janela nao é fechada
        glfw.poll_events()                                                              #tratamento de eventos
        render()	    
        glfw.swap_buffers(window)                                                       #troca de frame buffer(informação de cores dos pixels)
    glfw.terminate()                                                                    #finaliza a API GLFW

if __name__ == '__main__':
    main()