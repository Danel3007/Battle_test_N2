end = True
meter = 0
import time as t
import random, os
mini_boss_dict = ['Дарт Вейдер(Звездные Войны)','Донки Конг','Призрак(PACMAN)','Локи(Марвел)','Майлз Эджуорт(Ace Attorney)','Магнето(Люди Х)']

boss='get stick bugged lol'
while boss not in ['Дарт Вейдер(Звездные Войны)','Донки Конг','Призрак(PACMAN)','Локи(Марвел)','Майлз Эджуорт(Ace Attorney)','Магнето(Люди Х)']:
    boss = random.choice(mini_boss_dict)
    
game_state = {
  'items': [
    'Коготь Росомахи',
    'Электрошокер'
  ],
  'player_health':100,
  'taken':0,
  'charge':0,
  'scared':0,
  'memo':0,
  'choose':0,
  'meter':0,
  'wall':0,
  'sharp':0
}

vader_attacks = ['Сила','Взмах мечом','Легион штурмовиков','Заряд атаки']
dk_attacks = ['Банановая кожура','Суперудар','Бочка-пушка','Взятие']
ghost_attacks = ['Страшная рожица','Подход вплотную','Объединение призраков','Растворение']
loki_attacks = ['Скипетр','Кинжалы','Тессеракт','Иллюзия','Разговор']
miles_attacks = ['Удар кулаком','Бросок портфеля']
magneto_attacks = ['Удар кулаком','Град металла','Металлическая стена','Рейхсмарка','Затачивание металла']
loki_speech = ['Никогда не думал об изменении климата? Люди леса вырубают, а леса делают кислород. То есть вы сами себя лишаете кислорода. Ты можешь сказать, что "у нас есть водоросли, они вырабатывают больше О2, чем все леса вместе взятые" и дальше что? Вы также загрязняете океан. Водоросли от этого страдают. Вообщем, вот что я тебе скажу. Вали с этой планеты куда подальше. Я слышал, Марс прекрасен. Конечно, надо решить пару проблем с жизнеобеспечением, но есть же технологии. Подумай над этим.',
               'Есть ли Бог? Наука говорит, что нет, не существует. Религия же отвечает, что да, он существует. Ах, зачем об этом говорить, боги точно существуют. Например я. Вернемся к сражению',
               'Учитывая то, как быстро вы испортили планету, то есть примерно лет за двести, с начала индустриализации, вы вымрете лет через 30-40. Это возможно предотвратить, если вы объедините свои усилия. Хотя, в чем смысл говорить это тому виду, который не может нормально донести мусор до урны, и кидает его в метре от неё. Тот же вид думает только о себе и о, внимание, зеленых бумажках *грустный смех*. Если вы обиделись, подумайте над этим и постарайтесь так не делать. У вас ещё есть шанс измениться в лучшую сторону. Эх, кому я это говорю?',
               'Почему клонирование - это неэтично? Убивать растения ради сырья - это этично. Выводить животных специально для поедания - это тоже этично. Но клонировать? Такой потенциал открывается. Можно клонировать наиболее продуктивных людей и устраивать их на работу. В Австралии разрешено клонировать людей, но к сожалению никто этого не делает. Подумай над этим.',
]
import time as t

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
    print('Вас вызывает на битву',boss)
    
    def __init__(self):
        pass

    def battle(self, state={}):
        boss_health = 150

        while True:
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
            has_lamp = "Лампа" in state["items"]
            if has_lamp:
                print("C - Ослепить босса")
            has_tazer = "Электрошокер" in state["items"]
            if has_tazer:
                print("C - Разряд")

            choice = input()
            if state['scared']==1:
                print('Вы напуганы и не можете двигаться')
            
            if state['taken']==1:
                print('Вы не можете двигаться')

            if state['memo']==1:
                print('Вы не понимаете что происходит и не можете атаковать.')

            if state['wall']==1:
                print('Перед вами стена. Вы ничего не можете с этим поделать')

            if state['choose']==1:
                print('Введите номер: 1, 2, или 3')
                choose = random.randint(1,4)
            
            if choice == 'A' and not state['taken']==1 and not state['memo']==1 and not state['scared']==1 and not state['wall']==1: # удар
                if state['choose']==1:
                    print('Введите номер: 1, 2, или 3')
                    choose = random.randint(1,4)
                    hey = int(input())
                    if hey==choose:
                        print('Вы ударили Локи кулаком')
                        print('Это был правильный')
                        dmg = random.randint(13,17)                
                        print('Вы нанесли',dmg,'урона')
                        boss_health -= dmg
                        state['choose'] = 0
                        t.sleep(1)
                    elif hey!=choose:
                        print('Вы ударили Локи кулаком')
                        print('Это был не тот')
                        print('Л:"Честно говоря, я не удивлен"')
                        print('Иллюзии рассеялись')
                        state['choose'] = 0
                        t.sleep(1)
                elif state['choose']==0:
                    print('Вы ударили босса кулаком')
                    dmg = random.randint(13,17)                
                    print('Вы нанесли',dmg,'урона')
                    boss_health -= dmg
                    t.sleep(1)
                
            elif choice == 'B' and not state['taken']==1 and not state['memo']==1 and not state['wall']==1 : # зелья
                heal = random.randint(20,61) 
                print('Вы восстановили',heal,'очка здоровья')
                state['player_health'] += heal
                t.sleep(1)
            elif choice == 'C' and has_tazer and not state['taken']==1 and not state['memo']==1 and not state['wall']==1:
                print("Вы включили электрошокер")
                continue
            t.sleep(1)
            print("")
            state['scared'] = 0
            state['memo'] = 0
            state['taken'] = 0
            state['wall'] = 0
            
            

            # Проверки 
            if boss_health <= 0:
                print("Победа")
                return "WIN"

            def printEm(x):
                y = 0
                while y <= len(x):
                    os.system("cls")
                    print(x[:y])
                    t.sleep(0.02-0.01-0.001-0.0001)
                    y+=1
            
            # Ход босса
            def trial():
                print('*стук молотка*')
                input()
                print('Судья:"Дело о... Эмм... Протагонисте? объявляется открытым."')
                input()
                print('С:"Мистер Эджуорт?"')
                input()
                print('Майлз:"Начну. Сначала за мной приехали трое людей в черных толстовках с капюшоном. Они отчаянно пытались скрывать лица, что им удалось."')
                input()
                print('М:"Они сказали мне поехать с ними, заверив, что это безопасно и они мне заплатят. В качестве взноса я получил 1000 долларов наличными."')
                input()
                print('М:"Они отвезли меня за город, где был построен вход в какое-то подземелье. Они сказали войти туда, и ждать пока придет человек, а также никуда не уходить"')
                input()
                print('M:"Они перевели мне 2000 долларов на банковский счет, после чего оставили меня в комнате и уехали."')
                input()
                print('M:"Из комнаты вела дверь, запертая снаружи, а на другой стороне была ещё одна дверь с головоломкой, которую, скорее всего, нужно было решить чтобы открыть дверь."')
                input()
                print('М:"Спустя пять минут запертая снаружи дверь открылась, и из неё вышел подсудимый, кем является Протагонист."')
                input()
                print('M:"Он начал меня атаковать, я атаковал в ответ. Интересно то, что он соблюдал правило многих современных ролевых игр, то есть атаки шли по очереди."')
                input()
                print('M:"После двух атак мне это надоело и я пригласил его в зал суда."')
                input()
                print('М:"Это всё."')
                input()
                print('С:"Спасибо."')
                input()
                print('С:"Улики указывают на то, что подсудимый виновен."')
                input()
                print('С:"Не вижу смысла продолжать этот суд."')
                input()
                print('С:"Итак, подсудимый..."')
                t.sleep(0.8)
                print('OBJECTION!')
                input()
                print('Феникс:"Неверное утверждение!"')
                input()
                print('С:"Мистер Райт, вы хотите это оспорить?"')
                input()
                print('Ф:"Да, Ваша Честь."')
                input()
                print('Ф:"Майлз говорит что за ним приехали три человека в черных толстовках с капюшоном"')
                input()
                print('Ф:*хлопает по столу*')
                input()
                print('Ф:"НО НАС С ДЕТСТВА УЧИЛИ НЕ ДОВЕРЯТЬ НЕЗНАКОМЦАМ!"')
                input()
                printEm('С:"..."')
                input()
                printEm('М:"..."')
                input()
                print('C:"Мистер Райт, что вы хотите этим сказать"')
                input()
                print('Ф:*в замешательстве* "Ну... С чего-то же надо начать."')
                input()
                print('M:"Феникс, ну вот что ты творишь? Делать нечего?"')
                input()
                print('Ф:"У меня есть задача - доказать, что подсудимый невиновен."')
                input()
                print('M:"Ты зря тратишь моё время, также как и Фортнайт тратит время 12-летних детей."')
                input()
                print('OBJECTION!')
                input()
                print('Ф:*хлопает по столу*')
                print('Ф:"На Фортнайт полез?! Это же лучшая игра, она не только для 12-леток!"')
                input()
                print('М:"Так, Феникс, у нас тут заседание вообще-то! Но Фортнайт все равно фигня."')
                input()
                print('Ф:"Заседание подождет, нам разобраться надо. Фортнайт лучшая игра, не то что ваш квадратный Майнкрафт"')
                input()
                print('M:*рассерженно*"Да как ты смеешь Майн оскорблять?! Майнкрафт самая продаваемая игра после тетриса, что точно говорит о том, что эта игра намного лучше Форты!"')
                input()
                print('С:"К порядку! Тетрис лучше всего!"')
                input()
                print('М:"Может Тетрис чем-то и хорош, но он довольно-таки старый и уже не интересный. А Майну только 10 с половиной лет, и каждый год по массивному обновлению"')
                input()
                print('Ф:"В Форте ивенты есть"')
                input()
                print('М:"Да что ты со своими ивентами?!"')
                input()
                print('*звуки спора*')
                input()
                print('*звуки спора*')
                input()
                print('*звуки спора*')
                input()
                printEm('Вы решили тихонько покинуть спор')
                input()
                print("")
                
            def vader_turn():
                if state['charge']==1:
                    print('Дарт Вейдер использовал усиленную атаку мечом')
                    dmg = random.randint(10,14)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    state['charge'] = 0
                    return
                    
                choice = random.choice(vader_attacks)
                if choice == 'Сила':
                    print('Дарт Вейдер использовал Силу.')
                    dmg = random.randint(3,6)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'Взмах мечом':
                    print('Дарт Вейдер нанес удары мечом.')
                    for i in range(0,6):
                        dmg = random.randint(1,4)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg
                        t.sleep(0.5)
                        
                if choice == 'Легион штурмовиков':
                    print('Дарт Вейдер вызвал штурмовиков')
                    t.sleep(1)
                    print('Они начали в вас стрелять')
                    t.sleep(1)
                    print('И большинство промазали...')
                    dmg = random.randint(1,5)
                    print('Вам нанесли', dmg,'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'Заряд атаки':
                    print('Дарт Вейдер зарядил атаку.')
                    state['charge'] = 1

            def dk_turn():                   
                choice = random.choice(dk_attacks)
                if state['taken']==1:
                    print('Донки Конг выбросил вас')
                    dmg = random.randint(10,15)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    state['taken'] = 0
                    
                if choice == 'Банановая кожура':
                    print('Донки Конг бросил банановую кожуру')
                    print('Вы подскользнулись')
                    dmg = random.randint(4,6)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'Суперудар':
                    print('Донки Конг нанес суперудар')
                    for i in range(0,6):
                        dmg = random.randint(5,9)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg
                        t.sleep(0.5)
                        
                if choice == 'Бочка-пушка':
                    print('Донки Конг выстрелил из бочки-пушки')
                    print('В вас прилетел кокос')
                    dmg = random.randint(17,20)
                    print('Вам нанесли', dmg,'урона')
                    t.sleep(2)
                    print('Кокосы вообще-то тяжелые, поэтому не удивляйтесь')
                    state['player_health'] -= dmg
                    
                if choice == 'Взятие':
                    print('Донки Конг взял вас')
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
                    dmg = random.randint(4,8)
                    dmg1 = random.randint(3,5)
                    dmg2 = random.randint(7,14)
                    dmg3 = random.randint(1,3)
                    print('Инки нанес вам',dmg,'урона')
                    print('Пинки нанес вам',dmg1,'урона')
                    print('Блинки нанес вам',dmg2,'урона')
                    print('Клайд нанес вам',dmg3,'урона')
                    state['player_health'] -= (dmg+dmg1+dmg2+dmg3)
                    state['charge'] = 0
                    return
                    
                choice = random.choice(ghost_attacks)
                if choice == 'Страшная рожица':
                    print('Блинки скорчил страшную рожицу')
                    print('Вам стало страшно')
                    state['scared']=1
                    dmg = random.randint(4,6)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'Подход вплотную':
                    print('Блинки подлетел к вам')
                    t.sleep(random.randint(1,5))
                    print('БУ!')
                    t.sleep(2)
                    print('Вы подскользнулись и упали')
                    dmg = random.randint(5,10)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    t.sleep(0.5)
                        
                if choice == 'Растворение':
                    print('Блинки растворился')
                    t.sleep(2)
                    print('*teleports behind you*')
                    t.sleep(1.05)
                    print('Б:"Omae wa mou shindeiru"')
                    t.sleep(2.63)
                    print('Вы:"Nani?"')
                    t.sleep(1)
                    print('Блинки использовал суперсилы')
                    dmg = random.randint(17,20)
                    print('Вам нанесли',dmg,'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'Объединение призраков':
                    print('Блинки свистнул')
                    t.sleep(1)
                    print('К нему прилетел Пинки')
                    print('К нему прилетел Инки')
                    print('К нему прилетел Клайд')
                    state['charge'] = 1

            def loki_turn():
                state['memo'] = 0
                choice = random.choice(loki_attacks)
                    
                if choice == 'Скипетр':
                    print('Л:"Знаешь, а эта штука полезная"')
                    t.sleep(1)
                    print('Локи навел на вас скипетр')
                    t.sleep(1)
                    print('Вы впали в забытье')
                    state['memo'] = 1
                    
                if choice == 'Кинжалы':
                    print('Локи нанес удары кинжалами')
                    for i in range(0,2):
                        dmg = random.randint(7,12)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg
                        t.sleep(0.5)
                        
                if choice == 'Тессеракт':
                    print('Локи телепортировался')
                    t.sleep(4)
                    print('"Сюрприз"')
                    print('Локи пнул вас сзади')
                    dmg = random.randint(5,9)
                    print('Вам нанесли', dmg,'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'Иллюзия':
                    print('Локи создал клонов')
                    t.sleep(1)
                    print('"Л(хором):Попробуй угадай кто есть кто"')
                    print('Какого по счету Локи вы атакуете?')
                    state['choose'] = 1

                if choice == 'Разговор':
                    print('Локи начал с вами говорить')
                    t.sleep(1)
                    print(random.choice(loki_speech))

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
                    boss_health -= 150
               
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
                                    
                if choice == 'Удар кулаком':
                    print('Магнето вас ударил')
                    dmg = random.randint(4,6)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'Град металла':
                    print('Магнето:"Прогноз на сегодня: град из металла. Будет больно, крепись."')
                    t.sleep(2)
                    print('Магнето обрушил на вас металл')
                    for i in range(0,random.randint(5,14)):
                        dmg = random.randint(4,7)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg
                        t.sleep(0.5)
                        
                if choice == 'Металлическая стена':
                    print('Магнето возвел стену')
                    print('М:*приглушенно* "Посмотрим как ты будешь атаковать."')
                    state['wall'] = 1
                    
                if choice == 'Рейхсмарка':
                    print('Магнето взял свою монетку и направил её на вас')
                    dmg = random.randint(7,15)
                    print('Вам нанесли', dmg,'урона')
                    state['player_health'] -= dmg

                if state['sharp']:
                    print('Металл был острый, поэтому урона больше')
                    state['player_health'] -= 8
                    state['sharp'] = 0

                

            if boss=='Дарт Вейдер(Звездные Войны)':
                vader_turn()
            elif boss=='Донки Конг':
                dk_turn()
            elif boss=='Призрак(PACMAN)':
                ghost_turn()
            elif boss=='Локи(Марвел)':
                loki_turn()
            elif boss=='Майлз Эджуорт(Ace Attorney)':
                miles_turn()
            elif boss=='Магнето(Люди Х)':
                magneto_turn()
            if state['player_health']>=100:
                state['player_health']=100
                print("")
                # Проверки
            if state['player_health'] <= 0:
                print("Поражение")
                return "LOSE"

room = BossRoom()
result = room.battle(game_state)
if result == 'WIN':
    print("")
else:
    print('YOU DIED')
    print("")

print('Вы сыграли в версию 0.1.0')
print('Нажмите ENTER чтобы выйти')
print('Перезайдите чтобы сразиться с другим боссом (но есть шанс того, что вам попадется тот же босс)')
