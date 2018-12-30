from selenium import webdriver
#from selenium.webdriver.common.keys import Keys ---> enter tusu ile gönderebilmek için ama kullanmıycaz...
import time

#SELENIUM'un webdriver özelliğini Chrome Tarayıcısında kullanmak için driver adında bir belirteç kullanacağız ve bunu kullanacağız.

driver = webdriver.Chrome("D:\pyProject\SeleniumTest\drivers\chromedriver.exe")
driver.set_page_load_timeout(10)

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

#Kullanıcı oturumunu sonlandırmak amacıyla tıklanan profil simgesi
driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[7]/a").click()
time.sleep(2)

#LogOut için basılan çıkış indexi...
driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[7]/ul/li[6]/a").click()
time.sleep(2)
#Tekrar profilimize ulasmaya calısalım...
profilUrl= "http://www.unclesoftware.com/profile/member/osman"
driver.get(profilUrl)
time.sleep(2)

SimdikiUrl=driver.current_url

if SimdikiUrl != profilUrl:
    print("************************************")
    print("TEST ADI : LOGOUT TESTİ ")
    print("TEST SONUCU: BAŞARILI")

else:
    print("TEST ADI : LOGOUT TESTİ ")
    print("Test sonucu: başarısız")

time.sleep(4)
driver.quit()
