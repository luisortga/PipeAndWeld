import random
import sys

class Player:
    def __init__(self):
        self.health = 100
        self.ammo = 30
        self.kills = 0

class Enemy:
    def __init__(self):
        self.health = random.randint(20, 40)
        self.damage = random.randint(5, 15)

def display_status(player):
    print(f"\n=== SHOOTER GAME ===")
    print(f"Health: {player.health} | Ammo: {player.ammo} | Kills: {player.kills}")
    print(f"Commands: [s]hoot, [h]eal, [r]eload, [q]uit")

def main():
    player = Player()
    enemies_defeated = 0
    
    while player.health > 0:
        display_status(player)
        enemy = Enemy()
        
        print(f"\nEnemy appeared! Health: {enemy.health}")
        
        while enemy.health > 0 and player.health > 0:
            action = input("\nYour action: ").lower()
            
            if action == 's':
                if player.ammo > 0:
                    damage = random.randint(15, 35)
                    enemy.health -= damage
                    player.ammo -= 1
                    print(f"Shot! Dealt {damage} damage. Enemy health: {enemy.health}")
                else:
                    print("Out of ammo!")
            elif action == 'h':
                player.health = min(100, player.health + 25)
                print(f"Healed! Health: {player.health}")
            elif action == 'r':
                player.ammo = 30
                print("Reloaded!")
            elif action == 'q':
                print("Game over!")
                return
            
            if enemy.health > 0:
                damage = enemy.damage
                player.health -= damage
                print(f"Enemy attacked! Took {damage} damage.")
        
        if enemy.health <= 0:
            player.kills += 1
            print("Enemy defeated!")
    
    print(f"\nGAME OVER! Final kills: {player.kills}")

if __name__ == "__main__":
    main()