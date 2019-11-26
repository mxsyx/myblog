---
title: 测试
date: 2019-11-25 15:50:29
tags: 测试
reward: true
permalink: 1
categories: 基础知识
---

　　C++11 引入了对多线程语言级别的支持，<thread> 库是C++的标准线程库，它定义了与编写多线程程序相关的类。 相比于传统的POSIX线程标准，<thread> 库更符合C++的编程风格。

　　<thread> 库是跨平台的，这意味着你可以在任意平台上不经修改直接编译同一段多线程代码（前提是你没有在这段代码中调用其它系统相关的API）

### 创建一个线程

std::thread 类用来创建一个线程

```cpp
// dev01.cc
#include <iostream>
#include <thread>  // 引入线程库头文件

void Display(int index) {
  std::cout << "index 的值为!" << index << std::endl;
}

int main() {
  // 创建线程 trd, 传入参数 1
  std::thread trd(Display, 1);

  // 等待线程 trd 结束
  trd.join();

  return 0;
}
```
```shell
编译dev01.cc （需要动态链接pthread库）
g++ -o dev dev.cc -lpthread && ./dev
输出：index 的值为 1
```
　　std::thread 的初始化构造函数原型为`template <class Fn, class... Args>`, 构造函数的第一个参数为线程要执行的函数，后面是要传递给线程函数的实参。**值得注意的是，线程在thread类实例化之后就开始执行了，不需要显式的调用任何启动线程的函数。**

　　线程启动后，需要在主线程内调用线程对象的 join 函数。join 函数用于阻塞主线程的执行，当新创建的线程执行完成后，主线程继续执行。一个进程内的所有线程共享某些资源，若不调用线程对象的join 函数，一旦主线程执行结束，操作系统将回收这些资源，新创建的线程得不到这些应有的资源就会终止执行并抛出错误。

【拷贝构造函数】
 std::thread 类不支持拷贝构造 `thread (const thread&) = delete;`

【移动构造函数】
std::thread 类支持移动构造函数 `thread (thread&& x) noexcept;`
```cpp
// dev02.cc
#include <iostream>
#include <thread>

void Display(int index) {
  std::cout << "index 的值为!" << index << std::endl;
}

int main() {
  // 创建线程 trd, 传入参数 1
  std::thread trd(Display, 1);
  // 移动动构造一个线程对象
  // 该操作不会以任何方式影响被移动线程的执行
  std::thread trd1(std::move(trd));

  // 此时trd对象不再代表任何执行线程
  // trd.join();
  trd1.join();

  return 0;
}
```
【赋值操作符】
 可以使用赋值操作符移动赋值线程对象`thread& operator= (thread&& rhs) noexcept;`
 不可以使赋值操作符拷贝赋值线程对象`thread& operator= (const thread&) = delete;`
```cpp
// dev03.cc
#include <iostream>
#include <thread>

void Display(int index) {
  std::cout << "我是线程 " << index << std::endl;
}

int main() {
  // 创建线程对象数组
  // 调用类的默认构造函数
  std::thread trds[3];

  // 使用赋值操作符移动赋值
  // 该操作不会以任何方式影响被移动线程的执行
  for(int i = 0; i < 3; i++)
    trds[i] = std::thread(Display, i + 1);

  // 等待线程结束
  for(int i = 0; i < 3; i++)
    trds[i].join();

  return 0;
}
```
```shell
编译上面的程序输出：
我是线程 2
我是线程 3
我是线程 1
```
可以看到，线程的执行顺序是不确定的，这取决于操作系统如何调度线程的执行。
而且，输出也并不总是这样顺眼，比如下面的输出：
```shell
我是线程 我是线程 21我是线程 3
```
Display 函数中的输出语句是可中断的，当某个线程输出 “我是线程 ” 后，它完全有可能被操作系统挂起，等待一段时间后系统再次启动这个线程，输出剩余的内容。

### 获取线程ID

每个线程都有一个唯一标识，通过调用线程对象的 get_id 函数可以得到这个唯一标识。

```cpp
// dev04.cc
#include <iostream>
#include <thread>

void Display(int index) {
  //std::cout << "我是线程 " << index << std::endl;
}

int main() {
  std::thread trds[3];

  for(int i = 0; i < 3; i++)
    trds[i] = std::thread(Display, i + 1);

  for(int i = 0; i < 3; i++) {
    // 线程ID 的类型为 std::thread::id
    std::thread::id tid = trds[i].get_id();
    std::cout << "线程" << i + 1 << " " << tid << std::endl;
    trds[i].join();
  }

  return 0;
}
```
```shell
编译上面的程序输出：
线程1 140121399854848
线程2 140121391462144
线程3 140121383069440
```

### 检测线程可连接性

通过调用线程对象的 joinable 函数可以检测线程对象是否是可连接的。
如果线程对象表示执行线程，则该对象是可连接的。
在以下任何情况下，线程对象均不可连接：
1.  线程对象是由默认构造函数生成的
2. 线程对象已经被移动（通过移动构造函数或赋值操作符）
3. 已经调用过线程对象的 join 或 detach 函数

```cpp
// dev05.cc
#include <iostream>
#include <thread>

void Display(int index) {
  //std::cout << "我是线程 " << index << std::endl;
}

int main() {
  // 默认构造 trd1
  std::thread trd1;
  // 正常构造 trd2
  std::thread trd2(Display, 1);
  // 移动构造 trd3
  std::thread trd3(std::move(trd2));

  if(trd1.joinable()) {
    std::cout << "线程对象trd1可连接" << std::endl;
    trd1.join();
  } else {
    std::cout << "线程对象trd1不可连接，它是默认构造的" << std::endl;
  }
  
  if(trd2.joinable()) {
    std::cout << "线程对象trd2可连接" << std::endl;
    trd2.join();
  } else {
    std::cout << "线程对象trd2不可连接，它已经被移动了" << std::endl;
  }

  if(trd3.joinable()) {
    std::cout << "线程对象trd3可连接" << std::endl;
    trd3.join();
  } else {
    std::cout << "线程对象trd3不可连接" << std::endl;
  }

  if(trd3.joinable()) {
    std::cout << "线程对象trd3可连接" << std::endl;
    trd3.join();
  } else {
    std::cout << "线程对象trd3现在不可连接了" << std::endl;
  }

  return 0;
}
```
```shell
编译上面的程序输出：
线程对象trd1不可连接，它是默认构造的
线程对象trd2不可连接，它已经被移动了
线程对象trd3可连接
线程对象trd3现在不可连接了
```

### 分离线程

调用线程对象的detach函数可以使新创建的线程与主线程分离，与join函数不同的是，detach函数不会阻塞主线程的执行，若主线程早于新线程执行完毕，新线程将终止执行，不会抛出任何错误。

```cpp
// dev06.cc
#include <iostream>
#include <thread>
#include <chrono>

void DelayThread(int s) {
  // sleep_for函数使线程睡眠s秒
  std::this_thread::sleep_for(std::chrono::seconds(s));
  std::cout << s << "秒过去了" << std::endl;
}

int main() {
  std::thread trd1(DelayThread, 2);
  std::thread trd2(DelayThread, 8);

  // 分离线程
  trd1.detach();
  trd2.detach();

  // 主线程睡眠5s
  DelayThread(5);
  return 0;
}
```
```shell
编译上面的程序输出：
2秒过去了
5秒过去了
```

### 交换线程

通过调用线程对象的swap函数可以交换两个线程

```cpp
// dev07.cc
#include <iostream>
#include <thread>

void Display(int index) {
  // ...
}

int main() {
  std::thread trd1(Display, 2);
  std::thread trd2(Display, 8);

  std::cout << "交换前：" << std::endl;
  std::cout << "trd1 ID: " << trd1.get_id() << std::endl;
  std::cout << "trd2 ID: " << trd2.get_id() << std::endl;

  // 交换两个线程
  trd1.swap(trd2);
  // 同样可以调用非成员函数交换两个线程
  // swap(trd1, trd2);

  std::cout << "交换后：" << std::endl;
  std::cout << "trd1 ID: " << trd1.get_id() << std::endl;
  std::cout << "trd2 ID: " << trd2.get_id() << std::endl;

  trd1.join();
  trd2.join();

  return 0;
}
```
```shell
编译上面的程序输出：
交换前：
trd1 ID: 140593231992576
trd2 ID: 140593223599872
交换后：
trd1 ID: 140593223599872
trd2 ID: 140593231992576
```

### 获取硬件并发数量

有时我们想知道处理器支持的硬件并发数量，可以调用线程类的静态函数 hardware_concurrency 来获取这个值，该函数返回值是一个无符号整数。

```cpp
// dev08.cc
#include <iostream>
#include <thread>

int main() {
  std::cout << std::thread::hardware_concurrency();
  return 0;
}
```
```shell
编译上面的程序输出（在我的四核心处理器上）
4
编译上面的程序输出（在我的单核心处理器上）
1
```
值得注意的是：该函数的返回值不一定与系统中可用的处理器或内核的实际数量相匹配，系统可以为每个处理单元支持多个线程，或限制对程序的资源访问。

### 访问当前线程

　　std::this_thread 命名空间定义了几个访问当前线程的函数，你可以在线程函数中直接调用这些函数来实现一些功能。

+ get_id
`thread::id get_id() noexcept;`
获取当先线程ID
+ yield
`void yield() noexcept;`
阻塞当先线程的执行
+ sleep_for
`template <class Rep, class Period>`
`void sleep_for (const chrono::duration<Rep,Period>& rel_time);`
阻塞当前线程的执行一段时间

```cpp
// dev09.cc
#include <iostream>
#include <thread>
#include <chrono>

bool ready = false;

void SetReady() {
  // 等待 5 秒钟后设置全局变量 ready 的值为 true
  std::this_thread::sleep_for(std::chrono::seconds(5));
  std::cout << "Display 函数即将继续执行" << std::endl;
  ready = true;
}

void Display() {
  // 阻塞当前线程的执行，直到SetReady 函数设置
  // 全局变量 ready 的值为 true 的时候才继续执行
  while (!ready) {
    std::this_thread::yield();
  }
  std::cout << "线程ID: " << std::this_thread::get_id() << std::endl;
}


int main () {
  std::thread trd1(SetReady);
  std::thread trd2(Display);
  trd1.join();
  trd2.join();

  return 0;
}
```
```shell
编译上面的程序输出：
Display 函数即将继续执行
线程ID: 140362842375936
```

+ sleep_until
`template <class Clock, class Duration>`
`void sleep_until (const chrono::time_point<Clock,Duration>& abs_time);`
阻塞当前线程的执行直到某个时间

```cpp
// dev10.cc
// this_thread::sleep_for example

#include <iostream>
#include <iomanip>　　// std::put_time
#include <thread>
#include <chrono>
#include <ctime>　// std::time_t, std::tm, std::localtime, std::mktime

int main() {
  using std::chrono::system_clock;
  std::time_t tt = system_clock::to_time_t(system_clock::now());

  struct std::tm * ptm = std::localtime(&tt);
  std::cout << "Current time: " << std::put_time(ptm,"%X") << '\n';

  std::cout << "Waiting for the next minute to begin...\n";
  ++ptm->tm_min; ptm->tm_sec=0;
  std::this_thread::sleep_until(system_clock::from_time_t(mktime(ptm)));

  std::cout << std::put_time(ptm,"%X") << " reached!\n";

  return 0;
}
```
```shell
编译上面的程序输出：
Current time: 22:08:36
Waiting for the next minute to begin...
22:09:00 reached!
```
上面是摘自CPP官网的一段程序，主函数内生成一个关于系统时间的结构体，输出当前时间后使结构体内的分钟数自增1，之后调动 sleep_until 函数阻塞当前线程的执行直到下一分钟的到来。


以上是对C++标准线程库的简单介绍，此文章内的全部代码可在下面的链接中找到：[https://github.com/zsimline/sweetea/tree/master/code/archives-667](https://github.com/zsimline/sweetea/tree/master/code/archives-667)

参考资料：
[1] CPP官网 [http://www.cplusplus.com/reference/thread/](http://www.cplusplus.com/reference/thread/)
