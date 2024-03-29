# LAB 2, URL SHORTENER. NAMES: URL_PROJECT AND URL_APP.

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class URL(models.Model):

    # url_address = 'https://www.google.com/search?source=hp&q=this+is+a+long+url&oq=this+is+a+long+url&gs_l=psy-ab.3..0i22i30k1.1095.3196.0.3437.19.18.0.0.0.0.137.1480.14j4.18.0....0...1.1.64.psy-ab..1.18.1477.0..0j35i39k1j0i131k1j0i67k1j0i20i264k1j33i22i29i30k1.0.aJvctrIr-Ds'
    url_address = models.CharField(max_length=500, default='')
    short_code = models.CharField(null=True, blank=True, max_length=20)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.url_address



# new: # https://github.com/PdxCodeGuild/class_salmon/blob/main/4%20Django/labs/lab02-url-shortener.md
# old: # # # https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab02-url-shortener.md
# Version 1:

# A url shortener is a web service that can take long urls (https://www.google.com/search?source=hp&q=this+is+a+long+url&oq=this+is+a+long+url&gs_l=psy-ab.3..0i22i30k1.1095.3196.0.3437.19.18.0.0.0.0.137.1480.14j4.18.0....0...1.1.64.psy-ab..1.18.1477.0..0j35i39k1j0i131k1j0i67k1j0i20i264k1j33i22i29i30k1.0.aJvctrIr-Ds) and create a short url (goo.gl/pEc4vt).

# When the short url is accessed, the view will take the specific code associated with that url (pEc4vt) and look up the url associated with it in the database. If that URL is found, it then redirects to that URL.
# id 	code 	url
# 1 	pEc4vt 	https://www.google.com/search?s...
# 2 	fso3Fs 	https://www..

# You could use the ID in the url, instead of some code, but that then exposes some details about your database to the public.
# HINT: Remember the random password generator lab in python? Might be helpful in creating a random code

# Your app should contain the following:

#     1 model to store the long url and short code.
#     2 views
#         One to submit a url
#         And one to redirect the user
#     Use django's HTTPResponseRedirect to handle redirecting users
