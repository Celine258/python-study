class Record:
    def __init__(self,date,ID,money,province):
        self.date = date
        self.ID = ID
        self.money = money
        self.province = province

    def __str__(self):
        return (f"{self.date},{self.ID},{self.money},{self.province}")