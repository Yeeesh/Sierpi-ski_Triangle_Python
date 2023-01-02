#Importing librarys
from turtle import *
import random as rs

#Function for drawing the points
def drawpoint(x, y):
    up()
    goto(x, y)
    down()
    dot()
#Setting the corners of the triangle
A, B, C = [[0, 351], [-350, -350], [350, -351]]
#Get a random point inside the triangel
while True:
    #Get random Point
    P = [rs.randint(-350, 350), rs.randint(-350, 350)]
    #Check if random point is inside the triangle
    w1 = (A[0]*(C[1]*A[1])+(P[1]-A[1])*(C[0]-A[0])-P[0]*(C[1]-A[1]))/((B[1]-A[1])*(C[0]-A[0])-(B[0]-A[0])*(C[1]-A[1]))
    w2 = (P[1]-A[1]-w1*(B[1]-A[1]))/(C[1]-A[1])
    if w1 >= 0 and w2 >= 0:
        break
#Put corners in a list
corner = [A, B, C]
#Start
color("red")
up()
ht()
speed(0)
#Draw the corners
for j in corner:
    drawpoint(j[0], j[1])
#Draw the random point
drawpoint(P[0], P[1])
#The chaos game
for i in range(5000):
    z = rs.randint(0, 2)
    P[0] = (P[0] + corner[z][0])/2
    P[1] = (P[1] + corner[z][1])/2
    drawpoint(P[0], P[1])
    print(i)
done()
