from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

windowsize=500
r=20
R=100
mode=0
angle=90
x=-400
y=0
fps=60

def init():
    glClearColor(0,0,0.5,1)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)

def draw():
    global radius,angle
    glClear(GL_COLOR_BUFFER_BIT)

    #glPointSize(6)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,0)
    glVertex2f(x+R*math.cos(angle*math.pi/180),y+R*math.sin(angle*math.pi/180))
    for i in range (0,361,1):
        glVertex2f(x+R*math.cos(angle*math.pi/180)+r*math.cos(i*math.pi/180),y+R*math.sin(angle*math.pi/180)+r*math.sin(i*math.pi/180))    
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0.5,0)
    glVertex2f(-windowsize,-20)
    glVertex2f(-windowsize,-windowsize)
    glVertex2f(windowsize,-windowsize)
    glVertex2f(windowsize,-20)

    glEnd()

    glLineWidth(10)
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex2f(-windowsize,-26)
    glVertex2f(windowsize,-26)
    glEnd()

    

    glutSwapBuffers()

def animate(temp):
    global mode,R,angle,x,fps
    
    if mode==0:
        angle-=1
        if(angle==0):
            mode=1
    if mode==1:
        angle=180
        x=x+R+(R-20)
        R=R-20
        mode=0
    if(x>=20):
        R=100
        mode=0
        angle=90
        x=-400
        mode=0
    
    glutPostRedisplay()
    glutTimerFunc(int(1500/fps),animate,0)


def main():
    glutInit()
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("BOUNCING")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(draw)
    init()
    glutMainLoop()

main()