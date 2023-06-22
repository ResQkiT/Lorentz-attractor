from PIL import Image
class Loader:
    def __init__(self, path):
        self.image = Image.open(path)


    def getColor(self, c):
        c = c % self.image.size[0]
        pixelData = self.image.load()
        return pixelData[c,0][:-1:]

