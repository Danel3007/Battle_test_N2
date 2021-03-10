end = True
meter = 0
import time as t
import random, os
    
game_state = {
  'items': [

  ],
  'player_health':200,
  'lamp':0,
  'knife':0,
  'shoruken':0,
  'pipe':0,
  'crab':0,
  'ballon':0,
  'lmao':0,
  'potions':0
}

#https://youtu.be/ub82Xb1C8os

final_boss_dict = ['Санс(Undertale)','Дио Брандо(ДжоДжо Часть 3)']
dio_attacks = ['MUDA MUDA MUDA','RODA RORA DA','WRYYYYYYYYY','Армия зомби','Лазерные глаза'] 

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
                if state['potions'] >= 1:
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
                
            t.sleep(1)
            print("")

            # Проверки 
            if boss_health <= 0:
                print("Вы сумели одолеть босса.")
                input()
                print('Стена перед вами раздвинулась, за ней показался проход.')
                input()
                print('Вы прошли в проход.')
                input()
                print('После 10 минут ходьбы вы дошли до конца коридора.')
                input()
                print('Там стоит красная дверь с надписью "ВЫХОД".')
                input()
                while True:
                    print('Введите "Open" чтобы открыть дверь:')
                    o = str(input())
                    if o=='Open':
                        print('Вы потянули за ручку и открыли дверь.')
                        break
                    else:
                        print('Вы ввели неправильно.')
                        input()
                        continue
                input()
                print('Снаружи была пустыня')
                input()
                print('Дверь за вами захлопнулась')
                input()
                print('...')
                input()
                print('...')
                input()
                print('Хорошенько подумав, вы пошли куда глаза глядят.')
                input()
                print('THE END')
                return "WIN"

            def printEm(text, delay=1):
                for c in text:
                    print(c, end='', flush=True)
                t.sleep(delay)
                print()
                
            # Ход босса

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
                choice = random.choice(dio_attacks)
                if choice == 'MUDA MUDA MUDA':
                    print('Дио взмахнул рукой.')
                    input()
                    print('Дио:"私のシグネチャーアタックを使用する時が来ました！"')
                    print('Субтитры:"Пора использовать мою основную атаку!"')
                    input()
                    print('Дио приблизился на 2 метра и начал кидать ножи.')
                    input()
                    print('Дио:"MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA"')
                    print('Я думаю в переводе это не нуждается :/')
                    input()
                    print('В вас попали ножики')
                    input()
                    for i in range(1,random.randint(5,9)):
                        dmg = random.randint(10,15)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg
                    input()
                    
                if choice=='WRYYYYYYYYY':
                    print('Дио крикнул: "WRYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"')
                    input()
                    print('Вы оглохли.')
                    input()
                    dmg = random.randint(20,25)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    
                if choice=='Армия зомби':
                    print('Дио:"ゾンビを招待する時が来たと思います"')
                    print('Субтитры:"По-моему уже пора бы пригласить сюда зомби."')
                    input()
                    print('Дио махнул рукой')
                    input()
                    print('Прибежала армия зомби и начала вас атаковать.')
                    for i in range(1,random.randint(20,50)):
                        dmg = random.randint(1,3)
                        print('Зомби вас ударил, нанес', dmg, 'урона и убежал.')
                        state['player_health'] -= dmg
                    input()

                if choice == 'Лазерные глаза':
                    print('Дио:"吸血鬼のエッセンスを撃ちます！"')
                    print('Субтитры:"Я стрельну в тебя вампирской эссенцией!"')
                    input()
                    print('Из глаз Дио вырвались розовые струйки.')
                    input()
                    dmg = random.randint(30,40)
                    print('Вам нанесли',dmg,'урона')
                    state['player_health'] -= dmg
                    input()

                if choice == 'RODA RORA DA':
                    print('Дио взлетел.')
                    input()
                    print('Сверху показалась какая-то тень.')
                    input()
                    print('Вы подняли голову.')
                    input()
                    print('Это Дио, держащий каток и кричащий "RODA RORA DAAAAAAAAAAAAAAAAAAAAAA!!!"')
                    input()
                    print('BBBBBBBBBBBBBBBBBB             OOOOOOOOO               OOOOOOOOO          MMMMMMMM               MMMMMMMM')
                    print('B:::::::::::::::::B          OO:::::::::OO           OO:::::::::OO        M:::::::M             M:::::::M')
                    print('B::::::BBBBBB::::::B       OO:::::::::::::OO       OO:::::::::::::OO      M::::::::M           M::::::::M')
                    print('B::::::B     B::::::B     O:::::::OOO:::::::O     O:::::::OOO:::::::O     M:::::::::M         M:::::::::M')
                    print('B::::::B     B::::::B     O::::::O   O::::::O     O::::::O   O::::::O     M::::::::::M       M::::::::::M')
                    print('B::::::B     B::::::B     O:::::O     O:::::O     O:::::O     O:::::O     M:::::::::::M     M:::::::::::M')
                    print('B::::::BBBBBB::::::B      O:::::O     O:::::O     O:::::O     O:::::O     M:::::::M::::M   M::::M:::::::M')
                    print('B::::::::::::::::BB       O:::::O     O:::::O     O:::::O     O:::::O     M::::::M M::::M M::::M M::::::M')
                    print('B::::::BBBBBB::::::B      O:::::O     O:::::O     O:::::O     O:::::O     M::::::M  M::::M::::M  M::::::M')
                    print('B::::::B     B::::::B     O:::::O     O:::::O     O:::::O     O:::::O     M::::::M   M:::::::M   M::::::M')
                    print('B::::::B     B::::::B     O:::::O     O:::::O     O:::::O     O:::::O     M::::::M    M:::::M    M::::::M')
                    print('B::::::B     B::::::B     O::::::O   O::::::O     O::::::O   O::::::O     M::::::M     MMMMM     M::::::M')
                    print('B::::::BBBBBB:::::::B     O:::::::OOO:::::::O     O:::::::OOO:::::::O     M::::::M               M::::::M')
                    print('B::::::::::::::::::B       OO:::::::::::::OO       OO:::::::::::::OO      M::::::M               M::::::M')
                    print('B:::::::::::::::::B          OO:::::::::OO           OO:::::::::OO        M::::::M               M::::::M')
                    print('BBBBBBBBBBBBBBBBBB             OOOOOOOOO               OOOOOOOOO          MMMMMMMM               MMMMMMMM')
                    input()
                    dmg = random.randint(60,90)
                    print('Вам нанесли',dmg,'урона')
                    state['player_health'] -= dmg
                    input()
                                                                                                        
                
                
            if boss=='Санс(Undertale)':
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
