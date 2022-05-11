
![모놀리식-soa-msa](https://user-images.githubusercontent.com/80697064/167801616-d8e28d9a-d5bf-4f23-9e13-1eaeb97fc6c1.png)

### 모놀리식 아키텍처

모든 구성요소가 한 곳에 뭉쳐져 있는 형태.

애플리케이션의 한 프로세스에 대해 수요가 증가하면 해당 아키텍처 전체를 확장해야 한다.

**장점**

    한 번의 테스트, 빌드, 배포를 거치기 때문에 소규모 프로젝트에서는 매력적인 선택이 될 수 있다.

**단점**

    1. 기능별 적합한 기술(언어, 프레임워크, 데이터베이스)를 구현하기 힘들다.
    2. 하나의 프로세스가 고장나면 시스템 전체에 영향을 줄 수 있다
    3. 약간의 수정사항으로도 전체의 빌드와 배포가 재진행 되어야 함  

    → 유지보수가 힘들다


### SOA 🆚 MSA  
+ 공통 사항  
  둘 다 모듈의 의존성을 최소로 하기 위해 사용하는 아키텍처이다.  
  모놀리식에 비해 비용이 더 든다  
  구현이 어렵다  
  

+ 독립성을 유지 하는 정도  
  SOA: 공통 사항은 유지하려고 함 -- MSA : 모든 모듈이 독립을 원한다.

- MSA는 서비스 내의 독립이 아닌 서비스의 독립 그 자체를 지향한다.

  
**`노트북 패드 vs 매직 패드 vs 마우스`** 비교하는 것 이 가장 적절하지 않을까 싶다.

[출처](https://azderica.github.io/00-architecture-msa/)  
[콘웨이 법칙](https://wiki.webnori.com/display/devbegin/SOA+VS+MSA)  
[soa 추가 내용](https://www.redhat.com/ko/topics/cloud-native-apps/what-is-service-oriented-architecture) 
