from random import shuffle

class Die(object):

    def __init__(self, s = 6):
        self.sides = [str(s) for s in range(1, s+1)]
        self.side_up = self.sides[0]

    def __len__(self):
        return len(self.sides)

    def total_sides(self):
        return len(self.sides)

    def __getitem__(self, idx):
        return self.sides[idx]

    def __setitem__(self, idx, val):
        self.sides[idx] = val

    def roll(self):
        shuffle(self.sides)
        self.side_up = self.sides[0]
