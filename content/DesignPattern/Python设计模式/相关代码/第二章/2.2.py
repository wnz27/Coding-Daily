class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print(" __init__method called..")
        else:
            print("Instance already created:", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
   
s = Singleton()  ## class initialized, but object not created
print('*' * 80)
print("Object created", Singleton.getInstance())  # Object gets created here
print('*' * 80)
s1 = Singleton()  ## instance already created
