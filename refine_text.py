import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--in_file', default='output.txt')
parser.add_argument('--out_file', default=None)
args = parser.parse_args()

# 입,출력 파일명
INPUT_FILE_NAME = args.in_file #'output.txt'
if args.out_file == None:
    OUTPUT_FILE_NAME = '%s_cleand.txt'%INPUT_FILE_NAME.split('.')[0]
else:
    OUTPUT_FILE_NAME = args.out_file
 
# 클리닝 함수
def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', cleaned_text)
    return cleaned_text
    
 
# 메인 함수
def main():
    read_file = open(INPUT_FILE_NAME, 'r')
    write_file = open(OUTPUT_FILE_NAME, 'w')
    text = read_file.read()
    text = clean_text(text)
    write_file.write(text)
    read_file.close()
    write_file.close()
 
 
if __name__ == "__main__":
    main()


### 출처: http://yoonpunk.tistory.com/4 [윤빵꾸의 공부노트]