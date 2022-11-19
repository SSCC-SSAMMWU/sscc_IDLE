# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote
import json

CLIENT_ID = 'b7R84pPNshlnGmqooyXy'
CLIENT_SECRET = '2R5LNaDZEt'


def search_book(query):
    request = Request('https://openapi.naver.com/v1/search/book.json?query=' + quote(query))
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)
    response = urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        return json.loads(response_body.decode('utf-8'), strict=False)
    return None



# {
# 	"lastBuildDate":"Sun, 06 Nov 2022 22:24:12 +0900",
# 	"total":1,
# 	"start":1,
# 	"display":1,
# 	"items":[
# 		{
# 			"title":"라플라스의 마녀 (히가시노 게이고 장편소설)",
# 			"link":"https:\/\/search.shopping.naver.com\/book\/catalog\/32455547685",
# 			"image":"https:\/\/shopping-phinf.pstatic.net\/main_3245554\/32455547685.20221019143256.jpg",
# 			"author":"히가시노게이고",
# 			"discount":"13320",
# 			"publisher":"현대문학",
# 			"pubdate":"20160111",
# 			"isbn":"9788972757573",
# 			"description":"인류의 미지의 영역에 도전한 히가시노 게이고의 80번째 작품!\n\n히가시노 게이고 작가 데뷔 30주년 기념작 『라플라스의 마녀』. 그동안 치밀한 트릭과 반전이 빛나는 본격 추리소설부터 우리 시대의 문제점을 파고든 사회파 작품, 서스펜스, 판타지, SF에 이르기까지 다양한 장르를 오가며 미스터리의 경계를 넓혀온 히가시노 게이고, 30년 미스터리를 모조리 담은 작품이다.\n\n두 개의 죽음과 연관된 8년 전의 사고에 대한 열쇠를 쥐고 있는 한 소녀의 이야기를 담고 있는 이번 소설은 나비에 스토크스 방정식과 라플라스 이론 등 물리학, 수리학의 난제들과 함께 뇌의학의 세계, SF적 상상력 그리고 황화수소를 이용한 교묘한 범죄에 얽힌 주인공들의 가족사와 그들의 사랑과 복수를 그리고 있다. \n\n돌연한 토네이도에 휩쓸려 한순간에 엄마를 잃은 마도카. 그날 뇌의학계의 권위자인 아버지 우하라 박사는 한 소년의 수술 일정이 잡혀 재난을 피한다. 그로부터 8년 뒤, 마도카의 경호를 맡게 된 전직 경찰 다케오는 그녀가 미래를 예측하는 듯한 일들을 접하면서 마도카에게 어떤 신비한 '능력'이 있다고 느낀다. \n\n그 무렵, D현의 온천지에서 황화수소 중독으로 육십 대의 영화 프로듀서가 사망하고 또 다른 온천지에서도 유사한 양상의 황화수소 중독 사망 사고가 일어난다. 원인 규명에 나선 지구화학 전문가 아오에 교수는 불가사의한 현상을 해명하는 데 어려움을 겪던 중, 두 현장에서 누군가를 찾고 있는 마도카와 마주치는데……."
# 		}
# 	]
# }




def test():
    tmp = """
        {
        "lastBuildDate": "Sun, 06 Nov 2022 22:30:40 +0900",
        "total": 1,
        "start": 1,
        "display": 1,
        "items": [
            {
                "title": "혼자 공부하는 SQL (1:1 과외하듯 배우는 데이터베이스 자습서)",
                "link": "https:\/\/search.shopping.naver.com\/book\/catalog\/32477674953",
                "image": "https:\/\/shopping-phinf.pstatic.net\/main_3247767\/32477674953.20221019143351.jpg",
                "author": "우재남",
                "discount": "21600",
                "publisher": "한빛미디어",
                "pubdate": "20211101",
                "isbn": "9791162244739",
                "description": "혼자 해도 충분하다! \n1:1 과외하듯 배우는 데이터베이스 자습서(MySQL Community 8.0 지원)\n이 책은 아무런 사전 지식 없는 입문자가 ‘꼭 필요한 내용을 제대로’ 학습할 수 있도록 구성했다. ‘무엇을’, ‘어떻게’ 학습해야 할지조차 모르는 입문자의 막연한 마음을 살펴, 과외 선생님이 알려주듯 친절하게, 그러나 핵심적인 내용만 콕콕 집어준다. 책의 첫 페이지를 펼쳐서 마지막 페이지를 덮을 때까지, 혼자서도 충분히 SQL을 배울 수 있다는 자신감과 확신이 계속될 것이다!\n\n28명의 베타리더 검증으로, ‘함께 만든’ 입문자 맞춤형 도서\n베타리딩 과정을 통해 입문자에게 적절한 난이도, 분량, 학습 요소 등을 고민하고 적극 반영했다. 어려운 용어와 개념은 한번 더 풀어 쓰고, 복잡한 설명은 눈에 잘 들어오는 그림으로 풀어 냈다. ‘혼자 공부해본’ 여러 입문자의 마음과 눈높이가 책 곳곳에 반영된 것이 이 책의 가장 큰 장점이다.\n\n누구를 위한 책인가요?\nㆍ\tSQL을 처음 시작하려고 하는 학생, 취업 준비생\nㆍ\t데이터베이스 기초를 배우고자 하는 초보 개발자\nㆍ\tSQL의 이론과 실습을 동시에 학습하고 싶은 입문자\nㆍ\tSQL을 공부하다가 너무 어려워서 포기한 경험이 있는 입문자\nㆍ\t실무에서 SQL 관련 업무를 해야 하는 주니어 개발자"
            }
        ]
    }"""
    return json.loads(tmp, strict=False)



with open("books.txt", "r", encoding="utf-8") as fh:
    books = fh.readlines()

for book in books:
    try:
        items = search_book(book)['items'][0]

        print(items['isbn'], end='\t')
        print(items['title'], end='\t')
        print(items['author'], end='\t')
        print(items['publisher'], end='\t')
        print()
    except:
        print(book + "error")
    # break
    # print()
