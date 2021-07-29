import requests # url library 대신 사용
from bs4 import BeautifulSoup # 데이터 추출

LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"

def extract_indeed_pages():
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

def extract_indeed_jobs(last_page):
  jobs = []
  #for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "slider_container"}) # job 목록
  # job마다 title 찾기
  for result in results:
    # title attribute을 가지고 있는 span
    title = result.find("h2", {"class": "jobTitle"}).find("span", title=True).string 
    print(title)
  return jobs
