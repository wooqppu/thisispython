
# 파이썬 -> 이식성이 좋음
# 모듈 : 함수나 변수 또는 클래스를 모아놓은 파이썬 파일
# 표준 모듈 : 기본적으로 내장되있는 모듈 
# 외부 모듈 : 다른 사람이 만들어서 공개한 모듈

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__=="__main__":
    print(add(1,4))
    print(sub(4,2))