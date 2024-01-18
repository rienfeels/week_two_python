import random

class Treat:
    def __init__(self, name, fullness_effect, happiness_effect):
        self.name = name
        self.fullness_effect = fullness_effect
        self.happiness_effect = happiness_effect

class ColdPizza(Treat):
    def __init__(self):
        super().__init__("ColdPizza", 20, 10)

class Bacon(Treat):
    def __init__(self):
        super().__init__("Bacon", 30, 15)

class VeganSnack(Treat):
    def __init__(self):
        super().__init__("VeganSnack", 15, 5)

class Menu:
    def __init__(self, prompt_text, options):
        self.prompt_text = prompt_text
        self.options = options

    def get_choice(self):
        while True:
            try:
                print(self.prompt_text)
                for i, option in enumerate(self.options, start=1):
                    print(f"{i}. {option}")
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Invalid choice. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def eat_food(self, treat):
        self.fullness += treat.fullness_effect
        self.happiness += treat.happiness_effect

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

    def __str__(self):
        return f"Pet name: {self.name}, Fullness: {self.fullness}, Happiness: {self.happiness}"

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    def be_alive(self):
        super().be_alive()  # Call Pet's version of be_alive()
        self.happiness += self.mopiness / 2  # Increase happiness for CuddlyPet

    def cuddle(self, other_pet):
        # Super cuddle powers, activate!
        for i in range(self.cuddle_level):
            other_pet.get_love()

    def __str__(self):
        return f"Pet name: {self.name}, Fullness: {self.fullness}, Happiness: {self.happiness}, Extra cuddly"

def main():
    pet_menu = Menu("Choose a Pet:", ["Regular Pet", "Cuddly Pet", "Exit"])
    treat_menu = Menu("Choose a Treat:", ["ColdPizza", "Bacon", "VeganSnack", "Nothing", "Exit"])

    pet_instance = None  # Initialize pet_instance outside the loop

    while True:
        if not pet_instance:  # Create pet_instance only if it doesn't exist
            pet_choice = pet_menu.get_choice()
            if pet_choice == 1:
                pet_instance = Pet("Buddy")
            elif pet_choice == 2:
                pet_instance = CuddlyPet("Fluffy")
            elif pet_choice == 3:
                print("Exiting the game.")
                return
            else:
                print("Invalid choice. Try again.")
                continue

        treat_choice = treat_menu.get_choice()
        if treat_choice == len(treat_menu.options):  # Exit option
            print("Exiting the game.")
            return

        if treat_choice == 4:  # Treat that does nothing
            treat = Treat("Nothing", 0, 0)
        else:
            if treat_choice == 1:
                treat = ColdPizza()
            elif treat_choice == 2:
                treat = Bacon()
            elif treat_choice == 3:
                treat = VeganSnack()
            else:
                print("Invalid choice. Try again.")
                continue

            pet_instance.eat_food(treat)

            print(f"{pet_instance.name} enjoyed the {treat.name}!")

            # Simulate pet being alive
            pet_instance.be_alive()

            print(f"{pet_instance.name}'s Status - Fullness: {pet_instance.fullness}, Happiness: {pet_instance.happiness}")

            # Check if the pet is still alive
            if pet_instance.fullness <= 0 or pet_instance.happiness <= 0:
                print(f"{pet_instance.name} has passed away. Game over.")
                return

if __name__ == "__main__":
    main()
