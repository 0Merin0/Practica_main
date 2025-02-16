# Add required methods to the class Vehicle
class Vehicle:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def is_truck(self):
        return self.type == "truck"


if __name__ == "__main__":
    # Assign the needed value to the variable `c`
    # to make the script work without errors
    c = Vehicle("Mercedes", "truck")

    assert isinstance(c, Vehicle)
    assert c.is_truck()
