from color import Color
from rectangle import Rectangle


class Container:
    def __init__(self, x, y, background_color=Color.WHITE, border_color=Color.BLACK, border_width=0,
                 border_radius=0, padding=10, separation_distance=20, centered=False, children=None):
        if children is None:
            children = []
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.background_color = background_color
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.padding = padding
        self.separation_distance = separation_distance
        self.centered = centered

        self.rect = Rectangle(self.x - self.padding, self.y - self.padding, self.width, self.height,
                              self.background_color, self.border_color, self.border_width, self.border_radius)

        self.children = children
        self.set_size()
        self.update_children_position()

    def get_children(self):
        return self.children

    def get_child(self, index):
        return self.children[index]

    def get_child_count(self):
        return len(self.children)

    def get_child_index(self, child):
        return self.children.index(child)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.set_position(x - self.padding, y - self.padding)
        self.update_children_position()

    def update_children_position(self):
        child_y = self.y
        for i, child in enumerate(self.children):
            child_position_x = self.x + (self.width - 2 * self.padding - child.get_width()) // 2 if self.centered else self.x
            child_position_y = child_y
            if hasattr(child, 'padding'):
                child_position_x += self.padding
                child_position_y += self.padding

            child.set_position(child_position_x, child_position_y)
            child_y += child.get_height() + self.separation_distance

    def update(self):
        for child in self.children:
            if hasattr(child, 'update'):
                child.update()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.move(dx, dy)
        for child in self.children:
            child.move(dx, dy)

    def set_size(self):
        if self.get_child_count() == 0:
            self.width = 0
            self.height = 0
        else:
            self.width = max([child.get_width() for child in self.children]) + self.padding * 2
            self.height = sum([child.get_height() for child in self.children]) + self.padding * 2 + (self.get_child_count() - 1) * self.separation_distance
        self.rect.set_size(self.width, self.height)

    def add_child(self, child):
        self.children.append(child)
        self.set_size()
        self.update_children_position()

    def remove_child(self, child):
        self.children.remove(child)
        self.set_size()
        self.update_children_position()

    def draw(self, screen):
        self.rect.draw(screen)
        for child in self.children:
            child.draw(screen)
