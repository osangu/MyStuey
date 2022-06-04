### DNS란?
Domain Name System의 약자.
- OSI 7계층의 `운영 계층`의 프로토콜에 해당한다.
- 모든 IP를 기억할 수 없기에 문자열로 바꾸어 사용하는 것이다.
---
1. 브라우저 ➡️ Local DNS  
    원하는 웹사이트의 IP 주소 여부 확인
2. Local DNS ➡️ Root DNS  
    IP 주소 여부 확인
3. Root DNS ➡️ Local DNS  
    com 도메인을 관리하는 네이서버의 IP 주소 제공
4. Local DNS ➡️ com NS  
    www.naver.com을 아시나요?  
5. Com NS ➡️ Local DNS  
    naver.com의 IP주소 제공



<img width="50%" height="50%" alt="사진3" src=https://user-images.githubusercontent.com/80697064/172007884-cc0b3621-6a39-4d72-ad8f-ec23e766f37a.png>
<img width="50%" height="50%" alt="사진2" src="https://user-images.githubusercontent.com/80697064/172007772-e28974ea-d0a3-465f-859f-46b5b3bad5e2.png">
---- 

**Reference**  
[Rference 1](https://ja-gamma.tistory.com/entry/DNS%EA%B0%9C%EB%85%90%EB%8F%99%EC%9E%91%EC%9B%90%EB%A6%AC)