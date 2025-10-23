import time
import string
import random
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ----------------------------------------------------------------------
# Account info generator functions
# ----------------------------------------------------------------------
def generatingName():
    firstName = [
        "Alan", "Murat", "Azad", "Necati", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan",
        "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul",
        "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed",
        "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel"
    ]
    lastName = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"
    ]
    return random.choice(firstName) + " " + random.choice(lastName)

def username(size=12, chars=None):
    if chars is None:
        chars = string.ascii_lowercase
    word_list = [
        "cat", "dog", "bird", "fish", "lion", "tiger", "bear", "wolf", "fox", "deer",
        "apple", "banana", "cherry", "date", "elder", "fig", "grape", "honey", "ice", "jam"
    ]
    word_list += list(chars)
    result_username = 'x' * 100
    while len(result_username) < size or len(result_username) >= 30:
        n_word = random.randint(1, 2)
        target_word_list = list(map(lambda x: x.lower(), random.choices(word_list, k=n_word)))
        for word_i, target_word in enumerate(target_word_list):
            if random.random() < 0.05:
                target_word = target_word[::-1]
            target_word_list[word_i] = target_word
            for ch_i in range(len(target_word)):
                if random.random() < 0.03:
                    target_char = random.choice(['x', 'y'] + list(map(str, range(10))))
                    target_word = target_word[:ch_i] + target_char + target_word[ch_i + 1:]
            target_word_list[word_i] = target_word
            if random.random() < 0.07:
                target_word += (target_word[-1] * random.randint(1, 4))
            target_word_list[word_i] = target_word
        joining_char = random.choice(['.', '_'])
        result_username = joining_char.join(target_word_list)
        if random.random() < 0.3:
            if random.random() < 0.6:
                result_username += joining_char
            additional_number_list = []
            number_list = list(map(str, range(10)))
            additional_number_list.append(random.choice(number_list))
            number_list += [''] * 10
            additional_number_list += random.choices(number_list, k=5)
            result_username += ''.join(additional_number_list)
    return result_username

def generatePassword():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(12))

def generateEmail():
    prefix = username(size=10)
    suffix = ''.join(random.choices(string.digits, k=4))
    return f"{prefix}{suffix}@gmail.com"

# ----------------------------------------------------------------------
# Helper: Human delay
# ----------------------------------------------------------------------
def human_delay(min_sec=1.5, max_sec=4.0):
    time.sleep(random.uniform(min_sec, max_sec))

# ----------------------------------------------------------------------
# NEW: Like at least 3 songs + Save playlist
# ----------------------------------------------------------------------
def like_songs_and_save_playlist(driver):
    playlist_url = "https://open.spotify.com/playlist/0oVN9L5D44JyKQGQZuLyHC?si=fKuv0Mz9TeOLLxOMTydN3Q&pi=puSMc7-bQTmVY"
    
    print(f"\nNavigating to playlist: {playlist_url}")
    driver.get(playlist_url)
    human_delay(6, 9)

    try:
        # Wait for playlist to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@data-testid, "tracklist-row")]'))
        )
        print("Playlist loaded. Searching for songs...")

        # Find all "Like" heart buttons using SVG path + aria-label
        heart_buttons = driver.find_elements(By.XPATH, 
            '//button[.//svg[contains(@class, "e-91000-icon")] and .//path[@d="M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8"]]'
        )

        liked_count = 0
        max_likes = 3

        for button in heart_buttons[:10]:  # Limit to first 10 to avoid scrolling too far
            try:
                # Check if already liked (filled heart)
                aria_checked = button.get_attribute("aria-checked")
                if aria_checked == "true":
                    print("Song already liked, skipping...")
                    continue

                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                human_delay(0.8, 1.5)

                try:
                    button.click()
                    print(f"Liked song #{liked_count + 1}")
                    liked_count += 1
                except:
                    driver.execute_script("arguments[0].click();", button)
                    print(f"Liked song #{liked_count + 1} (JS)")

                if liked_count >= max_likes:
                    break

            except Exception as e:
                print(f"Could not like a song: {e}")
                continue

        if liked_count == 0:
            print("No songs were liked (all already liked or not found).")

        # Now save the playlist
        print("\nSaving playlist to library...")
        add_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="add-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        human_delay(1, 2)

        aria_checked = add_button.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Playlist already saved!")
        else:
            try:
                add_button.click()
                print("Clicked 'Save to Your Library'")
            except:
                driver.execute_script("arguments[0].click();", add_button)
                print("Clicked 'Save to Your Library' (JS)")

        print("Waiting 40 seconds on playlist page...")
        time.sleep(40)

    except Exception as e:
        print(f"Failed during playlist interaction: {e}")

# ----------------------------------------------------------------------
# Main Function
# ----------------------------------------------------------------------
def main():
    print("SPOTIFY SIGNUP + LIKE 3 SONGS + SAVE PLAYLIST STARTING...")

    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    print(f"User-Agent: {userAgent}")

    edge_options = Options()
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument(f"user-agent={userAgent}")
    edge_options.add_argument("--disable-blink-features=AutomationControlled")
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    edge_options.add_experimental_option('useAutomationExtension', False)
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--disable-extensions")

    service = Service(executable_path=r'C:\ac\msedgedriver.exe')
    driver = webdriver.Edge(service=service, options=edge_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    try:
        print("\nLoading signup page...")
        driver.get("https://www.spotify.com/in-en/signup/")
        human_delay(3, 5)

        if "signup" not in driver.current_url:
            raise Exception("Failed to load signup page")

        print("Signup page loaded")

        # Cookie consent
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                '//button[contains(text(), "Allow") or contains(text(), "Accept")]'))).click()
            print("Cookie consent accepted")
        except:
            print("No cookie prompt")

        # EMAIL
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        fake_email = generateEmail()
        email_field.clear()
        for c in fake_email:
            email_field.send_keys(c)
            time.sleep(random.uniform(0.05, 0.12))
        print(f"Email: {fake_email}")

        next_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="submit"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        human_delay(1, 2)
        try:
            next_btn.click()
        except:
            driver.execute_script("arguments[0].click();", next_btn)
        print("Next (Email)")
        human_delay(4, 6)

        # PASSWORD
        pw_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'new-password')))
        acc_password = generatePassword()
        pw_field.send_keys(acc_password)
        print(f"Password set")

        with open(r"C:\ac\spotify_accounts.txt", "a", encoding="utf-8") as f:
            f.write(f"{fake_email}:{acc_password}\n")
        print("Credentials saved")

        next_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="submit"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        human_delay(1, 2)
        try:
            next_btn.click()
        except:
            driver.execute_script("arguments[0].click();", next_btn)
        print("Next (Password)")
        human_delay(4, 6)

        # NAME / DOB / GENDER
        name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'displayName')))
        name_field.send_keys(generatingName())
        print("Name entered")

        month = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'month')))
        month.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//option[@value="4"]'))).click()

        driver.find_element(By.ID, 'day').send_keys("10")
        driver.find_element(By.ID, 'year').send_keys("1998")
        print("DOB: 10 April 1998")

        gender = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="gender_option_male"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", gender)
        human_delay(1, 2)
        try:
            gender.click()
        except:
            driver.execute_script("arguments[0].click();", gender)
        print("Gender: Male")

        next_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="submit"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        human_delay(1, 2)
        try:
            next_btn.click()
        except:
            driver.execute_script("arguments[0].click();", next_btn)
        print("Next (DOB)")
        human_delay(4, 6)

        # TERMS
        try:
            marketing = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="checkbox-marketing"]')))
            driver.execute_script("arguments[0].scrollIntoView(true);", marketing)
            human_delay()
            marketing.click()
            print("Opted out: Marketing")
        except:
            print("Marketing checkbox skipped")

        try:
            privacy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="checkbox-privacy"]')))
            driver.execute_script("arguments[0].scrollIntoView(true);", privacy)
            human_delay()
            privacy.click()
            print("Opted out: Privacy")
        except:
            print("Privacy checkbox skipped")

        signup_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="submit"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", signup_btn)
        human_delay(2, 4)
        try:
            signup_btn.click()
            print("FINAL SIGN UP CLICKED")
        except:
            driver.execute_script("arguments[0].click();", signup_btn)
            print("FINAL SIGN UP (JS)")

        # CAPTCHA PAUSE (ONLY HERE)
        print("\nCAPTCHA EXPECTED NOW! Solve it manually...")
        input("After solving CAPTCHA, press Enter to continue...")
        human_delay(5, 8)

        print("\nSPOTIFY SIGNUP COMPLETED!")

        # Like 3 songs + Save playlist
        like_songs_and_save_playlist(driver)

        print("\nALL TASKS DONE!")
        print("BROWSER STAYS OPEN – CLOSE MANUALLY")

    except Exception as e:
        print(f"\nSCRIPT ERROR: {e}")
    finally:
        print("\nScript finished. Browser remains open.")

if __name__ == "__main__":
    main()
