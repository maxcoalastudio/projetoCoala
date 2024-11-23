import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy import array
from numpy import cross
from math import cos, sin, pi, radians
from numpy import linalg 
class Camera:

    def __init__(self, width, height):
        
        #variaveis da camera
        self.camera_pos = array([0.0, 0.0, 3])
        self.camera_front = array([0.0, 0.0, -1.0])
        self.camera_up = array([0.0, 1.0, 0.0])
        self.camera_speed = 0.02
        self.yaw, self.pitch = -90, 0.0 # rotação eixo y, eixo x para primeira pessoa
        self.keys={}

        #variaveis do mouse
        self.first_mouse = True
        self.cursor_disabled  = False
        self.esc_pressed = False
        self.sensibility = 0.1
        self.last_x, self.last_y = width/2, height/2


    def updateCamera(self):
        glLoadIdentity()
        camera_target = self.camera_pos + self.camera_front
        gluLookAt(self.camera_pos[0], self.camera_pos[1], self.camera_pos[2], camera_target[0], camera_target[1], camera_target[2], self.camera_up[0], self.camera_up[1], self.camera_up[2])# onde a camera se encontra para onde ela olha, e a orientação dela

    # movimentando a camera 
    def key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            self.keys[key] = True
        elif action == glfw.RELEASE:
            self.keys[key] = False
    
    def process_input(self, window):
        if self.keys.get(glfw.KEY_W, False):
            self.camera_pos += self.camera_speed * self.camera_front
        if self.keys.get(glfw.KEY_S, False):
            self.camera_pos -= self.camera_speed * self.camera_front
        if self.keys.get(glfw.KEY_A, False):
            self.camera_pos -= cross(self.camera_front, self.camera_up) * self.camera_speed
        if self.keys.get(glfw.KEY_D, False):
            self.camera_pos += cross(self.camera_front, self.camera_up) * self.camera_speed

        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS and not self.esc_pressed:
            self.cursor_disabled = not self.cursor_disabled
            mode = glfw.CURSOR_DISABLED if self.cursor_disabled else glfw.CURSOR_NORMAL 
            glfw.set_input_mode(window, glfw.CURSOR, mode)
            self.esc_pressed = True
            self.first_mouse = self.cursor_disabled
            if not self.cursor_disabled:
                glfw.set_cursor_pos(window, self.last_x, self.last_y)
        elif glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.RELEASE:
            self.esc_pressed = False

    def mouse_callback(self, window, xPos, yPos):
        if not self.cursor_disabled:
             return
        if self.first_mouse:
            self.last_x = xPos
            self.slast_y = yPos
            self.first_mouse = False
        xOffset = xPos - self.last_x
        yOffset = self.last_y - yPos
        self.last_x = xPos
        self.last_y = yPos
        xOffset *= self.sensibility
        yOffset *= self.sensibility
        self.yaw += xOffset
        self.pitch += yOffset

        #angulo maxximo de pitch para subir e descer a camera primeira pessoa
        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0
        
        self.direction = array([
            cos(radians(self.yaw)) * cos(radians(self.pitch)),
            sin(radians(self.pitch)),
            sin(radians(self.yaw)) * cos(radians(self.pitch))
        ])

        self.camera_front = self.direction / linalg.norm(self.direction) 
