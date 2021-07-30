import requests # url library 대신 사용
from bs4 import BeautifulSoup # 데이터 추출

LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "pagination"})

  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))

  # print(pages[:-1]) # 마지막에서 첫번째 아이템 제외
  # print(pages[0:-1]) # 위와 같음
  # print(pages[0:4]) # 0부터 4개 아이템

  max_page = pages[-1]
  return max_page

def extract_job(html):
  # title attribute을 가지고 있는 span
  title = html.find("h2", {"class": "jobTitle"}).find("span", title=True).string 
  company = html.find("span", {"class": "companyName"}).string
  location = html.select_one("pre > div").text
  job_id = html.parent["data-jk"]
  '''
  company_anchor = company.find("a")
  if  is not None:
   print(company_anchor.string)
  else:
   print(company.string)
  '''
  return {'title': title, 'company': company, 'location': location, 'link': f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"}


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping indeed: Page: {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "slider_container"}) # job 목록
    # job마다 title 찾기
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  # 최대 페이지 구하기
  last_page = get_last_page()
  # 페이지당 일목록 가져오기
  jobs = extract_jobs(last_page)
  return jobs