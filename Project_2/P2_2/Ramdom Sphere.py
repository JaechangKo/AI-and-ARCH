#scripts to create Sol Lewitt Wall Painting #289
import rhinoscriptsyntax as rs
import random as rnd

#A class to create radial lines from corner points and center points of a rectangular
class randomLines():
    
    def __init__(self, Rect):
        #initialize class values from inputed numbers
        self.Rect = Rect
        
        
        #a function to draw radial lines from corner points and center points of a rectangular
    def drawLines(self):
        #find all the corner points of the given rectangular
        self.pts = rs.BoundingBox(self.Rect)
        
        #find all the corner point and their coordinations of the rectangular
        pt0 = rs.AddPoint(self.pts[0])
        pt1 = rs.AddPoint(self.pts[1])
        pt2 = rs.AddPoint(self.pts[2])
        pt3 = rs.AddPoint(self.pts[3])
        
        pt0coord = rs.PointCoordinates(pt0)
        pt1coord = rs.PointCoordinates(pt1)
        pt2coord = rs.PointCoordinates(pt2)
        pt3coord = rs.PointCoordinates(pt3)
        
        #find the coordination domain of points inside the rectangular
        x = [pt0coord[0],pt2coord[0]]
        x.sort()
        y = [pt0coord[1],pt2coord[1]]
        y.sort()
        
        xMin = x[0]
        xMax = x[1]
        
        yMin = y[0]
        yMax = y[1]
        
        #find the center point of the rectangular
        pt4 = [(pt0coord[0]+pt1coord[0])/2, (pt0coord[1]+pt1coord[1])/2, (pt0coord[2]+pt1coord[2])/2]
        pt5 = [(pt1coord[0]+pt2coord[0])/2, (pt1coord[1]+pt2coord[1])/2, (pt1coord[2]+pt2coord[2])/2]
        pt6 = [(pt2coord[0]+pt3coord[0])/2, (pt2coord[1]+pt3coord[1])/2, (pt2coord[2]+pt3coord[2])/2]
        pt7 = [(pt3coord[0]+pt0coord[0])/2, (pt3coord[1]+pt0coord[1])/2, (pt3coord[2]+pt0coord[2])/2]
        centerPt = [(pt0coord[0]+pt2coord[0])/2, (pt0coord[1]+pt2coord[1])/2, (pt0coord[2]+pt2coord[2])/2]
        
        #add the center points to the corner points list
        self.pts.append(pt4)
        self.pts.append(pt5)
        self.pts.append(pt6)
        self.pts.append(pt7)
        self.pts.append(centerPt)
        
        #clean up
        rs.DeleteObjects(pt0)
        rs.DeleteObjects(pt1)
        rs.DeleteObjects(pt2)
        rs.DeleteObjects(pt3)
        
        #a loop to draw radial lines from corner points and center points of a rectangular
        for pt in self.pts:
            for i in range(0,25):
                randX = rnd.uniform(xMin, xMax)
                randY = rnd.uniform(yMin, yMax)
                
                randomPt = rs.AddPoint(randX,randY,0)
                
                rs.AddLine(pt,randomPt)
                rs.DeleteObjects(randomPt)


def main():
    #let user to pick the rectangular
    Rect = rs.GetObjects("pick a rectangular")
    #call the class and its function
    SL289 = randomLines(Rect)
    SL289.drawLines()


#call the main function
main()

