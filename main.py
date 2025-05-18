from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):

        pass


class Sword(Weapon):
    def attack(self):
        print("бьёт мечом.")


class Bow(Weapon):
    def attack(self):
        print("стреляет из лука.")


class MagicWand(Weapon):
    def attack(self):
        print("кастует заклинание из волшебной палочки.")


class Monster:
    def __init__(self, name: str):
        self.name = name
        self.alive = True

    def get_defeated(self):
        self.alive = False
        print(f"{self.name} побеждён!")


class Fighter:
    def __init__(self, name: str, weapon: Weapon = None):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self):
        if not self.weapon:
            print(f"{self.name} безоружен и не может атаковать!")
        else:
            print(f"{self.name} ", end="")
            self.weapon.attack()


def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.get_defeated()


if __name__ == "__main__":
    hero = Fighter("Боец")

    goblin = Monster("Гоблин")
    hero.change_weapon(Sword())
    battle(hero, goblin)
    print()

    orc = Monster("Орк")
    hero.change_weapon(Bow())
    battle(hero, orc)
    print()


    dragon = Monster("Дракон")
    hero.change_weapon(MagicWand())
    battle(hero, dragon)