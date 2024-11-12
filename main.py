import glfw
#Função Principal
def main():
    glfw.init()
    #criando a janela(largura e altura, nome da janela, monitor, janela compartilhada)
    window = glfw.create_window(500,500,'Coala Engine Ver0.0.1', None, None)
    glfw.make_context_current(window)#cria um contexto atual para a janela 
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
if __name__ == '__main__':
    main()