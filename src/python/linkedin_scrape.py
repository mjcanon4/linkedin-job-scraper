import requests
from bs4 import BeautifulSoup
import random
import pandas as pd

title = 'Data Engineer'
location = 'Houston'
start = 0

list_url = f"https:www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={title}&location={location}&start={start}"

response = requests.get(list_url)

list_data = response.text
list_soup = BeautifulSoup(list_data, "html.parser")
page_jobs = list_soup.find_all("li")

id_list = []
# iterate thru to get list of job ids
for job in page_jobs:
    base_card_div = job.find("div", {"class": "base-card"})
    job_id = base_card_div.get("data-entity-urn").split(":")[3]
    print(job_id)
    id_list.append(job_id)

job_list = []
# Loop thru list of job IDs and get each URL
for job_id in id_list:
    job_url = f"https:linkedin.com/jobs-guest/jobs/api/JobPosting/{job_id}"

    job_response = requests.get(job_url)
    print(job_response.status_code)
    job_soup = BeautifulSoup(job_response.text, "html.parser")