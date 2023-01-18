import math

from characteristics.characteristic import Characteristic

class Wisdom(Characteristic):
  BASE_SKILLS: dict = {
    1: 'magic_cuts',
    2: 'magic_disease',
    3: 'enchantment',
    4: 'enchanted_barrier',
    5: 'charms_of_bane'
  }

  enchantment: int = 0

  def update_enchantment(self, items: int):
      self.update_enchantment += items

  def magic_cuts (self, chararacter: Character, goal: Character):
      character.additional_attack_damage += math.floor(self.current_mode/2)
      self.update_enchantment += 1
    # Волшебные порезы (М1) - Атаки по Цели усиливаются на 1/2 Мод. Мудрости до конца боя, даёт 1 Зачарование (М3).



  def magic_disease (self, chararacter: Character, goals: list):
        accessible_goals_count = math.floor(self.current_mode/2)
            if len(goals) == accessible_goals_count:
                for goal in goals:
                    character.current_attacks[attack] +=1
                    character.current_attacks[-1].goal = goal
                self.update_enchantment += 1

            elif len(goals) > accessible_goals_count:
                print(f'Not enough wisdom mode for {len(goals)} goals')

            else:
                print(f'You have {accessible_goals_count-goals} spell charges left')
                answer = input('Are you sure with all goals? Yes(1)/No(0)')

                if answer == '1':
                    for goal in goals:
                        character.current_attacks[attack] +=1
                        character.current_attacks[-1].goal = goal
                    self.update_enchantment += 2

                elif answer == '0':
                    print('Reaim the spell')
                    def magic_desease(self, chararacter: Character, goals: list)

                else:
                    answer = input('Your answer isn´t recognized, repeat it')
    # **Магическая болезнь (М2)** - Отнимает Хиты в размере Модификатора Мудрости у количества Целей, равного половине Модификатора Мудрости, даёт два Зачарования.



  def enchantment(self, character: Character):
        class Spellcasting(SideAction):
            spell_total_time = 0
            spell_current_time = 0
            spell_effects:  dict = {
                1: 'Grants 10 Defence',
                2: 'Grants additional Attack',
                3: 'Blocks first Attack on Host',
                4: 'Doubles the power of the skill',
                5: 'Makes skill unblockable',
                6: 'Top up 1 characteristic for 1/2 wisdom mode',
                7: 'Skill is applied on 1/2 wisdom mode goals'
            }

            def __init__ (self, spell_total_time):
                self.spell_total_time += spell_total_time

            def spell_casting (self):
                if self.spell_current_time == spell_total_time:
                    self.spell_cast(self.enchantment)
                else:
                    self.spell_current_time += 1

            def spell_cast (self, self.enchantment):
                'use self.spell_effects[self.enchantment]'

        self.update_enchantment(self, enchantment)
            self.enchantment += enchantment
    # **Зачарование (М3) (Пассивное) -** Владелец может отдельным Действием объявить от 1 до 7 Раундов Подготовки. Каждый ход Подготовки даёт 1 Зачарования. По окончанию Подготовки или достижения 7 Зачарования, первое Умение Владельца Зачаровывается:
    #  - **1** - Даёт 10 Защиты Владельцу.
    #  - **2** - Владелец совершает дополнительную Атаку.
    #  - **3** - Блокирует первую Атаку Цели.
    #  - **4** - Усиливает Умение вдвое.
    #  - **5** - Умение нельзя Блокировать.
    #  - **6** - Повышает любую Характеристику Владельца на 1/2 Модификатора Мудрости.
    #  - **7** - Умение действует на количество Целей, равное половине Модификатора Мудрости.



  def enchanted_barrier(self, character: Character, goal: Character):
    'Blocks 1/3 wisdom mode Skills for the goal, grants +3 enchantment'
    '**Заколдованный барьер (М4)** - Блокирует количество Умений по Цели, равное трети Модификатора Мудрости, даёт три Зачарования.'



    def charms_of_bane(self, character: Character, goal: Character):
    'Goal´s wisdom is lowed by 1/2 widom mode, grants +4 enchantment'
    '**Чары проклятия (М5)** - Снижает Мудрость Цели в размере половины Модификатора Мудрости плюс Зачарование, даёт четыре Зачарования.'
