# web-scraping
web scraping using python and run on aws ec2 cloud server


#Run this command, if necessary, to ensure your key is not publicly viewable:

 chmod 400 python-web-server.pem

#Connect to your instance using its Public DNS:
 ssh -i "python-web-server.pem" ec2-user@ec2-18-182-65-81.ap-northeast-1.compute.amazonaws.com

#to run the file:
python3 TheVerge.py

#Libraries included:
BeautifulSoup4
Requests
Pandas
sqlite3

#Github link:
https://github.com/Rakshithvishnu/web-scraping
