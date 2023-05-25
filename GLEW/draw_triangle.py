from OpenGL.GL import *
from OpenGL.GLUT import *
import glfw

def main():
    # Inicializar la biblioteca GLFW
    if not glfw.init():
        return -1

    # Crear una ventana con modo de ventana y su contexto OpenGL
    window = glfw.create_window(640, 480, "Hola Mundo", None, None)
    if not window:
        glfw.terminate()
        return -1

    # Establecer la ventana actual como contexto
    glfw.make_context_current(window)

    vertices = [
        0, 0.5, 0.0,  # esquina superior
        -0.5, -0.5, 0.0,  # esquina inferior izquierda
        0.5, -0.5, 0.0  # esquina inferior derecha
    ]

    # Bucle principal: ejecutar hasta que el usuario cierre la ventana
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        # Renderizar OpenGL aquí
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glDisableClientState(GL_VERTEX_ARRAY)

        # Intercambiar los buffers frontal y posterior
        glfw.swap_buffers(window)

        # Procesar los eventos
        glfw.poll_events()

    glfw.terminate()

if __name__ == '__main__':
    main()
