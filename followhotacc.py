from InstagramAPI import InstagramAPI
onlythem = ["3250759456", "2208388885", "6241679691", "5460601317", "3151687331", "6042552619", "1991903177",
            "3016754444", "7780971935",
            "6098326189", "2298597515", "5652484133", "2302559194", "4712779073", "4876075992", "7300451762"]
followthem = []

username = 'hotasnebula'
pssword = '128bitpassword'

api=InstagramAPI(username,pssword)
api.login()
for i in range(len(onlythem)):
    api.follow(onlythem[i])
    print(api.LastJson)