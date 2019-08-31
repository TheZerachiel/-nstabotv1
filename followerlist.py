from InstagramAPI import InstagramAPI
import threading
import random
import time
import datetime
bigaccs=['2959196915','2111407363','237681409','384728850','251091171','209500791','2017572216','554961375','317932194','270350200','26352342','173560420','2041553882','460711162','204318825','253160049','1364414581']
api=InstagramAPI("sclozdkn ","Amksenin")
api.login()
whotofollowlist = []
shitbool = False
templist = []
testone=[]
username=[]
private=[]
followbool=False
unfollowbool=False
likebool=False
coommentbool=False
followcount=0
likecount=0
commentcount=0
logtxt='---------PROGRAM STARTED İN THAT TİME:{}------------'.format(str(datetime.datetime.now().strftime("%H:%M:%S")))
commentbx=4
saytimebiatch=60

def whotofollow(pk):
    followers = []
    next_max_id = ''
    while True:
        api.getUserFollowers(pk, next_max_id)
        temp = api.LastJson
        for item in temp["users"]:
            followers.append(item)
        time.sleep(2)
        if not temp['big_list']:
            break
        next_max_id = temp["next_max_id"]
        if followers.__len__() > 150:
            break
    return followers
def follow():
    global followbool
    global followcount
    print("Start FOLLOWİNG!!!!")
    while 1:

        for i in range(whotofollowlist.__len__()):
            if followbool == True:
                break
            else:
                api.follow(whotofollowlist[i])
                followcount=1+followcount
                print("FOLLOWED: " + username[i] + ' ---' + str(
                    datetime.datetime.now().strftime("%H:%M:%S")) + " ---İs Private ?::: {}".format(private[i]))
            time.sleep(saytimebiatch)


def unfollow():
    global unfollowbool
    print("Start UNFOLLOWİNG!!!!")
    # beni takip edenler
    while 1:
        followers = []
        tmpfollowers = api.getTotalSelfFollowers()
        for i in range(tmpfollowers.__len__()):
            followers.append(tmpfollowers[i]['pk'])
        # benim takip ettiklerim
        tempfollowing = api.getTotalSelfFollowings()
        following = []
        for i in range(tempfollowing.__len__()):
            following.append(tempfollowing[i]['pk'])
        for i in range(following.__len__()):
            if (following[i] in followers) is False:
                if (following[i] in whotofollowlist) is False:
                    api.unfollow(following[i])
                    print("unfollow")
                    time.sleep(saytimebiatch)
                    if unfollowbool == True:
                        break
    #

def likeandcommenthastags():
    global commentbx
    global coommentbool
    global likebool
    global likecount
    global commentcount
    commentcounter=0
    randomlist = ["🤣", "😍", "😋", "😇", "😜", "🙏", "🤟", "💗", "◼", "🇹🇷", "♥", "🌃", "🌉", "🧡", "💛", "💚",
                  "💙", "💜", "🖤", "❣", "💕", "💞", "💓", "💗", "💖", "😀", "😬", "😁", "😂", "😃", "😄", "🤣",
                  "😅", "😆", "🤪"]
    Hastag = ["selfie", "follow", "istanbul", "aşk", "bff", "happy", "güzel", "gezi", "mode", "moda", "moda",
              "yemek", "yemek", "komik", "komik", "hayat", "hayat", "tbt", "life", "smile", "cool", "amazing"]

    randomsecondlist=["mükemmel olmuş","süpermiş","LOL","Çok Güzel","Cidden Mükemmelmiş","Çok Beğendim","Bir Tek Ben Beğenmiş Olamam","Bu da Ne Böyle","Kaçırdıgım Bir şey mi var?","Harikaaaaaa","Aşk","harika ötesi",
                      "Mükemmel demek az kalır","İnanması güç","Lütfen Takip Edib Süprizlerim Var"]
    while 1:
        try:
            api.getHashtagFeed(random.choice(Hastag), "")
            tagFeedJson = api.LastJson["items"]
            print("{} posts will be liked".format(len(tagFeedJson)))
            for i in range(10):
                if likebool == True:
                    break
                listofcomments = []

                mediathings = tagFeedJson[i]['pk']
                api.like(mediathings)
                likecount = 1 + likecount
                print("Liked ")
                commentcounter = commentcounter + 1
                if commentcounter % commentbx == 0 and coommentbool == False:

                    api.getMediaComments(str(mediathings))
                    try:
                        for z in range(10):
                            listofcomments.append(api.LastJson['comments'][z]['text'])
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

                    api.comment(mediathings, takecomment(0))
                    commentcount = 1 + commentcount
                    print("Commented")
                time.sleep(saytimebiatch)
        except:
            likeandcommenthastags()

def BlockControl():
    global unfollowbool
    global followbool
    global likebool
    global coommentbool
    global followcount
    global likecount
    global commentcount
    while 1:
        tt=api.LastResponse
        qq=api.qq
        if ("400" in str(tt)) is True:
            if ("comment"in str(qq)) and ("block" in str(qq)):
                coommentbool=True
                arg="comment"
                q=threading.Thread(target=MakeitFalse,args=(arg,))
                forlog='Comment is Blocked We Comment {} Times and the clock is {} '.format(str(commentcount),str(
                    datetime.datetime.now().strftime("%H:%M:%S")))
                writelog(forlog)
                q.start()
            if ("like" in str(qq)) and ("block" in str(qq)):
                arg="like"
                ü=threading.Thread(target=MakeitFalse, args=(arg,))
                forlog = 'Like is Blocked We Liked {} Times and the clock is {} '.format(str(likecount), str(
                    datetime.datetime.now().strftime("%H:%M:%S")))
                writelog(forlog)
                likebool=True
                ü.start()
            if ("follow" in str(qq)) and ("block" in str(qq)):
                arg="follow"
                ğ=threading.Thread(target=MakeitFalse, args=(arg,))
                forlog = 'Follow is Blocked We Followed {} Times and the clock is {} '.format(str(followcount), str(
                    datetime.datetime.now().strftime("%H:%M:%S")))
                writelog(forlog)
                followbool=True
                ğ.start()
            if ("unfollow" in str(qq)) and ("block" in str(qq)):
                arg="unfollow"
                ş=threading.Thread(target=MakeitFalse, args=(arg,))
                unfollowbool=True
                ş.start()


def MakeitFalse(boolname=''):
    global unfollowbool
    global followbool
    global likebool
    global coommentbool
    time.sleep(3600)
    if boolname=="comment":
        coommentbool=False
    if boolname=="like":
        likebool=False
    if boolname=="follow":
        followbool=False
    if boolname=="unfollow":
        unfollowbool=False

def timesleepcounter():
    myfollowers=api.getTotalSelfFollowers()

    return
def writelog(writethat):
    myfile=open('logs.txt','a')
    myfile.write(writethat)
    myfile.close()
while templist.__len__()<6:
    shitbool=False
    temp=random.choice(bigaccs)
    for i in range(templist.__len__()):
         if temp==templist[i]:
             shitbool=True
    if shitbool is False:
         templist.append(temp)
for i in range(templist.__len__()):
    tempfollowers=(whotofollow(templist[i]))
    for z in range(tempfollowers.__len__()):
        username.append(tempfollowers[z]['username'])
        whotofollowlist.append(tempfollowers[z]['pk'])
        private.append(tempfollowers[z]['is_private'])



writelog(logtxt)
print('{} account will be followed'.format(whotofollowlist.__len__()))
#
x=threading.Thread(target=follow,args=())#Following
y=threading.Thread(target=unfollow,args=())#Unfollowing
z=threading.Thread(target=likeandcommenthastags,args=())#Givinglikeandcommentstohastags
c=threading.Thread(target=BlockControl,args=())#Blockcontrolalghrıthm
print("Here we Go")
x.start()
y.start()
z.start()
c.start()



x.join()
y.join()
z.join()
#
# BlockControl()
# print(xbool)
#

# api.getProfileData()
# print(api.LastJson)


print("We Re finished")



