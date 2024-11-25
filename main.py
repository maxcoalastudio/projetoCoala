import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy import array
import time
from PIL import Image
#from PrimitiveObjects import PrimitiveObjects
from Camera import Camera
#from Mesh import Mesh
from Lights import Lights
from textureAtlas import TextureAtlas
from cubo import Cubo
from esfera import Esfera

if not glfw.init():
    raise Exception("Falha ao iniciar")

width, height = 1280, 720
window = glfw.create_window(width, height, "Coala Engine Ver0.0.1", None, None)
if not window:
    raise Exception("Falha ao criar a janela")

icon = "icon.png"
glfw.set_window_icon(window, 1, Image.open(icon))
glfw.make_context_current(window)
#glfw.swap_interval(1) #limitador de fps
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

glMatrixMode(GL_PROJECTION)

glEnable(GL_CULL_FACE)
glCullFace(GL_BACK)

glLoadIdentity()
gluPerspective(45, width / height, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

camera = Camera(width, height)

lights = Lights()

textura = TextureAtlas('minecraft.jpg', (32, 16))

#aqui chama os objetos primitivos da classe PrimitiveObjects
#cubo = Cubo(texture_atlas=textura, texture_indices=[3, 3, 3, 3, 2, 50])
esfera = Esfera()

#cubos com tamanhos unico para fazer o chão de grama, e passando um for para passar vairos cubos de uma vez 
lista_cubos = [
    Cubo(inital_position=[2*i, 0.0, 2*j],raio = 1, texture_atlas =textura, texture_indices=[3,3,3,3,2,50])
    for i in range(10)
    for j in range(10)
]



teia = [66, 66 , 66, 66, 66, 66]
craftable = [141,142,141,142,140,140]
fornalha = [145,145,143,145,146,146]
fornalha2 = [145,145,144,145,146,146]

novos_cubos = [
    Cubo(inital_position=[5, 2.0, 7], raio=1, texture_atlas=textura, texture_indices=teia),
    Cubo(inital_position=[7, 2.0, 7], raio=1, texture_atlas=textura, texture_indices=craftable),
    Cubo(inital_position=[9, 2.0, 7], raio=1, texture_atlas=textura, texture_indices=fornalha),
    Cubo(inital_position=[11, 2.0, 7], raio=1, texture_atlas=textura, texture_indices=fornalha2)
]
lista_cubos.extend(novos_cubos)

def listaExibicao(cubos):
    display_list = glGenLists(2)
    glNewList(display_list, GL_COMPILE)

    for cubo in lista_cubos:
        cubo.draw(0, 0, 0)

    glEndList()
    return display_list

glClearColor(0.5, 0.5, 0.5, 1)
glfw.set_key_callback(window, camera.key_callback)
glfw.set_cursor_pos_callback(window, camera.mouse_callback)



#mesh = Mesh([-5, -5, 0], [5, 5, 0], [0, 0, -1], 10000)

# Variáveis para calcular o FPS
frame_count = 0
start_time = time.time()
"""
#melhorar essas funções
def carregar_mapa_altura(caminho_imagem, escala_z=1):
    imagem = Image.open(caminho_imagem).convert("L")  # Converte para tons de cinza
    mapa_altura = array(imagem)
    # Normalizar a altura para um valor utilizável
    mapa_altura = (mapa_altura / 255.0) * escala_z
    return mapa_altura
def gerar_terreno(mapa_altura, textura, cubo_raio=1):
    cubos = []
    largura, altura = mapa_altura.shape
    for x in range(largura):
        for y in range(altura):
            altura_max = int(mapa_altura[x,y])

            for z in range(0, altura_max + 1, cubo_raio * 2):
                # Cria um cubo na posição correspondente
                cubo = Cubo(
                    inital_position=[x * cubo_raio * 2, z, y * cubo_raio * 2],
                    raio=cubo_raio,
                    texture_atlas=textura,
                    texture_indices=[3, 3, 3, 3, 2, 50],  # Ajuste se necessário
                )
                cubos.append(cubo)
    return cubos

mapa_altura = carregar_mapa_altura("perlin_noise.png", escala_z=10)
lista_cube = gerar_terreno(mapa_altura, textura)
lista_cubos.extend(lista_cube)
"""

lista_de_exebicao = listaExibicao(lista_cubos)
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

while not glfw.window_should_close(window):
    glfw.poll_events()
    camera.process_input(window)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    camera.updateCamera()

    glCallList(lista_de_exebicao)

    # Calcular FPS
    frame_count, start_time = calculate_fps(frame_count, start_time)

    #criando a camera
    
    #chamando as figuras bidimensionais
    #quads()#desenhando o quadrado
    #tris()#desenhando o triangulo
    #circle(0.4, -0.3, 0.3, 20)
    esfera.draw(3, 5, 0)
    
    #cubo.cube(1, 1, 1)
    
    #esfera.esfera(0, 0, 0, 0.5, 10, 10) 
    #piramide()
    #esfera(0.08, 20, 20)
    #fazendo o cubo rotacionar pelo angulo acrescido

    #angle +=  0.1
    #dir+= 0.04

    glTranslatef(0, 0.6, 0)
    #lights.configurar_luz_pontual(GL_LIGHT2, [2, 1, 0], [0.6, 0, 0], 0.7)#ponto de luz vermelho

    #lights.configurar_luz_pontual(GL_LIGHT3, [0, 1, 2], [0, 0.6, 0], 0.7)#ponto de luz verde

    #lights.configurar_luz_pontual (GL_LIGHT4, [0, 1, -2], [0, 0, 0.6], 0.7)#ponto de luz azul

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