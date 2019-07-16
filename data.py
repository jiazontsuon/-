'''
Created on 2019年7月12日

@author: ASUS
'''
from Hero import monster
from Hero import hero
from Hero import skill
from game import *


skill_ls = {0:skill("痛击",15,proc_chance=0.4),1:skill("致命波动",10,buff_attrs =0.1,proc_chance=0.9,buff="强化暴击"),2:skill("肘击",7,proc_chance=0.3,buff="晕眩"),\
            3:skill("毒液腐蚀",13,proc_chance=0.3,buff="轻毒"),4:skill("剧毒利爪",17,proc_chance=0.2,buff="剧毒"),5:skill("圣光",25,proc_chance=0.3,buff="回复"),6:skill("钢之爪",18,proc_chance=0.4),\
            7:skill("火焰冲拳",20,proc_chance=0.2,buff="灼伤"),8:skill("三昧炽焰",25,proc_chance=0.3,buff="灼伤"),9:skill("啸天赤影拳",30,proc_chance=0.2,buff = "重伤")}


monster_ls = {0:monster("树妖",(60,8,1,0.05),2,3,[skill_ls[0],skill_ls[1]]),1:monster("小鱼人",(40,13,1,0.08),4,5,[skill_ls[2],skill_ls[3]]),2:monster("炎法师",(110,15,3,0.08),10,15,[skill_ls[5],skill_ls[8]])\
              ,3:monster("地狱火",(260,35,10,0.1),40,63,[skill_ls[7],skill_ls[8]])}

if __name__ =="__main__":
    print (skill_ls[3])
    hero1 = hero("战士",[skill_ls[1],skill_ls[3],skill_ls[6]],"ningja",(100,10,2,0.05))
    print(hero1.skills_dict)
    print (hero1)
    