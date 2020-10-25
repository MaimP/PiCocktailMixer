class Drinks:

    def __init__(self):
        self.drinklist = []
        self.mainchoice = ["Korn", "Bacardi", "Vodka", "Fanta", "Cola", "Sprite"]
        self.readChoice()
        self.newchoice = self.old_new_choice
        self.newchoice

    def readDrinks(self):
        with open("drinks.txt") as file:
            drinks_raw = file.readlines()

        drinks = [x.strip() for x in drinks_raw]
        counter = 0
        for i in drinks:
            self.drinklist.append(drinks[counter])
            counter += 1
        file.close()

    def checkDrink(self, drink):
        self.readDrinks()
        if drink in self.drinklist:
            return True
        return False

    def newDrinks(self, drink):
        if not self.checkDrink(drink):
            file = open("drinks.txt", "a")
            file.write(drink + "\n")
            file.close()
        else:
            print("das getraenk ist bereits in der Liste")

    def searchDrink(self, drink):
        print("**2 1")
        self.readDrinks()
        self.searched_drink_index = None
        counter_index = 0
        if self.checkDrink(drink):
            print("**2 2 if")
            for i in self.drinklist:
                print("**2 3")
                if drink in self.drinklist[counter_index]:
                    print("**2 4")
                    self.searched_drink_index = counter_index
                    print("Index: {}".format(self.searched_drink_index))
                    return self.searched_drink_index
                counter_index += 1
                print("index: {}".format(counter_index))
        else:
            print("**2 2 else")
            print("Drink does not exist")


    def mainChoice(self):
        return self.mainchoice

    def readChoice(self):
        with open("drinks_newchoice.txt") as new_file:
            old_new_choice_raw = new_file.readlines()
        self.old_new_choice = [x.strip() for x in old_new_choice_raw]

    def writeChoice(self):
        file = open("drinks_newchoice.txt", "w")
        counter = 0
        for i in self.newchoice:
            file.write(self.newchoice[counter] + "\n")
            counter += 1
        file.close()

    def newChoice(self, old, new):
        # schreibe main in newcoice fuer anfangsausgang
        # bei neuer choice, schreibe alle in liste newChoice, danach alle in new choice.txt
        # anderen ueberschreiben
        self.readChoice()
        counter_index = 0
        for line in self.old_new_choice:
            if old in line:
                old_index = counter_index
            counter_index += 1

        self.newchoice[old_index] = new
        self.writeChoice()
        return self.newchoice

if __name__ == '__main__':
    test_var = Drinks()
    Drinks.newChoice(test_var, "Vodka", "Wasser")
