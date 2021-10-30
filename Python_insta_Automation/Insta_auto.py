from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import choice
from login_details import u_n , pw
from time import sleep


class insta_auto():

    links=[]
    
    comments = [
        'Amazing'   ,   'Awesome!'  ,   'Nice :)'   ,   'SuperB !!' ,   'Sukhibhava !!'
    ]
    def __init__(self):
        self.login(u_n,pw)
        self.like_commenter_feed()
        self.liking_commenting_Hashtags('technology')
        sleep(100)
        self.driver.close()

    def login(self,username,password):
        self.driver = webdriver.Chrome(r"Drivers\chromedriver.exe")
        self.driver.get("https://instagram.com/")
        sleep(5)
        username_box=self.driver.find_element_by_css_selector("input[name='username']")
        username_box.click()
        username_box.send_keys(username)
        sleep(2)
        password_box=self.driver.find_element_by_css_selector("input[name='password']")
        password_box.click()
        password_box.send_keys(password)
        sleep(2)
        login_btn = self.driver.find_element_by_css_selector("button[type='submit']")
        login_btn.click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(5)
    
    def liking_commenting_Hashtags(self,Hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(Hashtag))
        links=self.driver.find_elements_by_tag_name('a')

        def conditions(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(conditions,links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)
        
        for link in self.links:
            self.driver.get(link)
            sleep(3)
            buttons=self.driver.find_elements_by_xpath("//button[@class='wpO6b  ']")
            buttons[1].click()
            sleep(3)
            try:
                buttons[2].click()
                sleep(3)
                self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(choice(self.comments))
                sleep(3)
                self.driver.find_element_by_xpath("//button[@type='submit']").click()
                sleep(5)
                try:
                    self.driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
                    sleep(3)
                except:
                    continue
            except:
                continue

    def like_commenter_feed(self):
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        sleep(1)
        html.send_keys(Keys.HOME)
        sleep(3)
        links=self.driver.find_elements_by_xpath("//*[@aria-label='Like']//following::a[@class='zV_Nj']")
        def conditions(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(conditions,links))

        for i in range(3):
            link = valid_links[i].get_attribute('href')
            print(link)
            if link not in self.links:
                self.links.append(link)
        
        for link in self.links:
            self.driver.get(link)
            sleep(3)
            buttons=self.driver.find_elements_by_xpath("//button[@class='wpO6b  ']")
            buttons[1].click()
            sleep(3)
            try:
                buttons[2].click()
                sleep(3)
                self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(choice(self.comments))
                sleep(3)
                self.driver.find_element_by_xpath("//button[@type='submit']").click()
                sleep(5)
                try:
                    self.driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
                    sleep(3)
                except:
                    continue
            except:
                continue

        self.links=[]

                





def main(no_times):
    for i in range(no_times):
        Instagram_automation = insta_auto()
        sleep(100)


if __name__=='__main__':
    main(1)
