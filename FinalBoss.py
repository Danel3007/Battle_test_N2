end = True
meter = 0
import time as t
import random, os
    
game_state = {
  'items': [
    'Коготь Росомахи',
    'Электрошокер',
    'Лампа'
  ],
  'player_health':200,
  'lamp':0,
  'knife':0,
  'shoruken':0,
  'pipe':0,
  'crab':0,
  'ballon':0,
  'lmao':0
}

#https://youtu.be/ub82Xb1C8os

final_boss_dict = ['Дарт Сидиус(Звездные Войны)','Санс(Undertale)','Дио Брандо(ДжоДжо Часть 3)']
sidious_attacks = ['Молния Силы','Армия красных штурмовиков','Лазер Звезды Смерти','I AM The Senate','Экзорцизм']
dio_attacks = ['MUDA MUDA MUDA','RODA RORA DA','WRYYYYYYYYY','Ножи','Армия зомби'] 

evade = 0

class FinBossRoom:
    global boss
    global evade
    boss = random.choice(final_boss_dict)
    
    def __init__(self):
        pass

    def battlef(self, state={}):
        global evade
        boss_health=1
        if boss=='Санс(Undertale)':
            boss_health==1
        else:
            boss_health = 300
        print('Вас вызывает на битву',boss)

        while True:
            global evade
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
                print("L - Ослепить босса")
            has_tazer = "Электрошокер" in state["items"]
            if has_tazer:
                print("C - Разряд")

            choice = input()
            
            if choice == 'A' and boss !='Санс(Undertale)': # удар
                print('Вы ударили босса кулаком')
                t.sleep(1)
                dmg = random.randint(30,36)                
                print('Вы нанесли',dmg,'урона')
                boss_health -= dmg
                t.sleep(1)
            elif choice == 'A' and boss=='Санс(Undertale)':
                print('Вы ударили босса кулаком')
                t.sleep(1)
                if evade == 7:
                    print('Уф...')
                    input()
                    print('Я устал...')
                    input()
                    print('Пожалуй...')
                    input()
                    print('Вздремну...')
                    input()
                    while True:
                        print('Введите "Attack" чтобы атаковать.')
                        ch = str(input())
                        if ch=='Attack':
                            print('Вы нанесли 20 урона.')
                            input()
                            print('Санс проснулся, истекая кровью(как он истекает ею если он скелет??)')
                            input()
                            print('Хехе')
                            input()
                            print('Значит настал тот момент')
                            input()
                            print('Надо было пить больше кофе')
                            input()
                            print('Знаешь, надо бы произнести какую-нибудь прощальную речь')
                            input()
                            print('Но что-то мне лень')
                            input()
                            print('Проходи. Может, когда-нибудь мы увидимся снова')
                            input()
                            print('Санс выпил зелье лечения и ушел')
                            boss_health = 0
                            break
                        else:
                            print('Вы ввели неправильно.')
                            t.sleep(1)
                            print('Быстрее, а то он проснется.')
                            continue
                    
                elif evade != 7:
                    print('Санс увернулся')
                    
            elif choice == 'B': # зелья
                heal = random.randint(70,200) 
                print('Вы восстановили',heal,'очка здоровья')
                state['player_health'] += heal
                t.sleep(1)
                
            elif choice == 'L' and has_lamp:
                print('Вы ослепили босса')
                print('Босс подскользнулся и упал')
                dmg = random(randint(6,15))
                print('Вы нанесли',dmg,'урона')
                boss_health -= dmg
                t.sleep(1)
                continue
                
            t.sleep(1)
            print("")

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

            def sidious_turn():                    
                choice = random.choice(sidious_attacks)
                if choice == 'Молния Силы':
                    print('Дарт Сидиус использовал Молнию Силы.')
                    input()
                    dmg = random.randint(40,50)
                    print('Вам нанесли', dmg, 'урона')
                    input()
                    state['player_health'] -= dmg
                    
                if choice == 'Армия красных штурмовиков':
                    print('Дарт Сидиус взмахнул рукой.')
                    input()
                    number = random.randint(1,100)
                    print('Прибежали',number,'красных штурмовиков')
                    for i in range(1, number):
                        print('Вам нанесли 1 урона')
                        state['player_health'] -= 1
                        t.sleep(0.1)
                    print('Все убежали обратно')
                    input()
                        
                if choice == 'Лазер Звезды Смерти':
                    print('Дарт Сидиус достал контроллер из кармана')
                    input()
                    print('вверх вверх вниз вниз влево вправо влево вправо B A START')
                    input()
                    print('На вас обрушился лазер Звезды Смерти')
                    input()
                    dmg = random.randint(50,80)
                    print('Вам нанесли', dmg,'урона')
                    input()
                    state['player_health'] -= dmg
                    
                if choice == 'i AM The Senate':
                    print('Дарт Сидиус активировал световой меч и, крутясь и крича, прыгнул в вашу сторону')
                    input()
                    dmg = random.randint(10,20)
                    print('Вам нанесли', dmg,'урона')
                    input()
                    state['player_health'] -= dmg

                if choice == 'Экзорцизм':
                    print('Сидиус:"⚐♒︎⬧♓⧫♒︎ ⬧◻♓❒♓⧫⬧✏"')
                    input()
                    print('Сидиус:"✌♓♎︎ ❍♏︎ ♓■ ⧫♒♏︎ ♐♓♑♒⧫︎ ♋♑♋♓■⬧⧫︎ ⧫♒♋⧫︎ ♐□□●✏"')
                    input()
                    print('Сидиус:"☼♏❍□❖♏︎ ♒♓❍︎ ♐❒□❍︎ ⧫♒♏♏⌧♓⬧⧫♏■♍♏✏"')
                    input()
                    print('Вам становится не по себе')
                    input()
                    dmg = random.randint(40,60)
                    state['player_health'] -= dmg

            def sans_turn():
                global evade
                evade = evade + 1
                if evade == 1:
                    print('Я ведь даже не представился, а ты уже атакуешь.')
                    input()
                    print('Я Санс, скелет, назван в честь шрифта.')
                    input()
                    print('Наверное.')
                    input()
                    print('Наверняка ты слышал обо мне.')
                    input()
                    print('Если нет, то учти, что я бью сильно.')
                    input()
                    print('А, и ещё.')
                    input()
                    print('Иногда я ломаю четвертую стену, сам того не замечая.')
                    input()
                    print('Во всяком случае мне так сказали.')
                    input()
                    
                elif evade == 2:
                    print('Птички поют.')
                    input()
                    print('Или нет?')
                    input()
                    print('Не знаю.')
                    input()
                    print('В конце концов, мы ведь под землёй.')
                    input()
                    print('...')
                    input()
                    print('...')
                    input()
                    print('Странно получилось.')
                    input()

                elif evade == 3:
                    print('Если ты не понял, то атаковать бесполезно.')
                    input()
                    print('Наверное ты уже должен был понять, что это бесполезно.')
                    input()
                    print('Я ведь чемпион по уклонению.')
                    input()
                    print('На чемпионате по уклонениям я занял второе место.')
                    input()
                    print('Почему второе?')
                    input()
                    print('Я просто уснул в самом конце')
                    input()
                    print('Кто победил?')
                    input()
                    print('Думаю это не имеет значения')
                    input()

                elif evade == 4:
                    print('А ты знал что Undertale уже больше пяти лет?')
                    input()
                    print('Откуда я это знаю?')
                    input()
                    print('Не знаю.')
                    input()
                    print('Это просто то, что первое пришло на ум.')
                    input()
                    print('Вот я и сказал это.')
                    input()
                    print('Не имеет смысла?')
                    input()
                    print('Я знаю. Хехе.')
                    input()

                elif evade == 5:
                    print('Хочешь совет?')
                    input()
                    print('Когда ты в следующий раз придешь в комнату,')
                    input()
                    print('которая с шифром Цезаря,')
                    input()
                    print('то введи 6969 пять раз.')
                    input()
                    print('Там будет секретик.')
                    input()
                    print('Хехе.')
                    input()

                elif evade == 6:
                    print('Знаешь, у меня планы на вечер.')
                    input()
                    print('Ну, там, в кафешке посидеть,')
                    input()
                    print('в игры поиграть,')
                    input()
                    print('заработать на хотдогах.')
                    input()
                    print('Так что давай закончим побыстрее.')
                    input()
                    print('Идет?')
                    input()

                elif evade == 7:
                    print('*зевает*')
                    input()
                    print('Что-то спать хочется.')
                    input()
                    print('Хоть я и сплю 10 часов в день.')
                    input()
                    print('Может это из-за смены часовых поясов?')
                    input()
                    print('В любом случае, надо взбодриться!')
                    input()
                    print('Приготовься к сильной атаке!')
                    input()
                    
                print('ЖМИТЕ ENTER ЧТОБЫ УКЛОНЯТЬСЯ')
                t.sleep(1)
                f = random.randint(1,16)
                for i in range(0,f):
                    t.sleep((random.randint(6,11)*0.1))
                    print(' ')
                    print('ENTER')
                    startt = t.time()
                    input()
                    endt = t.time()
                    deltat = endt - startt
                    if deltat<=0.8:
                        print('Уклонение!')
                    else:
                        print('В вас попали')
                        if evade==7:
                            dmg = random.randint(40,60)
                        else:
                            dmg = random.randint(20,30)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg

            def dio_turn():
                if state['lmao'] >= 1:
                    state['lmao']+=1
                    print('Дио:"え？"')
                    print('Субтитры:"Хм?"')
                    input()
                    print('Дио:"あえて私と向き合うもう一人の愚か者、ディオ？"')
                    print('Субтитры:"Очередной глупец, который посмел выйти против меня?"')
                    input()
                    print('Дио:"それは問題ではありません。"')
                    print('Субтитры:"Это бессмысленно"')
                    input()
                    print('Дио:"「ザ・ワルド」の能力で、あなたを全滅させよう！"')
                    print('Субтитры:"С помощью「The World」, я тебя уничтожу!"')
                    input()
                    print('Дио:"ZA WARUDO!"')
                    print('Субтитры:"МИР!"')
                    input()
                    print('...')
                    input()
                    print('...')
                    input()
                    print('...')
                    input()
                    print('Ничего не произошло')
                    input()
                    print('...')
                    input()
                    print('Ах да, у вас же нет стенда.')
                    input()
                    print('Для продвижения сюжета притворимся, что у вас есть СтрелаTM и вы пронзили ей себя')
                    input()
                    print('Поздравляем, у вас теперь стенд.')
                    input()
                    print('Мастер стенда: Протагонист')
                    print('Название стенда: Megalo')
                    print('Сила:A')
                    print('Скорость:B')
                    print('Размах:C(10 метров)')
                    print('Прочность:B')
                    print('Точность:D')
                    print('Потенциал развития: A')
                    input()
                    print('Способность:Изготовление любого вида оружия')
                    print('Пользователь может создать любой вид оружия из ничего.')
                    print('Однако, пользователь не может контролировать какое оружие')
                    print('он создает, и поэтому оружие генерируется случайно.')
                    print('Оружие могут использовать даже люди, не имеющие стенды.')
                    print()
                    input()
                    print('Дио:"ああ、あなたは今スタンドを持っていますか？"')
                    print('Субтитры:"Хм, значит теперь у тебя есть Стенд?"')
                    input()
                    print('Дио:"この戦いはもうすぐ面白くなります..."')
                    print('Субтитры:"Эта битва обещает быть интересной."')
                    input()
                    print('Дио:"しかし、あなたの弱いスタンドはまだ「世界」に匹敵しません"')
                    print('Субтитры:"Но твой хилый стенд все равно не сравнится с мощью 「The World」"')
                    input()
                    print('Дио:"この戦いを始めましょう！"')
                    print('Субтитры:"Да начнется же битва!"')
                choice = random.choice(dio_attacks)
                

            if boss=='Дарт Сидиус(Звездные Войны)':
                sidious_turn()
                
            elif boss=='Санс(Undertale)':
                sans_turn()

            elif boss=='Дио Брандо(ДжоДжо Часть 3)':
                dio_turn()
                
            if state['player_health']>=200:
                state['player_health']=200
                print("")
                # Проверки
            if state['player_health'] <= 0:
                printEm("YOU DIED")
                return "LOSE"

#room = FinalBossRoom()
#result = room.battle(game_state)
#if result == 'WIN':
#     print("")
#else:
#     print('YOU DIED')
#     print("")

# print('Вы сыграли в версию 0.8.0')
# print('Нажмите ENTER чтобы выйти')
# print('Перезайдите чтобы сразиться с другим боссом (но есть шанс того, что вам попадется тот же босс)')
