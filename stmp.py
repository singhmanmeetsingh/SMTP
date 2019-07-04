import smtplib

gmail_user='manmeettestpython@gmail.com'
gmail_password='testpython@123'

sent_from=gmail_user

to='singhmanmeet523@gmail.com'
subject='IMPORTANT MESSaGE'
body='hi there'


msg = "\r\n".join([
  # "From: user_me@gmail.com",
  # "To: user_you@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])

try:
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg)
    server.close()



    print("email sent")



except:
    print("something went wrong")