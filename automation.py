from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random 
from selenium.webdriver import ActionChains


driver = webdriver.Chrome('Drivers\chromedriver.exe')

driver.maximize_window()
sleep(1)
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

def login(u_name,p_word):
    driver.find_element_by_name('username').send_keys(u_name)
    driver.find_element_by_name('password').send_keys(p_word)

    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div').click()
    sleep(3)

    try:
        driver.find_element_by_xpath('//html//body//div[1]//section//main//div//div//div//div//button').click()
    except :
        pass
    sleep(10)

    try:
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    except:
        pass
    sleep(3)


def Hashtags(hashtag_list=[]):
    user_list = []
    new_followed = []
    followed = 0
    for hashtag in hashtag_list:

        driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
        sleep(8)
        first_thumb = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        first_thumb.click()

        sleep(3)
        try:
            for members in range(1,3):

                username = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text
                if username not in user_list:

                    if driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button').text == 'Follow' :
                        #follow
                        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button').click()
                        new_followed.append(username)
                        followed += 1

                        #like
                        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()

                        sleep(3)

                        #comment
                        comm_prob = random.randint(1,10)

                        if comm_prob > 7:

                            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[2]/button').click()
                            comment_box = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')

                            if (comm_prob < 7):
                                comment_box.send_keys('Really cool!')
                                sleep(1)
                            elif (comm_prob > 6) and (comm_prob < 9):
                                comment_box.send_keys('Nice work :)')
                                sleep(1)
                            elif comm_prob == 9:
                                comment_box.send_keys('Nice gallery!!')
                                sleep(1)
                            elif comm_prob == 10:
                                comment_box.send_keys('So cool! :)')
                                sleep(1)

                            comment_box.send_keys(Keys.ENTER)
                            sleep(5)

                    driver.find_element_by_link_text('Next').click()
                    sleep(8)
                else:
                    driver.find_element_by_link_text('Next').click()
                    sleep(8)
        except:
            continue

ac=ActionChains(driver)


def Feed(num):
    for i in range(1,num):
        
    # Feed liking
        post=driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[2]/div/article['+str(i)+']/div/div[2]/div/div/div[2]')
        ac.double_click(post).perform()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[2]/div/article['+str(i)+']/div/div[3]/div/div/section[3]/div/form/textarea').click()
        sleep(1)

    # Feed commenting
        coment_box=driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[2]/div/article['+str(i)+']/div/div[3]/div/div/section[3]/div/form/textarea')
        com_prob=random.choice(['Nice work!', 'WOW!!','Excellent!!!','Superb :)','Awesome!'])
        coment_box.send_keys(com_prob)
        coment_box.send_keys(Keys.ENTER)
        sleep(5)



#Driver Code

if __name__=='__main__':

    u_name='intern831'
    p_word='account456'

    # Trial Account

    # u_name='uda.tej.sab'
    # p_word='account123'

    hashtag_list = ['nature', 'naturephotography', 'traveler']

    login(u_name,p_word)
    Feed(5)
    Hashtags(hashtag_list)
    driver.close()