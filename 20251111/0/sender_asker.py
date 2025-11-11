class Sender:
    first = True
    
    @classmethod
    def report(cls):
        if cls.first:
            print("Greetings!")
            cls.first = False
        else:
            print("Get away!")

class Asker:
    @staticmethod
    def askall(lst):
        for obj in lst:
            obj.report()

askr = Asker()
askr.askall([Sender(), Sender(), Sender()])
