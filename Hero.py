'''
Created on 2019年7月14日

@author: ASUS
'''
from game import *
import time
import random
from numpy.core._dtype import __repr__


   

class creature():
    #skills_dict 是一个以编号作为键（key)，skill类作为值（value) 的字典类型
    def __init__(self,attrs,exp,money,skills_dict=[],name ='无名氏',state="正常"):
        self.name = name
        self.HP,self.attack, self.defence, self.crit_chance = attrs
        self.state = state
        self.exp = exp 
        self.money = money
        self.skills_dict = skills_dict
    
    def adjust_attrs_HP(self,v):
        self.HP+=v
    def is_death(self):
        if (self.HP<=0):
            return True
        return False   
        
    ##buff_info 是skill类里get_buff_info()函数所返回的字符串，,是对获得buff状态过程的字面描述
    def update_state(self,state,buff_info):
        
        self.state = state
        s_print (self.name+buff_info)
    
    def randomly_pick_skill(self):
        if (len(self.skills_dict)==0):
            return skill("普通攻击",self.attack)
        random_index = random.randint(0,len(self.skills_dict)-1)
        if random.random()<self.skills_dict[random_index]._proc_chance:
            return self.skills_dict[random_index]
        else:
            return skill("普通攻击",self.attack)
    
    def skills_dict_toString(self):
        result =""
        for i in range(1,len(self.skills_dict)+1):
            result=result+ create_skillBar(i, str(self.skills_dict[i-1]))
        
        return result
    
    def __call__(self,opponent):
        if (opponent.state in ["轻毒","剧毒","重伤","灼伤"]):
            if (opponent.state == "轻毒"):
                s_print (f"{opponent.name}因【轻毒】状态，扣除3点HP")
                opponent.adjust_attrs_HP(-3)
            elif (opponent.state == "剧毒"):
                s_print (f"{opponent.name}因【剧毒】状态，扣除10点HP")
                opponent.adjust_attrs_HP(-10)
            elif (opponent.state == "重伤"):
                s_print (f"{opponent.name}因【重伤】状态，扣除15点HP")
                opponent.adjust_attrs_HP(-10)
            elif (opponent.state == "灼伤"):
                s_print (f"{opponent.name}因【灼伤】状态，扣除5点HP")
                opponent.adjust_attrs_HP(-5)
        if self.state == "晕眩":
            print (f"{self.name}被晕眩了，无法行动")
            self.state = "正常"
            time.sleep(0.8)
            
            return
            
        skill = self.randomly_pick_skill()
        
        
        
        if skill._attack!=0 :
            net_damage =  skill._attack-opponent.defence
            if net_damage <= 0:
                s_print (f"{opponent.name}的护甲太高了，{self.name}使用<{skill._name}> 无法对其造成伤害")
            elif is_fatal_attack(self.crit_chance):
                net_damage*=2
                s_print (f"{self.name}发现了{opponent.name}的弱点，使用<{skill._name}>打出一套暴击，对其造成了{net_damage}点伤害")
            else:
                s_print(f"{self.name}使用<{skill._name}>对{opponent.name}造成了{net_damage}点伤害")
        
            #扣除对手因技能而造成的血量损失
            opponent.adjust_attrs_HP(-net_damage)
            if (skill._buff =="暴击"):               
                self.update_state(skill._buff, skill.get_buff_info())
            else:
                opponent.update_state(skill._buff,skill.get_buff_info())
        else:
            print (f"{self.name}使用了{skill._name}")
        if skill._buff[0:2] == "强化" or skill._buff == "回复":
            
            if skill._buff == "回复":
                self.HP += skill._buff_attrs
            if skill._buff == "强化攻击":
                self.attack += skill._buff_attrs
                
            elif skill._buff == "强化防御":
                self.defence += skill._buff_attrs
                
            elif skill._buff == "强化暴击":
                self.crit_chance+=(skill._buff_attrs)
            
            self.update_state(skill._buff, skill.get_buff_info())
        
        #老的buff在这个回合内过期
        
        
        
        print (f"{opponent.name}血量剩余: {opponent.HP}\n")
        time.sleep(0.5)
            
    def __str__(self):
        result ="名字: {:<5}\n\
血量  :{:<5}\n\
攻击  :{:<5}\n\
防御   :{:<5}\n\
暴击率 :{:<5}\n\
技能:\n".format(self.name,self.HP,self.attack,self.defence,self.crit_chance)+self.skills_dict_toString()
        return result
    
    


class monster(creature):
    def __init__(self,name,attrs,exp,money,skills_dict,state="正常",info="一只神秘的灵兽，没有任何有关它的记载"):
        super(monster,self).__init__(attrs,exp,money,skills_dict,name,state)
        self.info=info
    def get_info(self):
        return self.info
        
        
        
          
  #def __init__(self,attrs,exp,money,skills_dict=[],name = '无名氏',state="正常"):      
class hero(creature):
    def __init__(self,occupation,skills_dict,name='无名氏',attrs=(100,12,2,0.05),state="正常",exp=0,money= 0,weapon=[None,None]):
        super(hero,self).__init__(attrs,exp,money,skills_dict,name,state)
        self.attrs = attrs
        
        self.occupation = occupation
       
        self.level = ensure_level(exp)
        
        self.weapon_ls = weapon
        
    
    def setName(self,new_name):
        self.name = new_name
    def updateAttrs(self,new_attrs):
        self.HP,self.attack,self.defence,self.crit_chance = new_attrs
    
    def updateExp(self,exp):
        self.exp+=exp
        level_difference = ensure_level(exp)-self.level
        if level_difference !=0:
            self.level +=level_difference
            for i in range(1,4):
                a = "> "*i
                print ("\r{}".format(a),end="")
                time.sleep(1)
            s_print("恭喜 {1}({0})，成功升级到  level {2}".format(self.occupation,self.name,self.level))
            updated_Attrs= tuple_minus(occupation_attrs[self.occupation][self.level], self.attrs)
            print("血量: {}↑; 攻击: {}↑; 防御: {}↑; 暴击率: {}↑".format(updated_Attrs[0],updated_Attrs[1],updated_Attrs[2],updated_Attrs[3]))
            self.updateAttrs(updated_Attrs)
    

class skill():
    def __init__(self,name,attack,buff="正常",proc_chance=1,buff_attrs =0,*info):
        self._name = name
        self._attack = attack
        self._buff =buff
        self._info = info
        self._proc_chance = proc_chance
        self._buff_attrs = buff_attrs
    def get_buff_info(self):
        if (self._buff =="轻毒"):
            return "中毒了"
        elif (self._buff == "剧毒"):
            return "身中剧毒"
        elif (self._buff=="灼伤"):
            return "被烧伤了"
        elif (self._buff == "晕眩"):
            return "被打晕了"
        elif (self._buff == "回复"):
            return "回复了{}点HP".format(self._buff_attrs)
        elif (self._buff == "强化攻击"):
            return f"提升了自身{self._buff_attrs}点攻击力"
        elif (self._buff == "强化防御"):
            return f"提升了自身{self._buff_attrs}点防御力"
        elif (self._buff=="强化暴击"):
            return f"的暴击率大大增强了"
        else:
            return "表示不屑"
    def __str__(self):
        return (f"{self._name}   威力:{self._attack}   触发几率:{self._proc_chance}   附加状态:{self._buff}")
    __repr__ = __str__
   
occupation_attrs = {"战士":{0:[40,10,2,0.05],1:[44,12,3,0.05],2:[53,15,3,0.05],3:[59,16,5,0.06],4:[75,19,8,0.07],\
                    5:[88,22,10,0.07],6:[98,25,11,0.07],7:[108,28,13,0.07],8:[120,30,14,0.07],9:[133,38,16,0.08],10:[144,43,18,0.08],\
                    11:[152,45,20,0.08],12:[168,53,22,0.09],13:[179,60,25,0.1],14:[188,72,30,0.1],15:[209,90,35,0.15]}}           

       