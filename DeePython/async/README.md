#### [asyncio document](https://docs.python.org/ko/3/library/asyncio-task.html)

+ `코루틴`이라고 나오는 부분을, 본 레포에서는 `비동기 함수`로 대체하였습니다. 
  + 제네레이터 vs 비동기 함수를 통한 코루틴에 대해 생각을 정리하는라 그렇습니다. 
  + 문서에서는 제네레이터에 `@asynic.coroutine`을 통해 코루틴임을 명시합니다.
+ 본 repo에서는 나오지 않는 함수들 중 docuemnt에서 읽으면 좋을 함수를 적습니다.
  + sleep
  + shield
  + to_thread
  + run_coroutine_threadsafe
