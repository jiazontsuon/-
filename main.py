'''
Created on 2019年7月15日

@author: ASUS
'''
from data import *
from past.builtins.misc import raw_input
import sys
from Hero import *
import json


def process_bar(content1="小提示：多刷怪",content2="广告位招租"):
    scale =50
    start = time.perf_counter()

    print ("{:-^18}".format(content1))
    for i in range(51):
    
        a = i*2
        b = "*"*i
        c = "."*(scale-i)
        dur = time.perf_counter()-start
        print ("\r{:<3}%[{}->{}] {:.2f}s".format(a,b,c,dur),end="")
        time.sleep(0.1)

    print ("\n{:-^18}".format(content2))

def exit_request(content = "你确定要退出吗？ Y/N\n>",kw = "y"):
    result = raw_input(content).lower()
    if result == kw:
        print("Goodbye my friendo")
        sys.exit()
    else:
        pass
def turn_skills_to_lists(skills_dict):
    result = []
    for i in skills_dict:
        result.append([i._name,i._attack,i._buff,i._proc_chance,i._buff_attrs])
    return result
def turn_lists_to_skills(lists):
    result = []
    for i in lists:
        result.append(skill(i[0],i[1],i[2],i[3],i[4]))
    return result
def save_game():
    
    try:
        saving_content = {0:main_hero.occupation,1:turn_skills_to_lists(main_hero.skills_dict),2:main_hero.name,3:main_hero.attrs,4:main_hero.state,5:main_hero.exp,6:main_hero.money,7:main_hero.weapon_ls}
        f = open("save.txt",'w+')
        f.write(json.dumps(saving_content))
        f.close()
        process_bar("正在存档中", "存档成功")
    except:
        print("存档失败")
    
def load_game():
    try:
        lg_file = open("save.txt","r")
        datas = json.loads(lg_file.read())
        global main_hero
        main_hero = hero(datas["0"],turn_lists_to_skills(datas["1"]),datas["2"],datas["3"],datas["4"],datas["5"],datas["6"],datas["7"])    
        
        process_bar("读档中", "读档成功")
    except:
        s_print("貌似没有可读的存档。。。")
        exit_request("请输入q退出游戏 ", "q")
        print("输入错误，5秒系统将自动退出")
        time.sleep(5)
        exit()
        

def start_new_game():
    while True:
        name = raw_input("请先给你的英雄取个名字： ")
        while True:
            occupation = raw_input("请选择英雄的职业（目前只有战士可选）<按q退出>：\n1.战士\n>>> ")
            if occupation != "1":
                continue
            if occupation == "q":
                exit_request()
            else:
                break
        
        
        #hero1 = hero("战士",[],"小菊人",(20,10,2,0.05),[skill_ls[1],skill_ls[3],skill_ls[6]])
        global main_hero
        main_hero = hero("战士",[skill_ls[1],skill_ls[3],skill_ls[6]],name,attrs =occupation_attrs["战士"][0] )
           
        
        print ("恭喜你，成功创造了一个角色！\n")
        break
        
def menu1():
    while True:
        
        string ="1.新游戏\n2.读取存档\n<按q退出界面>\n>>>"
        ipt = raw_input((string))
        if ipt == "1":
            start_new_game()
            break
        elif ipt =="2":
            load_game()  
            break
        elif ipt =="q" or ipt == "P":
            exit_request()
        else:
            print("你的输入有误，请重试\n")
def menu2():
    while True:        
        ipt =  raw_input("1.传送门\n2.英雄简介\n3.背包\n4.怪物图鉴\n5.保存游戏\n6.返回上一页\n<按q退出界面>\n>>>")
        if ipt == "1":
            chuansongmen_menu()
        elif ipt == "2":
            print(main_hero)
        elif ipt == "3":
            print ("背包暂未开放，因为武器类还没制作完成")
        elif ipt =="4":
            for i in range(len(monster_ls)):
                print(monster_ls[i])
        elif ipt == "5":
            save_game()
        elif ipt == "6":
            break
        if ipt == "q":
            exit_request()
        else:
            print ("")
                    
def chuansongmen_menu():
    while True:
        ipt = raw_input("1.树林\n2.火山口\n3.宝藏洞\n4.返回上一页\n>>>")
        if ipt == "1":
            combat(main_hero, monster_ls[random.randint(0,1)])
        elif ipt =="2":
            combat(main_hero, monster_ls[random.randint(2,3)]) 
        elif ipt =="3":
            print("这个地图还未开放，敬请期待")
        elif ipt =="4":
            break
        else:
            print("你的输入有误，请重试\n")   


def start():
    while True:
        menu1()
        menu2()
if __name__ =="__main__":
    start()