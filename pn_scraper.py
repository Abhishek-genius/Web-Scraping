from bs4 import BeautifulSoup
import requests
from csv import writer
import io
from requests.api import head





#by using  loop and cobditional statment we print from 1 to 10 page by default it print NULL
page_number = input("enter page number")
for i in range(1,int(page_number)+1): #in all pages some url are same and some url diffrent url can achived by for loop
   if(i<11):
      url = "https://www.ndtv.com/india/page-"+str(i) #this url use for diffrent pages  
   else: "NULL"
   
Page1 = requests.get(url) #here we retrive the content from webpage according to url
soup = BeautifulSoup(Page1.content,'html.parser')  #here we parse the html contenet
lists=soup.find_all("div",class_="news_Itm-cont")  #here retrive all the item of class news_Itm-cont

with open('output.csv','w',encoding='utf8',newline='') as f: #use to open csv file 
   thewriter=writer(f)
   header = ['headline','paragraph','source'] #here we assign attribut of table
   thewriter.writerow(header)
   for list in lists:  #this for use for retrive information from block
         headline=list.find('h2').text   #headline is to display headline of blocks
         paragraph=list.find('p',class_='newsCont').text  #paragraph is used for dislay paragraph
         source =list.find('span',class_='posted-by').text #source is use to display source/auther of news
         print(headline,paragraph,source)
         data=[headline,paragraph,source] #creat list of data element
         thewriter.writerow(data)  #IT ADD data in new row 
f.closed  #use to close csv file 


