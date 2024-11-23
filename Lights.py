from OpenGL.GL import *
from OpenGL.GLU import *


class Lights():
    def __init__(self, luzAmbiente = [0.5, 0.5, 0.5, 1]):
        #LUZ
        glEnable(GL_LIGHTING)
        glEnable(GL_DEPTH_TEST)

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)# cor da luz  ambiente

    def configurar_luz_pontual(self, light_id, position, color, intensity):
        glLightfv(light_id, GL_POSITION, position + [1])
        glLightfv(light_id, GL_DIFFUSE, [color[0] * intensity, color[1] * intensity, color[2] * intensity, 1])
        glLightfv(light_id, GL_SPECULAR, color + [1])

        glLightf(light_id, GL_CONSTANT_ATTENUATION, 0)
        glLightf(light_id, GL_LINEAR_ATTENUATION, 0.1)
        glLightf(light_id, GL_QUADRATIC_ATTENUATION, 0.01)

        glEnable(light_id)

        self.desenhar_esfera(position, color)

    def desenhar_esfera(self, position, cor):
        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])

        shininess = 50 

        glMaterialfv(GL_FRONT, GL_DIFFUSE, cor + [1])
        glMaterialfv(GL_FRONT, GL_SPECULAR, cor + [1])
        glMaterialfv(GL_FRONT, GL_AMBIENT, cor + [1])
        glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

        quadric = gluNewQuadric()
        gluSphere(quadric, 0.1, 20, 20)
        glPopMatrix()

    def configurar_luz_direcional(self, light_id, direction, color, intensity):
        glLightfv(light_id, GL_POSITION, direction + [0]) # sempre que quisermos um vetor vamos add um 0 no 4 elemento da direção, se quisermos um ponto colocamos 1
        glLightfv(light_id, GL_DIFFUSE, [color[0] * intensity, color[1] * intensity, color[2] * intensity, 1])
        glLightfv(light_id, GL_SPECULAR, color+[1])

        glLightf(light_id, GL_CONSTANT_ATTENUATION, 1)
        glLightf(light_id, GL_LINEAR_ATTENUATION, 0)
        glLightf(light_id, GL_QUADRATIC_ATTENUATION, 0)

        glEnable(light_id)
        self.desenhar_esfera(direction +[1], color)
        self.desenhar_linha(direction, color)
        
    def configurar_luz_spot(self, light_id, position, direction, color, intensity, cutOff, exponent):
        glLightfv(light_id, GL_POSITION, position+[1])
        glLightfv(light_id, GL_SPOT_DIRECTION, direction)
        glLightfv(light_id, GL_DIFFUSE, [color[0] * intensity, color[1] * intensity, color[2] * intensity, 1])
        glLightfv(light_id, GL_SPECULAR, color +[1]) 

        glLightf(light_id, GL_SPOT_CUTOFF, cutOff)
        glLightf(light_id, GL_SPOT_EXPONENT, exponent)

        glLightf(light_id, GL_CONSTANT_ATTENUATION, 0)
        glLightf(light_id, GL_LINEAR_ATTENUATION, 0.1)
        glLightf(light_id, GL_QUADRATIC_ATTENUATION, 0.01)

        glEnable(light_id)

        self.desenhar_esfera(position, color)
        self.desenhar_linha(direction, color, position)

    def desenhar_linha(self, direction, color, pos = [0, 0, 0]):
        glPushMatrix()
        glTranslatef = pos
        glBegin(GL_LINES)
        glVertex3f(pos[0], pos[1], pos[2])
        glVertex3f(direction[0], direction[1], direction[2])
        glColor3f(color[0], color[1], color[2])
        glEnd()
        glPopMatrix()
