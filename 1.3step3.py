class SuperHero:
    pass


batman = SuperHero()
superman = SuperHero()

# setattr(batman, 'can_fly', False)
# setattr(batman, 'damage', 175)
# setattr(superman, 'can_fly', True)
# setattr(superman, 'damage', 285)
# setattr(superman, 'alter_ego', 'Кларк Кент')

batman.can_fly = False
batman.damage = 175
superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'

print(batman.__dict__)
print(superman.__dict__)
