from duolingo.main import Duobot
import time

rounds = 5

jerry = Duobot('/lessons/de-verkehrskontrolle-teil-1-adaptation-a2')

for i in range(rounds):
    jerry.story_begin()
    jerry.click_continue(2)
    jerry.button_group_answer('hält sie an')
    jerry.click_continue(3)
    jerry.list_answer_keyword('owns')
    jerry.click_continue(7)
    jerry.buttons_order(['Ist', 'dies', 'Ihre', 'aktuelle', 'Adresse'])
    jerry.click_continue(5)
    jerry.list_answer_keyword('mistake')
    jerry.click_continue(2)
    jerry.button_group_answer('den Blinker benutzt')
    jerry.click_continue(5)
    jerry.list_answer_keyword('Strafzettel')
    jerry.click_continue(2)
    jerry.button_group_answer('Fahren haben')
    jerry.click_continue(3)
    jerry.list_answer_keyword('arrest')
    jerry.click_continue()
    jerry.pairing_buttons()
    jerry.click_continue()
    jerry.story_end()
    print(f"Round {i+1} completed. {jerry.xp[-1]} XP earned.")
print(f"Total XP earned: {sum(jerry.xp)}")

jerry.kill()
