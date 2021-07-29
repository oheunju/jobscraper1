from indeed import extract_indeed_pages, extract_indeed_jobs

# 최대 페이지 구하기
last_indeed_pages = extract_indeed_pages()
# 페이지당 일목록 가져오기
extract_indeed_jobs(last_indeed_pages)
