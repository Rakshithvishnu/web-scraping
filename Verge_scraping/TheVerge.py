from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.theverge.com/"
page = requests.get(url)
htmlContent = page.content

soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup)

lists = soup.find_all('li', class_="duet--content-cards--content-card")

with open('14042023_verge.csv', 'w', encoding='utf8', newline="") as file:
    #writer is going to write csv file
    thewriter = writer(file)

    #writing  heading row
    header = ['id', 'URL', 'headline', 'author', 'date']
    thewriter.writerow(header)

    #looping through lists to find id, url, headline, author and date
    for details in lists:
        Id = details.find('div', class_="z-10").text
        url  = details.find('a', class_="group-hover:shadow-underline-franklin")['href']
        title = details.find('a', class_="group-hover:shadow-underline-franklin").text
        author = details.find('a', class_="text-gray-31").text
        date = details.find('span', class_="text-gray-63").text
        info = [Id, url, title, author, date]
        #print(info)
        #writing info list to csv file (verge.csv)
        thewriter.writerow(info)
        
