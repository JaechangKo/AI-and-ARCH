#scripts to create recursive growth
import rhinoscriptsyntax as rs

#class to create the first group of objects
class CreateBox1():
    def __init__(self, box, iterations, factor):
        #initialize class values from inputed parameters
        self.box = []
        self.box.append(box)
        self.iterations = iterations
        self.factor = factor
        
        #function to draw objects
    def drawBox1(self): 
        #conditional to break recursion loop
        if self.iterations == 0:
            return
        else:
            #create blank list to store new branches in
            newboxes=[]
            #perform on each branch by looping through all
            for box in self.box:
                #evaluate object to locate growth origin
                points = rs.BoundingBox(box)
                #find the geometry center of the input object
                crv = rs.AddCurve((points[0],points[2],points[6],points[4],points[0]),degree=1)
                centroid = rs.CurveAreaCentroid(crv)
                centroid = centroid[0]
                #deleve process crv to clean
                rs.DeleteObject(crv)
                scale = [self.factor,self.factor,self.factor]
                #create vector for growth direction
                vector1 = rs.VectorCreate(points[1],centroid)
                vector2 = rs.VectorCreate(points[3],centroid)
                vector3 = rs.VectorCreate(points[4],centroid)
                vector4 = rs.VectorCreate(points[6],centroid)

                #create new objects by copy the input object and scale it
                newbox1 = rs.CopyObject(box,vector1)
                newbox1 = rs.ScaleObject(newbox1, points[1], scale, copy=False)
                newbox2 = rs.CopyObject(box,vector2)
                newbox2 = rs.ScaleObject(newbox2, points[3], scale, copy=False)
                newbox3 = rs.CopyObject(box,vector3)
                newbox3 = rs.ScaleObject(newbox3, points[4], scale, copy=False)
                newbox4 = rs.CopyObject(box,vector4)
                newbox4 = rs.ScaleObject(newbox4, points[6], scale, copy=False)

                #add new objects to the list for futher growth
                newboxes.append(newbox1)
                newboxes.append(newbox2)
                newboxes.append(newbox3)
                newboxes.append(newbox4)

            #assign the new list to growth parameter
            self.box = newboxes
            #go to next iteration
            self.iterations -=1
            #call the class's function again
            self.drawBox1()
            
            
#class to create the second group of objects(same logic, but opposite growth direction to increase the complexity of the final object)
class CreateBox2():
    def __init__(self, box, iterations, factor):
        self.box = []
        self.box.append(box)
        self.iterations = iterations
        self.factor = factor
        
    def drawBox2(self): 
        if self.iterations == 0:
            return
        else:
            newboxes=[]
            for box in self.box:
                points = rs.BoundingBox(box)
                crv = rs.AddCurve((points[0],points[2],points[6],points[4],points[0]),degree=1)
                centroid = rs.CurveAreaCentroid(crv)
                centroid = centroid[0]
                rs.DeleteObject(crv)
                scale = [self.factor,self.factor,self.factor]
                vector1 = rs.VectorCreate(points[0],centroid)
                vector2 = rs.VectorCreate(points[2],centroid)
                vector3 = rs.VectorCreate(points[5],centroid)
                vector4 = rs.VectorCreate(points[7],centroid)

                newbox1 = rs.CopyObject(box,vector1)
                newbox1 = rs.ScaleObject(newbox1, points[0], scale, copy=False)
                newbox2 = rs.CopyObject(box,vector2)
                newbox2 = rs.ScaleObject(newbox2, points[2], scale, copy=False)
                newbox3 = rs.CopyObject(box,vector3)
                newbox3 = rs.ScaleObject(newbox3, points[5], scale, copy=False)
                newbox4 = rs.CopyObject(box,vector4)
                newbox4 = rs.ScaleObject(newbox4, points[7], scale, copy=False)

                newboxes.append(newbox1)
                newboxes.append(newbox2)
                newboxes.append(newbox3)
                newboxes.append(newbox4)

            self.box = newboxes
            self.iterations -=1
            self.drawBox2()
                
                
def main():
    #ask user for base object
    box = rs.GetObjects("Select a geometry for growth")
    #call the first class and its embedded function to create the first group of objects
    Object1 = CreateBox1(box,4,0.5)
    Object1.drawBox1()
    
    #call the second class and its embedded function to create the second group of objects
    Object2 = CreateBox2(box,4,0.5)
    Object2.drawBox2()
    

#rs.EnableRedraw(False)


#call the main function
main()

