class PhoneBook:
    def __init__(self):
        self.contact = {}
    def add(self,name,mobile = None,office= None,email=None):
        self.contact[name]=name
        self.contact[mobile]=mobile
        self.contact[office]=office
        self.contact[email]=email
    def __str__(self):
        msg = ""
        for value in self.contact.values():
            msg+=f"{value}\n"
        return msg

obj = PhoneBook()
obj.add("kim",office="1234567",email="kim@company.com")
obj.add("park",office="234567",email="Park@company.com")
print(obj)




