from typing import Type
import random


class Weapon:
    def __init__(self, name: str, 
                 model: str, 
                 range: float):
        self.name = name
        self.model = model
        self.range = range

    def shoot(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
    
    def random_hit_result(self, start_range, end_range, k):
        hit = round(random.uniform(start_range, end_range), 3)
        print(f"HIT PERCENT: {round(hit*100, 1)}%")
        no_hit = round(1 - hit, 3)
        print(f"NO_HIT PERCENT: {round(no_hit*100,1)}%")
        hits, weights = ["hit", "no_hit"], (hit, no_hit)
        random_shoot = random.choices(hits, 
                                    weights=weights, 
                                    k=k)
        return random_shoot


class Pistol(Weapon):
    def shoot(self, range_to_target: float):
        print(f"shoot from {self}")
        random_shoot = []
        if range_to_target <= self.range:
            random_shoot = self.random_hit_result(start_range=0.5, 
                                                  end_range=0.7, 
                                                  k=1)
        return random_shoot
    
    def __str__(self):
        return f"Pistol<{self.name} {self.model}>"


class Shotgun(Weapon):
    def shoot(self, range_to_target: float):
        print(f"shoot from {self}")
        random_shoot = []
        if range_to_target <= self.range:
            random_shoot = self.random_hit_result(start_range=0.2, 
                                                  end_range=0.5,
                                                  k=6)
        return random_shoot
    
    def __str__(self):
        return f"Shotgun<{self.name} {self.model}>"


class AssaultRifle(Weapon):
    def shoot(self, range_to_target: float, 
              clip_size: int):
        print(f"shoot from {self}")
        random_shoot = []
        if range_to_target <= self.range:
            random_shoot = self.random_hit_result(start_range=0.4, 
                                                  end_range=0.6, 
                                                  k=clip_size)
        return random_shoot
    
    def __str__(self):
        return f"Assault Rifle<{self.name} {self.model}>"


class WeaponFactory:
    def __init__(self, weapon_factory: Type[Weapon]) -> None:
        self.weapon_factory = weapon_factory
    
    def buy_weapon(self, 
                   name: str, 
                   model: str, 
                   range: float):
        weapon = self.weapon_factory(name,
                                     model,
                                     range)
        print(f"You get {weapon}")
        return weapon


if __name__ == "__main__":
    pistol_factory = WeaponFactory(Pistol)
    astra = pistol_factory.buy_weapon("Astra", "Model 900", 1000)
    shoot_result = astra.shoot(750)
    print(f"- hits: {shoot_result.count('hit')}\n")

    shotgun_factory = WeaponFactory(Shotgun)
    ks_23 = shotgun_factory.buy_weapon("Shotgun", "KS-23", 150)
    shoot_result = ks_23.shoot(75)
    print(f"- hits: {shoot_result.count('hit')}\n")

    rifle_factory = WeaponFactory(AssaultRifle)
    m16 = rifle_factory.buy_weapon("AR", "M16A2", 550)
    shoot_result = m16.shoot(400, 100)
    print(f"- hits: {shoot_result.count('hit')}")
