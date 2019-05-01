from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import choice
class InstagramBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Firefox()


# 14 tanesi boş

    def login(self):
        driver=self.driver
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(3)
        namesection=driver.find_element_by_name("username")
        namesection.send_keys(self.username)
        passwordsetion=driver.find_element_by_name("password")
        passwordsetion.send_keys(self.password)
        passwordsetion.send_keys(Keys.RETURN)
        time.sleep(3)
        asdlas = driver.find_elements_by_css_selector("div[class='aOOlW  bIiDR  ']")
        if asdlas is not None:
            try:
                NotifiationScreenclose = driver.find_element_by_css_selector("button[class='aOOlW   HoLwm ']")
                NotifiationScreenclose.click()
            except Exception as e:
                time.sleep(2)



        print("Successfully logged in")
    def closeBrowser(self):
        self.driver.close()
    def explorelike(self):
        time.sleep(10)
        driver=self.driver
        driver.get("https://www.instagram.com/explore/")
        time.sleep(2)
        hrefs=driver.find_elements_by_tag_name('a')
        print(int(len(hrefs)))
        i=0
        IsComment=True
        randomlist=["🤣","😍","😋","😇","😜","🙏","🤟","💗","◼","🇹🇷","♥","🌃","🌉","🧡","💛","💚","💙","💜","🖤","❣","💕","💞","💓","💗","💖","😀","😬","😁","😂","😃","😄","🤣","😅","😆","🤪"]
        pichrefs=[elem.get_attribute('href') for elem in hrefs]
        pichrefs=[href for href in pichrefs]
        for pichref in pichrefs:
            i=i+1
            if i > 14:
                driver.get(pichref)
                time.sleep(2)
                if len(driver.current_url)<30:
                    print("Finish")
                    break
                try:

                    driver.find_element_by_css_selector("button[class='dCJp8 afkep _0mzm-']").click()
                    time.sleep(1)
                    ss = driver.find_element_by_css_selector("textarea[class='Ypffh']")
                    ss.click()
                    if i % 5 == 0 and IsComment == True:
                        yy = driver.find_element_by_xpath(
                            "/html/body/span/section/main/div/div/article/div[2]/section[3]/div/form/textarea")
                        yy.click()
                        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                        yy.send_keys("{}  {}".format(choice(randomlist),choice(randomlist)))
                        yy.send_keys(Keys.RETURN)

                        time.sleep(25)

                except Exception as e:
                    time.sleep(5)

    def MakePhone(self):
        user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
        profile = webdriver.FirefoxProfile
        profile.set_preference("general.useragent.override", user_agent)
        driver = webdriver.Firefox(profile)
        driver.set_window_size(360, 640)
        # https: // www.toolsqa.com / selenium - webdriver / custom - firefox - profile /
    def LikeTaggedPhotos(self):
        driver=self.driver
        # print("Which Hastag Do You Want to Like")
        # Hastag=input()
        # Hastag=Hastag.replace(" ","")
        IsComment=True
        # while 1:
        #     print("Do You Want to comment?")
        #     print("0 For NO and 1 For YES!")
        #     Comment = input()
        #     if Comment=="1":
        #         IsComment=True
        #         print("OK Thank You:)")
        #         break
        #     elif Comment=="0":
        #         IsComment=False
        #         print("OK Thank YOU:)")
        #         break
        #     else:
        #         continue

        Hastag = ["selfie", "follow", "istanbul", "aşk", "bff", "happy", "güzel", "gezi", "mode", "moda", "moda",
                  "yemek", "yemek", "komik", "komik", "hayat", "hayat", "tbt", "life", "smile","cool","amazing"]
        driver.get("https://www.instagram.com/explore/tags/"+str(choice(Hastag))+"/")
        time.sleep(2)
        randomlist = ["🤣", "😍", "😋", "😇", "😜", "🙏", "🤟", "💗", "◼", "🇹🇷", "♥", "🌃", "🌉", "🧡", "💛", "💚",
                      "💙", "💜", "🖤", "❣", "💕", "💞", "💓", "💗", "💖", "😀", "😬", "😁", "😂", "😃", "😄", "🤣",
                      "😅", "😆", "🤪"]

        hrefs=driver.find_elements_by_tag_name('a')
        pic_hrefs=[elem.get_attribute('href') for elem in hrefs]
        pic_hrefs=[href for href in pic_hrefs]
        i=0
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(1)
            if len(driver.current_url)<30:
                print("Finish")
                break
            try:
                driver.find_element_by_css_selector("button[class='dCJp8 afkep _0mzm-']").click()
                time.sleep(1)
                ss=driver.find_element_by_css_selector("textarea[class='Ypffh']")
                ss.click()
                if i%5==0 and IsComment==True:
                    yy = driver.find_element_by_xpath(
                        "/html/body/span/section/main/div/div/article/div[2]/section[3]/div/form/textarea")
                    yy.click()
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    yy.send_keys("{}  {}".format(choice(randomlist),choice(randomlist)))
                    yy.send_keys(Keys.RETURN)

                time.sleep(25)
                i=i+1
            except Exception as e:
                time.sleep(15)
    def FollowTheGuysFollowers(self):
        time.sleep(1)
        driver=self.driver
        People = ["aogofficial", "aykutelmas", "halilibrahimgoker", "cezmikalorifer", "jahrein", "wtcn",
                  "kendinemuzisyen.jpg", "reynmen","atakanozyurt","remixadam","oguzhanugur_","ilberortayli","cmylmz",
                  "incicaps","onediocom","cagritaner","danlabilic"]
        driver.get("https://www.instagram.com/"+str(choice(People)))
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(12)
        i=0
        z=0
        try:
            godownbro=driver.find_element_by_css_selector("button[class='_0mzm- sqdOP  L3NKy       ']")
            godownbro.send_keys(Keys.END)
        except Exception as e:
            time.sleep(3)

        time.sleep(1)
        follows=driver.find_elements_by_css_selector("button[class='_0mzm- sqdOP  L3NKy       ']")
        clicks=[follow for follow in follows]
        for click in reversed(clicks):

            try:
                click.click()
                i=i+1
                print("{}.Follow".format(i))
                time.sleep(25)
            except Exception as e:
                time.sleep(1)





# Dil Sorunu Yuzunden sadece Türkçe olarak çalismakta Dil sorununu halledınce (butun dillerde dakıka ne demek ) çalısacak. Yapıcagımı sanmıyorum :)
    # def TakeTimeTry(self):
    #     driver=self.driver
    #     driver.get("https://www.instagram.com/p/BvU5nsAARhZ/")
    #     time.sleep(3)
    #     tsme=driver.find_element_by_css_selector("time[class='_1o9PC Nzb55']")
    #     whattime=tsme.get_attribute("innerHTML")
    #     asd=str(whattime)
    #     asd=int(asd.find("minutes"))
    #     if asd>0:
    #         print("Dakika var")



# print("Your username:")
# username=input()
# print("Your Password(You Are Safe:))")
# password=input()
print(  " username:")
kadı=input()
print("Password:")
pswrd=input()

mroussbot=InstagramBot(kadı,pswrd)
i=0
mroussbot.login()
for i in range(1,1000):
    mroussbot.FollowTheGuysFollowers()
    # mroussbot.MakePhone()
    mroussbot.LikeTaggedPhotos()
    time.sleep(5)
    mroussbot.explorelike()
    time.sleep(5)



