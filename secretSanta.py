from random import sample
import random
import smtplib

from email.mime.text import MIMEText

def shuffle_list(some_list):
	randomized_list = some_list[:]
	while True:
		random.shuffle(randomized_list)
		for a, b in zip(some_list, randomized_list):
			if a == b:
				break
		else:
			return randomized_list

def send_email(emailAddress, Name):

	fromEmailAddress = raw_input("Please enter the email address you wish to send from:")


	sender = fromEmailAddress
	receiver = emailAddress

	message = """From: <%s>
	To: <%s>	
	Subject: Secret Santa Email Allocation

	%s
		
	""" % (sender, receiver, Name)

	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender, receiver, message)
	print "successfully sent email"
	

var = raw_input("Please enter each persons name followed by their email dividing everything with a comma (e.g. Tim, tim@email.com, John, john@email.com): ")
NamesAndEmails = var.split(",")
print NamesAndEmails

Names = []
Names = NamesAndEmails[::2]

print Names

Emails = []
Emails = NamesAndEmails[1::2]

NamesShuffle = shuffle_list(Names)

print NamesShuffle

for i in range(0, len(Emails)):
	send_email(Emails[i], NamesShuffle[i])	
