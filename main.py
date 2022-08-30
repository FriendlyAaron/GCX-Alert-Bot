import time
import praw
import os
import alert
import re

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
    for submission in subreddit.new(limit=2):
      slink = submission.url 
      stitle = submission.title.lower() 
      max = 84
      shave = stitle[3:stitle.find('[w]')]
      swant = stitle[stitle.find('[w]')+3:]
      print (stitle)
      if not submission.stickied and submission.is_self and not submission.saved and (any(x in swant for x in paymentOption)) and (any(x in shave for x in lookingFor)):
        if '%' in swant:
          percentage = int(swant[swant.find('%')-2:swant.find('%')])
          if percentage <= max:
            submission.save() 
            alert.email_alert('New offer! ',stitle+' '+slink,personalEmail)
            print ('New offer sent!')
        elif '$' in shave and '$' in swant :
          hmoney = (shave[shave.find('$')+1:shave.find('$')+4])
          wmoney = (swant[swant.find('$')+1:swant.find('$')+4])
          if any(char.isdigit() for char in hmoney) and any(char.isdigit() for char in wmoney) and ('.' not in hmoney and '.' not in wmoney):
            hmoney = int(re.sub(r'\D+', '',hmoney))
            wmoney = int(re.sub(r'\D+', '',wmoney))
            if (wmoney / hmoney) <= (max/100):
              submission.save() 
              alert.email_alert('New offer! ',stitle+' '+slink,personalEmail)
              print ('New offer sent!')
  except Exception as e: 
    print(e) 
    print ('Error collecting submission data')

    


while True:
  getSubmission()
  time.sleep(30)
