from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import urllib.request
def desease_info():
    driver = webdriver.Chrome(r'/home/bharath/Desktop/Assignment/chromedriver')
    driver.get('https://dermnetnz.org/image-library/')
    container = driver.find_elements(By.XPATH,'//a[@class="imageList__group__item"]')
    df = pd.DataFrame({
        'Disease_Name':[],
        'URL_assosiated_with_disease':[],
        'image_url':[]
    })
    for info in container:
        dict_info = {
            'Disease_Name':info.find_element(By.XPATH,'.//div[2]').text.strip(),
            'URL_assosiated_with_disease' :info.get_attribute("href").strip(),
            'image_url':info.find_element(By.XPATH,'.//div/img').get_attribute("src").strip()     
        }
        df = df.append(dict_info, ignore_index=True)
        Disease_Name=info.find_element(By.XPATH,'.//div[2]').text.strip()
        image_url=info.find_element(By.XPATH,'.//div/img').get_attribute("src").strip()
        try:
            response = requests.get(image_url)  
        except:
            print('Error')    
        else:
            if response.status_code == 200:
                with open(r'/home/bharath/Desktop/Assignment/image_folder/'+str(Disease_Name)+'.jpg', 'wb') as f:
                    f.write(response.content)
    return df

df = desease_info()
df.to_csv('df.csv',index = False)
