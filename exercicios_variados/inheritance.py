class Parent():
    def __init__(self  , last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("\nlast name: "+ self.last_name)
        print ("eye color: "+self.eye_color)

class Child (Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    
    def show_info(self):
        Parent.show_info(self)
        print("toys: "+self.number_of_toys)


g = Parent("Leal", "brown")
g.show_info()
gChild = Child("Luke", "black","10")
gChild.show_info()

