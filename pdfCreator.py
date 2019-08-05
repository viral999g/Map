import requests, time, pymongo
from bs4 import BeautifulSoup
from selenium import webdriver

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']


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

    # print(html_source)


    # # data = requests.get('http://13.59.213.80/ballarpur/village_data.html?location_id=29').text
    soup = BeautifulSoup(html_source)

    div_can = str(soup.find('div')).replace('"canvas"', '"canvas' + '-' + str(i) + '"')
    script_tag = soup.find_all('script')[-1]
    # print(script_tag[-1])
    # div_can = soup.find('body')

    tables = soup.find_all('table')
    tables.insert(4, div_can)
    for t in tables:
      file.write(str(t))

    # file.write('</body>')
    # file.write(str(script_tag).replace('&gt;', '>'))


  except:
    pass

for i in range(1, 154):

  lineChartData = {
    labels: ['2014 LS', '2014 VS', '2019 LS'],
    datasets: [{
      label: 'BJP',
      borderColor: '#ff9933',
      backgroundColor: '#ff9933',
      fill: false,
      data: [],
      yAxisID: 'y-axis-1',
    }, {
      label: 'INC',
      borderColor: '#0000ff',
      backgroundColor: '#0000ff',
      fill: false,
      data: [],
      yAxisID: 'y-axis-1'
    },
    {
      label: 'Others',
      borderColor: '#ffff00',
      backgroundColor: '#ffff00',
      fill: false,
      data: [],
      yAxisID: 'y-axis-1'
    }]
  }

  bjp_ls_14 = 0
  bjp_vs_14 = 0
  bjp_ls_19 = 0

  inc_ls_14 = 0
  inc_vs_14 = 0
  inc_ls_19 = 0

  others_ls_14 = 0
  others_vs_14 = 0
  others_ls_19 = 0

  bjp_data = []
  inc_data = []
  others_data = []

  data = VILLAGESCOLL.find_one({"location_id": str(i)})

  ls_2019 = data['election_2019']



