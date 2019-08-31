from InstagramAPI import InstagramAPI
import threading
import random
import time
import datetime

import Tryforexploreacc
class Tryagaın:
    def __init__(self, username='', password='',time=60):
         self.usernamex=username
         self.passwordx=password
         self.onlythem = ["3250759456", "2208388885", "6241679691", "5460601317", "3151687331", "6042552619", "1991903177",
                      "7780971935", "6098326189", "2298597515", "5652484133", "2302559194", "1819469370",
                     "4712779073", "4876075992",
                     "7300451762", "1609544161","5923190686"]
         self.bigaccs = ['2959196915', '2111407363', '237681409', '384728850', '251091171', '209500791', '2017572216',
                    '554961375', '317932194', '270350200', '26352342', '173560420', '2041553882', '460711162',
                    '204318825', '253160049', '1364414581']
         self.api = InstagramAPI(username, password)
         self.whotofollowlist = []
         self.shitbool = False
         self.templist = []
         self.testone = []
         self.username = []
         self.private = []
         self.followbool = False
         self.unfollowbool = False
         self.likebool = False
         self.coommentbool = False
         self.followcount = 0
         self.likecount = 0
         self.commentcount = 0
         self.commentbx = 4
         self.followercount=0
         self.saythetime=time
    def runtheprogram(self):
        user=''
        user=self.usernamex
        logtxt = '---------PROGRAM STARTED İN THAT TİME:{}------------'.format(
            str(datetime.datetime.now().strftime("%H:%M:%S")))
        self.api.login()
        while self.templist.__len__() < 6:
            self.shitbool = False
            temp = random.choice(self.bigaccs)
            for i in range(self.templist.__len__()):
                if temp == self.templist[i]:
                    self.shitbool = True
            if self.shitbool is False:
                self.templist.append(temp)
        for i in range(self.templist.__len__()):
            tempfollowers = (self.whotofollow(self.templist[i]))
            for z in range(tempfollowers.__len__()):
                self.username.append(tempfollowers[z]['username'])
                self.whotofollowlist.append(tempfollowers[z]['pk'])
                self.private.append(tempfollowers[z]['is_private'])

        self.writelog(logtxt,user)
        print('{} account will be followed'.format(self.whotofollowlist.__len__()))
        #
        x = threading.Thread(target=self.follow, args=())  # Following
        y = threading.Thread(target=self.unfollow, args=())  # Unfollowing
        z = threading.Thread(target=self.likeandcommenthastags, args=())  # Givinglikeandcommentstohastags
        c = threading.Thread(target=self.BlockControl, args=())  # Blockcontrolalghrıthm
        print("Here we Go")
        x.start()
        y.start()
        z.start()
        c.start()

        # x.join()
        y.join()
        z.join()
        #
        # BlockControl()
        # print(xbool)
        #

        # api.getProfileData()
        # print(api.LastJson)

        print("We Re finished")


    def whotofollow(self,pk):
        followers = []
        next_max_id = ''
        while True:
            try:
                self.api.getUserFollowers(pk, next_max_id)
                temp = self.api.LastJson
                for item in temp["users"]:
                    followers.append(item)
                time.sleep(2)
                if not temp['big_list']:
                    break
                next_max_id = temp["next_max_id"]
                if followers.__len__() > 150:
                    break
            except:pass
        return followers

    def follow(self):
        print("Start FOLLOWİNG!!!!")
        while 1:
            try:
                x=60
                if self.whotofollowlist.__len__()<x:
                    x=self.whotofollowlist.__len__()
                for i in range(x):
                    if self.followbool == True:
                        break
                    else:
                        self.api.follow(self.whotofollowlist[i])
                        self.followcount = 1 + self.followcount
                        print("FOLLOWED: " + self.username[i] + ' ---' + str(
                            datetime.datetime.now().strftime("%H:%M:%S")) + " ---İs Private ?::: {}".format(
                            self.private[i]))
                    time.sleep(self.saythetime*2)
            except:pass
    def unfollow(self):
        print("Start UNFOLLOWİNG!!!!")

        while 1:
            try:



                    followers = []
                    tmpfollowers = self.api.getTotalSelfFollowers()
                    for i in range(tmpfollowers.__len__()):
                        followers.append(tmpfollowers[i]['pk'])
                    # benim takip ettiklerim
                    tempfollowing = self.api.getTotalSelfFollowings()
                    following = []
                    for i in range(tempfollowing.__len__()):
                        following.append(tempfollowing[i]['pk'])
                    for i in range(following.__len__()):
                        if self.unfollowbool == True:
                            break
                        else:
                            if (following[i] in followers) is False:
                                if (following[i] in self.whotofollowlist) is False:
                                    if (str(following[i]) in self.onlythem) is False:
                                        self.api.unfollow(following[i])
                                        print("unfollow ")
                                        time.sleep(self.saythetime)


            except:pass

    def likeandcommenthastags(self):
        self.timesleepcounter()
        if self.followercount < 500:
            self.commentbx = 12
        commentcounter =0
        randomlist = ["🤣", "😍", "😋", "😇", "😜", "🙏", "🤟", "💗", "◼", "🇹🇷", "♥", "🌃", "🌉", "🧡", "💛", "💚",
                      "💙", "💜", "🖤", "❣", "💕", "💞", "💓", "💗", "💖", "😀", "😬", "😁", "😂", "😃", "😄", "🤣",
                      "😅", "😆", "🤪"]
        Hastag = ["selfie", "follow", "istanbul", "aşk", "bff", "happy", "güzel", "gezi", "mode", "moda", "moda",
                  "yemek", "yemek", "komik", "komik", "hayat", "hayat", "tbt", "life", "smile", "cool", "amazing"]

        randomsecondlist = ["mükemmel olmuş", "süpermiş", "LOL", "Çok Güzel", "Cidden Mükemmelmiş", "Çok Beğendim",
                            "Bir Tek Ben Beğenmiş Olamam", "Bu da Ne Böyle", "Kaçırdıgım Bir şey mi var?",
                            "Harikaaaaaa", "Aşk", "harika ötesi",
                            "Mükemmel demek az kalır", "İnanması güç", "Lütfen Takip Edib Süprizlerim Var"]
        while 1:
            try:
                self.api.getHashtagFeed(random.choice(Hastag), "")
                tagFeedJson = self.api.LastJson["items"]
                print("{} posts will be liked".format(len(tagFeedJson)))
                for i in range(10):
                    if self.likebool == True:
                        break
                    listofcomments = []

                    mediathings = tagFeedJson[i]['pk']
                    self.api.like(mediathings)
                    self.likecount = 1 + self.likecount
                    print("Liked ")
                    commentcounter = commentcounter + 1
                    if commentcounter % self.commentbx == 0 and self.coommentbool == False:

                        self.api.getMediaComments(str(mediathings))
                        try:
                            for z in range(10):
                                listofcomments.append(self.api.LastJson['comments'][z]['text'])
                        except:
                            print()

                        def takecomment(trynumber):
                            trynumber = trynumber + 1
                            if listofcomments.__len__() > 0:
                                comment = random.choice(listofcomments)
                                if ('@' in comment) is False and listofcomments.__len__() > 0:
                                    return comment
                                else:
                                    if trynumber < 10:
                                        takecomment(trynumber)
                            else:
                                return "{}{}{}".format(random.choice(randomlist), random.choice(randomsecondlist),
                                                       random.choice(randomlist))

                        self.api.comment(mediathings, takecomment(0))
                        self.commentcount = 1 + self.commentcount
                        print("Commented")
                    time.sleep(self.saythetime)
            except:
                self.likeandcommenthastags()

    def BlockControl(self):
        user=self.usernamex
        while 1:
            tt = self.api.LastResponse
            qq = self.api.qq
            if ("400" in str(tt)) is True:
                if ("comment" in str(qq)) and ("block" in str(qq))and (self.coommentbool is False):
                    self.coommentbool = True
                    arg = "comment"
                    q = threading.Thread(target=self.MakeitFalse, args=(arg,))
                    forlog = 'Comment is Blocked We Comment {} Times and the clock is {} '.format(str(self.commentcount),
                                                                                                  str(
                                                                                                      datetime.datetime.now().strftime(
                                                                                                          "%H:%M:%S")))
                    if q.isAlive():
                        continue
                    else:
                        self.writelog(forlog,user)
                        q.start()
                if ("like" in str(qq)) and ("block" in str(qq))and (self.likebool is False):
                    arg = "like"
                    ü = threading.Thread(target=self.MakeitFalse, args=(arg,))
                    forlog = 'Like is Blocked We Liked {} Times and the clock is {} '.format(str(self.likecount), str(
                        datetime.datetime.now().strftime("%H:%M:%S")))
                    self.likebool = True
                    if ü.isAlive():
                        pass
                    else:
                        self.writelog(forlog, user)

                        ü.start()
                if ("follow" in str(qq)) and ("block" in str(qq))and (self.followbool is False):
                    arg = "follow"
                    ğ = threading.Thread(target=self.MakeitFalse, args=(arg,))
                    forlog = 'Follow is Blocked We Followed {} Times and the clock is {} '.format(str(self.followcount), str(
                        datetime.datetime.now().strftime("%H:%M:%S")))
                    self.followbool = True
                    if ğ.isAlive():
                        pass
                    else:
                        self.writelog(forlog, user)
                        ğ.start()
                if ("unfollow" in str(qq)) and ("block" in str(qq))and (self.unfollowbool is False):
                    arg = "unfollow"
                    ş = threading.Thread(target=self.MakeitFalse, args=(arg,))
                    self.unfollowbool = True

                    if ş.isAlive():
                        pass
                    else:
                        ş.start()
    def MakeitFalse(self,boolname=''):
        time.sleep(3600)
        if boolname == "comment":
            self.coommentbool = False
        if boolname == "like":
            self.likebool = False
        if boolname == "follow":
            self.followbool = False
        if boolname == "unfollow":
            self.unfollowbool = False

    def timesleepcounter(self):
        myfollowers = self.api.getTotalSelfFollowers()
        self.followercount=myfollowers.__len__()

    def writelog(self,writethat,username):
        myfile = open('logs.txt', 'a')
        myfile.writelines(writethat+username+"\n")
        myfile.close()
print("username")
username=input()
print("password")
pss=input()
x=Tryagaın(username,pss,120)
# y=Tryagaın('İDS','PSS')
# z=Tryagaın('İDS','psS')
x=threading.Thread(target=x.runtheprogram,args=())
x.start()


time.sleep(3)
qqq=threading.Thread(target=Tryforexploreacc.run,args=())
qqq.start()
time.sleep(10)

# y=threading.Thread(target=y.runtheprogram,args=())

# y.start()
time.sleep(10)
# z=threading.Thread(target=z.runtheprogram,args=())

# z.start()
time.sleep(10)
# z.join()
x.join()
# y.join()
print('scaryashell')


