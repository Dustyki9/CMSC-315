"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================
"""

from copy import copy, deepcopy


class House:  # having it describe the House
    Frontdoor = 1

    def __init__(self, beds, baths):  # how many beds and baths the house has
        self.beds = beds
        self.baths = baths

    def description(self):
        return f"{self.beds} beds and {self.baths} baths, with {self.Frontdoor} Frontdoor."


class Apartment(House):
    has_elevator = True

    def __init__(self, beds, baths, floor_number, monthly_rent):
        super().__init__(beds, baths)
        self.floor_number = floor_number
        self.monthly_rent = monthly_rent

    def elevator_status(self):
        if self.has_elevator:
            return "Ding going up!"
        else:
            return "I guess ill take the stairs :("

    def description(self):
        return f"Apartment {self.beds} beds, {self.baths} Baths on floor {self.floor_number} with {self.monthly_rent} monthly rent."


def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    apt1 = Apartment(2, 1, 5, 1500)
    apt2 = Apartment(3, 2, 8, 2200)

    print("Class access:", Apartment.has_elevator)
    print("Instance access:", apt1.has_elevator)

    apt1.pet_friendly = True

    print("apt1 namespace:", apt1.__dict__)
    print("apt2 namespace:", apt2.__dict__)
    print("Class namespace:", Apartment.__dict__)


def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    apt1 = Apartment(2, 1, 5, 1500)
    apt1.amenities = ["Pool", "Gym"]

    shallow = copy(apt1)
    deep = deepcopy(apt1)

    apt1.amenities.append("sauna")

    print("Original amenities:", apt1.amenities)
    print("Shallow copy amenities:", shallow.amenities)
    print("Deep copy amenities:", deep.amenities)


def main():
    print("=== Unit 1 OOP Assignment ===")

    my_house = House(4, 2)
    print("my_house.description(): ", my_house.description())

    my_apartment = Apartment(2, 1, 5, 1500)
    print(my_apartment.description())
    print(my_apartment.elevator_status())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
