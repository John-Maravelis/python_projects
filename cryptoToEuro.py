# Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα λεξικό από αρχείο το οποίο περιέχει τα κρυπτονομίσματα (όνομα) που έχει 
# ένας χρήστης και πόσα από αυτά. Χρησιμοποιείστε το API https://min-api.cryptocompare.com για να βρείτε σε τι ποσό σε ευρώ αντιστοιχούν.
 
# In order for the code to run you should add your own api key from https://min-api.cryptocompare.com
import requests
import os 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')

# specify the name and quantity of crypto you want to calculate
crypto = {
    "name" : "BTC",
    "quantity" : "1000" 
}

url = "https://min-api.cryptocompare.com/data/price?fsym=" + crypto["name"] + "&tsyms=EUR&api_key=" + API_KEY
try:
    response = requests.get(url)
    euroPrice = response.json()
    print(float(euroPrice["EUR"]) * float(crypto["quantity"]), "€")
except:
  print("Request returned an error.")

 
   