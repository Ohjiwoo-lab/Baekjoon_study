from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize==0:
        answer=5*len(cities)
    else:
        q=deque([])
        for city in cities:
            city=city.lower()  # 도시 이름을 전부 소문자로 변경
            
            # 캐시에 값이 뭐라도 있는 경우
            if q:
                if city in q:
                    answer+=1
                    q.remove(city)
                    q.append(city)
                elif len(q)>=cacheSize:
                    answer+=5
                    q.popleft()
                    q.append(city)
                else:
                    answer+=5
                    q.append(city)

            # 캐시에 아무런 값이 없는 경우 -> miss
            else:
                answer+=5
                q.append(city)

    return answer
