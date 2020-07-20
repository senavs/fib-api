from typing import Optional

from fastapi import APIRouter, Depends

from ..models.fibonnaci import GenerateFibonacciSequence
from ..database.connector import init_database
from ..database.models import Fibonacci
from ..tasks import task_gen_fibonacci

router = APIRouter()


@router.get('/{id}', summary='get fibonacci list generator result', status_code=201)
async def get_fibonacci(id: int, conn=Depends(init_database)):
    fib = Fibonacci.find_by_id(conn, id)

    if not fib.IN_VIEWED:
        fib.IN_VIEWED = True

    fib = fib.to_dict()
    return fib


@router.post('/', summary='async fibonacci list generator', status_code=201)
async def post_fibonacci(gen_fib: GenerateFibonacciSequence, conn=Depends(init_database)):
    new_fib = Fibonacci()
    new_fib.add(conn)
    new_fib = new_fib.to_dict()

    task_gen_fibonacci.delay(gen_fib.n, new_fib['id_fibonacci'])

    return {'id': new_fib['id_fibonacci']}
