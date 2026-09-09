class Arma:
  def __init__(self, nome, dano):

    # Atributos arma
    self.__nome = nome
    self.__dano = dano


  # metodos arma
  def obter_nome(self):
    return self.__nome


  def obter_dano(self):
    return self.__dano


class Personagem:
  def __init__(self, nome, vida, arma):

    # Atributo do personagem
    self.__nome = nome
    self.__vida = vida
    self.__arma = arma

  def obter_nome(self):
    return self.__nome

  def obter_vida(self):
    return self.__vida


  def obter_arma(self):
    return self.__arma


  def receber_dano(self, dano):
    self.__vida -= dano
    if self.__vida <= 0:
      self.__vida = 0
      print(f"{self.__nome} morreu, não pode mais batalhar!")
    else:
      print(f"{self.__nome} foi atingido, perdeu {dano} pontos de vida")


  def atacar(self, jogador):
    print(f"{self.__nome} realizou um ataque comum")


  def status(self):
    print(f"-=" * 30)
    print(f"Nome: {self.__nome}")
    print(f"Vida: {self.__vida}")
    print(f"Arma: {self.__arma.obter_nome()} | Dano: {self.__arma.obter_dano()}")
    print(f"-=" * 30)


class Guerreiro(Personagem):
  def __init__(self, nome, vida, arma):
    # Atributos do guerreiro
    super().__init__(nome, vida, arma)



  def atacar(self, jogador):
    print(f"{self.obter_nome()} disferiu um ataque!")
    jogador.receber_dano(self.obter_arma().obter_dano())
  

  def receber_dano(self, dano):
    return super().receber_dano(dano)


class Pally(Personagem):
  def __init__(self, nome, vida, arma):
    super().__init__(nome, vida, arma)
    self.__flechas = 10

  # Metodos palla
  def atacar(self, jogador):
    self.__flechas -= 1
    if self.__flechas <= 0:
      self.__flechas = 0
      print(f"Suas flechas acabaram.")
    else:
        print(f"{self.obter_nome()} acertou a flechada!")
        jogador.receber_dano(self.obter_arma().obter_dano())


  def receber_dano(self, dano):
    super().receber_dano(dano)


  def status(self):
    print(f"-=" * 30)
    print(f"Nome: {self.obter_nome()}")
    print(f"Vida: {self.obter_vida()}")
    print(f"Arma: {self.obter_arma().obter_nome()} | Dano: {self.obter_arma().obter_dano()}")
    print(f"Flechas restantes: {self.__flechas}")
    print(f"-=" * 30)

# Programa principal
espada = Arma("Dragon Sword", 28)
arco = Arma("Dragon Bow", 30)
kina = Guerreiro("Moratoqk", 500, espada)
pally = Pally("Felipe Xa", 105, arco)
kina.status()
pally.status()
kina.atacar(pally)
pally.atacar(kina)
kina.status()
pally.status()
