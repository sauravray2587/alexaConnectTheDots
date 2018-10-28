from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(15)
url = "https://www.sixdegreesofwikipedia.com/?source=Tanushree%20Dutta&target=Nana%20Patekar"
driver.get(url)

button = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/button')
button.click()
driver.implicitly_wait(15)
element=driver.find_element_by_xpath('//*[@class="sc-htoDjs bYbIip"]')

degreePath=driver.find_element_by_xpath('//*[@class="sc-jKJlTe fChiJW"]')
degree=(degreePath.text).split('\n')[-1].split(' ')[4]
degree=int(degree)+1
text_list=(element.text).split('\n')
pathListOfList=[]
tempList=[]
for iter, word in enumerate(text_list):
    if (1+iter)%(2*degree)==0:
        pathListOfList.append(tempList)
        tempList=[]
    if iter%2==1:
        continue
    tempList.append(word)

print(pathListOfList)
