def setup():
    global a,M
    size(400,400,P3D)
    smooth(8)
    ortho()
    M = Matrix(X,Y,0.85)
    a = 0
def draw():
    global a
    background(0)
    ortho(-width/2, width/2, 
          -height/2, height/2)
    X = 15
    Y = 15
    sz = 50
    sx = 80
    sy = 80
    #Applying custom shear Matrix

    rotateX(PI/4)
    rotateZ(PI/4)
    stroke(0,20)
    for i in range(X):
        parami = 5.0*i/(X-1)
        for j in range(-Y,Y):
            paramj = 5.0 * j/(Y-1)
            with pushMatrix():
                translate(i*sx,j*sy,0)
                boxc(sz,sz,100,sn(TWO_PI*a+parami+paramj))
    a += 0.0025
    if(a > 1.0): exit()
    #saveFrame("output/animation###.png")
def boxc(L,W,H,T):
    points = [PVector(0,0),
              PVector(L,0),
              PVector(L,W),
              PVector(0,W),
              PVector(0,0)]
    #noStroke()
    #
    #
    with beginShape(QUAD_STRIP):
        for i in points:
            fill(lerp(255,0,T))
            vertex(i.x,i.y,0)
            fill(lerp(0,255,T))
            vertex(i.x,i.y,lerp(-H,H,T))

def smoothstep(edge0, edge1, x):
    # Scale, bias and saturate x to 0..1 range
    x = constrain((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    # Evaluate polynomial
    return x * x * (3 - 2 * x)

def normalizeList(alist,multiply): return [1.0*multiply*i/sum(alist) for i in alist]
def sn(q): return smoothstep(0.0,0.8,sin(q))#lerp(-1, 1, ease(map(sin(q), -1, 1, 0, 1), 5))

#########
def expression(time,i,j):
    amplitude = 5.0
    frequency = 0.1
    delay = 1.0*(i+j)/(X+Y-2)
    
    transformation = sin(TWO_PI*time+delay*frequency)
    transformation += cos(TWO_PI*time+frequency+delay)
    transformation += sin(TWO_PI*time+frequency*2.1+delay)
    transformation += sin(TWO_PI*time+frequency*1.72+delay)
    transformation += cos(TWO_PI*time+frequency*2.221+delay)
    transformation += sin(TWO_PI*time+frequency*3.1122+delay)
    transformation *= amplitude
    return map(transformation,-amplitude,amplitude,0,1)

class Matrix(object):
    def __init__(self, X, Y, chance):
        #coloroptions = [color(225,0,0),color(225,128,0),color(0,50,230),color(255,255,255)]
        self.X = X
        self.Y = Y
        self.WIDTH = 1100
        self.HEIGHT = 1100
        #self.modules = data
        
        #self.biases = [0,1,3,1,2,2,1,1,2,0,1,1,1,1]
        #self.modules = bias(self.modules,self.biases)
        #self.modules = shuffle(self.modules)
        #self.choices = [[floor(random(len(self.modules))) for j in range(X)] for i in range(Y)]
        
        #Cancel a module given some chance threshold
        self.canceled = [[1 if random(1)>=chance else 0 for j in range(X)] for i in range(Y)]
        
    def module(self,someShape,X,Y,W,H):
        #DEFUNCT, USE DATA LOADER ABOVE
        """This function is where you'll keep your module. Keep in mind that this is
        considering the display in CORNER mode.
        """
        global Ushape
        
        if(W != 0):
            shape(someShape,X,Y,W,H)
            #shape(anotherShape,X,Y,W,H)
            #shape(sides,X,Y,W,H)
    def getMatrix(self):
        """This is where Matrix is dynamically updated"""
        #Choice of using sin and cos vs sin and cos
        return [[0 if not self.canceled[i][j] else expression(a,i,j) for j in range(self.X)] for i in range(self.Y)]
    def displayH(self):
        """Equal spaced Y, dynamic X"""
        Matrix = self.getMatrix()
        Matrix = [normalizeList(i,width) for i in Matrix]
        shiftY = 0
        spaceY = 1.0*height/Y
        param = [0,0]
        for row in Matrix:
            shiftX = 0
            param[0] = 0
            for i in row:
                with pushMatrix():
                    #scale(1,1,555*noise(scl*param[1]+cos(TWO_PI*a),scl*param[0]+sin(TWO_PI*a)))
                    #self.module(shiftX,shiftY,i,spaceY)
                    scale(1,1,255*noise(radius*cos(TWO_PI*a)+sum(param)))
                    if(i > 0): self.module(self.modules[self.choices[param[1]][param[0]]],shiftX,shiftY,i,spaceY)
                shiftX += i
                param[0]+=1
            shiftY += spaceY
            param[1]+=1
    def displayV(self):
        """Equal spaced X, dynamic Y"""
        Matrix = self.getMatrix()
        Matrix = [normalizeList(i,width) for i in Matrix]
        shiftX = 0
        spaceX = 1.0*width/X
        param = [0,0]
        for row in Matrix:
            shiftY = 0
            param[0] = 0
            for i in row:
                with pushMatrix():
                    #scale(1,1,555*noise(scl*param[0]+cos(TWO_PI*a),scl*param[1]+sin(TWO_PI*a)))
                    scale(1,1,255*noise(radius*cos(TWO_PI*a)+sum(param)))
                    if(i > 0): self.module(self.modules[self.choices[param[1]][param[0]]],shiftX,shiftY,spaceX,i)
                shiftY += i
                param[0]+=1
            shiftX += spaceX
            param[1]+=1
    def displayU(self):
        """Unequal spaced Y, dynamic X"""
        Matrix = self.getMatrix()
        Matrix = [normalizeList(i,self.WIDTH) for i in Matrix]
        shiftY = 0
        spaceY = [sin(TWO_PI*a+1.0*i/(1-Y)) for i in range(Y)]
        spaceY = normalizeList(spaceY,self.HEIGHT)
        param = [0,0]
        stretch = False
        for row in Matrix:
            shiftX = 0
            val = spaceY.pop(0)
            param[0] = 0
            for i in row:
                with pushMatrix():
                    scale(1,1,255*sin(TWO_PI*a+5.0*sum(param)/(X+Y-2)))
                    #scale(1,1,555*noise(cos(TWO_PI*a)+sum(param)))
                    if(not stretch): self.module(self.modules[self.choices[param[1]][param[0]]],shiftX,shiftY,i,val)
                shiftX += i
                param[0]+=1
            shiftY += val
            param[1]+=1
    def display(self):
        """Dynamic Y, dynamic X"""
        Matrix = self.getMatrix()
        Matrix = [normalizeList(i,width) for i in Matrix]
        shiftY = 0
        spaceY = [[noise(scl*i+cos(TWO_PI*a)+25334,scl*j+radius*sin(TWO_PI*a)+25334) for j in range(X)] for i in range(Y)]
        spaceY = [normalizeList(row,height) for row in spaceY]
        shiftY = [0 for i in range(X)]
        param = [0,0]
        for row in Matrix:
            shiftX = 0
            someValues = spaceY.pop(0)
            
            count = 0
            param[0] = 0
            for j,i in zip(shiftY,row):
                val = someValues.pop(0)
                with pushMatrix():
                    scale(1,1,255*noise(radius*cos(TWO_PI*a)+sum(param)))
                    self.module(self.modules[self.choices[param[1]][param[0]]],shiftX,j,i,i)                
                shiftX += i
                shiftY[count] += val
                count+=1
                param[0]+=1
            param[1]+=1

def noiseFunc():
    pass
    
############

def normalizeList(alist,multiply): return [1.0*multiply*i/(sum(alist)+0.0001) for i in alist]

def bias(modules, multiples):
    output = []
    for i,j in zip(modules,multiples):
        output+=[i]*j
    return output

def shuffle(alist):
    jumble = alist
    for i,letter in enumerate(jumble):
        r = int(random(i))
        jumble[i],jumble[r] = jumble[r],jumble[i]
    return jumble

def keyPressed():
    frameCount = -1;
##########

def setPShape(someShape):
    someShape.disableStyle()
    someShape.setStrokeWeight(5)
    someShape.setFill(color(230))
    return someShape

def ease(p): return 3*p*p - 2*p*p*p;

def ease(p, g):
    if (p < 0.5): 
        return 0.5 * pow(2*p, g);
    else:
        return 1 - 0.5 * pow(2*(1 - p), g);

def sn(q): return lerp(-1, 1, ease(map(sin(q), -1, 1, 0, 1), 5))
def cs(q): return lerp(-1, 1, ease(map(cos(q), -1, 1, 0, 1), 5))
