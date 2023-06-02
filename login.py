import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): #test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_failed_login(self): #test cases 1 (blank password field)
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        driver.find_element(By.ID, "btn-login").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[class='lead text-danger']").text
        self.assertIn("Login failed! Please ensure the username and password are valid.", error_message)

    def test_c_failed_login(self): #test cases 2 (blank username field)
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("ThisIsNotAPassword")
        driver.find_element(By.ID, "btn-login").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[class='lead text-danger']").text
        self.assertIn("Login failed! Please ensure the username and password are valid.", error_message)

    def test_b_failed_login(self): #test cases 3 (blank field)
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        driver.find_element(By.ID, "btn-login").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[class='lead text-danger']").text
        self.assertIn("Login failed! Please ensure the username and password are valid.", error_message)

    def test_d_failed_login(self): #test cases 4 (invalid username)
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        driver.find_element(By.ID, "txt-username").send_keys("Jojon")
        driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("ThisIsNotAPassword")
        driver.find_element(By.ID, "btn-login").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[class='lead text-danger']").text
        self.assertIn("Login failed! Please ensure the username and password are valid.", error_message)

    def test_e_failed_login(self): #test cases 5 (invalid password)
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("apa")
        driver.find_element(By.ID, "btn-login").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[class='lead text-danger']").text
        self.assertIn("Login failed! Please ensure the username and password are valid.", error_message)

    def test_e_failed_login(self): #test cases 6 (invalid username & password)
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        driver.find_element(By.ID, "txt-username").send_keys("Jojon parjojon")
        driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("apaya")
        driver.find_element(By.ID, "btn-login").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[class='lead text-danger']").text
        self.assertIn("Login failed! Please ensure the username and password are valid.", error_message)

    def test_success_login(self): #test cases 7 (valid username & password)
        driver = self.browser
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("ThisIsNotAPassword")
        driver.find_element(By.ID, "btn-login").click()

if __name__ == '__main__':
    unittest.main()