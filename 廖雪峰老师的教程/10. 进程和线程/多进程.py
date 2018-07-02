# fork() 返回2次  因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回

# 子进程永远返回0，而父进程返回子进程的ID

import os

'''
print('process (%s) start...' % os.getpid())

# # Only works on Unix/Linux/Mac:
pid= os.fork()

if pid ==0 :  # 子进程
    print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(),pid))
'''

# multiprocessing  模块就是跨平台版本的多进程模块。

# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


# Pool  如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Pool
import time,random

def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()  #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    print('All subprocesses done.')