import random
import tweepy #Tweepy is the magical tool.
import time
import datetime
slp = time.sleep
subjects = ['A bean','A taco','Beef','Genuine KRAFT Mac & Cheese','Starch','Pingu','Syrup','That car','The grinch','A burger','Jello','Sir Elon', 'Prosecution','Defense','Ridley','Wii Fit Trainer','The lamp','My moth','His truck','Garfield']
predicates = ['is very good','tastes like pure trash','is my spouse','is my strange addiction','is not yellow','is the president of my kitchen','is very juicy','is not educational','is a bright young lad','is basically my wifu','is not invited to my birthday party','hits me up in need of Pocky Sticks','is my ultimate goal','is my main','has been spawned.']
#SET STRING BASED ON thisDate
thisDate = datetime.datetime.now().date()
testDate = "TESTDATE" #Use for testing new date
strThisDate = str(thisDate)
print("Getting Keys...") #Begin snaggin the keys
CONSUMER_KEY='keyhere'
CONSUMER_SECRET='keyhere'
ACCESS_KEY='keyhere'
ACCESS_SECRET='keyhere'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#REAL CODE
#Save names to a text, to avoid spamming, even if the bot is restarted. Clears daily.
#(Not used right now.)

"""
#Clear if it's a new day, write names
with open('listOfscreenNm.txt') as listFile:
    if strThisDate not in listFile.read():
        print("It's a brand new day")
        listFile.close()
        listFile = open('listOfscreenNm.txt', 'w')
        usedNames = []
        listFile.write(strThisDate)
        listFile.close()
"""


thingsToSay = ['Nothing much, you?','Absolutly nothing.','Nothing of interest','Oh, nothing','Random stuff','Not much, I don\'t have a life.', 'Sitting in my basement, all alone :\'(','Eating tacos','reking noobs','Helping the gang beat the water temple','I\'m just goin to the park','Hangin around','I\'m looking for the Dokis, have you seen them?','I am in the process of water-proofing my house with Flex Tape, the super-strong water-proof tape, that can instantly patch, bond, seal, and repair.','Oh, nothin, just eating the Flex Seal family of products.','I may or may not be listening in on your conversations. lol jk.']
               
findThingsToReply = api.search(q="@PanchoBoy4")
specificSearch = ["@PanchoBoy4 Hey what's up?", "@PanchoBoy4 Hey, what's up?","@PanchoBoy4 What's up?","@PanchoBoy4, what's up?","@PanchoBoy4 whats up","@PanchoBoy4 what's up","@PanchoBoy4 what's up?!"]
print("Starting")
              
usedNames = []
sleepTime = 20
lastPhrase = "bean"
lastReply= "barns"
tweet = 0
while True:
    if tweet == 0:
        print("Waiting to tweet...")
        subjLen = len(subjects) - 1
        predLen = len(predicates) - 1
        subjectInt = random.randint(0,subjLen)
        predicateInt = random.randint(0,predLen)
        subjectUsed = subjects[subjectInt]
        predicateUsed = predicates[predicateInt]
        phrase = subjectUsed + " " + predicateUsed
        if phrase == lastPhrase:
            print("Phrase is duplicate.")
        elif phrase !=lastPhrase:
            print("Tweeting!")
            api.update_status(phrase)
        lastPhrase = phrase
        slp(sleepTime)
        tweet = random.randint(0,1)
        print(tweet)
    elif tweet == 1:
     for s in findThingsToReply:
            for i in specificSearch:
                if i == s.text:
                    
                    print("Target spotted")
                    thingsToSayLength = len(thingsToSay) - 1
                    tTSLindex = random.randint(0, thingsToSayLength) #tTSL = 'things to say list'
                    messageTxt = thingsToSay[tTSLindex]
                    #Tweet
                    screenNm= s.user.screen_name
                    m = ("@%s " + messageTxt)  % (screenNm)
                    tweetDate = s.created_at.date()
                    strTweetDate = str(tweetDate)
                    print("ABOUT TO TWEET\nTweet Date: " + strTweetDate + "\nToday: " + strThisDate + "\nUser: " + screenNm)
                    if tweetDate == thisDate and  screenNm not in usedNames and m != lastReply:
                        print("Replying!")
                        s = api.update_status(m,s.id)
                        usedNames.append(screenNm)
                        print(usedNames)
                        lastReply = m
		    else:
			print("Already responded to this boy, it was tweeted on a different day, or phrase is duplicate. Ignoring.")
		    slp(sleepTime)
                    tweet = random.randint(0,1)
                    print(tweet)
    thisDate = datetime.datetime.now().date()
    strThisDate = str(thisDate)
		

#Avoid spam. Not working yet. Just use [usedNames].
"""
        for s in findThingsToReply:
            for i in specificSearch:
                if i == s.text:
                    
                    print("Target spotted")
                    thingsToSayLength = len(thingsToSay) - 1
                    tTSLindex = random.randint(0, thingsToSayLength) #tTSL = 'things to say list'
                    messageTxt = thingsToSay[tTSLindex]
                    #Tweet
                    screenNm= s.user.screen_name
                    m = ("@%s " + messageTxt)  % (screenNm)
                    tweetDate = s.created_at.date()
                    strTweetDate = str(tweetDate)
                    print("ABOUT TO TWEET\nTweet Date: " + str(tweetDate) + "\nToday: " + strThisDate + "\nUser: " + screenNm)
                    listFile = open('listOfscreenNm.txt','r')
                    listFileContents = listFile.read()
                    print(listFileContents)
                    print("screenNm in listFileContents:" + str(screenNm in listFileContents))
                    if tweetDate == thisDate and (screenNm in listFileContents == False):
                        print("Replying!")
                        s = api.update_status(m,s.id)
                        usedNames.append(screenNm)
                        print(usedNames)
                        listFile = open('listOfscreenNm.txt', 'a')
                        listFile.write(str(usedNames))
                        listFile.close()
"""
