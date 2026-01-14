import time
import praw
import os
import alert
import smtplib
import re
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv("info.env")


#Login to Reddit
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)
settings = {
    "subreddit": "giftcardexchange",
    "looking_for": ["amazon", "ebay"],
    "payment_options": ["paypal", "zelle", "cashapp"],
    "max_percent": 80,
    "personal_emails": os.getenv("PERSONAL_EMAILS")
}

subreddit = reddit.subreddit(settings["subreddit"])
lookingFor = settings["looking_for"]
paymentOption = settings["payment_options"]
max_percent = settings["max_percent"]
personalEmail = settings["personal_emails"]

def handle_new_offer(submission):
    submission.save()
    alert.email_alert('New offer!', submission.title + ' ' + submission.url, personalEmail)
    print('New offer sent!')

#Search posts
def getSubmission ():
  try:
    for submission in subreddit.new(limit=10):
      slink = submission.url
      stitle = submission.title.lower()
      shave = stitle[3:stitle.find('[w]')]
      swant = stitle[stitle.find('[w]')+3:]
      print (stitle)
      if not submission.stickied and submission.is_self and not submission.saved and (any(x in swant for x in paymentOption)) and (any(x in shave for x in lookingFor)):
        if '%' in swant:
          percentage = int(swant[swant.find('%')-2:swant.find('%')])
          if percentage <= max_percent:
            handle_new_offer(submission)
        elif '$' in shave and '$' in swant :
          hmoney = (shave[shave.find('$')+1:shave.find('$')+4])
          wmoney = (swant[swant.find('$')+1:swant.find('$')+4])
          if any(char.isdigit() for char in hmoney) and any(char.isdigit() for char in wmoney) and ('.' not in hmoney and '.' not in wmoney):
            hmoney = int(re.sub(r'\D+', '',hmoney))
            wmoney = int(re.sub(r'\D+', '',wmoney))
            if (wmoney / hmoney) <= (max_percent/100):
             handle_new_offer(submission)
  except Exception as e:
    print(e)
    print ('Error collecting submission data')



while True:
  getSubmission()
  time.sleep(30)


