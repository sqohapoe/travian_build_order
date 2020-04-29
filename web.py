from requests import Session
from bs4 import BeautifulSoup


village_id = [70724, 72719, 75306, 77045, 77869, 78462, 79007, 79572]

with Session() as s:
    site = s.get(r"https://ts1.travian.com/login.php")
    login_data = {"name":["formosa"], "password":["polytechnique"]}
    s.post(r"https://ts1.travian.com/login.php", data=login_data)
    for i in range(len(village_id)):
        s.get(r'https://ts1.travian.com/dorf1.php?newdid={}&'.format(village_id[i])) # go to tainan
        home_page = s.get(r"https://ts1.travian.com/dorf1.php")
        bs = BeautifulSoup(home_page.text, "html.parser")
        lumber = bs.find(id='l1').contents[0]
        clay = bs.find(id='l2').contents[0]
        iron = bs.find(id='l3').contents[0]
        crop = bs.find(id='l4').contents[0]
        print("village number ", i+1)
        print(lumber, clay, iron, crop)