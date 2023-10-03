class Pokemon:
    def __init__(self, element, species, level=1, name=None):
        self.element = element
        self.species = species
        self.level = level

        if name:
            self.name = name
        else:
            self.name = species

    def __str__(self):
        return '{}, Level {}'.format(self.name, self.level)

    def attack(self, pokemon):
        print(f'{self} attacked {pokemon}')


class ElectricPokemon(Pokemon):
    pass


my_pokemon = ElectricPokemon('Electric', 'Pikachu')

print(my_pokemon)
