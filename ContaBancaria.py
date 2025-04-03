class ContaBancaria:
  def __init__(self, titular,saldo, limite):
    self.titular = titular #Público
    self.__saldo = saldo #Privado
    self.__limite = limite

  def depositar(self,valor):
    if valor > 0:
      self.__saldo += valor
      print(f"Depósito de R$ {valor:.2f} realizado com sucesso!!")
    else:
      print("Valor de depósito inválido!")


  def sacar(self, valor):
        if 0 < valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saque não permitido! Verifique seu saldo e limite.")
    

# Método GET para pegar e retornar o saldo
  def get_saldo(self):
    return self.__saldo

# Método SET definir um novo valor para o saldo
  def set_saldo(self,valor):
      if valor >- 0:
         self.__saldo = valor
      else:
         print("valor negativo inválido!!")

  def set_limite(self, novo_limite):
    if novo_limite >= 0:
      self.__limite = novo_limite
      print(f"Novo limite definido para R$ {novo_limite:.2f}")
    else:
      print("O limite não pode ser negativo!")


conta = ContaBancaria("Stephanie", 1000.0, 500.0)
conta.depositar(200)
conta.sacar(300)
print(f"Saldo atual: R$ {conta.get_saldo():.2f}")
conta.set_limite(700)