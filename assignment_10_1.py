'''
Luke Rasmussen
Assignment 10.1 Your Own Class
This script contains code for a class based on a real world object
'''

class Cup():
    # class variable
    what_is_my_purpose = 'My purpose is to hold liquid.'

    # Constructor
    def __init__(self, size, volume, name):
        self.__cup_size = size
        self.__volume = volume
        self.__volume_state = 'This cup is full.'
        self.__name = name

    # get methods
    def get_cup_size(self):
        return self.__cup_size
    def get_volume(self):
        return self.__volume
    def get_name(self):
        return self.__name

    # set methods
    def set_cup_size(self, new_size):
        self.__cup_size = new_size
    def set_volume(self, new_volume):
        self.__volume = new_volume

    # other methods
    def display(self):
        print("\n" + self.what_is_my_purpose)
        print(f"Size of the {self.get_name()} cup: {self.get_cup_size()}")
        print(f"Volume of the {self.get_name()} cup: {self.get_volume()}")

    def spill(self):
        self.__volume_state = (f"\nOh No! Our {self.get_name()} cup! It's empty!")
        self.__volume = 0
        print(self.__volume_state)

def main():
    # create the cup objects and display their information, including all data and class variables.
    first_cup = Cup('medium', 300, 'First')
    second_cup = Cup('large', 600, 'Second')
    first_cup.display()
    second_cup.display()

    # edit the size and volume of one of the cups
    first_cup.set_cup_size('small')
    first_cup.set_volume(150)
    first_cup.display()

    # use one of the class' methods to spill one of the cups
    first_cup.spill()
    first_cup.display()

    # use the other methods in the class to share between the two cups
    new_volume = int(second_cup.get_volume() / 2)
    second_cup.set_volume(new_volume)
    if (second_cup.get_volume() == first_cup.get_volume()):
        first_cup.set_volume(new_volume)
    else:
        new_volume = int(second_cup.get_volume() / 4)
        first_cup.set_volume(new_volume)
        second_cup.set_volume(second_cup.get_volume() + new_volume)
    first_cup.display()
    second_cup.display()
    
if __name__ == '__main__':
    main()