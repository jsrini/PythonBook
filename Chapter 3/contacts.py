class Contacts(dict):


    def __init__(self):
        self.data = dict()
        
    def addContact(self,first,last,phone,email):
        self.data[first + ' ' + last] = (first,last,phone,email)

    def deleteContact(self,first,last):
        del self.data[first + ' ' + last]

    def printNames(self):
        for key, (first,last,phone,email) in self.data.items():
            self.printContact(first,last,phone,email)
            print('--')

    def searchByName(self,name):
        count = 0
        for key, (first,last,phone,email) in self.data.items():
            if first.find(name) != -1 or last.find(name) != -1:
                self.printContact(first,last,phone,email)
                print('--')
                count = count+1

        if count == 0:
            print("No results found")
        else:
            print("Found " + str(count) + " result(s)")
        


    def getContactByFullName(self,name):
        key = name
        if key in self.data:
            (first,last,phone,email) = self.data[key]
            self.printContact(first,last,phone,email)
        else:
            print("Contact does not exist")


    def printContact(self,first,last,phone,email):
            print('Name:   ' + first + ' ' + last)
            print('Phone:  ' + phone)
            print('E-mail: ' + email)
 

 


                  
        
