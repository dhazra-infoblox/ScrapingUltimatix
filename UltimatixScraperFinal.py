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
br.form['USER'] = 'username'
br.form['PASSWORD'] = 'password'
br.submit()

response = br.open(my_url).read()
page_soup = BeautifulSoup(response)
containers = page_soup.findAll("tr", {"class": "dtgItemStyle"})
container1 = page_soup.findAll("tr", {"class": "dtgAlternatingItemStyle"})
container2 = page_soup.findAll("span", {"id": "ucPageHeader1_lblWelcome"})

row_td = ["" for x in range(2*int(len(containers)))]
for row in range(int(len(containers))):
	row_td[row] = containers[row].findAll('td')
	row_td[row+2] = container1[row].findAll('td')

with open('ticket3.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	for i in range(int(len(row_td))):
		arr = [""]
		for j in row_td[i]:
			arr.append(j.text)
			arr = filter(None, arr)
		writer.writerow(arr)	

print(container2[0].text)
print("CSV file generated!")
csvFile.close()	
