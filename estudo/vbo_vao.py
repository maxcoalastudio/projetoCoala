import glfw
from OpenGL.GL import * 
import numpy as np
import ctypes
width, height = 1920, 1080

vertices = [
    [-0.8, -0.8],
    [0.0, -0.8],
    [-0.4, 0.0],
    [0.0, -0.8],
    [0.8, -0.8],
    [0.4, 0.0],
    [-0.4, 0.0],
    [0.4, 0.0],
    [0.0, 0.8],
]
qtdVertices = len(vertices)
vaoId=0


#Função PARA CONFIGURAÇÕES INICIAIS DA MINHA aplicação
def init():
    global vertices, vaoId #importando os vertices pra dentro da função
    glClearColor(1, 1, 1, 1)#cor do fundo da janela
    vertices = np.array(vertices, np.dtype(np.float32)) # conversão para valores de float com 32 bits cada ou 4bytes
    #criar o VAO #vamos criar o VAO vertex array object que descreve e encapsula o vbo
    vaoId = glGenVertexArrays(1)# retorna a quantidade de vao 
    #ativando o VAO
    glBindVertexArray(vaoId)# tornando vao ativo
    #daqui pra baixo tudo é incorporado e precisa ser desativado caso queiramos chamar outro objeto
    #criar o VBO
    vboId = glGenBuffers(1)# retorna um id de indentificador, no caso quantidade de buffers
    #tornar o VBO ativo
    glBindBuffer(GL_ARRAY_BUFFER, vboId)
    #enviar os dados pra esse VBO
    glBufferData(GL_ARRAY_BUFFER, #TIPO DE BUFFER
                vertices.nbytes, #tamanho do buffer
                vertices, # os dados
                GL_STATIC_DRAW)#uso do buffer
    #PRECISAMOS DEFINIS OS ATRIBUTOS DOS DADOS DO BUFFER, hora de descrever a organização
    glVertexAttribPointer(0, #codigo  de indentificação do ponteiro para posição 
                        2,#quantidade de valores de vertices
                        GL_FLOAT,# tipo de dado
                        GL_FALSE,#normalização de valores , tornar entre 0 a 1
                        2*4,#DE QUANTOS EM QUANTO BYTES vou procurar a nova posição 
                        ctypes.c_void_p(0))#onde que o atributo começa, ponteiro pra void do inicio dos vertices
    #tornando o atributo ativo
    glEnableVertexAttribArray(0)#usando o codigo do ponteiro de atributos
    #desativando o VAO e VBO
    glBindBuffer(GL_ARRAY_BUFFER, 0) #DESATIVANDO O BUFFER primeiro pois esta encapsulado pelo array
    glBindVertexArray(0)


#função para atualizar a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)                                                        #limpando o buffer dos pixels
    #tornando o nosso buffer ativo
    glBindVertexArray(vaoId)
    glDrawArrays(#substituindo o glBegin e glEnd
        GL_TRIANGLES, #QUAL TIPO DE PRIMITIVA
        0, #por onde começar ?
        qtdVertices#quantidade de vertices do objeto
     )
    glBindVertexArray(0)

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