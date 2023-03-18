from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

window=500
x=150
y=20
theta=0
dir=1

def init_disp():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    gluOrtho2D(-window,window,-window,window)

def body():
    glColor3f(0.1,0.5,0.1)
    glBegin(GL_POLYGON)
    glVertex2f(0, 100)
    glVertex2f(50, 50)
    glVertex2f(50, -50)
    glVertex2f(0,-100)
    glVertex2f(-50, -50)
    glVertex2f(-50, 50)
    glEnd()
    
def hand():
    glColor3f(1.0,0.5,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(50, 50)
    glVertex2f(50, 10)
    glVertex2f(150*math.cos(math.radians(theta))-37.5*math.sin(math.radians(theta)),150*math.sin(math.radians(theta))+37.5*math.cos(math.radians(theta)))
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-50, 50)
    glVertex2f(-50, 10)
    glVertex2f(-150*math.cos(math.radians(theta))-37.5*math.sin(math.radians(theta)),-150*math.sin(math.radians(theta))+37.5*math.cos(math.radians(theta)))
    glEnd()
    
def head():
    glColor3f(1.0,0.5,0.0)
    i=0
    xc=0
    yc=150
    r=50
    glBegin(GL_LINES)
    while i<6.28:
        glVertex2f(xc, yc)
        glVertex2f(r*math.cos(i)+xc,r*math.sin(i)+yc)
        i+=.01
    glEnd()

def leg():
    glColor3f(1.0,0.5,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(0,-100)
    glVertex2f(-50, -50)
    glVertex2f(-100, -175)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(50, -50)
    glVertex2f(0,-100)
    glVertex2f(100, -175)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    body()
    head()
    hand()
    leg()
    glFlush()
    glutSwapBuffers()

def animate(temp):
    global theta,dir
    glutTimerFunc(int(1000/60),animate,int(0))
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
    glutCreateWindow("Excercise")
    init_disp()
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glutMainLoop()

main()