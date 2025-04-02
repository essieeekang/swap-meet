from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.vendor import Vendor


def test_item_created_correctly_with_age():
    skirt = Clothing(age=1)
    poster = Decor(age=1)
    gameboy = Electronics(age=1)

    assert skirt.age == 1
    assert poster.age == 1
    assert gameboy.age == 1


def test_item_created_correctly_with_default_age():
    skirt = Clothing()
    poster = Decor()
    gameboy = Electronics()

    assert skirt.age == 0
    assert poster.age == 0
    assert gameboy.age == 0


def test_get_newest_my_item():
    skirt = Clothing(age=3)
    poster = Decor(age=1)
    gameboy = Electronics(age=5)
    tai = Vendor(inventory=[skirt, poster, gameboy])

    newest_item = tai.get_newest()

    assert newest_item == poster


def test_get_newest_empty_inventory():
    jesse = Vendor()

    newest_item = jesse.get_newest()

    assert not newest_item


def test_swap_by_newest():
    skirt = Clothing(age=3)
    poster = Decor(age=1)
    gameboy = Electronics(age=5)
    shirt = Clothing(age=1)
    chair = Decor(age=4)
    tai = Vendor(inventory=[skirt, poster, gameboy])
    jesse = Vendor(inventory=[shirt, chair])

    result = tai.swap_by_newest(jesse)

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 2
    assert skirt in tai.inventory
    assert gameboy in tai.inventory
    assert shirt in tai.inventory
    assert poster in jesse.inventory
    assert chair in jesse.inventory


def test_swap_by_newest_inventory_empty():
    skirt = Clothing(age=3)
    poster = Decor(age=1)
    gameboy = Electronics(age=5)
    tai = Vendor(inventory=[skirt, poster, gameboy])
    jesse = Vendor()

    result = tai.swap_by_newest(jesse)

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert skirt in tai.inventory
    assert gameboy in tai.inventory
    assert poster in tai.inventory
