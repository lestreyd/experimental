def add_mech_attributes(attributes):
    def decorate_class(cls):
        for attribute in attributes:
            def get_attribute(self, attr_name=attribute):
                return getattr(self, "_" + attr_name)
            def set_attribute(self, value, attr_name=attribute):
                setattr(self, "_" + attr_name, value)
            additional_property = property(get_attribute, set_attribute)
            setattr(cls, attribute, additional_property)
            setattr(cls, "_" + attribute, None)
        return cls
    return decorate_class


@add_mech_attributes(['model', 'vendor', 'weight'])
class MechPart:
    def __init__(self, price=0):
        self.price = price


@add_mech_attributes(['accuracy', 'weapon'])
class MechArm(MechPart):
    def __init__(self):
        super().__init__(self)


if __name__ == "__main__":
    mech_arm = MechArm()
    mech_arm.model = "M-1"
    mech_arm.vendor = "Lockheed"
    mech_arm.weight = 30
    mech_arm.price = 71_000
    mech_arm.accuracy = .4
    mech_arm.weapon = "Assault Rifle"

    print (f"{mech_arm.vendor} {mech_arm.model} [{mech_arm.weapon}]")