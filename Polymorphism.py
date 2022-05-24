





class Twins():
    name = ""
    father = "Jerome"
    id_number = "1234"
    dob = ""

    def getTwinsInfo(self):
        enter_name = input("Enter your name: ")
        enter_father = input("Enter your fathers name: ")
        enter_id_number = input("Enter your id number: ")
        enter_dob = input("Enter your date of birth: ")
        if (enter_father == self.father and enter_id_number == self.id_number):
            print("Welcome back, {}!".format(enter_name))
        else:
            print("The fathers name or id number is incorrect")
    

class Tom(Twins):
    name = "Tom Tucker"
    father = "Jerome"
    ssn = 123
    height = "6\' 4\""
    weight = "212" + "lbs"
    shoe_size = "12"

class Brady(Twins):
    name = "Brady Quinn"
    father = "Jerome"
    ssn = 124
    height = "6\' 2"
    weight = "195" + "lbs"
    shoe_size = "12"

    def getTwinsInfo(self):
        enter_name = input("Enter your name: ")
        enter_father = input("Enter your fathers name: ")
        enter_ssn = int(enter_ssn)
        if (enter_name == self.name and enter_ssn == self.ssn):
            print("Welcome back, {}".format(enter_name))
        else:
            print("The name or ssn is incorrect")


system = Twins()
system.getTwinsInfo()

twin_one = Tom()
twin_one.getTwinsInfo()

twin_two = Brady()
twin_two.getTwinsInfo()
