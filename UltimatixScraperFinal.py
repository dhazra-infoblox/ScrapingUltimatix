import mechanize
from BeautifulSoup import BeautifulSoup
import csv

br = mechanize.Browser()	
my_url = 'https://ghd.ultimatix.net/ehelp/changemgmt/wfchnghistory.aspx'
br.open(my_url)

formcount=0
for frm in br.forms():  
  if str(frm.attrs["name"])=="loginForm":
    break
  formcount=formcount+1

br.select_form(nr=formcount)
br.form['USER'] = '1355885'
br.form['PASSWORD'] = 'Chayan#107'
br.submit()

response = br.open(my_url).read()
page_soup = BeautifulSoup(response)
containers = page_soup.findAll("tr", {"class": "dtgAlternatingItemStyle"})
container2 = page_soup.findAll("span", {"id": "ucPageHeader1_lblWelcome"})

for row in containers:
	row_td = row.findAll('td')

arr = ["" for x in range(int(len(row_td)))]
for i in range(int(len(row_td))):
	if(row_td[i].text):
		arr[i] = row_td[i].text

arr = filter(None, arr)
with open('ticket.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(arr)

print(container2[0].text)
print("CSV file generated!")
csvFile.close()	