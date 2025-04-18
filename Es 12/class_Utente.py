class Utente:
    def __init__(self, nome, password, email):
        self.__nome = nome # attributi privati
        self.__password = password
        self.__email = email
        
    def get_nome(self): # metodi getter e setter
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password = password
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email