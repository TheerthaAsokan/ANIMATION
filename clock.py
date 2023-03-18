from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
GLOBAL_SANGLE = 90
GLOBAL_MANGLE = 90
FPS = 50


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def drawCircle():
    global GLOBAL_SANGLE
    global GLOBAL_MANGLE
    glColor3f(0.3, 0.5, 0.9)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(0, 361, 1):
        glVertex2f(200 * math.cos(math.pi * i / 180.0), 200 * math.sin(math.pi * i / 180.0))

    glEnd()
    x1 = 180 * math.cos(math.pi * GLOBAL_SANGLE / 180.0)
    y1 = 180 * math.sin(math.pi * GLOBAL_SANGLE / 180.0)
    x2 = 150 * math.cos(math.pi * GLOBAL_MANGLE / 180.0)
    y2 = 150 * math.sin(math.pi * GLOBAL_MANGLE / 180.0)
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x1, y1)
    glEnd()
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x2, y2)
    glEnd()


def drawClock():
    drawCircle()
    glutSwapBuffers()


def animate(temp):
    global GLOBAL_SANGLE
    global GLOBAL_MANGLE

    glutPostRedisplay()
    glutTimerFunc(int(1000 / FPS), animate, int(0))

    if GLOBAL_SANGLE == 0:
        if GLOBAL_MANGLE == 0:
            GLOBAL_MANGLE = 360
        else:
            GLOBAL_MANGLE -= 6
        GLOBAL_SANGLE = 360
    else:
        GLOBAL_SANGLE -= 6

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Clock")
    glutDisplayFunc(drawClock)
    glutTimerFunc(0, animate, 0)
    #glutIdleFunc(drawClock)
    init()
    glutMainLoop()


main()