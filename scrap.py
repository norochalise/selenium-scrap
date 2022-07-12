from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd


web = "https://weworkremotely.com/top-remote-companies"
path = "/home/noro/Desktop/we_work_remotely/chromedriver"


# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)



# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="jobs-container"]/li')


company_names = []
job_counts = []
company_descriptions = []
links = []



for container in containers:
    company_name = container.find_element(by='xpath', value='./a/span[@class="company"]').text
    job_count = container.find_element(by='xpath', value='./a/span[@class="job-count"]').text
    company_description = container.find_element(by='xpath', value='./a/span[@class="company-title"]').text
    link = container.find_element(by='xpath', value='./div[@class="tooltip"]/a/').get_attribute('href')
    

    company_names.append(company_name)
    job_counts.append(job_count)
    company_descriptions.append(company_description)
    links.append(link)



company_dict = {
    'company_name': company_names, 
    'job_count': job_counts, 
    'company_description':company_descriptions, 
    'link': links}


df = pd.DataFrame(company_dict)
df.to_csv('100_remote_job_company.csv')
driver.quit()



# # //div[@class="jobs-container"]//li/a//span[@class='company']
# # //div[@class="jobs-container"]//li/a//span[@class='company-title']
# # //div[@class="jobs-container"]//li/a//span[@class='job-count']
# # //div[@class="jobs-container"]//li//div[@class="tooltip"]//a








