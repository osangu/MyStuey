### DNS란?
Domain Name System의 약자.
- OSI 7계층의 `운영 계층`의 프로토콜에 해당한다.
- 모든 IP를 기억할 수 없기에 문자열로 바꾸어 사용하는 것이다.

---
> 사진에 따르면 아래 과정을 실행하기 전에  Cache 폴더와 Hashes 파일을 거쳐가는 과정이 존재한다.  
> 여기서의 TTL은 캐시에 도메인의 정보가 남아있는 시간을 뜻한다.

**`브라우저 ↔️️ Local DNS`**  
  1. Domain Name에 대한 질문   
  2. 있으면 IP 제공 
  3. 없으면 아래 과정 실시

**`Local DNS ↔️ Root DNS`**      
  1. 원하는 웹 서버의 정보를 질의  
  2. com Domain을 관리하는 네임 서버의 이름과 IP 제공  

**`Local DNS ↔️ com NS(TLD)`**   
  1. 원하는 웹 서버의 정보 질의  
  2. naver.com을 관리하는 네임 서버의 이름과 IP 제공  

**`Local DNS ↔️  naver.com 관리하는 네임 서버`**  
  1. 아세요?  
  2. IP 제공  

**`Root DNS ➡️ 브라우저`**    
  1. 받은 IP 제공  

----
아래에 출처란에 있는 `제일 잘 설명된 출처`를 꼭 보자! 
#### Resolver
- 클라이언트가 DNS에게 IP 주소를 물을 때, 그 역할을 하는 것

#### Local DNS 서버

- Domain Name을 입력했을 때 가장 먼저 찾는 DNS 서버
- 인터넷을 사용할 수 있게 IP를 할당한 통신사의 DNS서버가 등록됨.
- 있으면 바로 알려주고, 없으면 root dns에게 묻는 위의 과정이 실행되는 것이다.

#### Root DNS 서버
- 트리구조로 만들어져있다.
- 해당 서버에 없을 경우, naver.com의 com을 daum.net의 net 주소를 보내준다.

#### Top-Level Domain(com DNS) 
- com, net, kr 같은 도메인들을 관리하는 서버
----

<img width="50%" height="50%" alt="사진3" src=https://user-images.githubusercontent.com/80697064/172007884-cc0b3621-6a39-4d72-ad8f-ec23e766f37a.png>
<img width="50%" height="50%" alt="사진2" src="https://user-images.githubusercontent.com/80697064/172007772-e28974ea-d0a3-465f-859f-46b5b3bad5e2.png">

---- 

**Reference**  
[Cache에 DNS의 정보를 저장하는 시간 TTL](https://www.domainclub.kr/domain_webdns_info.htm)  
[제일 잘 설명된 출처](https://hwan-shell.tistory.com/320)    
[Reference 1](https://securitynewsteam.tistory.com/entry/DNS-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C%EC%9D%98-%EC%9E%91%EB%8F%99%EC%9B%90%EB%A6%AC)  
[Reference 2](https://ja-gamma.tistory.com/entry/DNS%EA%B0%9C%EB%85%90%EB%8F%99%EC%9E%91%EC%9B%90%EB%A6%AC)  
[Reference 3](https://velog.io/@goban/DNS%EC%99%80-%EC%9E%91%EB%8F%99%EC%9B%90%EB%A6%AC)