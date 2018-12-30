from selenium import webdriver
import time


#SELENIUM'un webdriver özelliğini Chrome Tarayıcısında kullanmak için driver adında bir belirteç kullanacağız ve bunu kullanacağız.

driver = webdriver.Chrome("D:\pyProject\SeleniumTest\drivers\chromedriver.exe")
driver.set_page_load_timeout(2)

#Gideceğimiz Sayfayı belirtiyoruz...

driver.get("http://www.unclesoftware.com/")
time.sleep(2)

#find_element... lar ile sayfanın html dizaynı üzerinde gezinerek seçimler yapıyoruz.Burada ana sayfadan giriş yapma kısmına geliyoruz...
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul/li[2]/a").click()
time.sleep(2)

driver.maximize_window() #Sayfamızı büyütelim...


#Adı emailorname olan içeriğe e posta adresini send ediyoruz.
driver.find_element_by_name("emailorname").send_keys("o.gul1907@hotmail.com")
time.sleep(2)
#password içeriğine şifremizi gönderiyoruz...
driver.find_element_by_name("password").send_keys("111222333444")
time.sleep(2)
#Oturumu açmak için giriş butonuna basmamızı sağlayan xpath yolu
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/form/div[3]/a").click()
time.sleep(2)

#Profile gitmek için profil simgesine tıklayalım...
driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[7]/a").click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[7]/ul/li[1]/a").click()
time.sleep(2)


driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[1]/div[1]/a/button/i").click()

driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/div[2]/div/input").send_keys("D://pyProject/SeleniumTest/1-min.jpeg")


#Resim küçültmeye tıklıyoruz arka arkaya
driver.find_element_by_xpath("//*[@id='btnZoomOut']/i").click()
driver.find_element_by_xpath("//*[@id='btnZoomOut']/i").click()
driver.find_element_by_xpath("//*[@id='btnZoomOut']/i").click()
driver.find_element_by_xpath("//*[@id='btnZoomOut']/i").click()
driver.find_element_by_xpath("//*[@id='btnZoomOut']/i").click()
driver.find_element_by_xpath("//*[@id='btnZoomOut']/i").click()


driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/div[2]/button[3]").click()
time.sleep(25)
driver.quit()
assert("TEST TAMAMLANDI")

print("*****************")
print("TEST ADI : FOTOĞRAF EKLEME ")
print("Başarılı")
