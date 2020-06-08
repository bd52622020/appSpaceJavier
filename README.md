# Javier Sanchez repository

Repository to upload all the assignments during the training course. This repository will be divided into folders called Weeks. I will add useful information about data engineering in this README.


## Training nodes

### Q1) Which are the differences between multiprocessing and multithreading?

Before getting into the differences between these two concepts, I would like to define each one:

- **Multiprocessing:** A multiprocessing system has more than two processors. The CPUs are added to the system that helps to increase the computing speed of the system. Every CPU has its own set of registers and main memory. However, because each CPU are separate, it may happen that one CPU may not have anything to process. One processor may sit idle, and the other may be overloaded with the specific processes. In such a case, the process and resources are shared dynamically among the processors. 

- **Multithreading:** Multithreading is a program execution technique that allows a single process to have multiple code segments (like threads). It also runs concurrently within the "context" of that process. Multi-threaded applications are applications that have two or more threads that run concurrently. Therefore, it is also known as concurrency. 

- **Multiprocessing vs Multithreading:** 

  - First of all, the **multithreading** uses threads, the **multiprocessing** uses processes. The difference is that threads run in the same memory space, while processes have separate memory.
  - **Multiprocessing** helps you to increase computing power. **Multithreading** helps you to create computing threads of a single process to increase computing power. 
  - In **multiprocessing** code is usually straightforward. However, in **multithreading** code is usually harder to understand and to get right.
  - **Multithreading** is a great option for I/O-bound applications.
  - **Multithreading** has a shared-state. However, **multiprocessing** like it has its own memory, do not.
  - In **multiprocessing** child processes are interruptible/killable, and in **multithreading** no.

So, in **summary**: Concurrency and parallelism are related terms but not the same, and often misconceived as the similar terms. The crucial difference between concurrency and parallelism is that concurrency is about dealing with a lot of things at same time (gives the illusion of simultaneity) or handling concurrent events essentially hiding latency. On the contrary, parallelism is about doing a lot of things at the same time for increasing the speed.

More practical information in Python [here.](https://medium.com/contentsquare-engineering-blog/multithreading-vs-multiprocessing-in-python-ece023ad55a)



### Q2) Is Python trully multiprocessing in computer systems?

No, Python does have multithreading. In fact, it uses system threads. The problem is just that it can't use more than one of the available cores. This is due to something called the GIL(Global Interpreter Lock). Python threads still work for I/O bound tasks as opposed to CPU bound tasks which may cause deadlocks and race conditions. Many Python libraries solve this issue by using C extensions to bypass the GIL. Of course, this is all in the case of CPython.

[Interesting talk about multithreading and multiprocessing](https://www.youtube.com/watch?v=Bv25Dwe84g0)

