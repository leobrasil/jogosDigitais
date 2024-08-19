class NaveEspacial:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.position = (0, 0)  # Posição inicial
        self.direction = 0  # Direção inicial (0 graus)
        self.speed = 0  # Velocidade inicial
        self.shield = 100  # Nível de escudo inicial
        self.energy = 100  # Energia inicial

    def move(self):
        # Implementação para mover a nave
        print(f"{self.name} está se movendo para a frente.")

    def turn(self, direction):
        # Implementação para girar a nave
        if direction.lower() == 'esquerda':
            self.direction -= 90  # Exemplo de rotação
        elif direction.lower() == 'direita':
            self.direction += 90
        print(f"{self.name} virou para a {direction}.")

    def shoot(self):
        # Implementação para lançar um projétil
        if self.energy >= 10:
            self.energy -= 10  # Custo de energia para atirar
            print(f"{self.name} lançou um projétil.")
        else:
            print(f"{self.name} não tem energia suficiente para atirar.")

    def hit(self, damage):
        # Implementação para quando a nave é atingida
        self.shield -= damage
        if self.shield <= 0:
            self.alive = False
            print(f"{self.name} foi destruída.")
        else:
            print(f"{self.name} foi atingida! Escudo restante: {self.shield}")

    def recharge(self):
        # Implementação para recarregar energia
        self.energy = 100
        print(f"{self.name} recarregou sua energia.")

# Exemplo de uso
nave = NaveEspacial("Falcon")
nave.move()
nave.turn("esquerda")
nave.shoot()
nave.hit(20)
nave.recharge()
