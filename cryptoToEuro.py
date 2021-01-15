# Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα λεξικό από αρχείο το οποίο περιέχει τα κρυπτονομίσματα (όνομα) που έχει 
# ένας χρήστης και πόσα από αυτά. Χρησιμοποιείστε το API https://min-api.cryptocompare.com για να βρείτε σε τι ποσό σε ευρώ αντιστοιχούν.

from crypto_to_euro.api_key import API_KEY 
# keeping the api key secret for privacy reasons. 
# In order for the code to run you should add your own api key from https://min-api.cryptocompare.com
from crypto_to_euro.inputDict import crypto
import requests

url = "https://min-api.cryptocompare.com/data/price?fsym=" + crypto["name"] + "&tsyms=EUR&api_key=" + API_KEY
try:
    response = requests.get(url)
    euroPrice = response.json()
    print(float(euroPrice["EUR"]) * float(crypto["quantity"]), "€")
except:
  print("Request returned an error.")

 
   