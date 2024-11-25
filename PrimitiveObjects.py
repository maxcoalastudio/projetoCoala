from OpenGL.GL import *
import math
from OpenGL.GLU import *
from PIL import Image

from numpy import array
from numpy import uint8
#imagens
escolha = {
    "1" : "world.jpg",
    "2" : "grass.jpg"
}


class PrimitiveObjects:
    def __init__(self, initial_position = [0.0, 0.0, 0.0], radius = 1, texture_atlas=None, texture_indices=[0,1,2,3,4,5], texture_file = escolha["1"]):
        self.radius = radius
        self.texture_atlas = texture_atlas
        self.texture_indices = texture_indices
        self.position = initial_position
        self.texture_id = None
        self.texture_file = texture_file

        #VERTICES DE FACES
        self.verticesQuad = [
            [-0.5, 0.5, 0.0],
            [0.5, 0.5, 0.0],
            [0.5, 0.0, 0.0],
            [-0.5, 0.0, 0.0]
            ]

    def esfera(self, x, y, z, radius = 1.0, slices = 20, stacks =20 ):
        glPushMatrix()
        glTranslatef(self.position[0] + x, self.position[1] + y, self.position[2] + z)
        
        glRotatef(-90, 1, 0, 0)
        
        if self.texture_id:
            print(self.texture_id)
            print(self.texture_file)

            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_id) 

        quad = gluNewQuadric()
        gluQuadricTexture(quad, GL_TRUE)
        gluSphere(quad, radius, slices, stacks)

        if self.texture_id:
            glDisable(GL_TEXTURE_2D)
        
        glPopMatrix()#fecha a matriz


    def cube(self, x, y, z):
        #vertices do cubo
        vertices = [
            [-self.radius, -self.radius, -self.radius],#traseiras (-z) construidos da esquerda pra direita de cima para baixo
            [self.radius, -self.radius, -self.radius],
            [self.radius, self.radius, -self.radius],
            [-self.radius, self.radius, -self.radius],
            
            [-self.radius, -self.radius, self.radius],#frontais (+z)construido de baixo para cima da direita para esquerda
            [self.radius, -self.radius, self.radius],
            [self.radius, self.radius, self.radius],
            [-self.radius, self.radius, self.radius],
            
        ]
        #vamos passar as faces por que futuramente vamos passar cores a elas
        faces = [
            [3, 0, 1, 2],#frente
            [7, 3, 2, 6],#direita
            [4, 7, 6 ,5],#traseira
            [0, 4, 5, 1],#esquerda
            [1, 5, 6, 2],#superior
            [4, 0, 3, 7],#inferior
        ]
        normais = [
            [0, 0, -1],
            [1, 0, 0],
            [0, 0, 1],
            [-1, 0, 0],
            [0, 1, 0],
            [0, -1, 0]
        ]

        """
        color = [0.6, 0.6, 0.6, 1]
        colors = [
            [1, 0, 0, 0.8], [0, 1, 0, 0.8], [0, 0, 1, 0.8], [1, 1, 0, 0.8], [1, 0, 1, 0.8], [0, 1, 1,0.8 ], [1, 1, 1, 0.8], [1, 0.5, 0, 0.8]
        ]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glMaterialfv(GL_FRONT, GL_SPECULAR, color)
        glMaterialfv(GL_FRONT, GL_AMBIENT, color)
        glMaterialfv(GL_FRONT, GL_SHININESS, 0.5)
        """


        glPushMatrix()#abre a matriz
        glTranslatef(self.position[0] + x, self.position[1] + y, self.position[2] + z)

        if self.texture_atlas:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_atlas.texture_id)

        #iniciando a contrução dele
        glBegin(GL_QUADS)
        for i, face in enumerate(faces):#passando um laço em cada lista(face)
            glNormal3fv(normais[i])
            uvs = self.texture_atlas.get_uv_coords(self.texture_indices[i])
            for j, vertex in enumerate(face):#passando um laço em cada valor de de cada lista a cada loop
                glTexCoord2fv(uvs[j])
                #glColor4fv(colors[vertex])
                glVertex3fv(vertices[vertex])#desehando as faces usando triangulos, usando os loopes acima
        glEnd()
        if self.texture_atlas:
            glDisable(GL_TEXTURE_2D)
        glPopMatrix()#fecha a matriz


    def piramide(self):
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

    def esfera1(self, raio, slices, stacks):
        
        for i in range(stacks ):
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
        

    #Desenhando figuras Bidimensionais
    
    #função pra desenhar usando os vertices
    def quads(self):
        glColor4f(1.0, 0.0, 0.5, 0.5)
        glBegin(GL_QUADS)#inicia uma forma geometrica basica
        for vertice in self.verticesQuad:#agora vamos passar os vertices para o opengl
            glVertex3f(vertice[0], vertice[1], vertice[2])
        glEnd()#sempre que começa com um begin tem que termionar

    def tris(self):
        glColor4f(0.0, 1.0, 0.5, 0.5)
        glBegin(GL_TRIANGLES)#inicia uma forma geometrica basica
        for vertice in self.verticesQuad:#agora vamos passar os vertices para o opengl
            glVertex3f(vertice[0]+0.4, vertice[1]+0.3, vertice[2])
        glEnd()#sempre que começa com um begin tem que termionar

    def circle(self, x, y, raio, segment):#circulo baseado no ponto central
        glColor4f(0.2, 0.3, 0.8, 0.8)
        glBegin(GL_TRIANGLE_FAN)#do ponto inicial ele calcula o angulo de inclinação
        glVertex2f(x, y)
        for i in range(segment + 1):# um loop com a quantidade de segmentos corrigida
            angle = 2* math.pi* i/segment #calculando o angulo de acordo com a quantidade de segmentos 
            glVertex2f(x + math.cos(angle) * raio, y + math.sin(angle) *raio)#desenhando os triangulos usando o angulo 
        glEnd()

    