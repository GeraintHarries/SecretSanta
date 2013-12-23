from random import sample

var = raw_input("Please enter each persons name followed by their email dividing everything with a comma (e.g. Tim, tim@email.com, John, john@email.com): ")
NamesAndEmails = var.split(",")
print NamesAndEmails

Names = []
Names = NamesAndEmails[::2]

print Names

Emails = []
Emails = NamesAndEmails[1::2]

print Emails

print sample(xrange(len(Names)), len(Emails))


