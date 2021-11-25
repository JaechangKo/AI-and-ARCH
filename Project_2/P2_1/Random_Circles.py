import rhinoscriptsyntax as rs
import random as rnd

#Ask the user for number of points, minimum and maximum values
intCount = rs.GetInteger("How Many points?", 100, 2, 500)
intMin = rs.GetInteger("Enter minimum value", 0, 0, 100)
intMax = rs.GetInteger("Enter maximum value", 100,100,200)

#A Function that takes as input a number of points, min value and maximum value and returns a list of points
def createRandomPoints(ptCount, ptMin, ptMax):
    #create empty list
    pts = []    
    #a loop to create random point values
    for i in range(0,ptCount):
        x = rnd.uniform(ptMin,ptMax)
        y = rnd.uniform(ptMin,ptMax)
        #combine random x,y,z data into a point 
        pt = [x,y,0]
        #add the points to the list
        pts.append(pt)
    #return the list of points
    return pts


#A Function that takes a set of points as input and creates a set of circles
def createCircle(pts):
    #A loop to perform as many times as the length of the list of points
    for i in range(0, (len(pts))):
        #radius is a random number
        radius = rnd.uniform(0,5)
        #Add circles to Rhino
        rs.AddCircle(pts[i],radius)

#call the Function createRandomPoints, providing the user inputted data
ptList = createRandomPoints(intCount, intMin, intMax)
#call the createCircle Function, providing the list of points
createCircle(ptList)

