class computer:

    brand = "Dell" #class variable

    def __init__(self,cpu, ram ,ssd):
        print("init called")
        self.cpu = cpu #instance variable
        self.ram = ram #instance variable
        self.ssd = ssd #instance variable

    def config(self):
        print("config : ", self.cpu, self.ram, self.ssd)

    @classmethod #decorator - says python that this is a class method
    def info(cls): #cls is just a variable name, but it is widely acknowledged
        return cls.brand

    @staticmethod #utility method, just for some processing
    def gb_to_bytes(gb):
        return gb * (1024 **3)


com1 = computer("i5", "16GB", "512GB")
com2 = computer("i9", "96GB", "2TB")

com1.config()
com2.config()
print("direct access : ", computer.brand)
print("access using class method: ", computer.info())

print(computer.gb_to_bytes(16))


#class variable goes into class namespace
#instance variable goes inot object namespace

