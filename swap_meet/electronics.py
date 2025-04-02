from swap_meet.item import Item


class Electronics(Item):

    def __init__(self, id=None, condition=0, age=0, type="Unknown"):
        super().__init__(id, condition, age)
        self.type = type

    def __str__(self):
        return super().__str__() + f" This is a {self.type} device."
