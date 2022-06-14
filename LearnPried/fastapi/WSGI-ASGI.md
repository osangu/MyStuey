### CGI
초창기에는 웹 서버를 통해서 정적으로 처리해도 별로 무리가 없었다.  

하지만 정적으로 처리하는 것의 한계를 느껴,  
웹 서버와 애플리케이션이 통신하게 만들어줄 수 있도록 만들어진 프로토콜이 CGI이다.
 
- Request가 들어올 때마다 프로세스를 새로 생성해서 자원을 소비하게 된다.
- 위 단점으로 인해 서버의 부하가 생길 수 있다.

### FastCGI
CGI의 단점을 보완해서 만들어진 프로토콜이다.  
1개의 프로세로만 처리하여, 프로세스를 생성하면서 생기는 부를 없앴다
- 웹 서버와 애플리케이션을 소켓 통신하 뒷단에 서버를 구축하는 것을 WAS라고 한다.


----

### WSGI
WSGI의 등장 전에는 CGI, Fast CGI, mod_python 중에서 하나를 골라 선택했어야 했다고 한다.  
[ 서버와 게이트웨이 ]  ↔  WSGI  ↔ [애플리케이션과 프레임워크]
위와 같은 상황에서 `WSGI 미들웨어`라는 것이 Request와 view funtion같은 것들을 활용한다고 한다.

### ASGI
WSGI에 비동기와 동기를 선택할 수 있는 기능을 추가 하여 사용할 수 있게 하는 것이다.


----
### REFERENCE
> **CGI - FastCGI**  
> https://server-talk.tistory.com/308  
> https://blog.neonkid.xyz/249

 
> **WSGI - ASGI - UWSGI**  
> https://blog.neonkid.xyz/249  
> https://breezymind.com/start-asgi-framework/
> https://nitro04.blogspot.com/2020/01/django-python-asgi-wsgi-analysis-of.html  
