#duck typing - means polymorphism. if a crow quacks like duck, it's duck typing
#polymorphism using ducktyping
#in example below both class Laptop and Desktop quacks ( using build() method)

class Laptop: # Duck
    def build(self):
        print("Laptop builded")

class Desktop: #Crow
    def build(self):
        print("Desktop builded")

class Tablet:
    def watch_netflix(self):
        print("Tablet watch netflix")

class Alien:
    def code(self, machine : Laptop):
        print("Alien builded")
        machine.build()


asus = Laptop()
dell = Desktop()
lenovo_tab = Tablet()

nirakash = Alien()
#nirakash.code(asus)
nirakash.code(dell)
nirakash.code(lenovo_tab) #this won't work because class Lenovo is not quacking i.e. no build method



