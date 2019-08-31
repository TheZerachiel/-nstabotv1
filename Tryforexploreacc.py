from InstagramAPI import InstagramAPI
import random
import time
import threading

my_dict = {}
# Here The pages that you want to take main pages ( program will follow the likers of this pages and give comment of this pages's posts)
# This pages are the most populer pages ids of Turkey replace the page ids with the page that you want
onlythem = ["3250759456", "2208388885", "6241679691", "5460601317", "3151687331", "6042552619", "1991903177",
            "3016754444", "7780971935",
            "6098326189", "2298597515", "5652484133", "2302559194", "4712779073", "4876075992", "7300451762"]
followthem = []
print("username")
username =input()
print("password")
pssword = input()
saytime = 120


api = InstagramAPI(username, pssword)
api.login()




def followstart():
    i = 0
    while 1:
        try:
            api.follow(followthem[i])
            print("Followed")
            i = i + 1
            time.sleep(saytime)
        except:
            pass


peepee = threading.Thread(target=followstart, args=())


peepee.start()

def lookwork(media):
    mediax = media
    #HERE ARE COMMENTS. TRANSLATE THEM TO YOUR MAİN LANGUAGE
    randomlist = ["🤣", "😍", "😋", "😇", "😜", "🙏", "🤟", "💗", "◼", "🇹🇷", "♥", "🌃", "🌉", "🧡", "💛", "💚",
                  "💙", "💜", "🖤", "❣", "💕", "💞", "💓", "💗", "💖", "😀", "😬", "😁", "😂", "😃", "😄", "🤣",
                  "😅", "😆", "🤪"]
    randomsecondlist = ["mükemmel olmuş", "süpermiş", "LOL", "Çok Güzel", "Cidden Mükemmelmiş", "Çok Beğendim",
                        "Bir Tek Ben Beğenmiş Olamam", "Bu da Ne Böyle", "Kaçırdıgım Bir şey mi var?",
                        "Harikaaaaaa", "Aşk", "harika ötesi",
                        "Mükemmel demek az kalır", "İnanması güç", "Lütfen Takip Edib Süprizlerim Var"]
    listofcomments = []

    api.like((mediax))
    api.getMediaComments(mediax)
    for z in range(50):
        try:
            listofcomments.append(api.LastJson['comments'][z]['text'])
        except:
            pass

    def takecomment(trynumber):
        trynumber = trynumber + 1
        comment = "{}{}{}".format(random.choice(randomlist), random.choice(randomsecondlist), random.choice(randomlist))
        if listofcomments.__len__() > 0:
            comment = random.choice(listofcomments)
            if (('@' in comment) is False) and (listofcomments.__len__() > 0) and (('Gt' in comment) is False):

                return comment
            else:
                if trynumber < 30:
                    takecomment(trynumber)
        comment = "{}{}{}".format(random.choice(randomlist), random.choice(randomsecondlist), random.choice(randomlist))
        return comment

    x = takecomment(0)

    api.comment(mediax, x)

    api.getMediaLikers(mediax)
    for i in range(100):
        try:
            followthem.append(api.LastJson['users'][i]['pk'])
        except:
            pass


def run():
    time.sleep(5)
    with open('LastMedia.txt', 'r+')as f:
        for line in f:
            line = line.replace("\n", "")
            (key, val) = line.split(":")
            my_dict[key] = str(val)
        f.close()
    print(my_dict)
    while 1:
        for i in range(my_dict.__len__()):
            api.getUserFeed(onlythem[i])
            gg = ''
            try:
                print(i)
                gg = api.LastJson['items'][0]['pk']
                if (my_dict[onlythem[i]] == str(gg)) is True:
                    pass
                else:
                    print("Wechange")
                    my_dict[onlythem[i]] = str(gg)
                    with open('LastMedia.txt', 'w+')as f:
                        f.truncate(0)
                        for p in range(len(my_dict)):
                            x = "{}:{}\n".format(onlythem[p], my_dict[onlythem[p]])
                            f.write(str(x))

                    xxx = my_dict[onlythem[i]]
                    time.sleep(saytime)
                    lookwork(xxx)

            except(KeyError, IndexError):
                pass
#
# with open('LastMedia.txt','w+') as f:
#     for i in range(onlythem.__len__()):
#         api.getUserFeed(onlythem[i])
#         gg=''
#         try:
#             gg = api.LastJson['items'][0]['pk']
#         except:
#             pass
#         f.writelines(str(onlythem[i]) + ":" + str(gg) + "\n")
