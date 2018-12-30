from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


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

#FOOTER ALANINDA BULUNAN HAKKIMIZDA,ÇEREZLER VE KOŞULLAR SAYFALARI
# AYRICA BODY KISMINDA YER ALAN SORU-CEVAP VE EĞİTİM SAYFALARININ AÇILMAMASI SORUNU

print(driver.title)
print("Tıklanmadan önceki hali",driver.current_url)

simdikiSayfa = driver.current_url

#Hakkımızda sayfasına tıklamamızı sağlayalım ve url kısmının değişip değişmediğine bakalım...

page=driver.find_element_by_tag_name("html")
page.send_keys(Keys.END) #SCROLL aşağı insin ve tıklamayı görelim...
time.sleep(3)

driver.find_element_by_xpath("/html/body/footer/div/nav/ul/li[2]/a")

# Linke tıkladıktan sonra normalde URL kısmının değişmesi ve hakkımızda sayfasına yönlendirmesi gerekiyor...
#Kontrolünü yaptıralım...

HakkimizdayaGittiMi =driver.current_url
print("TIKLANDIKTAN SONRAKİ HALİ",HakkimizdayaGittiMi)

driver.close()

if simdikiSayfa == HakkimizdayaGittiMi:
    print("HAKKIMIZDA SAYFASI AÇILMADI...DURUM : BAŞARISIZ..")
else:
    print("Hakkımızda sayfasi acildi")
