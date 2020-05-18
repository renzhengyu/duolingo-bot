import time
import json
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

pause = 0.1
rounds = 2
try:
    with open('duolingo-credential.json', 'r') as filehandle:
        duolingo = json.load(filehandle)
except:
    print("Check duolingo-credential.json ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(375, 812)
driver.get('https://stories.duolingo.com')

try:
    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "login-button"))
    ).click()
    time.sleep(pause)

    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Email or username']"))
    ).send_keys(duolingo["username"])
    time.sleep(pause)

    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='password']"))
    ).send_keys(duolingo["password"])
    time.sleep(pause)

    submit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "submit-button"))
    ).click()
    time.sleep(pause)

    for i in range(rounds):
        story_guten_morgen = submit_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[@href='/lessons/de-eine-sache']"))
        ).click()
        time.sleep(pause)

        # Eine Sache
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Steffi und ihr Bruder Marvin sind zu Hause
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Oh nein, ich brauche Brot für mein Sandwich.
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Gehst du zum Supermarkt?
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # click "No" and continue
        answer_no = submit_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[text()='No']"))
        ).click()
        time.sleep(pause)
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Ja.
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Oh, ich brauche auch eine sache.
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # answer "auch" then click continue
        auch_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[text()='auch'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Was brauchst du?
        was_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@class='phrase' and contains(., 'Was')][not(@disabled)]"))
        ).click()
        time.sleep(pause)
        brauchst_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@class='phrase' and contains(., 'brauchst')][not(@disabled)]"))
        ).click()
        time.sleep(pause)
        du_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@class='phrase' and contains(., 'du')][not(@disabled)]"))
        ).click()
        time.sleep(pause)
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Eine Tomate, bitte.
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Gut
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Danke!
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # ... und ich brauche auch Kaffee.
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Ja ...
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # und Zucker
        und_zucker_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(., 'Zucker')][not(@disabled)]"))
        ).click()
        time.sleep(pause)
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Was?!
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # und Milch.
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Hmm... Ich habe eine Idee.
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Hier ist Geld, Marvin, Du gehst zum Supermarket.
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Geld
        geld_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(., 'Geld')][not(@disabled)]"))
        ).click()
        time.sleep(pause)
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Warum?
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        # Ich brauche eine Sache: Brot.
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)
        answer_asked = submit_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(., 'asked')][not(@disabled)]"))
        ).click()
        time.sleep(pause)
        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        pairs = [
            ('no', 'nein'),
            ('at', 'zu'),
            ('sandwich', 'Sandwich'),
            ('to the', 'zum'),
            ('please', 'bitte'),
            ('her', 'ihr'),
            ('is', 'ist'),
            ('why', 'Warum'),
            ('for', 'für'),
            ('idea', 'Idee'),
            ('need', 'brauche'),
            ('milk', 'Milch'),
            ('you', 'du'),
            ('are', 'sind'),
            ('bread', 'Brot'),
            ('home', 'Hause'),
            ('tomato', 'Tomate'),
            ('thank you', 'Danke'),
            ('money', 'Geld'),
            ('and', 'und'),
            ('and sugar', 'und Zucker'),
            ('brother', 'Bruder'),
            ('go', 'Gehst'),
            ('have', 'habe'),
            ('coffee', 'Kaffee'),
            ('also', 'auch'),
            ('my', 'mein'),
            ('what', 'Was'),
            ('yes', 'Ja'),
            ('one', "Eine"),
            ('good', 'Gut'),
            ('I', 'ich'),
            ('here', 'Hier'),
            ('supermarket', 'Supermarkt'),
            ('thing', 'Sache'),
        ]
        pairs.sort()

        button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(@class, 'selectable-token')]"))
        )
        time.sleep(pause)

        matched_pairs = 0
        words = driver.find_elements_by_class_name('selectable-token')
        en_de_dict = dict((en, de) for en, de in pairs)
        de_en_dict = dict((de, en) for en, de in pairs)
        en_words = []
        de_words = []
        for word in words:
            if word.text in en_de_dict:
                en_words.append(word.text)
            elif word.text in de_en_dict:
                de_words.append(word.text)
            else:
                print(f"Found a new word: {word.text}")

        for en in en_words:
            de = en_de_dict[en]
            try:
                button_en = WebDriverWait(driver, 0).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, f"//button[contains(@class, 'selectable-token') and text()='{en}'][not(@disabled)]"))
                )
                button_de = WebDriverWait(driver, 0).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, f"//button[contains(@class, 'selectable-token') and text()='{de}'][not(@disabled)]"))
                )
                if button_en and button_de:
                    matched_pairs += 1
                    button_en.click()
                    button_de.click()
            except:
                print(f"{en}/{de} not found.")
            if matched_pairs == 5:
                break

        continue_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        continue_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue end-slides-continue-button'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        continue_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='continue finish-button end-slides-continue-button'][not(@disabled)]"))
        ).click()
        time.sleep(pause)

        print(f"Round {i} completed.")
finally:
    driver.quit()
