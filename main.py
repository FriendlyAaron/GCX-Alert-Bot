import time
import praw
import os
import alert

#Login to Reddit
reddit = praw.Reddit(
  client_id = os.environ ['client_id'],
  client_secret =os.environ ['client_secret'],
  username = os.environ ['username'],
  password =os.environ ['password'],
  user_agent = "giftcardexchange"
)
personalEmail = os.environ ['personalEmail']
#Set the subreddit
subreddit = reddit.subreddit("giftcardexchange")
lookingFor = ['amazon']
paymentOption = ['paypal']

#Search posts
def getSubmission ():
  try:
    for submission in subreddit.new(limit=5):
      slink = submission.url 
      stitle = submission.title.lower() 
      max = 85
      shave = stitle[3:stitle.find('[w]')]
      swant = stitle[stitle.find('[w]')+3:]
      if '%' in swant:
        percentage = int(swant[swant.find('%')-2:swant.find('%')])
        if not submission.stickied and submission.is_self and not submission.saved and (any(x in shave for x in lookingFor)) and (any(x in swant for x in paymentOption)) and percentage <= max:
         submission.save() 
         alert.email_alert('New offer! ',stitle+' '+slink,personalEmail)
         print ('new offer sent!')
  except:
    print ('Error collecting submission data')

    



while True:
  getSubmission()
  time.sleep(60)



