import json
import time

from celery import Celery

from ..database.models import Fibonacci
from ..database.connector import Connector
from ..settings import settings

app = Celery(__name__, backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER_URL)


@app.task(name='api.fibonacci')
def task_gen_fibonacci(n: int, id_: int):
    with Connector() as conn:
        new_fib = Fibonacci.find_by_id(conn, id_)

        time.sleep(10)  # simulating durable async task

        numbers = []
        a, b = 0, 1
        for _ in range(n):
            numbers.append(a)
            a, b = b, a + b
        else:
            numbers = json.dumps(numbers)

        new_fib.LT_FIBONACCI = numbers
        new_fib.IN_FINISHED = True
        new_fib.add(conn)
