'''


@author: ASUS
'''
import time
from copy import deepcopy
import random



def tuple_minus(tuple1,tuple2):
    result = []
    for i in range(len(tuple1)):
        result.append(tuple1[i]-tuple2[i])
    return tuple(result)
    
def s_print(string):
    for i in range(len(string)):
        print("\r{}".format(string[0:i+1]),end="")
        time.sleep(0.1)
    print("\n")
        
        
def generate_exp_reference_ls(levels):
    result = [0]
    for i in range(levels+1):
        result.append(result[i]+(i+1)**2)
    return result

      
def ensure_level(exp):
    MAX_level = 15
    level_ls = generate_exp_reference_ls(MAX_level)
    if exp>= level_ls[-1]:
        return MAX_level
    for i in range(len(level_ls)):
        if (exp>=level_ls[i] and exp<level_ls[i+1]):
            
            return i
def is_fatal_attack(crit_chance):
    if (random.random()<crit_chance):
        return True    
    else:
        return False

def print_header(content = "combat start"):
    print ("{}\n{:^20}\n{}".format("*"*20,content,"*"*20))

def create_skillBar(num = 1,content="Not Available"):
    return "{:=^60}\n{:^40}\n{}\n\n".format(f"skill {num}",content,"="*60)
    


def combat(hero,monster):
    hero_copy = deepcopy(hero)
    monster_copy = deepcopy(monster)
    round =0
    print_header()
    while True:
        if round%2==0:
            hero_copy(monster_copy)
            if (monster_copy.is_death()):
                print (f"恭喜你成功击败了{monster_copy.name},获得{monster_copy.exp}点经验和{monster_copy.money}金币\n")
                hero.money+=monster.money
                hero.updateExp(monster.exp)
                del monster_copy
                del hero_copy
                break
        else:
            monster_copy(hero_copy)
            if (hero_copy.is_death()):
                money_loss = hero.money *0.2
                hero.money-=money_loss
                print (f"很遗憾，被打败了。。。损失{money_loss}金币\n")
                del monster_copy
                del hero_copy
                break
        round +=1

     

    
    
   