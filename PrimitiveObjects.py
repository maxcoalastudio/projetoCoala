from OpenGL.GL import *
import math
class PrimitiveObjects:
    def __init__(self, initial_position = [0.0, 0.0, 0.0]):
        self.position = initial_position
        self.verticesQuad = [
        [-0.5, 0.5, 0.0],
        [0.5, 0.5, 0.0],
        [0.5, 0.0, 0.0],
        [-0.5, 0.0, 0.0]
        ]

    def cube(self, x, y, z):
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
            [0, 1, 2, 3],#frente
            [1, 5, 6, 2],#direita
            [5, 4, 7 ,6],#traseira
            [4, 0, 3, 7],#esquerda
            [3, 2, 6, 7],#superior
            [4, 5, 1, 0],#inferior
        ]
        normais = [
            [0, 0, -1],
            [1, 0, 0],
            [0, 0, 1],
            [-1, 0, 0],
            [0, 1, 0],
            [0, -1, 0]
        ]
        color = [0.6, 0.6, 0.6, 1]
        colors = [
            [1, 0, 0, 0.8], [0, 1, 0, 0.8], [0, 0, 1, 0.8], [1, 1, 0, 0.8], [1, 0, 1, 0.8], [0, 1, 1,0.8 ], [1, 1, 1, 0.8], [1, 0.5, 0, 0.8]
        ]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glMaterialfv(GL_FRONT, GL_SPECULAR, color)
        glMaterialfv(GL_FRONT, GL_AMBIENT, color)
        glMaterialfv(GL_FRONT, GL_SHININESS, 0.5)

        glPushMatrix()#abre a matriz
        glTranslatef(self.position[0] + x, self.position[1] + y, self.position[2] + z)
        #iniciando a contrução dele
        glBegin(GL_QUADS)
        for i, face in enumerate(faces):#passando um laço em cada lista(face)
            glNormal3fv(normais[i])
            for vertex in face:#passando um laço em cada valor de de cada lista a cada loop
                #glColor4fv(colors[vertex])
                glVertex3fv(vertices[vertex])#desehando as faces usando triangulos, usando os loopes acima
        glEnd()
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

    def esfera(self, raio, slices, stacks):
        
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