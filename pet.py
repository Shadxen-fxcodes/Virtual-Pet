class Pet:
    def __init__(self):
        self.name = "Fluffy"
        self.hunger = 100
        self.happiness = 100
        self.energy = 100
        self.health = 100
    
    def feed(self):
        self.hunger = min(100, self.hunger + 10)

    def play(self):
        self.happiness = min(100, self.happiness + 10)
        self.energy = max(0, self.energy - 5)

    def sleep(self):
        self.energy = min(100, self.energy + 20)

    def update(self):
        self.hunger = max(0, self.hunger - 1)
        self.happiness = max(0, self.happiness - 1)

        if self.hunger < 20:
            self.health = max(0, self.health - 1)
