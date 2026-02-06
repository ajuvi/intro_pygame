class GameObject:

    def __init__(self, x, y, width=None, height=None, color=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color=color

    def Update():
        pass

    def Draw(self, pantalla):
        pass

    def __str__(self):
        return f"GameObject(x={self.x}, y={self.y}, width={self.width}, height={self.height})"