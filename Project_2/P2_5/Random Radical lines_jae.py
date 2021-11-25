#scripts to creat a 6x6 morphospace of absolute tower

import rhinoscriptsyntax as rs
        
class MyColumn:
    #A Class to create a column profile.
    
    def __init__(self, segments, radius, offset, origin):
        #create variables, passed from initialization declaration
        self.radius = radius
        self.origin = origin
        self.segments = segments
        self.offset = offset
        
        #create circle at origin of radius provided
        self.circle = rs.AddCircle(self.origin,self.radius)  
        #divide circle by number of segments provided
        self.pts = rs.DivideCurve(self.circle, self.segments)
        
        #for loop to select every other point on curve...note step of 2
        for i in range(0,len(self.pts),2):
            #create vector from each point to center and scale by offset provided
            vector = rs.VectorCreate(self.origin, self.pts[i])
            vector = rs.VectorUnitize(vector)
            vector = rs.VectorScale(vector,self.offset)
            self.pts[i] = rs.PointAdd(self.pts[i],vector)
        #add first point of list to end of list of points to close curve    
        self.pts.append(self.pts[0])
        
        #delete the circle curve to clean up final geometry
        rs.DeleteObject(self.circle)
            
        #return points
        return self.pts
        
    def makeProfile(self, degree):
        #a function to draw a curve of a degree provided
        self.degree = degree
        return rs.AddCurve(self.pts,self.degree)

def main():
    #assign height for columns
    height = 30
    
    #create an empty list for column profiles
    profiles = []
    
    #make the drawing faster
    rs.EnableRedraw(False)
    
    #loop to call class
    for i in range(0,6):
        for j in range(0,6):
            #set an origin point
            ColumnPt = [i*20,j*20,0]
            
            #set a radius for top and bottome crv
            radius = i/2+1.5
            
            #create bottom and top profiles for columns and add them to the profile list
            bottom = rs.AddCircle(ColumnPt,radius)
            profiles.append(bottom)
            top = rs.CopyObject(bottom,[0,0,height])
            profiles.append(top)
            
            #call the column class to create middle profile for column and add them to the profile list
            middle = MyColumn((i+3)*2,3,2,[ColumnPt[0],ColumnPt[1],ColumnPt[2]+(height/5+j*4)])
            middle = middle.makeProfile(3)
            profiles.append(middle)
            
            #loft the profiles to get columns
            column = rs.AddLoftSrf((bottom,middle,top),start=None, end=None, loft_type=0, simplify_method=0, value=0, closed=False)
            
            #cap geometry
            rs.CapPlanarHoles(column)

    #delete profiles to clean up
    rs.DeleteObjects(profiles)
    
    
#call the main function
main()







