import random

class Tree:
    def __init__(self):
        self.shade_effect = 2

class Gnome:
    def __init__(self):
        self.rain_chance = 0.05

class Woodchuck:
    def __init__(self):
        self.disappear_chance = 0.05

class Garden:
    def __init__(self):
        self.trees = []
        self.gnomes = []
        self.woodchucks = []
        self.fruit_trees = []
        self.squirrels = [] 

def simulate_turn(garden, turn):
    # Check for rain
    rain_chance = sum(gnome.rain_chance for gnome in garden.gnomes)
    if random.random() < rain_chance:
        print(f"Turn {turn}: It's raining!")

    # Check for Woodchuck
    woodchuck_chance = sum(woodchuck.disappear_chance for woodchuck in garden.woodchucks)
    if random.random() < woodchuck_chance:
        if garden.trees:
            removed_tree = random.choice(garden.trees)
            garden.trees.remove(removed_tree)
            print(f"Turn {turn}: A Woodchuck moved in and a Tree disappeared!")

    # Check for new Tree or Gnome every 10 turns
    if turn % 10 == 0:
        if random.choice([True, False]):
            garden.trees.append(Tree())
            print(f"Turn {turn}: A new Tree grew!")

        if random.choice([True, False]):
            garden.gnomes.append(Gnome())
            print(f"Turn {turn}: A new Gnome moved in!")

def simulate_garden():
    garden = Garden()
    turn = 1

    while len(garden.trees) < 10 and sum(fruit_tree.fruit < 10 for fruit_tree in garden.fruit_trees) == 0:
        simulate_turn(garden, turn)

        # Check for FruitTree
        for tree in garden.trees:
            if isinstance(tree, FruitTree):
                if tree.water_level >= 100:
                    tree.fruit += 1
                    print(f"Turn {turn}: A FruitTree produced a fruit!")

        # Check for Squirrel
        squirrel_chance = sum(squirrel.decrease_chance for squirrel in garden.squirrels)
        for fruit_tree in garden.fruit_trees:
            if random.random() < squirrel_chance and fruit_tree.fruit > 0:
                fruit_tree.fruit -= 1
                print(f"Turn {turn}: A Squirrel ate a fruit from a FruitTree!")

        turn += 1

    print("Simulation ended.")

class FruitTree(Tree):
    def __init__(self):
        super().__init__()
        self.water_level = 0
        self.fruit = 0

class Squirrel:
    def __init__(self):
        self.decrease_chance = 0.05

simulate_garden()
