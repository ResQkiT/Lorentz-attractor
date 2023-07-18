from PIL import Image
class Loader:
    image = 0
    imageData = []
    @staticmethod
    def init(path):
        Loader.image = Image.open(path)
        Loader.imageData = Loader.image.load()

    @staticmethod
    def getColor(c):
        if Loader.image == 0:
            print("Пройдите инициализацию")
            return 0

        c = c % Loader.imageData[0]

        if len(Loader.imageData[c,0]) > 3:
            return Loader.imageData[c,0][:-1:]
        return Loader.imageData[c, 0]
