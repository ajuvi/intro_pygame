from GameObject import GameObject

class Nau(GameObject):

    def __init__(self, x, y, width=None, height=None, color=None):
        super().__init__(x, y, width, height, color)
        self.velocitat = 5
        self.vx = 1
        self.vy = 0

    def update(self):
        self.x += self.vx * self.velocitat
        self.y += self.vy * self.velocitat

    def direccio(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def setPosicio(self, x, y):
        self.x=x
        self.y=y

    def draw(self,pantalla):
        pantalla.pintar_rectangle(self.x,self.y,self.width,self.height,self.color) 

    def colissio(self,other):
        pass

    def __str__(self):
        return f"Nau(x={self.x}, y={self.y}, width={self.width}, height={self.height})"