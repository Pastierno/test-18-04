class Contatto:
    def __init__(self, nome, cognome, telefono, email):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.nome} {self.cognome}, Telefono: {self.telefono}, Email: {self.email}"
    