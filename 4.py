class Device:
    def turn_on(self):
        print("Device is turned on")


    def turn_off(self):
        print("Device is turned off")


class Phone(Device):
    pass


class Laptop(Device):
    pass


class TV(Device):
    pass


phone = Phone()
laptop = Laptop()
tv = TV()

phone.turn_on()
laptop.turn_on()
tv.turn_off()