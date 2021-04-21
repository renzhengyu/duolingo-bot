import re
import time
import json
import pathlib
import pprint
import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Duobot:
    def __init__(self, story_url):  # example: /lessons/de-verkehrskontrolle-teil-1-adaptation-a2
        self.duolingo_credential_file = 'duolingo-credential.json'
        self.window_size_x = 1200
        self.window_size_y = 600
        self.story_home_url = 'https://stories.duolingo.com'
        self.pause = 0.5
        self.loading_wait = 30
        self.story_url = story_url
        self.dictionary = {}  # or DuoDictionary (with DB)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_window_size(self.window_size_x, self.window_size_y)
        self.load()
        self.login()
        self.xp = []

    def load(self):
        print(f"Loading {self.story_home_url}")
        self.driver.get(self.story_home_url)

    def kill(self):
        print(f"Closing {self.driver}")
        self.driver.quit()

    @property
    def login_button(self):
        return self.element_by_xpath("//button[@id='sign-in-btn']")

    @property
    def username_input(self):
        return self.element_by_xpath("//input[@placeholder='Email or username']")

    @property
    def password_input(self):
        return self.element_by_xpath("//input[@type='password']")

    @property
    def submit_button(self):
        return self.element_by_xpath("//button[@type='submit']")

    @property
    def story_icon(self):
        return self.element_by_xpath(f"//a[@href='{self.story_url}']")

    def story_begin(self):
        print("Story begins.")
        # ActionChains(self.driver).move_to_element(self.story_icon).perform()
        # self.story_icon.click()
        self.driver.get('https://stories.duolingo.com'+self.story_url)
        self.wait()
        self.element_by_xpath("//button[@data-test='story-start']").click()
        self.wait()

    def key_in_answer(self, answer, tag_name='textarea'):
        textarea = self.element_by_tag_name(tag_name)
        self.wait()
        textarea.send_keys(answer)
        self.wait()

    def element_by_tag_name(self, tag):
        element = WebDriverWait(self.driver, self.loading_wait).until(
            EC.presence_of_element_located((By.TAG_NAME, tag)))
        return element

    def element_by_xpath(self, xpath):
        element = WebDriverWait(self.driver, self.loading_wait).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        return element

    def element_by_class_name(self, class_name):
        element = WebDriverWait(self.driver, self.loading_wait).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, class_name))
        )
        return element

    def wait(self):
        time.sleep(self.pause)

    def login(self):
        with open(self.duolingo_credential_file, 'r') as filehandle:
            print(f"Reading {self.duolingo_credential_file}")
            self.credentials = json.load(filehandle)

        print(f"Logging in {self.credentials['username']}")
        self.login_button.click()
        self.wait()
        self.username_input.send_keys(self.credentials["username"])
        self.wait()
        self.password_input.send_keys(self.credentials["password"])
        self.wait()
        self.submit_button.click()
        time.sleep(5)
        print("Log in successful.")

    @property
    def continue_button(self):
        return self.element_by_xpath("//button[@data-test='stories-player-continue'][not(@disabled)]")

    def click_continue(self, times=1):
        print(f"Clicking CONTINUE {times} times.")
        for i in range(times):
            self.continue_button.click()
            self.wait()

    def button_group_answer(self, answer):
        print(f"Clicking {answer} button")
        self.element_by_xpath(
            f"//button[(@data-test='stories-token' or @data-test='stories-choice') and text()='{answer}'][not(@disabled)]").click()
        self.wait()

    def list_answer_keyword(self, keyword):
        print(f"clicking the right answer that contains: {keyword}")
        self.element_by_xpath(
            f"//span[text()='{keyword}'][not(@disabled)]").click()
        self.wait()

    def word_button(self, the_word):
        return self.element_by_xpath(
            f"//span[@data-test='stories-phrase' and contains(., '{the_word}')][not(@disabled)]")

    def buttons_order(self, ordered_words):
        print(f"Clicking buttons in this order: {ordered_words}")
        for word in ordered_words:
            self.word_button(word).click()
            self.wait()

    def wait_until_pairing_buttons_appear(self):
        button = self.element_by_xpath(
            "//button[@data-test='stories-token']")
        self.wait()

    @property
    def all_elements_with_words_for_pairing(self):
        return self.driver.find_elements_by_xpath("//button[@data-test='stories-token']")

    @property
    def all_words_for_pairing(self):
        all_words = [
            element.text for element in self.all_elements_with_words_for_pairing]
        for matched_word in self.all_matched_words:
            if matched_word in all_words:
                all_words.remove(matched_word)
        return all_words

    @property
    def all_matched_words(self):
        elements = self.driver.find_elements_by_class_name(
            '_3alTu')
        return [element.text for element in elements]

    def end_slides_continue_button(self):
        self.element_by_xpath(
            "//button[@class='continue end-slides-continue-button'][not(@disabled)]").click()
        self.wait()

    def finish_button(self):
        self.element_by_class_name("finish-button").click()
        self.wait()

    @property
    def xp_earned(self):
        element = self.element_by_class_name("streak-slide-title")
        xp = int(re.findall(r"(\d+)", element.text)[0])
        return xp

    def story_end(self):
        time.sleep(5)  # 5 seconds to see the earned xp
        # self.xp.append(self.xp_earned)
        self.end_slides_continue_button()
        self.finish_button()

    @property
    def word_pairs_filename(self):
        return self.story_name + '.json'

    @property
    def story_name(self):
        return re.findall(r"^\/lessons\/(\S+)", self.story_url)[0]

    def load_dictionary(self):
        word_pairs_file = pathlib.Path(self.word_pairs_filename)
        if word_pairs_file.exists():
            print(f"Loading dictionary from {self.word_pairs_filename}.")
            with open(self.word_pairs_filename, 'r') as filehandle:
                self.dictionary = json.load(filehandle)
                print(
                    f"Found {len(self.dictionary)} pairs of words in dictionary:")
                pp = pprint.PrettyPrinter(indent=4)
                pp.pprint(self.dictionary)
        else:
            print(
                f"Dictionary doesnot exist. Will create {self.word_pairs_filename}")

    def find_duplicate(self):
        check_list = []
        for word in self.all_words_for_pairing:
            if word in check_list:
                return word
            else:
                check_list.append(word)
        return None

    def pairing_buttons(self):
        # 0. If there's a pair of identical words, click them.
        if self.find_duplicate():
            buttons = self.driver.find_elements_by_xpath(
                f"//button[@data-test='stories-token'] and text()='{self.find_duplicate()}'][not(@disabled)]")
            for button in buttons:
                button.click()
                self.wait()

        self.load_dictionary()
        # 1. use up the dictionary
        for word in self.all_words_for_pairing:
            if self.word_in_dict(word):
                a = word
                b = self.translate(a)
                print(f"Found pair {a} / {b} in dictionary.")
                self.button_group_answer(a)
                self.button_group_answer(b)

        # 2. If there are still word unsolved
        previously = self.all_words_for_pairing
        while len(self.all_words_for_pairing) > 0:
            print('Please pair 2 words.')
            if len(previously) - len(self.all_words_for_pairing) == 2:
                difference = list(set(previously) -
                                  set(self.all_words_for_pairing))
                a = difference[0]
                b = a if len(difference) == 1 else difference[1]
                previously = self.all_words_for_pairing
                print(f"Found manual pairing: {a} / {b}")
                self.commit_words_to_dictionary(a, b)
            else:
                time.sleep(1)
            if len(self.all_words_for_pairing) == 2:
                a = self.all_words_for_pairing[0]
                b = self.all_words_for_pairing[1]
                self.button_group_answer(a)
                self.button_group_answer(b)
                print(f"Regarding the last 2 words as a new pair: {a} / {b}")
                self.commit_words_to_dictionary(a, b)

    def commit_words_to_dictionary(self, a, b):
        self.dictionary[a] = b
        with open(self.word_pairs_filename, 'w', encoding='utf8') as filehandle:
            print(
                f"Saving {len(self.dictionary)} pairs to {self.word_pairs_filename}")
            json.dump(self.dictionary, filehandle,
                      ensure_ascii=False, indent=4, sort_keys=True)

    def word_in_dict(self, word):
        return word in self.dictionary

    def translate(self, word):
        return self.dictionary[word]
