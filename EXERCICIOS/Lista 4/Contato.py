import datetime

class Contato:

  def __init__(self, nome, email, telefone, dataNascimento):
    self.__nome = nome
    self.__email = email
    self.__telefone = telefone
    self.__dataNascimento = dataNascimento

  def inicializarContato(self, nome, email, telefone, dataNascimento):
    self.__nome = nome
    self.__email = email
    self.__telefone = telefone
    self.__dataNascimento = dataNascimento

  def getNome(self):
    return self.__nome

  def setNome(self, nome):
    self.__nome = nome

  def getEmail(self):
    return self.__email

  def setEmail(self, email):
    self.__email = email

  def getTelefone(self):
    return self.__telefone

  def setTelefone(self, telefone):
    self.__telefone = telefone

  def getDataNascimento(self):
    return self.__dataNascimento

  def setDataNascimento(self, dataNascimento):
    self.__dataNascimento = dataNascimento

  def imprimirContato(self):
    print(f"Nome: {self.__nome}")
    print(f"Email: {self.__email}")
    print(f"Telefone: {self.__telefone}")
    print(f"Data de Nascimento: {self.__dataNascimento}")

  def calcularIdade(self):
    data_nascimento = datetime.datetime.strptime(self.__dataNascimento, '%d/%m/%Y')
    hoje = datetime.datetime.now()
    idade = hoje.year - data_nascimento.year
    return idade


contato = Contato("Henrique Barreto", "hbpereira.cic@uesc.br", "(73)0000-0000", "18/08/2000")
contato.imprimirContato()
print(f"Idade: {contato.calcularIdade()} anos")
