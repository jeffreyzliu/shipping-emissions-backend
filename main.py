from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/shipment/<id>' , methods=['GET'])
def info(id):
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  return jsonify({"destination":"DURHAM, NC US","origin":"Compton, CA US"})

  driver = webdriver.Chrome(options=chrome_options)
  driver.implicitly_wait(10)
  driver.get("https://www.fedex.com/apps/fedextrack/?action=track&trackingnumber=" + str(id) + "&cntry_code=ca&locale=en_CA#")
  time.sleep(5)

  html = driver.page_source

  html = html.split('"redesignAddressDisplayTVC tank-text addressSection light tank-text-flat tank-text-center address_cscp"')

  temp = html[1]

  from_address = temp.split("<", 1)[0][1:]

  temp = html[2]

  to_address = temp.split("<", 1)[0][1:]

  html = driver.page_source

  html = html.split('<span class="shipmentFactsRowTVC value tank-ship-facts__item-description">')
  weight = None
  for x in html:
    if "lbs" in x:
      weight = x.split()[0]
  try:
    weight = float(weight)
  except ValueError:
    weight = 1.0
  print({
    "origin": from_address,
    "destination": to_address,
    "weight": weight
  })
  return jsonify({
    "origin": from_address,
    "destination": to_address,
    "weight": weight
  })

app.run(host='0.0.0.0', port=8080)



