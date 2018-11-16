from random import randint

class Hero:
    def __init__(self, name, starting_health=100):
        ''' 
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
        abilities:List
        name:
        starting_health:
        current_health:
         '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        ''' 
        Calculates damage from list of abilities.
        This method should call Ability.attack() 
        on every ability in self.abilities and
        return the total.

        '''
        if len(self.abilities) == 0:
            return 0
        return sum([a.attack() for a in self.abilities])

    

    def __repr__(self):
        # TODO change here
        string = "Name of a hero: " + self.name
        string += "\nAbilities:\n\t"
        string += "\n\t".join(["{}: {}".format(a.name, a.attack_power) for a in self.abilities])
        return string

    # TODO revisit this function
    def is_alive(self):  
        '''
        This function will 
        return true if the hero is alive 
        or false if they are not. 
        this function should be replaced with better one
        '''
        if self.current_health > 0:
            return True
        else:
            return False
    
    def defend(self):
        if self.current_health == 0:
            return self.current_health
        return sum([a.defend() for a in self.armors])
    
    # TODO revisit this func
    def take_damage(self, damage):
        ''' 
        This method should update self.current_health 
        with the damage that is passed in.
        '''
        self.current_health -= damage
        if self.current_health <= 0:
            self.deaths += 1

    def add_kill(self, kill_num):
        self.kills += kill_num

    def add_armor(self, armor):
        self.armors.append(armor)
        

    

    def fight(self, opponent):  
        '''
        Runs a loop to attack the opponent until someone dies.
        '''
        pass


class Ability:
    def __init__(self, name, max_damage):
        ''' 
        Initialize the values passed into this 
        method as instance variables.
         '''
        pass

    def attack(self):
        ''' 
        Return a random attack value 
        between 0 and max_damage.
        '''
        pass


if __name__ == "__main__":
    # If you run this file from the terminal 
    # this block is executed.
    pass

hero = Hero("Wonder Woman")
print(hero.name)

# ! NOT WORKING - MAKE it WORK

# ? DOING GOOD?

# TODO 1: testing
# TODO 2:
# TODO 3:
# TODO 4:


