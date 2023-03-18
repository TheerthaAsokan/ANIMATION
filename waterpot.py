import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


windowsize=500
FPS=60
bx=0
by=0
sy=0
wy=0
m=5/3
mode=0

def clearscreen():
    glClearColor(0.5,0.5,1,1)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)

def pic():

    global bx,by,mode,sy,wy

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,1,1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-200,0)
    glVertex2f(250,0)
    glVertex2f(250,-250)
    glVertex2f(-200,-250)
    glEnd()

    glColor3f(0,0,0.8)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-200,-150+wy)
    glVertex2f(250,-150+wy)
    glVertex2f(250,-250)
    glVertex2f(-200,-250)
    
    glEnd()
    
    glColor3f(0.3,0.3,0.3)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-350+bx,-150+by)
    glVertex2f(-300+bx,-190+by)
    glVertex2f(-350+bx,-230+by)
    glVertex2f(-400+bx,-190+by)
    
    glEnd()

   
    glColor3f(0.3,0.3,0.3)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-298+bx,-220+by)
    glVertex2f(-280+bx,-190+by)
    glVertex2f(-290+bx,-180+by)
    glVertex2f(-300+bx,-190+by)

    glEnd()
    
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(-350+bx,-230+by)
    glVertex2f(-350+bx,-250+by)
    
    glEnd()
    
    if mode==1:
        glColor3f(0,0,0)
        glPointSize(6)
        glBegin(GL_POINTS)
        glVertex2f(-150,40-sy)
        glEnd()


    

   

    glutSwapBuffers()


def animate(temp):

    global bx,by,m,mode,sy,wy
    
    if (mode == 0):

        bx+=1
        by = m*bx
        if(bx == 150):
            mode = 1
        
    if mode==1:
        sy+=1
        if sy==200:
            wy+=5
            mode=2
    if mode==2:
        sy=0
        bx-=1
        by = m*bx
        if(bx == 0):
            mode = 0



    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)
    glutCreateWindow("view")
    glutDisplayFunc(pic)
    glutIdleFunc(pic)
    glutTimerFunc(0,animate,0)
    clearscreen()
    glutMainLoop()

main()