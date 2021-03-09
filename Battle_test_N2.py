end = True
meter = 0
import time as t
import random, os
    
game_state = {
  'items': [

  ],
  'player_health':100,
  'taken':0,
  'charge':0,
  'scared':0,
  'memo':0,
  'choose':0,
  'meter':0,
  'wall':0,
  'sharp':0,
  'lamp':0,
  'knife':0,
  'shoruken':0,
  'pipe':0,
  'crab':0,
  'ballon':0,
  'trial':0,
  'potions':0
}

mini_boss_dict = ['Дарт Вейдер(Звездные Войны)','Донки Конг','Призрак(PACMAN)','Локи(Марвел)','Майлз Эджворт(Ace Attorney)','Дио(ДжоДжо Часть 3)']
vader_attacks = ['Сила','Взмах мечом','Легион штурмовиков','Заряд атаки']
dk_attacks = ['Банановая кожура','Суперудар','Бочка-пушка','Взятие']
ghost_attacks = ['Страшная рожица','Подход вплотную','Объединение призраков','Растворение']
loki_attacks = ['Скипетр','Кинжалы','Тессеракт','Иллюзия','Разговор']
miles_attacks = ['Удар кулаком','Бросок портфеля']
loki_speech = ['Никогда не думал об изменении климата? Люди леса вырубают, а леса делают кислород. То есть вы сами себя лишаете кислорода. Ты можешь сказать, что "у нас есть водоросли, они вырабатывают больше О2, чем все леса вместе взятые" и дальше что? Вы также загрязняете океан. Водоросли от этого страдают. Вообщем, вот что я тебе скажу. Вали с этой планеты куда подальше. Я слышал, Марс прекрасен. Конечно, надо решить пару проблем с жизнеобеспечением, но есть же технологии. Подумай над этим.',
               'Есть ли Бог? Наука говорит, что нет, не существует. Религия же отвечает, что да, он существует. Ах, зачем об этом говорить, боги точно существуют. Например я. Вернемся к сражению',
               'Учитывая то, как быстро вы испортили планету, то есть примерно лет за двести, с начала индустриализации, вы вымрете лет через 30-40. Это возможно предотвратить, если вы объедините свои усилия. Хотя, в чем смысл говорить это тому виду, который не может нормально донести мусор до урны, и кидает его в метре от неё. Тот же вид думает только о себе и о, внимание, зеленых бумажках *грустный смех*. Если вы обиделись, подумайте над этим и постарайтесь так не делать. У вас ещё есть шанс измениться в лучшую сторону. Эх, кому я это говорю?',
               'Почему клонирование - это неэтично? Убивать растения ради сырья - это этично. Выводить животных специально для поедания - это тоже этично. Но клонировать? Такой потенциал открывается. Можно клонировать наиболее продуктивных людей и устраивать их на работу. В Австралии разрешено клонировать людей, но к сожалению никто этого не делает. Подумай над этим.',
]

def qte():
    global end
  # 8.358885049819946
  # 2.5497920513153076
    val = 0

    for i in range(10):
        start = t.time()
        input()
        end = t.time()

        delta = end - start
        val = val + delta
        print(delta)

    print(val)
    if val < 4:
        # win
        end = True
        return end

    end = False
    return end

class BossRoom:
    global boss
    boss = random.choice(mini_boss_dict)
    
    def __init__(self):
        pass

    def battle(self, state={}):
        global boss
        boss_health = 150
        boss = random.choice(mini_boss_dict)
        print('Вас вызывает на битву',boss)

        while True:
            if state['trial']==1:
                boss_health -= 150
                state['trial']=0
            hearts = state['player_health']//10
            hearts2 = boss_health//10
            print("Player: {}".format(state['player_health']),end="", flush=True)
            for i in range(1,hearts+1):
                print('❤',end="", flush=True)
            print("Boss: {}".format(boss_health),end="", flush=True)
            for i in range(1,hearts2):
                print('❤',end="", flush=True)
            print('❤')
            
            # Ход игрока
            print("A - Удар кулаком")
            print('В - Лечение')
            has_lamp = "лампа." in state["items"]
            has_pipe = "труба." in state["items"]
            has_knife = "ножик." in state["items"]
            has_ballon = "газовый баллон." in state["items"]
            has_headcrab = "питомец-хедкраб." in state["items"]
            has_shoruken = "сюрикен." in state["items"]
            if has_lamp:
                print("L - Ослепить босса")
            has_tazer = "Электрошокер" in state["items"]
            if has_tazer:
                print("T - Разряд")
            if has_pipe:
                print("P - Труба")
            if has_knife:
                print("K - Ножик")
            if has_ballon:
                print("G - Баллончик с краской")
            if has_headcrab:
                print("H - Питомец-хедкраб")
            if has_shoruken:
                print("S - Сюрикен")

            choice = input()
            if state['scared']==1:
                print('Вы напуганы и не можете двигаться')
            
            if state['taken']==1:
                print('Вы не можете двигаться')

            if state['memo']==1:
                print('Вы не понимаете что происходит и не можете атаковать.')

            if state['wall']==1:
                print('Перед вами стена. Вы ничего не можете с этим поделать')

                
            
            if choice == 'A' and not state['taken']==1 and not state['memo']==1 and not state['scared']==1 and not state['wall']==1: # удар
                if state['choose']==1:
                    print('Введите номер: 1, 2, или 3')
                    choose = random.randint(1,4)
                    hey = int(input())
                    if hey==choose:
                        print('Вы ударили Локи кулаком')
                        input()
                        print('Это был правильный')
                        dmg = random.randint(20,51)                
                        print('Вы нанесли',dmg,'урона')
                        boss_health -= dmg
                        state['choose'] = 0
                        t.sleep(1)
                    elif hey!=choose:
                        print('Вы ударили Локи кулаком')
                        input()
                        print('Это был не тот')
                        input()
                        print('Л:"Честно говоря, я не удивлен"')
                        input()
                        print('Иллюзии рассеялись')
                        state['choose'] = 0
                        t.sleep(1)
                elif state['choose']==0:
                    print('Вы ударили босса кулаком')
                    t.sleep(1)
                    dmg = random.randint(15,21)                
                    print('Вы нанесли',dmg,'урона')
                    boss_health -= dmg
                    t.sleep(1)
                
            elif choice == 'B' and not state['taken']==1 and not state['memo']==1 and not state['wall']==1 : # зелья
                if state['potions'] <= 1:
                    print('Вы выпили зелье лечения.')
                    input()
                    heal = random.randint(50,150)
                    print('Вы восстановили',heal,'здоровья')
                    state['player_health'] += heal
                    state['potions'] -= 1
                    input()
                else:
                    print('Зелья кончились ¯\_(ツ)_/¯')
                    continue
                
            elif choice == 'T' and has_tazer and not state['taken']==1 and not state['memo']==1 and not state['wall']==1 and not state['scared']==1:
                print("Вы включили электрошокер")
                if boss=='Дарт Вейдер(Звездные Войны)':
                    print("Вы ударили босса электрошокером.")
                    input()
                    print("Дарт Вейдер сломался...")
                    input()
                    boss_health -= 150

                else:
                    print("Вы ударили босса электрошокером")
                    t.sleep(1)
                    dmg = random.randint(15,51)
                    print("Вы нанесли",dmg,"урона")
                    boss_health -= dmg

            elif choice == 'L' and has_lamp and not state['taken']==1 and not state['memo']==1 and not state['wall']==1 and not state['scared']==1:
                state['lamp'] += 1
                if state['lamp']>=7:
                    print('Батарейка села.')
                    input()
                    print('Вы не можете использовать лампу.')
                    continue
                else:
                    print('Вы сильно посветили в босса')
                    input()
                    print('Босс подскользнулся и упал.')
                    input()
                    dmg = random.randint(4,8)
                    print("Вы нанесли ему",dmg,"урона")
                    boss_health -= dmg
                    input()
                    print('Босс не атакует')
                    input()
                    continue

            elif choice == 'P' and has_pipe and not state['taken']==1 and not state['memo']==1 and not state['wall']==1 and not state['scared']==1:
                state['pipe'] +=1
                if state['pipe']>=7:
                    print('Труба сломалась и вы не можете её использовать.')
                    continue
                else:
                    print('Вы ударили босса трубой')
                    input()
                    dmg = random.randint(20,31)
                    print("Вы нанесли",dmg,"урона")
                    boss_health -= dmg
                    input()

            elif choice == 'S' and has_shoruken and not state['taken']==1 and not state['memo']==1 and not state['wall']==1 and not state['scared']==1:
                state['shoruken'] += 1
                if state['shoruken']>=7:
                    print('Сюрикены кончились¯\_(ツ)_/¯')
                    continue
                else:
                    print('Вы кинули в босса сюрикен')
                    input()
                    dmg = random.randint(15,40)
                    print("Вы нанесли",dmg,"урона")
                    boss_health -= dmg
                input()

            elif choice == 'K' and has_knife and not state['taken']==1 and not state['memo']==1 and not state['wall']==1 and not state['scared']==1:
                state['knife'] += 1
                if state['knife']>=7:
                    print('Нож сточился и вы не можете его использовать')
                    input()
                    continue
                else:
                    punch = random.randint(10,30)
                    if punch==28:
                        print('Двадцать восемь ударов ножом!')
                        input()
                        print('Ты действовал наверняка, да?!')
                        input()
                        print('Это была ненависть?!')
                        input()
                        print('Гнев?!')
                        input()
                        print('Он был в крови!')
                        input()
                        print('Умолял о пощаде!')
                        input()
                        print('Но ты снова, и снова наносил ему удары!')
                    else:
                        print('Вы ударили босса ножом',punch,'раз.')
                    dmg=0
                    for i in range(1,punch+1):
                        h = random.randint(1,3)
                        dmg = dmg+h
                    print("Вы нанесли",dmg,"урона")
                    boss_health -= dmg
                input()

            elif choice == 'G' and has_ballon and not state['taken']==1 and not state['memo']==1 and not state['wall']==1 and not state['scared']==1:
                state['ballon'] += 1
                if state['ballon']>=7:
                    print('Краска в баллончике кончилась')
                    continue
                else:
                    print('Вы побрызгали в босса краской')
                    input()
                    location_dict = ['С потолка свалился ','Из стены вылез ','Через дверь вышел ','Сзади телепортировался ','На самолете прилетел ']
                    char_dict = ['слон ','Starship SN9 ','Микки Маус ','Диаволо ','грустный смайлик ','Пушкин ','Мейс Винду ','Пьюдипай ','Моршу ','Т-800 ']
                    act_dict = ['и кинул в босса камень, ','и сыграл на трубе ','и крикнул "СВОБОДУ ПОПУГАЯМ!", ','и прыгнул на босса, ','и ударил босса, ']
                    fin_dict = ['после чего сбежал.','после чего заглючил в четвертое измерение.','после чего умер.','после чего взорвался.','после чего его увезли.']
                    print(random.choice(location_dict),random.choice(char_dict),random.choice(act_dict),random.choice(fin_dict))
                    input()
                    dmg = random.randint(10,250)
                    print("Вы нанесли",dmg,"урона")
                    boss_health -= dmg
                    input()

            elif choice == 'H' and has_headcrab and not state['taken']==1 and not state['memo']==1 and not state['wall']==1 and not state['scared']==1:
                state['crab'] += 1
                if state['crab']>=7:
                    print('Хедкраб устал')
                    continue
                if state['crab']==1:
                    print('Вы кинули в босса хедкраба')
                    input()
                    print(".".format(state['player_health']),end="", flush=True)
                    t.sleep(1)
                    print(".".format(state['player_health']),end="", flush=True)
                    t.sleep(1)
                    print(".".format(state['player_health']),end="", flush=True)
                    t.sleep(1)
                    print(".".format(state['player_health']),end="", flush=True)
                    t.sleep(1)
                    print(".".format(state['player_health']),end="", flush=True)
                    t.sleep(1)
                    print(".")
                    t.sleep(1)
                    print('Короче там такое произошло...')
                    input()
                    print('Если я это скажу игре поднимут рейтинг до 18+')
                    input()
                    print('Вообщем вы поняли какая фигня там творилась...')
                    input()
                    dmg = random.randint(15,40)
                    print("Вы нанесли",dmg,"урона")
                    boss_health -= dmg
                    input()
                else:
                    print('Вы кинули в босса хедкраба')
                    input()
                    print('Ну вы дальше знаете')
                    input()
                    dmg = random.randint(15,40)
                    print("Вы нанесли",dmg,"урона")
                    boss_health -= dmg
                    input()
                    
            state['scared'] = 0
            state['memo'] = 0
            state['taken'] = 0
            state['wall'] = 0
            
            

            # Проверки 
            if boss_health <= 0:
                print("Победа")
                return "WIN"

            def printEm(text, delay=1):
                for c in text:
                    print(c, end='', flush=True)
                t.sleep(delay)
                print()
                
            # Ход босса
            def trial():
                print('*стук молотка*')
                input()
                printEm('Судья:"Дело о... Эмм... Протагонисте? объявляется открытым."')
                input()
                printEm('С:"Мистер Эджворт?"')
                input()
                printEm('Майлз:"Начну. Сначала за мной приехали трое людей в черных толстовках с капюшоном. Они отчаянно пытались скрывать лица, что им удалось."')
                input()
                printEm('М:"Они сказали мне поехать с ними, заверив, что это безопасно и они мне заплатят. В качестве взноса я получил 1000 долларов наличными."')
                input()
                printEm('М:"Они отвезли меня за город, где был построен вход в какое-то подземелье. Они сказали войти туда, и ждать пока придет человек, а также никуда не уходить"')
                input()
                printEm('M:"Они перевели мне 2000 долларов на банковский счет, после чего оставили меня в комнате и уехали."')
                input()
                printEm('M:"Из комнаты вела дверь, запертая снаружи, а на другой стороне была ещё одна дверь с головоломкой, которую, скорее всего, нужно было решить чтобы открыть дверь."')
                input()
                printEm('М:"Спустя пять минут запертая снаружи дверь открылась, и из неё вышел подсудимый, кем является Протагонист."')
                input()
                printEm('M:"Он начал меня атаковать, я атаковал в ответ. Интересно то, что он соблюдал правило многих современных ролевых игр, то есть атаки шли по очереди."')
                input()
                printEm('M:"После двух атак мне это надоело и я пригласил его в зал суда."')
                input()
                printEm('М:"Это всё."')
                input()
                printEm('С:"Спасибо."')
                input()
                printEm('С:"Улики указывают на то, что подсудимый виновен."')
                input()
                printEm('С:"Не вижу смысла продолжать этот суд."')
                input()
                printEm('С:"Итак, подсудимый..."')
                input()
                print('OBJECTION!')
                input()
                printEm('Феникс:"Неверное утверждение!"')
                input()
                printEm('С:"Мистер Райт, вы хотите это оспорить?"')
                input()
                printEm('Ф:"Да, Ваша Честь."')
                input()
                printEm('Ф:"Майлз говорит что за ним приехали три человека в черных толстовках с капюшоном"')
                input()
                printEm('Ф:*хлопает по столу*')
                input()
                printEm('Ф:"НО НАС С ДЕТСТВА УЧИЛИ НЕ ДОВЕРЯТЬ НЕЗНАКОМЦАМ!"')
                input()
                printEm('С:"..."')
                input()
                printEm('М:"..."')
                input()
                printEm('C:"Мистер Райт, что вы хотите этим сказать"')
                input()
                printEm('Ф:*в замешательстве* "Ну... С чего-то же надо начать."')
                input()
                printEm('M:"И что это значит? Делать нечего?"')
                input()
                printEm('Ф:"*чешет голову* Нуууу... меня есть задача - доказать, что подсудимый невиновен."')
                input()
                printEm('M:"Ты зря тратишь моё время, также как и Фортнайт тратит время 12-летних детей."')
                input()
                print('OBJECTION!')
                input()
                printEm('Ф:*хлопает по столу*')
                input()
                printEm('Ф:"На Фортнайт полез?! Это же лучшая игра, она не только для 12-леток!"')
                input()
                printEm('М:"Так, Феникс, у нас тут заседание вообще-то! Но Фортнайт все равно фигня."')
                input()
                printEm('Ф:"Заседание подождет, нам разобраться надо. Фортнайт лучшая игра, не то что ваш квадратный Майнкрафт"')
                input()
                printEm('M:*рассерженно*"Да как ты смеешь Майн оскорблять?! Майнкрафт самая продаваемая игра после тетриса, что точно говорит о том, что эта игра намного лучше Форты!"')
                input()
                printEm('*стук молотка 3 раза*')
                input()
                printEm('С:"К порядку! Тетрис лучше всего!"')
                input()
                printEm('М:"Может Тетрис чем-то и хорош, но он довольно-таки старый и уже не интересный. А Майну только 10 с половиной лет, и каждый год по массивному обновлению"')
                input()
                printEm('Ф:"В Форте ивенты есть"')
                input()
                printEm('М:"Да что ты со своими ивентами?!"')
                input()
                printEm('*звуки спора*')
                input()
                printEm('*звуки спора*')
                input()
                printEm('*звуки спора*')
                input()
                printEm('Вы решили тихонько покинуть спор')
                input()
                state['trial']==1
                
            def vader_turn():
                if state['charge']==1:
                    print('Дарт Вейдер использовал усиленную атаку мечом')
                    input()
                    dmg = random.randint(20,35)
                    print('Вам нанесли', dmg, 'урона')
                    input()
                    state['player_health'] -= dmg
                    state['charge'] = 0
                    return
                    
                choice = random.choice(vader_attacks)
                if choice == 'Сила':
                    print('Дарт Вейдер использовал Силу.')
                    input()
                    dmg = random.randint(13,16)
                    print('Вам нанесли', dmg, 'урона')
                    input()
                    state['player_health'] -= dmg
                    
                if choice == 'Взмах мечом':
                    print('Дарт Вейдер нанес удары мечом.')
                    input()
                    for i in range(0,6):
                        dmg = random.randint(10,14)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg
                        t.sleep(0.5)
                    input()
                        
                if choice == 'Легион штурмовиков':
                    print('Дарт Вейдер вызвал штурмовиков')
                    input()
                    print('Они начали в вас стрелять')
                    input()
                    print('И большинство промазали...')
                    dmg = random.randint(1,5)
                    print('Вам нанесли', dmg,'урона')
                    input()
                    state['player_health'] -= dmg
                    
                if choice == 'Заряд атаки':
                    print('Дарт Вейдер зарядил атаку.')
                    input()
                    state['charge'] = 1

            def dk_turn():                   
                choice = random.choice(dk_attacks)
                if state['taken']==1:
                    print('Донки Конг выбросил вас')
                    input()
                    dmg = random.randint(10,15)
                    print('Вам нанесли', dmg, 'урона')
                    input()
                    state['player_health'] -= dmg
                    state['taken'] = 0
                    
                if choice == 'Банановая кожура':
                    print('Донки Конг бросил банановую кожуру')
                    input()
                    print('Вы подскользнулись')
                    input()
                    dmg = random.randint(4,6)
                    print('Вам нанесли', dmg, 'урона')
                    input()
                    state['player_health'] -= dmg
                    
                if choice == 'Суперудар':
                    print('Донки Конг нанес суперудар')
                    input()
                    for i in range(0,6):
                        dmg = random.randint(5,9)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg
                        t.sleep(0.5)
                    input()
                        
                if choice == 'Бочка-пушка':
                    print('Донки Конг выстрелил из бочки-пушки')
                    input()
                    print('В вас прилетел кокос')
                    input()
                    dmg = random.randint(17,20)
                    print('Вам нанесли', dmg,'урона')
                    input()
                    state['player_health'] -= dmg
                    
                if choice == 'Взятие':
                    print('Донки Конг взял вас')
                    input()
                    print('Жмите ENTER чтобы освободиться')
                    qte()
                    if end == False:
                        print('Вы не смогли вырваться')
                        state['taken'] = 1
                    else:
                        print('Вы вырвались')

            def ghost_turn():
                if state['charge']==1:
                    print('Призраки атаковали в группе')
                    input()
                    dmg = random.randint(4,8)
                    dmg1 = random.randint(3,5)
                    dmg2 = random.randint(7,14)
                    dmg3 = random.randint(1,3)
                    print('Инки нанес вам',dmg,'урона')
                    input()
                    print('Пинки нанес вам',dmg1,'урона')
                    input()
                    print('Блинки нанес вам',dmg2,'урона')
                    input()
                    print('Клайд нанес вам',dmg3,'урона')
                    input()
                    state['player_health'] -= (dmg+dmg1+dmg2+dmg3)
                    state['charge'] = 0
                    return
                    
                choice = random.choice(ghost_attacks)
                if choice == 'Страшная рожица':
                    print('Блинки скорчил страшную рожицу')
                    input()
                    print('Вам стало страшно')
                    input()
                    state['scared']=1
                    dmg = random.randint(4,6)
                    print('Вам нанесли', dmg, 'урона')
                    input()
                    state['player_health'] -= dmg
                    
                if choice == 'Подход вплотную':
                    print('Блинки подлетел к вам')
                    t.sleep(random.randint(1,5))
                    print('БУ!')
                    input()
                    print('Вы подскользнулись и упали')
                    input()
                    dmg = random.randint(5,10)
                    print('Вам нанесли', dmg, 'урона')
                    input()
                    state['player_health'] -= dmg
                    t.sleep(0.5)
                        
                if choice == 'Растворение':
                    print('Блинки растворился')
                    input()
                    print('*teleports behind you*')
                    input()
                    print('Б:"Omae wa mou shindeiru"')
                    input()
                    print('Вы:"Nani?"')
                    input()
                    print('Блинки использовал суперсилы')
                    input()
                    dmg = random.randint(17,20)
                    print('Вам нанесли',dmg,'урона')
                    input()
                    state['player_health'] -= dmg
                    
                if choice == 'Объединение призраков':
                    print('Блинки свистнул')
                    input()
                    print('К нему прилетел Пинки')
                    input()
                    print('К нему прилетел Инки')
                    input()
                    print('К нему прилетел Клайд')
                    input()
                    state['charge'] = 1

            def loki_turn():
                state['memo'] = 0
                choice = random.choice(loki_attacks)
                    
                if choice == 'Скипетр':
                    print('Л:"Знаешь, а эта штука полезная"')
                    input()
                    print('Локи навел на вас скипетр')
                    input()
                    print('Вы впали в забытье')
                    input()
                    state['memo'] = 1
                    
                if choice == 'Кинжалы':
                    print('Локи нанес удары кинжалами')
                    input()
                    for i in range(0,2):
                        dmg = random.randint(17,29)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg
                        t.sleep(0.5)
                    input()
                        
                if choice == 'Тессеракт':
                    print('Локи телепортировался')
                    t.sleep(4)
                    print('"Сюрприз"')
                    input()
                    print('Локи пнул вас сзади')
                    input()
                    dmg = random.randint(5,9)
                    print('Вам нанесли', dmg,'урона')
                    input()
                    state['player_health'] -= dmg
                    
                if choice == 'Иллюзия':
                    print('Локи создал клонов')
                    input()
                    print('"Л(хором):Попробуй угадай кто есть кто"')
                    input()
                    print('Какого по счету Локи вы атакуете?')
                    state['choose'] = 1

                if choice == 'Разговор':
                    print('Локи начал с вами говорить')
                    input()
                    print(random.choice(loki_speech))
                    input()
                    print('Л:"Ну и как же без атаки?"')
                    input()
                    print('Локи кинул в вас Тессеракт')
                    input()
                    print('Это было больно')
                    input()
                    dmg = random.randint(10,19)
                    print('Вам нанесли', dmg,'урона')
                    input()
                    state['player_health'] -= dmg

            def miles_turn():
                state['meter'] += 1

                if state['meter']==2:
                    print('"То что вы делали только что расценивается как покушение на жизнь человека. Я подаю на вас в суд. Вы можете позвонить своему адвокату."')
                    input()
                    print('Вы достали телефон и открыли контакты')
                    input()
                    print('Вы набрали Феникса Райта')
                    input()
                    t.sleep(3)
                    printEm('На следующий день')
                    trial()
                    dmg = 150
                    boss_health -= dmg
               
                choice = random.choice(miles_attacks)
                
                if choice == 'Удар кулаком':
                    print('Майлз ударил вас')
                    print('Это было не сильно')
                    dmg = random.randint(2,5)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'Бросок портфеля':
                    print('Майлз бросил портфель')
                    print('В вас прилетел портфель')
                    print('А что, логично')
                    dmg = random.randint(7,10)
                    print('Вам нанесли', dmg,'урона')
                    state['player_health'] -= dmg
                
            def magneto_turn():                   
                choice = random.choice(magneto_attacks)                    
                                    
                if choice == '':
                    pass
                    
                if choice == '':
                    pass
                        
                if choice == '':
                    pass
                    
                if choice == '':
                    pass

                if choice=='':
                    pass

                    

                

            if boss=='Дарт Вейдер(Звездные Войны)':
                vader_turn()
            elif boss=='Донки Конг':
                dk_turn()
            elif boss=='Призрак(PACMAN)':
                ghost_turn()
            elif boss=='Локи(Марвел)':
                loki_turn()
            elif boss=='Майлз Эджворт(Ace Attorney)':
                miles_turn()
            elif boss=='Магнето(Люди Х)':
                magneto_turn()
            if state['player_health']>=100:
                state['player_health']=100
                print("")
                # Проверки
            if state['player_health'] <= 0:
                printEm("YOU DIED")
                return "LOSE"

# room = BossRoom()
# result = room.battle(game_state)
# if result == 'WIN':
#     print("")
# else:
#     print('YOU DIED')
#     print("")
