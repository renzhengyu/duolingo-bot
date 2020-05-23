from duolingo.main import Duobot
import time

rounds = 5

jerry = Duobot('/lessons/de-ueberraschung')

for i in range(rounds):
    jerry.story_begin()

    jerry.click_continue(3)
    jerry.list_answer_keyword('Yes')
    jerry.click_continue(5)
    jerry.list_answer_keyword('him')
    jerry.click_continue(4)
    jerry.buttons_order(['Sie', 'heißt', 'Kathie'])
    jerry.click_continue(5)
    jerry.list_answer_keyword('Sweetheart')
    jerry.click_continue(4)
    jerry.list_answer_keyword('deine')
    jerry.click_continue(5)
    jerry.list_answer_keyword('is')
    jerry.click_continue()
    jerry.pairing_buttons()
    jerry.click_continue()
    jerry.story_end()
    print(f"Round {i+1} completed. {jerry.xp[-1]} XP earned.")
print(f"Total XP earned: {sum(jerry.xp)}")

jerry.kill()
