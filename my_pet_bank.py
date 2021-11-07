# python Pet Banks
from random import randrange


# defineing the pet
class Pet(object):
    """A Virtual Pet for Better Banking Habits"""
    age = 0
    excitment_reduce = 3
    excitment_max = 10
    excitment_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"Grrr..."', '"Hello"']
    
# building pet needs and happiness
    
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.food = randrange(self.excitment_max)
        self.excitment = randrange(self.excitment_max)
        self.vocab = self.vocab[:]
    
# -delta happiness
    def __clock_tick(self):
        self.excitment -= 1
        self.food -= 1

# perameters of happiness   
    def mood(self):
        if self.food > self.food_warning and self.excitment > self.excitment_warning:
            return "Happy"
        elif  self.food < self.food_warning and self.excitment < self.excitment_warning:
            return "Bored and Hungry"
        elif self.food < self.food_warning:
            return "Hungry"
        elif self.excitment < self.excitment_warning:
            return "Bored"
        
# 
    def __str__(self):
        return "\nI'm" + self.name + "."+ "\n I am" + self.mood() + "."
    
    def teach(self, word):
        self.vocab.append(word)
        self.__clock_tick()
        
    def talk(self):
        print(
            "I am a ",
            self.animal_type,
            " named ",
            self.name,
            ".",
            "I feel ",
            self.mood(),
            " now.\n"
            )
        self.__clock_tick()
        
    def feed(self):
        print("***Crunch*** \n mmm.. Thank you!")
        meal = randrange(self.food, self.food_max)
        self.food += meal
        
        if self.food < 0:
            self.food = 0
            print("I am still hungry")
        elif self.food > self.food_max:
            self.food = self.food_max
            print("I am so Full, I feel fat!")
        else:
            print("I am fine but, I would could eat more food.")
        self.__clock_tick()
    
    def play(self):
        print("Weeeee!!!")
        fun = randrange(self.excitment, self.excitment_max)
        self.excitment += fun
        if self.excitment < 0: 
            self.excitment = 0
            print("I am bored.")
        elif self.excitment > self.excitment_max:
            self.excitment = self.excitment_max
            print("That was fun i should relax now!")
        self.__clock_tick


def main():
    pet_name = input("What do you want to name your pet?")
    pet_type = input("What kind of animal is your pet")
    
#Create new pet
    my_pet = Pet(pet_name, pet_type)
    input(
        "Hello World! I am " +
        my_pet.name + 
        "I am new here!" +
        "\n Press enter to start."
    )
    
    choice = None
    
    while choice != 0:
        print(
            """
            Interact with your pet.
            
            1. Feed your pet_name
            2. Talk to your pet
            3. Teach your pet a new word
            4. Play with your pet
            0. quit
            
            """
        )
        choice = input("choice: ")
        
        if choice == "0":
            print("I'm glad you came. I'll see your next time.\n Goodbye")
        elif choice == "1":
            my_pet.feed()
        elif choice == "2":
            my_pet.talk()
        elif choice == "3":
            new_word = input("What would you like to teach " + my_pet.name +" to say?")
            my_pet.teach(new_word)
        elif choice == "4":
            my_pet.play()
        else:
            print("silly, that DoSnT MAKE scensesssssssssssss <<<INVALID RESPONSE>>>")
main()