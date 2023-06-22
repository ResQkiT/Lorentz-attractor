from PIL import Image
class Loader:
    def __init__(self, path):
        self.image = Image.open(path)


    def getColor(self, c):
        c = c % self.image.size[0]
        pixelData = self.image.load()
        if len(pixelData[c,0]) > 3:
            return pixelData[c,0][:-1:]
        return pixelData[c, 0]
