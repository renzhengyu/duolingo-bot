from duolingo.main2 import DuobotWithDB
import time

rounds = 5

jerry = DuobotWithDB(
    '/lessons/de-fi-fi-braucht-ein-zimmer-adaptation-a2')

for i in range(rounds):
    jerry.story_begin()
    jerry.click_continue(2)
    jerry.button_group_answer('Sie bitte hier')
    jerry.click_continue(4)
    jerry.list_answer_keyword("want")
    jerry.click_continue(6)
    jerry.list_answer_keyword('Haustiere')
    jerry.click_continue(3)
    jerry.key_in_answer('in Ihr Zimmer')
    jerry.click_continue(3)
    jerry.buttons_order(['Dann', 'können', 'Sie', 'auf sie aufpassen'])
    jerry.click_continue(4)
    jerry.list_answer_keyword('No')
    jerry.click_continue(7)
    jerry.list_answer_keyword('elevator')
    jerry.click_continue(8)
    jerry.list_answer_keyword('took')
    jerry.click_continue()
    jerry.pairing_buttons()
    jerry.click_continue()
    jerry.story_end()
    print(f"Round {i+1} completed. {jerry.xp[-1]} XP earned.")
print(f"Total XP earned: {sum(jerry.xp)}")

jerry.kill()
