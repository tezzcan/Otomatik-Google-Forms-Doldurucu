import random
import time
from selenium import webdriver

GONDERIM_SAYISI = 10 # Kaç tane form girilecek?
URL = r"https://docs.google.com/forms/d/e/1FAIpQLScrrnMxrFtCBOcBrSfq5C__pe__w-MKj9Xg6LF0WC9Pbdh09Q/viewform"
# Tabiki girilecek formun adresi lazım :)

driver = webdriver.Chrome()
driver.get(URL)
time.sleep(1)

tekilSecenekler = [
    [0,1,2],
    [3,4,5,6],
    [7,8,9,10,11],
    [12,13],
    [14,15],
    [16,17],
    [18,19],
    [20,21],
    [22,23],
    [24,25],
    [26,27]
] #tekil secenekten ne kastettiğimi readmeye koydum.

cogulSecenekler = [
    [0,1,2,3,4,5],
    [6,7,8,9,10,11],
    [12,13,14,15,16,17],
    [18,19,20,21,22,23],
    [24,25,26,27,28,29],
    [30,31,32,33,34,35],
    [36,37,38,39,40,41],
    [42,43,44,45,46,47],
    [48,49,50,51,52,53],
    [54,55,56,57,58,59],
    [60,61,62,63,64,65],
    [66,67,68,69,70,71],
    [72,73,74,75,76,77],
    [78,79,80,81,82,83],
    [84,85,86,87,88,89],
    [90,91,92,93,94,95],
    [96,97,98,99,100,101],
    [102,103,104,105,106,107],
    [108,109,110,111,112,113],
    [114,115,116,117,118,119]
] #bunu da koydum.

def formuDoldur():
    cogulButonlar = driver.find_elements_by_xpath("//*[@class='appsMaterialWizToggleRadiogroupElContainer exportContainerEl  freebirdThemedRadio freebirdThemedRadioDarkerDisabled']")
    for i in range(len(cogulSecenekler)):
        cogulButonlar[random.choice(cogulSecenekler[i])].click()
    
    # Önce çoğul butonları buluyoruz
    # Kaç tane çoğul seçenek yapabileceğim INPUT ALANI varsa her biri için
    # o anki seçenekler arasından random seçim alıp tıklıyoruz.
    
    tekilButonlar = driver.find_elements_by_xpath("//*[@class='freebirdFormviewerViewItemsRadioOptionContainer']")
    for i in range(len(tekilSecenekler)):
        tekilButonlar[random.choice(tekilSecenekler[i])].click() 
    
    # Aynısı tekil butonlar için geçerli.
    
    gonder = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div/div/div')
    gonder.click()
    # Gönder butonunu bulup basıyoruz.
    
    driver.execute_script("window.history.go(-1)")
    # Aynı işlemi tekrarlaması için geri geliyoruz.

sayac = 0
while GONDERIM_SAYISI != sayac:
    formuDoldur()
    sayac += 1
    time.sleep(0.75)

print(f'Belirtilen adrese {sayac} kayıt eklendi.')