import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver


file = open('full.html', 'a')

options = webdriver.ChromeOptions()
options.add_argument('--headless')


driver = webdriver.Chrome(options=options)

for i in range(1, 154):
  print(i)

  try:
    driver.get('http://13.59.213.80/ballarpur/village_data.html?location_id=' + str(i))

    time.sleep(3)

    html_source = driver.page_source


    # data = requests.get('http://13.59.213.80/ballarpur/village_data.html?location_id=29').text
    soup = BeautifulSoup(html_source)

    tables = soup.find_all('table')
    for t in tables:
      file.write(str(t))
  except:
    pass

