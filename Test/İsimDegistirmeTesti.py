from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#SELENIUM'un webdriver özelliğini Chrome Tarayıcısında kullanmak için driver adında bir belirteç kullanacağız ve bunu kullanacağız.

driver = webdriver.Chrome("D:\pyProject\SeleniumTest\drivers\chromedriver.exe")
driver.set_page_load_timeout(2)

#Gideceğimiz Sayfayı belirtiyoruz...

driver.get("http://www.unclesoftware.com/")
time.sleep(1)
driver.maximize_window() #Sayfamızı büyütelim...

#find_element... lar ile sayfanın html dizaynı üzerinde gezinerek seçimler yapıyoruz.Burada ana sayfadan giriş yapma kısmına geliyoruz...
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul/li[2]/a").click()
time.sleep(1)

#Adı emailorname olan içeriğe e posta adresini send ediyoruz.
driver.find_element_by_name("emailorname").send_keys("o.gul1907@hotmail.com")
time.sleep(2)
#password içeriğine şifremizi gönderiyoruz...
driver.find_element_by_name("password").send_keys("111222333444")
time.sleep(1)
#Oturumu açmak için giriş butonuna basmamızı sağlayan xpath yolu
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/form/div[3]/a").click()
time.sleep(1)

#Kullanıcı profil simgesi
driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[7]/a").click()
time.sleep(1)

#Profile gitme indexi...
driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[7]/ul/li[1]/a").click()
time.sleep(1)

isim=driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[2]").text

driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[3]/a").click()

eskiIsim=driver.find_element_by_name("user_namesurname").clear()
eskiIsim=driver.find_element_by_name("user_namesurname").send_keys("ERDEM")

driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/div[2]/table/tbody/tr[6]/td/button").click()
print("*******************************************")
print("TEST ADI : İSİM DEĞİŞTİRME")

if isim == eskiIsim:
    print("BAŞARISIZ")
else:
    print("Başarılı")
