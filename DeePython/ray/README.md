### 내가 이해한 것들
+ 병렬성
  + 여러 프로세서가 여러 프로세스를 처리하는 것
  + 논리적인 개념
  
    
+ 병행성(동시성)
  + 하나의 프로세서가 여러 프로세스들을 순차적으로 실행시킴
    + 속도가 매우 빨라서 동시에 진행되는 것 처럼 보임
  + 물리적인 개념

### 기록해야 할 것 같은 것들
병렬 처리 모델은 크게 두 가지로 나뉜다  
 + Data 병렬 처리 모델
   + 해야할 일이 N이고, 1번당 M개 씩 실행시켜야 할 때,
   + M을 증폭 시켜서 실행 회수를 최대한 줄이는 느낌
   + `한 번에 처리하는 M을 최대로 늘려 실행회수가 1이 되도록 한다.`
   + [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
   

 + Task 병렬 처리 모델
   + 해야할 일이 N이고, 1번당 M개씩 실행시켜야 할 때,
   + N을 조작해서 실행 회수를 1에 가깝게 하는 느낌?
   + `N에서 공동사항 끼리 묶어서 1번만 실행 시키게 하도록 한다`
   + [
   + [1, 3, 5, 7, 9 ]
   + [2, 4, 6, 8, 10]
   + ]


 + 암달의 법칙 & 존 구스타푸슨   
  

 + 분산 처리는 아래 URL 확인
   + [한국데이터 산업진흥원](https://dataonair.or.kr/db-tech-reference/d-lounge/technical-data/?mod=document&uid=235894)
   + https://jihyeong-ji99hy99.tistory.com/102

기록해야 할 것들에 있는 것들을 2번 URL을 보시면 더 세세하게 나옵니다. 꼭 보세요!!

----
REFERENCES  
+ [참고 사이트](https://nesoy.github.io/articles/2018-09/OS-Concurrency-Parallelism)    
[참고 사이트](https://medium.com/naver-cloud-platform/%EC%9E%AC%EB%AF%B8%EB%A1%9C-%EC%9D%BD%EC%96%B4%EB%B3%B4%EB%8A%94-%EB%B3%91%EB%A0%AC%EC%B2%98%EB%A6%AC-c60c8e3b62a7)  
[참고 사이트](https://mafams.tistory.com/54)  
[참고 사이트](https://nesoy.github.io/articles/2018-09/OS-Concurrency-Parallelism)  
[참고 사이트](https://seamless.tistory.com/42)  
[참고 사이트](https://ko.gadget-info.com/difference-between-concurrency)
