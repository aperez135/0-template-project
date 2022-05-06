"""
PokeCardDex template.  This is a template file that is used to 
"""
import random
from ssl import CHANNEL_BINDING_TYPES
from unicodedata import name
from xml.dom import NamespaceErr




class Pokemon():
    generation = 1
    def __init__(self, name, start_hp, energy_type, weakness, resistence, moves):
        # The following is a summary of the inputs to this class:
        # - (str) name: the name of the pokemon
        # - (int) start_hp: the starting (or base) hp of the pokemon
        # - (str) energy_type: the energy type of the pokemon (electric, water,
        #   fire, etc,.)
        # - (str) weakness: the energy type the pokemon is weak against
        # - (str) resistence: the energy type the pokemon is resistant against
        # - (tuple) moves: a tuple of ((str), (int)) pairs that represent the
        #   move name and damage amount
        self.name = name 
        self.start_hp = start_hp
        self.energy_type = energy_type
        self.weakness = weakness
        self.resistance = resistence
        self.moves = moves

        if energy_type == "Water":
            self.weakness == "Fire"
            self.resistance == "Grass"
            self.moves == {

            }
        elif energy_type == "Grass":
            self.weakness == "Fire"
            self.resistance == "Water"
            self.moves == {

            }
        
        elif energy_type == "Fire":
            self.weakness == "Water"
            self.resistance == "Grass"
            self.moves == {

            }

    def take_damage(self, damage_amount):
        self.hp = self.hp - damage_amount

    def __str__(self):
        return ('Pokemon: '), {self.name} ('with'), {self.hp} ('HP left')



class PokeCardDex():
    def __init__(self, json_file_path=None):
        # NOTE: It is important to handle the case where no path is passed in
        # meaning that json_file_path has a value of None.
        pass
    
    import json

    with open ('/Users/aprilschool/Documents/GitHub/0-template-project/myParty.json') as f:
        data = json.load(f)
        # print(data.items())
        pokemon = data.get(type="Skarmory")
        print(pokemon.type) 
    
    def set_order(self, order):
        self.order = PokeCardDex.pokemon
        print("Name: ", {name}, "")
        pass

    def battle(self, challenger_party):
        print('BATTLE')
        print("Type: ", self.name)
        print("Attack: ", self.attack)
        print("Defense: ", self.defense )
        
        print("\n vs.")

        print("Type: ", challenger_party.name)
        print("Attack: ", challenger_party.attack)
        print("Defense: ", challenger_party.defense )
        
        while self.hp > 0 and challenger_party.hp > 0:
            self.take_damage(challenger_party.moves[1])
            challenger_party.take_damage(self.moves[1])
            print(self)
            print(challenger_party)
        
        while True:
            
            if challenger_party.start_hp <= 0:
                print({challenger_party}, "has fainted")
                print({self}, "has won!")

            if self.start_hp <= 0:
                print({self}, "has fainted")
                print({challenger_party}, "has won!")

        pass
    
    def heal_party(self, heal_amount):
        heal_amount = random.randint(5,20)
        self.start_hp += heal_amount
        return heal_amount
        pass

    def add_to_party(self, pokemon):
        # for self.pokemon.append(pokemon)
        pass

class WaterPokemon(Pokemon):
    def __init__(self, name, level, start_hp, moves):
        super().__init__(name, level, start_hp, 'water', moves)

class FirePokemon(Pokemon):
    def __init__(self, name, level, start_hp, moves):
        super().__init__(name, level, start_hp, 'fire', moves)

class GrassPokemon(Pokemon):
    def __init__(self, name, level, start_hp, moves):
        super().__init__(name, level, start_hp, 'grass', moves)



# Below is an example usage for using the classes
if __name__ == "__main__":
    my_dex = PokeCardDex('pokemon_party.json')
    rival_dex = PokeCardDex()
    pikachu = Pokemon('Pikachu', 100, 'electric', None, None, (('electric charge', 30),))
    rival_dex.add_to_party(pikachu)

    # my_dex.battle(rival_dex)

    # for pokemon in my_dex.party:
    #     print(pokemon.is_fainted)

    my_dex.heal_party()