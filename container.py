from color import Color
from rectangle import Rectangle


class VBoxContainer:
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

    def center(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.set_position(x - (self.width - 2 * self.padding) // 2, y - (self.height - 2 * self.padding) // 2)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.set_position(x - self.padding, y - self.padding)
        self.update_children_position()

    def update_children_position(self):
        child_y = self.y
        for i, child in enumerate(self.children):
            child_position_x = self.x + (
                    self.get_width() - 2 * self.padding - child.get_width()) // 2 if self.centered else self.x
            child_position_y = child_y
            if hasattr(child, 'padding'):
                child_position_x += child.padding
                child_position_y += child.padding

            child.set_position(child_position_x, child_position_y)
            child_y += child.get_height() + self.separation_distance
        self.rect.set_size(self.get_width(), self.get_height())

    def update(self):
        for child in self.children:
            if hasattr(child, 'update'):
                child.update()
        self.update_children_position()

    def get_width(self):
        if self.get_child_count() == 0:
            return 0
        return max([child.get_width() for child in self.children]) + self.padding * 2

    def get_height(self):
        return sum([child.get_height() for child in self.children]) + self.padding * 2 + (
                self.get_child_count() - 1) * self.separation_distance

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
            self.height = sum([child.get_height() for child in self.children]) + self.padding * 2 + (
                    self.get_child_count() - 1) * self.separation_distance
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


class HBoxContainer:
    def __init__(self, x, y, background_color=Color.WHITE, border_color=Color.BLACK, border_width=0,
                 border_radius=0, padding=10, separation_distance=20, centered=True, children=None):
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

    def center(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.set_position(x - (self.width - 2 * self.padding) // 2, y - (self.height - 2 * self.padding) // 2)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.set_position(x - self.padding, y - self.padding)
        self.update_children_position()

    def update_children_position(self):
        child_x = self.x
        for i, child in enumerate(self.children):
            child_position_x = child_x
            child_position_y = self.y + (
                    self.get_height() - 2 * self.padding - child.get_height()) // 2 if self.centered else self.x

            if hasattr(child, 'padding'):
                child_position_x += child.padding
                child_position_y += child.padding

            child.set_position(child_position_x, child_position_y)
            child_x += child.get_width() + self.separation_distance
        self.rect.set_size(self.get_width(), self.get_height())

    def update(self):
        for child in self.children:
            if hasattr(child, 'update'):
                child.update()
        self.update_children_position()

    def get_width(self):
        return sum([child.get_width() for child in self.children]) + self.padding * 2 + (
                self.get_child_count() - 1) * self.separation_distance

    def get_height(self):
        if self.get_child_count() == 0:
            return 0
        return max([child.get_height() for child in self.children]) + self.padding * 2

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
            self.width = sum([child.get_width() for child in self.children]) + self.padding * 2 + (
                    self.get_child_count() - 1) * self.separation_distance
            self.height = max([child.get_height() for child in self.children]) + self.padding * 2
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


class GridContainer:

    def __init__(self, x, y, rows, columns, background_color=Color.WHITE, border_color=Color.BLACK, border_width=0,
                 border_radius=0, padding=10, separation_distance=20, children=None):
        if children is None:
            children = [[None for _ in range(columns)] for _ in range(rows)]
        else:
            if len(children) != rows:
                raise ValueError('Children must be a 2D array of size rows x columns')
            for row in children:
                if len(row) != columns:
                    raise ValueError('Children must be a 2D array of size rows x columns')

        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.rows = rows
        self.columns = columns

        self.grid = VBoxContainer(x, y, background_color, border_color, border_width, border_radius, padding,
                                  separation_distance, True)
        for row in children:
            self.grid.add_child(
                HBoxContainer(x, y, background_color, border_color=background_color, border_width=0, border_radius=0,
                              padding=0, separation_distance=separation_distance, centered=True, children=row))
        self.children = children

    def get_children(self):
        return self.children

    def get_child(self, row, col):
        return self.children[row][col]

    def get_child_count(self):
        counter = 0
        for row in self.children:
            counter += len(row)
        return counter

    def get_child_index(self, child):
        for row in self.children:
            if child in row:
                return self.children.index(child)
        return -1

    def center(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.set_position(x - (self.width - 2 * self.grid.padding) // 2, y - (self.height - 2 * self.grid.padding) // 2)
        self.grid.center(x, y)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.grid.set_position(x, y)

    def update(self):
        self.grid.update()

    def get_width(self):
        return sum([child.get_width() for child in self.children]) + self.grid.padding * 2 + (
                self.get_child_count() - 1) * self.grid.separation_distance

    def get_height(self):
        return sum([child.get_height() for child in self.children]) + self.grid.padding * 2 + (
                self.get_child_count() - 1) * self.grid.separation_distance

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.grid.move(dx, dy)

    def set_size(self):
        if self.get_child_count() == 0:
            self.width = 0
            self.height = 0
        else:
            self.width = sum([child.get_width() for child in self.children]) + self.grid.padding * 2 + (
                    self.get_child_count() - 1) * self.grid.separation_distance
            self.height = sum([child.get_height() for child in self.children]) + self.grid.padding * 2 + (
                    self.get_child_count() - 1) * self.grid.separation_distance
        self.grid.set_size()

    def add_child(self, child, row, col):
        self.children[row][col] = child
        self.grid.set_size()
        self.grid.update_children_position()

    def remove_child(self, child):
        self.children.remove(child)
        self.grid.set_size()
        self.grid.update_children_position()

    def draw(self, screen):
        self.grid.draw(screen)
