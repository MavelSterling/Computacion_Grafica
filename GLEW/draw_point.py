from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import glfw


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():
    if not glfw.init():
        return -1

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Hello World", None, None)

    if not window:
        glfw.terminate()
        return -1

    glfw.make_context_current(window)
    glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    pointVertex = np.array([SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2], dtype=np.float32)
    pointVertex2 = np.array([SCREEN_WIDTH * 0.75, SCREEN_HEIGHT / 2], dtype=np.float32)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glEnable(GL_POINT_SMOOTH)
        glEnableClientState(GL_VERTEX_ARRAY)
        glPointSize(50)
        glVertexPointer(2, GL_FLOAT, 0, pointVertex)
        glDrawArrays(GL_POINTS, 0, 1)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisable(GL_POINT_SMOOTH)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(2, GL_FLOAT, 0, pointVertex2)
        glPointSize(10)
        glDrawArrays(GL_POINTS, 0, 1)
        glDisableClientState(GL_VERTEX_ARRAY)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
