"""
https://docs.ray.io/en/latest/
https://zzsza.github.io/mlops/2021/01/03/python-ray/ 
https://velog.io/@otzslayer/Ray를-이용해-병렬-처리-쉽게-하기
https://ebbnflow.tistory.com/338
https://docs.python.org/ko/3/library/multiprocessing.html
https://titania7777.tistory.com/15
"""


if __name__ == '__main__':

    import ray
    import random

    ray.init()

    @ray.remote
    def ex_func(): return random.randrange(0,100)

    rand_value = ex_func.remote()

    ray.get(rand_value)

    ray.shutdown()

