#!/usr/bin/python3

class square():
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        The Area of The square
        """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """
        permiter of my square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        diplaying the object
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
