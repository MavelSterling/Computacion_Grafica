from OpenGL.GL import *
from OpenGL.GLUT import *
import glfw

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():
    # Inicializar la biblioteca GLFW
    if not glfw.init():
        return -1

    # Crear una ventana con modo de ventana y su contexto OpenGL
    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Hola Mundo", None, None)

    screenWidth, screenHeight = glfw.get_framebuffer_size(window)

    if not window:
        glfw.terminate()
        return -1

    # Establecer la ventana actual como contexto
    glfw.make_context_current(window)

    glViewport(0, 0, screenWidth, screenHeight)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, 0, 600)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    halfScreenWidth = SCREEN_WIDTH / 2
    halfScreenHeight = SCREEN_HEIGHT / 2

    halfSideLength = 200

    vertices = [
        halfScreenWidth, halfScreenHeight + halfSideLength, 0.0,
        halfScreenWidth - halfSideLength, halfScreenHeight - halfSideLength, 0.0,
        halfScreenWidth + halfSideLength, halfScreenHeight - halfSideLength, 0.0
    ]

    colour = [
        255, 0, 0,
        0, 255, 0,
        0, 0, 255
    ]

    # Bucle principal: ejecutar hasta que el usuario cierre la ventana
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        # Renderizar OpenGL aquí
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)
        glColorPointer(3, GL_FLOAT, 0, colour)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glDisableClientState(GL_COLOR_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)

        # Intercambiar los buffers frontal y posterior
        glfw.swap_buffers(window)

        # Procesar los eventos
        glfw.poll_events()

    glfw.terminate()

if __name__ == '__main__':
    main()
