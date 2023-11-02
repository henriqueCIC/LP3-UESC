import datetime

class Contato:
    def __init__(self, nome, email, telefone, dataNascimento):
        if not self.validarEmail(email):
            raise ValueError("Email inválido")
        if not self.validarTelefone(telefone):
            raise ValueError("Telefone inválido")
        if not self.validarDataNascimento(dataNascimento):
            raise ValueError("Data de nascimento inválida")

        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__dataNascimento = dataNascimento
        #

    def validarEmail(self, email):
        if "@" in email:
            parts = email.split("@")
            if len(parts) == 2 and "." in parts[1]:
                return True
        return False

    def validarTelefone(self, telefone):
        # Remova espaços em branco do número de telefone e verifique se ele contém apenas dígitos
        telefone_limpo = "".join(telefone.split())
        if len(telefone_limpo) >= 10:
            return True
        return False
    #

    def validarDataNascimento(self, dataNascimento):
        try:
            datetime.datetime.strptime(dataNascimento, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def imprimirContato(self):
        print(f"Nome: {self.__nome}")
        print(f"Email: {self.__email}")
        print(f"Telefone: {self.__telefone}")
        print(f"Data de Nascimento: {self.__dataNascimento}")

    def calcularIdade(self):
        data_nascimento = datetime.datetime.strptime(self.__dataNascimento, "%d/%m/%Y")
        hoje = datetime.datetime.now()
        idade = hoje.year - data_nascimento.year
        return idade
    
    
contato = Contato("joao lucas ", "joao.cic@gmail.com", "73991945126","18/08/2000")
contato.imprimirContato()
print(contato.calcularIdade())