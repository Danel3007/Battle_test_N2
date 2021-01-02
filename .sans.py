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
}

final_boss_dict = ['Дарт Сидиус(Звездные Войны)','Санс(Undertale)']
sidious_attacks = ['Молния Силы','Армия красных штурмовиков','Лазер Звезды Смерти','i AM The Senate','Экзорцизм']

boss = random.choice(mini_boss_dict)

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

    if val < 4:
        # win
        end = True
        return end

    end = False
    return end

class BossRoom:
    global boss
    boss = random.choice(final_boss_dict)
    print('Вас вызывает на битву',boss)
    
    def __init__(self):
        pass

    def battle(self, state={}):
        if boss=='Санс(Undertale)':
            boss_health==1
        else:
            boss_health = 320

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
                print("L - Ослепить босса")
            has_tazer = "Электрошокер" in state["items"]
            if has_tazer:
                print("C - Разряд")

            choice = input()
            
            if choice == 'A' and boss !='Санс(Undertale)': # удар
                print('Вы ударили босса кулаком')
                t.sleep(1)
                dmg = random.randint(150,201)                
                print('Вы нанесли',dmg,'урона')
                boss_health -= dmg
                t.sleep(1)
            elif boss=='Санс(Undertale)':
                print('Вы ударили босса кулаком')
                t.sleep(1)
                evade = evade + 1
                if evade == 7:
                    print('Санс:"Уф..."')
                    t.sleep(2)
                    print('Санс:"Я устал..."')
                    t.sleep(2)
                    print('Санс:"Пожалуй..."')
                    t.sleep(2)
                    print('Санс:"Вздремну..."')
                    t.sleep(2)
                    print('Нажмите Enter чтобы атаковать')
                    input()
                    print('Вы нанесли 20 урона.')
                    t.sleep(3)
                    print('Санс проснулся, истекая кровью(как он истекает ею если он скелет??)')
                    t.sleep(4)
                    print('Санс:"Хехе"')
                    t.sleep(2)
                    print('Санс:"Значит настал тот момент"')
                    t.sleep(3)
                    print('Санс:"Надо было пить больше кофе"')
                    t.sleep(3)
                    print('Санс:"Знаешь, надо бы произнести какую-нибудь прощальную речь"')
                    t.sleep(5)
                    print('Санс:"Но что-то мне лень"')
                    t.sleep(3)
                    print('Санс:"Проходи. Может, когда-нибудь мы увидимся снова"')
                    t.sleep(4)
                    print('Санс выпил зелье лечения и ушел')
                    boss_health = 0
                    
                elif evade != 7:
                    print('Санс увернулся')
                    
            elif choice == 'B': # зелья
                heal = random.randint(20,61) 
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
                    dmg = random.randint(40,50)
                    print('Вам нанесли', dmg, 'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'Армия красных штурмовиков':
                    print('Дарт Сидиус взмахнул рукой.')
                    number = random.randint(1,100)
                    print('Прибежали',number,'красных штурмовиков')
                    for i in range(1, number):
                        dmg = random.randint(1,100)
                        dmg1 = dmg*0.0001
                        print('Вам нанесли', dmg1, 'урона')
                        state['player_health'] -= dmg1
                        t.sleep(0.5)
                    print('Все убежали обратно')
                    t.sleep(0.5)
                        
                if choice == 'Лазер Звезды Смерти':
                    print('Дарт Вейдер достал контроллер из кармана')
                    print('вверх вверх вниз вниз влево вправо влево вправо B A START')
                    t.sleep(2)
                    print('На вас обрушился лазер Звезды Смерти')
                    dmg = random.randint(100,500)
                    print('Вам нанесли', dmg,'урона')
                    state['player_health'] -= dmg
                    
                if choice == 'i AM The Senate':
                    print('Дарт Сидиус активировал световой меч и, крутясь и крича, прыгнул в вашу сторону')
                    dmg = random.randint(10,20)
                    print('Вам нанесли', dmg,'урона')
                    state['player_health'] -= dmg

                if choice == 'Экзорцизм':
                    print('Сидиус:"⚐♒︎⬧♓⧫♒︎ ⬧◻♓❒♓⧫⬧✏"')
                    t.sleep(1.5)
                    print('Сидиус:"✌♓♎︎ ❍♏︎ ♓■ ⧫♒♏︎ ♐♓♑♒⧫︎ ♋♑♋♓■⬧⧫︎ ⧫♒♋⧫︎ ♐□□●✏"')
                    t.sleep(1.5)
                    print('Сидиус:"☼♏❍□❖♏︎ ♒♓❍︎ ♐❒□❍︎ ⧫♒♏♏⌧♓⬧⧫♏■♍♏✏"')
                    t.sleep(1.5)
                    print('Вам становится не по себе')
                    dmg = random.randint(40,80)
                    state['player_health'] -= dmg

            def sans_turn():
                talk = talk + 1
                if talk == 1:
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
                    
                if talk == 2:
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

                if talk == 3:
                    print('Слушай, а может хватит уже атаковать?')
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

                if talk == 4:
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

                if talk == 5:
                    print('*зевает*')
                    input()
                    print('Что-то спать хочется.')
                    input()
                    print('Хоть я и сплю 10 часов в день.')
                    input()
                    print('Может это из-за сменs часовых поясов?.')
                    input()
                    print('В любом случае, надо взбодриться!.')
                    input()
                    print('Приготовься к сильной атаке!')
                    input()
                    
                print('ЖМИТЕ ENTER ЧТОБЫ УКЛОНЯТЬСЯ')
                t.sleep(1)
                f = random.randint(1,16)
                for i in range(0,f):
                    print('ENTER')
                    startt = t.time()
                    input()
                    endt = t.time()
                    deltat = endt - startt
                    if deltat<=1:
                        print('Уклонение!')
                    else:
                        print('В вас попали')
                        if talk==5:
                            dmg = random.randint(20,30)
                        else:
                            dmg = random.randint(40,60)
                        print('Вам нанесли', dmg, 'урона')
                        state['player_health'] -= dmg

            if boss=='Дарт Сидиус(Звездные Войны)':
                sidious_turn()
            elif boss=='Санс(Undertale)':
                sans_turn()
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

# print('Вы сыграли в версию 0.3.0')
# print('Нажмите ENTER чтобы выйти')
# print('Перезайдите чтобы сразиться с другим боссом (но есть шанс того, что вам попадется тот же босс)')
