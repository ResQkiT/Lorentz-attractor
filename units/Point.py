from Loader import Loader

class Point:
    def __init__(self, x, y, z, lightWeight, drawable):
        self.x = x
        self.y = y
        self.z = z
        self.drawable = drawable
        self.lightWeight = lightWeight

    def isDrawAble(self):
        return self.drawable

    def getNext(self, deltaTime):
        return self.lightWeight.getNext(self.x,
                                        self.y,
                                        self.z,
                                        deltaTime)

    def draw(self):
        self.lightWeight.draw(self.x, self.y, self.z)

