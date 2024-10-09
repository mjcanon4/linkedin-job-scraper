from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# soup = BeautifulSoup(html_content, 'html.parser')

username = 'michaeljamescanon@gmail.com'
password = 'Purple104'

driver.get('https://www.linkedin.com/login')
time.sleep(2)


# Handle login using credentials
username_field = driver.find_element(By.ID, 'username')
username_field.send_keys(username)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
time.sleep(5)


# def find_jobs():
#     job_listings = soup.find_all('div', class_='job-listing')
#     for job in job_listings:
#         title = job.find('h2', class_='job-title').get_text()
#         company = job.find('span', class_='company').get_text()
#         location = job.find('span', class_='location').get_text()
#         print(f"Title: {title}")
#         print(f"Company: {company}")
#         print(f"Location: {location}")
#         print("---")
