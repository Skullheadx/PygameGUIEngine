class Color:
    BLACK = (0, 0, 0)
    DARK_GRAY = (64, 64, 64)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (192, 192, 192)
    WHITE = (255, 255, 255)

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    @staticmethod
    def darken(color, amount):
        return max(0, color[0] - amount), max(color[1] - amount, 0), max(color[2] - amount, 0)

    @staticmethod
    def lighten(color, amount):
        return min(255, color[0] + amount), min(color[1] + amount, 255), min(color[2] + amount, 255)
