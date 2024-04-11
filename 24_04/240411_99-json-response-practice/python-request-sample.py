import requests
from pprint import pprint


response = requests.get('http://127.0.0.1:8000/api/v1/articles/')

# json을 python 타입으로 변환
result = response.json()

# print(type(result))
# pprint(result)
# pprint(result[0])
'''
1번 게시글 접근
{'content': 'Bill third easy employee outside. Cup international bring '
            'quality.\n'
            'Relate success degree. Indeed choose actually threat quite '     
            'partner friend. Important sort bring start space blood present.', 'created_at': '2015-02-23T05:35:10Z',
 'id': 1,
 'title': 'Land probably you.',
 'updated_at': '2010-08-05T01:26:46Z'}
'''
pprint(result[0].get('title'))
# 1번 게시글 제목 'Land probably you.'

# 실제로 파이썬 파일을 실행해보면 <class 'list'>라고 뜬다.
