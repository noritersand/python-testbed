from bs4 import BeautifulSoup

page_source = '<div class=:selectScroll"> <div class ="wrap"> <div class ="box" id ="option_all_view_area"> <a class = "optionLine" name ="opt_select" optprdno="7042309496"> <div class ="number">1</div> <div class ="option" name="opt_veiw_all_name_area">225</div></a> <a class = "optionLine" name ="opt_select" optprdno="7042309496"> <div class ="number">2</div> <div class ="option" name="opt_veiw_all_name_area">230</div></a> <a class = "optionLine" name ="opt_select" optprdno="7042309496"> <div class ="number">3</div> <div class ="option" name="opt_veiw_all_name_area">235</div></a> <a class = "optionLine" name ="opt_select" optprdno="7042309496"> <div class ="number">4</div> <div class ="option" name="opt_veiw_all_name_area">240</div></a> </div> </div> </div>'

soup = BeautifulSoup(page_source, "html.parser")
optionLines = soup.find_all('a', class_='optionLine');

##print(optionLines)
##print(type (optionLines))
##optionLines.find_all('div') # ResultSet 타입은 find_all() 메서드가 없다.

resultArr = []
for ele in optionLines:
##    ele.find_all('div')
##    print(type (ele))
    resultArr.append(ele.find('div', class_='option').text)

print(resultArr) # ['225', '230', '235', '240']
