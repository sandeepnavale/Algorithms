import  asyncio
import time
def isPrime(y):
    return not any(y//i == y /i for i in range(y-1,1,-1))

async def higest_prime_below(x):
    print('Highest prime below %d ' %x)
    for y in range(x,0,-1):
        if (isPrime(y)):
            print('Highest prime in from %d is %d' %(x,y))
            return y
        await asyncio.sleep(.01)
    return None

async def amain():
    await asyncio.wait(
        [
            higest_prime_below(10000),
            higest_prime_below(1000),
            higest_prime_below(100),
            higest_prime_below(10)
        ]
    )


if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(amain())
    loop.close()
    t2 = time.time()
    print("Time Consumed ",(t2-t1)*1000)
