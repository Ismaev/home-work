class Hero:
    Head = 1
    ability = True

    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self, a):
        print(self.hp + a)
    def two_damage(self, a):
        print(self.damage * a)
    def greetings(self):
        print('my name is ' + self.name)
    def brand_phrase(self):
        print('good will win ')

hero1 = Hero('Amir', 'Naruto', 100, 80 )
hero2 = Hero('Rinat', 'Saske', 100, 90)
hero3 = Hero('Rahim', 'Kakashi', 100, 70)
hero4 = Hero('Alina', 'Sakura', 100, 50)

print(hero1.name, hero1.nickname, hero1.hp, hero1.damage, hero1.Head, hero1.ability)
print(hero2.name, hero2.nickname, hero2.hp, hero2.damage, hero2.Head, hero2.ability)
print(hero3.name, hero3.nickname, hero3.hp, hero3.damage, hero3.Head, hero3.ability)
print(hero4.name, hero4.nickname, hero4.hp, hero4.damage, hero4.Head, hero4.ability)
hero1.heal(100)
hero2.two_damage(2)
hero3.greetings()
hero4.brand_phrase()
