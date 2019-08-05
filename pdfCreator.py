import requests, time, pymongo
from bs4 import BeautifulSoup
from selenium import webdriver

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']


file = open('full2.html', 'a')

options = webdriver.ChromeOptions()
options.add_argument('--headless')


driver = webdriver.Chrome(options=options)

for i in range(1, 154):
  print(i)

  try:
    driver.get('http://localhost/map/village_data.html?location_id=' + str(i))

    time.sleep(3)

    html_source = driver.page_source

    # print(html_source)


    # # data = requests.get('http://localhost/map/village_data.html?location_id=29').text
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

# for i in range(1, 2):

#   try:

#     bjp_ls_14 = 0
#     bjp_vs_14 = 0
#     bjp_ls_19 = 0

#     inc_ls_14 = 0
#     inc_vs_14 = 0
#     inc_ls_19 = 0

#     others_ls_14 = 0
#     others_vs_14 = 0
#     others_ls_19 = 0

#     bjp_data = []
#     inc_data = []
#     others_data = []

#     data = VILLAGESCOLL.find_one({"location_id": str(i)})


#     ls_2019 = data['election_2019']['votes_data']
#     ls_2014 = data['ls_2014']['votes_data']
#     vs_2014 = data['vs_2014']['votes_data']

#     for d in ls_2014:
#       if d['party'] == 'BJP':
#         bjp_ls_14 += int(d['votes_per'].replace('%', ''))
#       elif d['party'] == 'INC':
#         inc_ls_14 += int(d['votes_per'].replace('%', ''))
#       else:
#         others_ls_14 += int(d['votes_per'].replace('%', ''))

#     for d in vs_2014:
#       if d['party'] == 'BJP':
#         bjp_vs_14 += int(d['votes_per'].replace('%', ''))
#       elif d['party'] == 'INC':
#         inc_vs_14 += int(d['votes_per'].replace('%', ''))
#       else:
#         others_vs_14 += int(d['votes_per'].replace('%', ''))
    
#     for d in ls_2019:
#       if d['party'] == 'BJP':
#         bjp_ls_19 += int(d['votes_per'].replace('%', ''))
#       elif d['party'] == 'INC':
#         inc_ls_19 += int(d['votes_per'].replace('%', ''))
#       else:
#         others_ls_19 += int(d['votes_per'].replace('%', ''))


#     bjp_data = [bjp_ls_14, bjp_vs_14, bjp_ls_19]
#     inc_data = [inc_ls_14, inc_vs_14, inc_ls_19]
#     others_data = [others_ls_14, others_vs_14, others_ls_19]


#     lineChartData = '''
#     <script>
#     var lineChartData = {
#       labels: ['2014 LS', '2014 VS', '2019 LS'],
#       datasets: [{
#         label: 'BJP',
#         borderColor: '#ff9933',
#         backgroundColor: '#ff9933',
#         fill: false,
#         data: ''' + str(bjp_data) + ''',
#         yAxisID: 'y-axis-1',
#       }, {
#         label: 'INC',
#         borderColor: '#0000ff',
#         backgroundColor: '#0000ff',
#         fill: false,
#         data: ''' + str(inc_data) + ''',
#         yAxisID: 'y-axis-1'
#       },
#       {
#         label: 'Others',
#         borderColor: '#ffff00',
#         backgroundColor: '#ffff00',
#         fill: false,
#         data: ''' + str(others_data) + ''',
#         yAxisID: 'y-axis-1'
#       }]
#     }; \n'''

#     showchart_func = '''function showChart() {
#               var ctx = document.getElementById('canvas-''' + str(i)  + '''').getContext('2d');
#               ctx.height = 400;
#         window.myLine = Chart.Line(ctx, {
#           data: lineChartData,
#           options: {
#                       responsive: true,
#                       maintainAspectRatio: false,
#             hoverMode: 'index',
#             stacked: false,
#             title: {
#               display: true,
#               text: 'Voting Trends'
#             },
#             scales: {
#               yAxes: [{
#                 type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
#                 display: true,
#                 position: 'left',
#                               id: 'y-axis-1',
#                               ticks: {
#                                   callback: function(value, index, values) {
#                                       return value + '%';
#                                   }
#                               }
#               }],
#                       },
#                       tooltips: {
#                           callbacks: {
#                               label: function(tooltipItem, data) {
#                                   return ' ' + data.datasets[tooltipItem.datasetIndex].label + ' : ' + tooltipItem.yLabel + '%'
#                               }
#                           }
#                       },
#                         elements: {
#                         line: {
#                             tension: 0
#                         }
#                     }
#           }
#         });
#           };

#         showChart();
#         </script>
#         '''


#     file.write(lineChartData + showchart_func)
#   except:
#     pass





