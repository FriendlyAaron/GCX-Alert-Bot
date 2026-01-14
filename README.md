# GCX-Alert-Bot
This is a GCX (Giftcardexchange) bot that alerts you via email, about specific offers that you may be looking for from the subreddit [r/giftcardexchange](https://www.reddit.com/r/giftcardexchange/new/) from Reddit so that you can be notified of new posts for specific gift cards that you may be looking for. This project is currently hosted on Replit.

### Setup
###### Reddit App:
1. Create a [Reddit](https://www.reddit.com) account
2. [Navigate to the Apps page ](https://www.reddit.com/prefs/apps/)
3. Click *create an app*
4. **name:** Set a name for your app
5. **type:** Script
6. **description:** Optional
7. **about url:** Optional
8. **redirect url:** http://localhost
9. Note the outputted *client id* and *secret*

###### Bot Google email:
1. Create a [gmail account](https://accounts.google.com/signup) or use an exisiting gmail
2. Set up 2-step verification
3. Set app password 
4. Choose other (Custom name) & name it
5. Click generate
6. Note down the password

###### config ENV file:
1. **REDDIT_USERNAME:** Your Reddit username
2. **REDDIT_PASSWORD:** Your Reddit password
3. **CLIENT_ID:** The outputted client id
4. **CLIENT_SECRET** The outputted client secret
5. **EMAIL:** The email address you created 
6. **EMAIL_PASSWORD:** Your generated password
7. **PERSONAL_EMAILS:** Your personal email address that you wish to receive the alerts on

###### config main file:
1. **lookingFor:** The Item that you want. It is currently configured to Amazon and can be changed to other options like Best Buy, Ebay, or Target. You can also add to the list in case you are looking for mutiple items.
2. **paymentOption:** How you want to pay for the item. It is currently configured to Paypal but can be changed to other options like Zelle, crypto, or Cashapp. You can also add to the list in case you have mutiple payment options. 
3. **max_percent:** The max percentage you would pay. It is currently configured to 80 but it can be changed to a higher or lower amount



         
      

## Gallery:
Here are some examples of email alerts the bot has made and the correlating post.

Alert for Bbox gift card:
![SCR-20220821-sis](https://user-images.githubusercontent.com/84158176/185818934-b3b3b697-026f-40c6-bfb4-8e453b93b867.png)
![SCR-20220821-scr](https://user-images.githubusercontent.com/84158176/185818935-93f42312-e879-4e02-a21b-413d5da82ee9.png)

Alert for Amazon gift card:
![SCR-20220821-w03](https://user-images.githubusercontent.com/84158176/185830443-7ea6330a-0d4b-4f30-ba00-e203d9b81fa5.png)
![SCR-20220821-vzk](https://user-images.githubusercontent.com/84158176/185830444-e5726e63-ba1c-4b01-a2c4-0430d42ddf45.png)

Alert for Google gift card:
![SCR-20220822-epw](https://user-images.githubusercontent.com/84158176/185948019-d0a79a58-7275-4259-ae1d-70ef85e8dd08.png)
![SCR-20220822-epb](https://user-images.githubusercontent.com/84158176/185948021-ac2af6d2-4fd2-4d98-8d81-99ee7831597e.png)
