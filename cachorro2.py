class Cachorro:
    def __init__(self, nome, raca, comida):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = True
        self.feliz = True
        self.energia = 100
        
    def __str__(self):
        return f"Nome: {self.nome}, Raça: {self.raca}, Comida: {self.comida}, Acordado: {self.acordado}, Feliz: {self.feliz}"
        
    def comer(self,quantidade):
        if self.comida > 0:
            self.comida -= 1
            self.feliz = True
            print(f"{self.nome} está comendo e está muito feliz!!comida restante: {self.comida}.")
        else:
         print(f"{self.nome} está MORRENDO de fome, mas há comida acabou!!")
        
    def dormir (self):
        self.acordado = False
        self.energia = 100
        print (f"{self.nome} está cansado e foi dormir e está domindo agora.🤫💤Energia total sendo restaurada!")
        
    def acordar (self):
        self.acordado = True
        print(f"{self.nome} acordou!!🥱A energia restaurada, mas está morrendo de fome!")
        
    def brincar (self):
        if self.energia >= 20:
            self.energia -= 20
            self.feliz = True
            print (f"{self.nome} Brincou e está muito Feliz!! Energia restante:{self.energia}")
        else:  
                print(f"{self.nome} está muito cansado e não tem energia suficiente para brincar!")

    def ignorar (self):
        self.feliz = False
        print(f"{self.nome} está sendo ignorado e por isso está triste!!")
        
    def latir (self):
        if self.acordado is True:
         print(f"{self.nome} está latindo!!")
        else:
         print(f"{self.nome} está dormindo e não pode latir") 
         

        
# Criando um objeto de classe cachorro
meu_cachorro=Cachorro ("Enzo", "Dachshund", 5)
        

#Interagindo com o objeto
meu_cachorro.comer(2)
meu_cachorro.brincar ()
meu_cachorro.ignorar()
meu_cachorro.latir()
meu_cachorro.dormir()
meu_cachorro.latir()
meu_cachorro.acordar()
meu_cachorro.latir()
