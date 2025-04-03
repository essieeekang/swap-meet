import uuid

CONDITION_DESCRIPTIONS = {
    0: "Acceptable",
    1: "Good",
    2: "Very Good",
    3: "Excellent",
    4: "Like New",
    5: "New"
}


class Item:
    def __init__(self, id=None, condition=0, age=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age  # age in years

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        condition = self.condition // 1

        if condition not in CONDITION_DESCRIPTIONS:
            return "Condition Out of Range"

        return CONDITION_DESCRIPTIONS[condition]
