---
title: 解决Debina系统自动更新软件包的问题
date: 2019-12-02 23:09:23
permalink: 2
categories: Linux
tags: Linux
reward: true
toc: true
---

　　不知从何时开始，我的电脑每天开机连接上网络之后，不断的在下载数据，状态栏显示网速达到每秒1到2兆。开始我还不太在意，不过后来由于带宽全部被这种莫名其奥妙的下载占据了，我连网页都无否正常浏览了，所以我决定解决掉这个问题。下面记录一下解决这个问题的过程。

　　首先我利用一款名为`nethogs`的实时网速监控程序查看是哪个进程在占据带宽，发现占据带宽的正是系统的APT包管理工具，我想肯定是系统在执行自动更新。杀掉这个进程后，我便去Google了一下如何关闭APT包管理工具的的自动更新。网上人们提供的解决方案大都一致：修改APT的配置文件。
<!-- More -->
APT关于自动更新的配置文件位于"/etc/apt/apt.conf.d/20auto-upgrades", 将其中的
```shell
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
```
更改为
```shell
APT::Periodic::Update-Package-Lists "0";
APT::Periodic::Unattended-Upgrade "0";
```
其中
- APT::Periodic::Update-Package-Lists; 每一天自动运行一次 apt-get update，1 表示启用，0 表示禁用。
- APT::Periodic::Unattended-Upgrade; 每一天运行一次 unattended-upgrade 安全升级脚本，1 表示启用，0 表示禁用。
  
　　然而，并无卵用，第二天开机后APT又执行自动更新了，更奇怪的是杀掉APT进程不久之后它会再一次运行。这时我才意识到一件事情，APT是不会自动把自己调入内存运行的，一定是另有进程调用了它。打开进程管理器之后，查看 APT 进程的依赖关系，发现果然它有一个名为 `packagekit` 的父进程，我查了一下 `packagekit` 是一个旨在简化Linux发行版安装和更新软件的系统，它为不同的包管理工具提供了统一的前端，你可以在不同的Linux发行版中使用它来管理软件包。

　　我的系统默认在开机时启动packgekit服务，查看 `packagekit` 的启动单元: 
`cat /lib/systemd/system/packagekit.service`
```shell
[Unit]
Description=PackageKit Daemon
# PK does not know how to do anything on ostree-managed systems;
# currently the design is to have dedicated daemons like
# eos-updater and rpm-ostree, and gnome-software talks to those.
ConditionPathExists=!/run/ostree-booted

[Service]
Type=dbus
BusName=org.freedesktop.PackageKit
User=root
ExecStart=/usr/lib/packagekit/packagekitd
```
*系统每次开机时都会启动这个单元，执行 `/usr/lib/packagekit/packagekitd` 命令，而 `packagekit` 又将在运行期间调起APT下载需要更新的软件包。*

　　知道了这些问题自然也就解决了，禁用此服务: `systemctl disable packagekit.service`.
　　或者干脆删除 `/lib/systemd/system/` 目录下的 `packagekit.service` (当然你也可以把这个文件移动到别的地方去，以后用到时再放回来)

　　在那之后，系统便再也没有执行过自动更新了。
　　
[附]
>[nethohs](https://github.com/raboof/nethogs)是一个能按进程实时监控网络的命令行工具，它可以动态的展示某一时刻正在进行通信的进程的网络流量信息。

在 Debian/Ubuntu 下，使用`apt-get install nethogs` 安装它。
或编译安装:
```shell
wget -c https://github.com/raboof/nethogs/archive/v0.8.5.tar.gz
tar xf v0.8.5.tar.gz 
cd ./nethogs-0.8.5/
make && make install
```
如果编译失败需要安装依赖库
```
apt-get install libncurses5-dev libpcap-dev
```

使用

```shell
root@zsimline$ nethogs
NetHogs version 0.8.5-2+b1
PID  USER    PROGRAM                   DEV  SENT      RECEIVED  
2181 mxsyx  /usr/share/code/code       usb0 0.449   0.900 KB/sec
1598 mxsyx  /usr/lib/chromium/chromium usb0 0.031   0.018 KB/sec
?    root   unknown TCP                     0.000   0.000 KB/sec

  TOTAL                                     0.480       0.917 KB/se
```

指定网卡
```shell
root@zsimline$ nethogs wlan0 # 监听wlan0
root@zsimline$ nethogs -a    # 监听所有网卡
```

指定刷新频率 -d seconds (默认为1)
```shell
root@zsimline$ nethogs -d 2
```

指定刷新次数 -c number (默认不限)
```shell
root@zsimline$ nethogs -c 10
```

交互模式
在进入 nethogs 之后，可以使用如下的交互命令:
```shell
q: 退出
s: 按照发送流量排序
r: 按照流量排序
m: 修改网速单位 (KB, B, MB) and KB/s
```