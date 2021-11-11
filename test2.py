from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
   

#include <GL/glut.h>
#include <GL/freeglut_ext.h>
#include "src/chair.h"
#include "src/table.h"
#include "src/cupboard.h"
#include "src/window.h"
#include "src/snowman.h"
#include "src/fan.h"
#include "src/shelf.h"

WINDOW_WIDTH =1000
WINDOW_HEIGHT =1000


# // angle of rotation for the camera direction
angle = 0.0
yAngle = 0.0
# // actual vector representing the camera's direction
lx = 0.0
ly = 0.0 
lz = -1.0
# // XZ position of the camera
x = -5.0
z = 18.0
roll = 0.0

# //for mouse movements
halfWidth = (float)(WINDOW_WIDTH/2.0)
halfHeight = (float)(WINDOW_HEIGHT/2.0)
mouseX = 0.0
mouseY = 0.0

v_cube = [[0.0, 0.0, 0.0], #0
    [0.0, 0.0, 3.0], #1
    [3.0, 0.0, 3.0], #2
    [3.0, 0.0, 0.0], #3
    [0.0, 3.0, 0.0], #4
    [0.0, 3.0, 3.0], #5
    [3.0, 3.0, 3.0], #6
    [3.0, 3.0, 0.0]  #7
]

quadIndices = [
    [0, 1, 2, 3], #bottom
    [4, 5, 6, 7], #top
    [5, 1, 2, 6], #front
    [0, 4, 7, 3], # back is clockwise
    [2, 3, 7, 6], #right
    [1, 5, 4, 0]  #left is clockwise
]

colors = [
    [0.4, 0.1, 0.0], #bottom
    [0.6, 0.0, 0.7], #top
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0],
    [0.8, 0.0, 0.0],
    [0.3, 0.6, 0.7]
]



def drawCube():

    glBegin(GL_QUADS)
    for i in range(6):    
        glVertex3f(v_cube[quadIndices[i][0]][0],v_cube[quadIndices[i][0]][1],v_cube[quadIndices[i][0]][2])
        glVertex3f(v_cube[quadIndices[i][1]][0],v_cube[quadIndices[i][1]][1],v_cube[quadIndices[i][1]][2])
        glVertex3f(v_cube[quadIndices[i][2]][0],v_cube[quadIndices[i][2]][1],v_cube[quadIndices[i][2]][2])
        glVertex3f(v_cube[quadIndices[i][3]][0],v_cube[quadIndices[i][3]][1],v_cube[quadIndices[i][3]][2])
    
    glEnd()

# //Fan
# Fan f

# def interactWithSnowman :
	
# 	char str1[] = "Hello! You seem to be the only student in class today."
# 	int l1 = strlen(str1) // see how many characters are in text string.
# 	glPushMatrix()

# 	glColor3f(0.0, 0.0, 0.0)

# 	glRasterPos3f(-9.6, 2.7, -2.8) // location to start printing text
# 	for( int i=0 i < l1 i++) // loop until i is greater then l
# 	{
# 		glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, str1[i]) // Print a character on the screen
# 	}
# 	glPopMatrix()


def cupboard():
    #Cupboard/Almari ************************************************************
        
        #cupboard
        glColor3f(0.5,0.2,0.2) #0.3,0.1,0.0
        glPushMatrix()
        glTranslatef(4,0,4.4)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 1, 0.5)
        drawCube()
        glPopMatrix()
        
        #cupboard's 1st vertical stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,1,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 0.01, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's 2nd vertical stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,0.5,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 0.01, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's last stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,0,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 0.01, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's lst horizontal stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(5.5,0,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.01, 1, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's right side horizontal stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.75,1,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.01, 0.67, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's left side horizontal stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,0,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.01, 1, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's handle right
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(5,1.4,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.02, 0.18, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's handle left
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.5,1.4,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.02, 0.18, 0.01)
        drawCube()
        glPopMatrix()
        
        #cupboard's drawer's 1st handle
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.5,0.7,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.16, 0.02, 0.01)
        drawCube()
        glPopMatrix()
        
        #cupboard's drawer's 2nd handle
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.5,0.25,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.16, 0.02, 0.01)
        drawCube()
        glPopMatrix()



def renderScene():
    global angle,yAngle,lx,ly,lz,mouseX,mouseY
    # // Clear Color and Depth Buffers

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # // Reset transformations
    glLoadIdentity()
    # // Set the camera
    gluLookAt(x, 2.5, z,
        x + lx, 2.5 + ly, z + lz,
        roll + 0.0, 2.5, 0.0)

    # // Draw floor
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glEnd()
    
    cupboard()
    # //wall
    glColor3f(0.9294, 0.9216, 0.8353)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glEnd()

    # //wall
    glColor3f(1.0, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glEnd()

    # //wall with door
    glColor3f(1.0, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, 10.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glVertex3f(-6.0, 7.0, 10.0)
    glVertex3f(-6.0, 0.0, 10.0)
    glEnd()

    glColor3f(1.0, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 0.0, 10.0)
    glVertex3f(-3.0, 7.0, 10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glEnd()

    glColor3f(1.0, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(-6.0, 7.0, 10.0)
    glVertex3f(-6.0, 5.0, 10.0)
    glVertex3f(-3.0, 5.0, 10.0)
    glVertex3f(-3.0, 7.0, 10.0)
    glEnd()

    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(-6.0, 5.0, 10.01)
    glVertex3f(-3.0, 5.0, 10.01)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-6.0, 5.0, 10.01)
    glVertex3f(-6.0, 0.0, 10.01)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-3.0, 0.0, 10.01)
    glVertex3f(-3.0, 5.0, 10.01)
    glEnd()


    # //wall
    glColor3f(1.0, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(10.0, 0.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glEnd()

    glColor3f(1.0, 0.851, 0.702)
    glBegin(GL_QUADS)
    glVertex3f(10.0, 0.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glEnd()

    # //ceiling
    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glEnd()

    # # // Draw prof's chair
    # Chair profChair
    # glPushMatrix()
    # glTranslatef( 6.0, 1.0, -9.0)
    # glScalef(0.32, 0.32, 0.32)
    # glRotatef(-30.0, 0.0, 1.0, 0.0)
    # profChair.drawChair()
    # glPopMatrix()

    # # // Draw prof's table
    # Table profTable
    # glPushMatrix()
    # glTranslatef( 6.0, 1.4, -7.6)
    # glScalef(0.5, 0.5, 0.5)
    # glRotatef(-30.0, 0.0, 1.0, 0.0)
    # profTable.drawTable()
    # glPopMatrix()

    # # // Draw student chairs
    # Chair studentChair[4][4]
    # for (int i = -3 i <= 3 i+=2){
    #     for (int j = -3 j <= 3 j+=2) {
    #         glPushMatrix()
    #         glTranslatef(i*2.0, 0.8, j * 2.0 + 2.2)
    #         glScalef(0.25, 0.25, 0.25)
    #         glRotatef(180.0, 0.0, 1.0, 0.0)
    #         studentChair[i][j].drawChair()
    #         glPopMatrix()
    #     }

	# # // Draw student tables
	# Table studentTable[4][4]
	# for (int i = -3 i <= 3 i+=2){
	# 	for (int j = -3 j <= 3 j+=2) {
	# 		glPushMatrix()
	# 		glTranslatef(i*2.0 + 0.3, 1.2, j * 2.0 + 1.2)
	# 		glScalef(0.4, 0.4, 0.4)
	# 		// glRotatef(180.0, 0.0, 1.0, 0.0)
	# 		studentTable[i][j].drawTable()
	# 		glPopMatrix()
	# 	}
	# }

	# // Draw cupboard
	# Cupboard cupboard
	# glPushMatrix()
	# glTranslatef( 8.49, 0.0, -3.5)
	# glRotatef(-90.0, 0.0, 1.0, 0.0)
	# cupboard.drawCupboard()
	# glPopMatrix()

	# // Draw blackboard
    glColor3f(0.4, 0.2, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-6.0, 2.0, -9.99)
    glVertex3f(-6.0, 5.5, -9.99)
    glVertex3f(6.0, 5.5, -9.99)
    glVertex3f(6.0, 2.0, -9.99)
    glEnd()

    glColor3f(0.149, 0.149, 0.149)
    glBegin(GL_QUADS)
    glVertex3f(-5.8, 2.2, -9.98)
    glVertex3f(-5.8, 5.3, -9.98)
    glVertex3f(5.8, 5.3, -9.98)
    glVertex3f(5.8, 2.2, -9.98)
    glEnd()


    # #Lamp *****************************************
        
    #     #lamp base
    # glColor3f(0,0,1)
    # glPushMatrix()
    # glTranslatef(.6,0.5,9.1)
    # glScalef(0.07, 0.02, 0.07)
    # drawCube()
    # glPopMatrix()
       
    #     #lamp stand
    # glColor3f(1,0,0)
    # glPushMatrix()
    # glTranslatef(.7,0.35,9.2)
    # glScalef(0.01, 0.2, 0.01)
    # drawCube()
    # glPopMatrix()
        
    #     #lamp shade
    # glColor3f(0.000, 0.000, 0.545)
    # glPushMatrix()
    # glTranslatef(.7,0.9,9.2)
    # glScalef(0.08, 0.09, 0.08)
    # drawCube()
    # glPopMatrix()

	# //Floor pattern
	# glColor3f(0.149, 0.149, 0.149)
	# glLineWidth(3.0)
	# for(int i = 0 i < 20 i += 2)
	# {
	# 	glBegin(GL_LINES)
	# 	glVertex3f(-10.0 + i, 0.001, -10.01)
	# 	glVertex3f(-10.0 + i, 0.001, 10.01)
	# 	glEnd()
	# }
	# for(int i = 0 i < 20 i += 2)
	# {
	# 	glBegin(GL_LINES)
	# 	glVertex3f(-10.0, 0.001, -10.01 + i)
	# 	glVertex3f(10.0, 0.001, -10.01 + i)
	# 	glEnd()
	# }

	# //windows
	# Window w
	# w.drawWindow1()
	# w.drawWindow2()
	# w.drawWindowSill()
	# glPushMatrix()
	# glTranslatef( 0.0, 0.0, 8.0)
	# w.drawWindowSill()
	# glPopMatrix()

	# //Draw Snowmen
	# Snowman s
	# glPushMatrix()
	# glTranslatef(-9.7, 2.0, -3.0)
	# glScalef(0.3, 0.3, 0.3)
	# s.drawSnowMan()
	# glPopMatrix()
	
	# if ( x < -8.0 && x > -9.0 && z < -1.0 && z > -2.0) {
	# 	interactWithSnowman()
	# }

	
	# glPushMatrix()
	# glTranslatef(0.0, 6.0, 0.0)
	# glScalef(0.3, 0.3, 0.3)
	# f.drawFan()
	# glPopMatrix()

	# Shelf sh
	# glPushMatrix()
	# glTranslatef(8.99, 3.5, 4.0)
	# glScalef(0.25, 0.25, 0.25)
	# glRotatef(-90, 0.0, 1.0, 0.0)
	# sh.drawShelf()
	# glPopMatrix()
	
    if(abs(mouseX) > 0.3):
        angle -= (0.004 * mouseX)
        lx = math.math.sin(angle)
        lz = -math.math.cos(angle)

    if(abs(mouseY) > 0.3):
        if(abs(yAngle) < (math.pi/2)):
            yAngle += (0.002 * mouseY)
        ly = math.math.sin(yAngle)


    glutSwapBuffers()


# // Handles the events triggered when one of the arrow keys are pressed.
# // @param key : key pressed
# // @param xx : x coordinate of mouse position
# // @param yy : y coordinate of mouse position
def processSpecialKeys(key,xx,yy):
    global x,z,angle,lx,lz

    fraction = 0.1

    if GLUT_KEY_LEFT:
        x += math.sin(angle - math.pi/2.0) * fraction
        z += -math.cos(angle - math.pi/2.0) * fraction
    if GLUT_KEY_RIGHT:
        x += math.sin(math.pi/2.0 + angle) * fraction
        z += -math.cos(math.pi/2.0 + angle) * fraction
    if GLUT_KEY_UP:
        x += lx * fraction
        z += lz * fraction
    if GLUT_KEY_DOWN:
        x -= lx * fraction
        z -= lz * fraction
		



# // Handles the events triggered when any key on the keyboard is pressed.
# //Specifically, handles w,a,s,d and Esc.
# // moves the camera frward, backward and sideways.
# // @param key : key pressed
# // @param xx : x coordinate of mouse position
# // @param yy : y coordinate of mouse position
def processNormalKeys(key,xx,yy):
    global x,z,roll,lx,ly,lz,angle
    fraction = 0.1
    print('keyss')
    print(key)
    if key == b'w':
        x += lx * fraction
        z += lz * fraction
    elif(key == b'a'):
        x += math.sin(angle - math.pi/2.0) * fraction
        z += -math.cos(angle - math.pi/2.0) * fraction
    elif(key == b's'):
        x -= lx * fraction
        z -= lz * fraction
    elif(key == b'd'):
        x += math.sin(math.pi/2.0 + angle) * fraction
        z += -math.cos(math.pi/2.0 + angle) * fraction
    elif (key == b'x'): 
        roll += 0.5
    elif (key == b'z'):
        roll -= 0.5

    if (key == 27):
        exit(0)


#  // Handles the events triggered when the mouse is moved in the window area. 
# // Handles yaw and pitch of the camera.
# // @param xx : x coordinate of mouse position
# // @param yy : y coordinate of mouse position
def processMouseMovement(xx,yy):

    global angle,yAngle,lx,lz,ly 
    mouseX = (float)(halfWidth - xx)/halfWidth
    mouseY = (float)(halfHeight - yy)/halfHeight
    angle -= (0.005 * mouseX)
    lx = math.sin(angle)
    lz = -math.cos(angle)

    if(abs(yAngle) < (math.pi/2)):
        yAngle += (0.005 * mouseY)
    ly = math.sin(yAngle)


#  // Adjusts the viewport sie when the window size is changed and sets the projection.
#  // @param w : new width of window
#  // @param h : new height of window
def changeSize(w, h) :

	# // Prevent a divide by zero, when window is too short
	# // (you cant make a window of zero width).
	if (h == 0):
		h = 1
	ratio = w * 1.0 / h

	# // Use the Projection Matrix
	glMatrixMode(GL_PROJECTION)

	# // Reset Matrix
	glLoadIdentity()

	# // Set the viewport to be the entire window
	glViewport(0, 0, w, h)
	halfWidth = (float)(w/2.0)
	halfHeight = (float)(h/2.0)

	# // Set the correct perspective.
	gluPerspective(45.0, ratio, 0.1, 100.0)

	# // Get Back to the Modelview
	glMatrixMode(GL_MODELVIEW)


# void animate () {

#     f.rotateFan()

#     /* refresh screen */
#     glutPostRedisplay()
# }



# // init GLUT and create window
glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowPosition(0, 0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow("Classroom")

# // register callbacks
glutDisplayFunc(renderScene)
glutReshapeFunc(changeSize)
# glutIdleFunc(animate)
glutKeyboardFunc(processNormalKeys)
glutSpecialFunc(processSpecialKeys)
glutIdleFunc(renderScene)
glutPassiveMotionFunc(processMouseMovement)

# // OpenGL init
glEnable(GL_DEPTH_TEST)

# // enter GLUT event procesmath.sing cycle
glutMainLoop()


