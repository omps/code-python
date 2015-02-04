#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup
import datetime
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


today = datetime.date.today()
_makeurl = "http://dilbert.com/strip/" + str(today)
_todaydilbert = urllib2.Request(_makeurl)
_dilbertresp = urllib2.urlopen(_todaydilbert)
_soup = BeautifulSoup(_dilbertresp)
_dilbertimgurl = _soup.find(itemprop="image").img.attrs["src"]
_dilberttitle = _soup.find(itemprop="image").img.attrs["alt"]

_todaydilbertimgfile = urllib2.urlopen(_dilbertimgurl)

_filename = str(today) + ".gif"
_outfile = open(_filename, 'wb')
_outfile.write(_todaydilbertimgfile.read())
_outfile.close()


#now send mail.
# Define these once; use them twice!
strFrom = 'torque.india@gmail.com'
strTo = 'ompnix@gmail.com'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = _dilberttitle
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open(_filename, 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
smtp = smtplib.SMTP()
smtp.connect('localhost')
#smtp.login('exampleuser', 'examplepass')
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
