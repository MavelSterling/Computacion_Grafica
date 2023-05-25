from OpenGL.GL import *
from OpenGL.GLUT import *
import glfw

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480

def main():
    # Inicializar la biblioteca GLFW
    if not glfw.init():
        return -1

    # Crear una ventana con modo de ventana y su contexto OpenGL
    window = glfw.create_window(ANCHO_PANTALLA, ALTO_PANTALLA, "Hola Mundo", None, None)
    if not window:
        glfw.terminate()
        return -1

    # Establecer la ventana actual como contexto
    glfw.make_context_current(window)

    glViewport(0, 0, ANCHO_PANTALLA, ALTO_PANTALLA)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, ANCHO_PANTALLA, 0, ALTO_PANTALLA, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    vertices_poligono = [
        20, 100, 0,
        100, 300, 0,
        500, 50, 0,
        320, 10, 0,
        40, 40, 0
    ]

    # Bucle principal: ejecutar hasta que el usuario cierre la ventana
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        # Renderizar OpenGL aquí
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices_poligono)
        glDrawArrays(GL_POLYGON, 0, 5)
        glDisableClientState(GL_VERTEX_ARRAY)

        # Intercambiar los buffers frontal y posterior
        glfw.swap_buffers(window)

        # Procesar los eventos
        glfw.poll_events()

    glfw.terminate()

if __name__ == '__main__':
    main()
