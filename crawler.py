from bs4 import BeautifulSoup # html parsing
import urllib.request # HTTP request, response


# 출력 파일 명
OUTPUT_FILE_NAME = 'output.txt'
# 긁어 올 URL
URL = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=055'\
      '&aid=0000445667'
 
 
# 크롤링 함수
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    return text
 
 
# 메인 함수
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w')
    result_text = get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()
    
 
if __name__ == '__main__':
    main()


### 출처: http://yoonpunk.tistory.com/4 [윤빵꾸의 공부노트]