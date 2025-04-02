class Vendor:

    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory \
                or their_item not in other_vendor.inventory:
            return False

        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        self.remove(my_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        return self.swap_items(
                            other_vendor,
                            self.inventory[0],
                            other_vendor.inventory[0]
                            )

    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)

        return items_in_category

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        try:
            best_item = max(items, key=lambda item: item.condition)
            return best_item
        except ValueError:
            return None

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False

        self.swap_items(other_vendor, my_best_item, their_best_item)
        return True
