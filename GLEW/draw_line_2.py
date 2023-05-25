from OpenGL.GL import *
from OpenGL.GLUT import *
import glfw

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def draw_line():
    glClear(GL_COLOR_BUFFER_BIT)
    
    lineVertices = [
        200, 100, 0,
        100, 300, 0
    ]
    
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_LINE_STIPPLE)
    glPushAttrib(GL_LINE_BIT)
    glLineWidth(10)
    glLineStipple(1, 0x00FF)
    
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, lineVertices)
    glDrawArrays(GL_LINES, 0, 2)
    glDisableClientState(GL_VERTEX_ARRAY)
    
    glPopAttrib()
    glDisable(GL_LINE_STIPPLE)
    glDisable(GL_LINE_SMOOTH)
    
    glutSwapBuffers()

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
    
    while not glfw.window_should_close(window):
        draw_line()
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()
    return 0

if __name__ == '__main__':
    main()
