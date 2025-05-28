class TV:
    def turn_on (self):
        print("TV is on")
    def turn_off (self):
        print("TV is off")
class remote:
    def __init__(self):
        self.TV = TV()

    def turn_on (self):
        self.TV.turn_on()
    def turn_off (self):
        self.TV.turn_off()
remote = remote()
remote.turn_on()
remote.turn_off()

