from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

window=500
x=150
y=20
theta=0
DIR=1

def init_disp():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5,0.6,0.6)
    gluOrtho2D(-window,window,-window,window)

def triangle():
    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(-50,-50 )
    glVertex2f(50, -50)
    glEnd()

def rod():
    glLineWidth(15)
    glBegin(GL_LINES)
    glVertex2f(x*math.cos(math.radians(theta))-y*math.sin(math.radians(theta)), x*math.sin(math.radians(theta))+y*math.cos(math.radians(theta)))
    glVertex2f(-x*math.cos(math.radians(theta))-y*math.sin(math.radians(theta)), -x*math.sin(math.radians(theta))+y*math.cos(math.radians(theta)))
    glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    triangle()
    rod()
    glFlush()
    glutSwapBuffers()

def animate(temp):
    global theta,dir
    glutTimerFunc(int(1000/200),animate,int(0))
    glutPostRedisplay()

    if theta>20:
        dir=0
    if theta<-20:
        dir=1

    if (dir==1):
        theta+=.1
    else:
        theta-=.1
    
    

def main():
    glutInit()
    glutInitWindowSize(window,window)
    glutInitWindowPosition(50,50)
    glutCreateWindow("SeeSaw")
    init_disp()
    glutDisplayFunc(draw)
    glutTimerFunc(1,animate,0)
    glutMainLoop()

main()