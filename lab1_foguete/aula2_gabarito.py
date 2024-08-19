import random

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
        print(f"{self.name} está se movendo para a frente.")
        # Implementação simplificada para movimento
        self.position = (self.position[0] + self.speed, self.position[1])

    def turn(self, direction):
        if direction.lower() == 'esquerda':
            self.direction -= 90  # Exemplo de rotação
        elif direction.lower() == 'direita':
            self.direction += 90
        print(f"{self.name} virou para a {direction}.")

    def shoot(self, target):
        if self.energy >= 10:
            self.energy -= 10  # Custo de energia para atirar
            damage = random.randint(15, 30)  # Dano aleatório
            target.hit(damage)
            print(f"{self.name} lançou um projétil em {target.name} causando {damage} de dano.")
        else:
            print(f"{self.name} não tem energia suficiente para atirar.")

    def hit(self, damage):
        self.shield -= damage
        if self.shield <= 0:
            self.alive = False
            print(f"{self.name} foi destruída.")
        else:
            print(f"{self.name} foi atingida! Escudo restante: {self.shield}")

    def recharge(self):
        self.energy = 100
        print(f"{self.name} recarregou sua energia.")

# Função para executar o turno de um jogador
def turno_jogador(player, opponent):
    print(f"\nTurno de {player.name}:")
    action = input("Escolha uma ação (move, turn [esquerda/direita], shoot, recharge): ")

    if action == "move":
        player.move()
    elif action.startswith("turn"):
        _, direction = action.split()
        player.turn(direction)
    elif action == "shoot":
        player.shoot(opponent)
    elif action == "recharge":
        player.recharge()
    else:
        print("Ação inválida.")

# Inicialização do jogo
player1 = NaveEspacial("Nave 1")
player2 = NaveEspacial("Nave 2")

# Loop do jogo
while player1.alive and player2.alive:
    turno_jogador(player1, player2)
    if not player2.alive:
        break
    turno_jogador(player2, player1)

# Resultado do jogo
if player1.alive:
    print("\nNave 1 venceu!")
else:
    print("\nNave 2 venceu!")
