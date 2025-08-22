# Ubuntu From Beginner to Master

----系统开发指南（配合CSAPP & 顶会计划）

## Bash From beginner to Master
### Map Overview
```txt
终端命令
├── 文件操作：ls, cd, mv, cp, rm, mkdir
├── 权限管理：sudo, chmod, chown
├── 软件安装：apt, dpkg, snap
├── 编辑器：nano, vim, code
├── 编译工具：gcc, make, gdb
├── 网络命令：ping, curl, ssh
├── 进程控制：ps, top, kill, htop
└── 其他：man（帮助文档）, echo, cat
```

| Tool       | Type                       | What It Does                                                                     | When to Use                                                       |
| ---------- | -------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **`nano`** | Text editor (simple)       | Opens a small, beginner-friendly editor inside the terminal.                     | Quick edits to config files or scripts.                           |
| **`vim`**  | Text editor (advanced)     | A very powerful modal editor (steeper learning curve than `nano`).               | Professional editing, scripting, programming.                     |
| **`cat`**  | File viewer / concatenator | Prints the contents of a file to the terminal, or joins multiple files together. | Quickly check file contents, or combine files.                    |
| **`echo`** | Output command             | Prints text/variables to the terminal.                                           | Debugging scripts, printing values, redirecting to files.         |
| **`less`** | File viewer (pager)        | Opens a file in a scrollable view, without editing.                              | Reading long files/logs, navigating with arrows, search with `/`. |

以下是 **完整终端命令清单**：

```
终端命令
├── 文件操作：ls, cd, mv, cp, rm, mkdir, rmdir, touch, find, locate, stat, file, tree, ln, shred, diff, cmp
├── 权限管理：sudo, chmod, chown, chgrp, umask, getfacl, setfacl, sudo visudo
├── 软件安装与包管理：apt, dpkg, snap, flatpak, yum, dnf, rpm, pacman, zypper, brew, dpkg -l, apt-cache search
├── 编辑器：nano, vim, emacs, code, gedit
├── 编译与开发工具：gcc, g++, make, gdb, cmake, clang, valgrind
├── 网络命令：ping, curl, wget, ssh, scp, ftp, rsync, netstat, ifconfig, ip, traceroute, telnet, nc (netcat)
├── 进程控制：ps, top, kill, htop, pgrep, pkill, nice, renice, nohup, bg, fg
├── 系统监控：uptime, free, df, du, iostat, vmstat, lsof, dstat, mpstat, sar
├── 磁盘操作：fdisk, mkfs, mount, umount, blkid, lsblk, fsck, tune2fs
├── 包管理工具：dpkg, apt-get, apt-cache, apt-mark, apt-key, snap, flatpak
├── 文件查找与文本处理：grep, egrep, sed, awk, cut, sort, uniq, tr, wc, tee, xargs, head, tail
├── 其他：man (帮助文档), echo, cat, less, tar, gzip, bzip2, zip, unzip, file, diff
└── 脚本与自动化：bash, sh, cron, at, crontab, export, alias, unset, source
```

- **文件操作**：这类命令帮助你在文件系统中操作文件与目录，像 `find` 用来查找文件，`locate` 用来快速定位。
    
- **权限管理**：`chmod` 和 `chown` 是操作文件权限和拥有者的关键命令，`sudo visudo` 是修改权限的高级命令。
    
- **软件安装与包管理**：不同的 Linux 发行版有不同的包管理工具（如 `apt`, `yum`, `pacman`），这些工具帮助你管理软件包的安装、更新和删除。
    
- **编译与开发工具**：这类命令帮助开发人员编译和调试代码，`make` 用于自动化构建过程，`gdb` 用于调试。
    
- **网络命令**：网络命令帮助你检查和调试网络连接，`ping` 检查网络是否可达，`ssh` 远程登录，`scp` 安全地复制文件。
    
- **进程控制**：这类命令用于管理系统中的进程，`kill` 用于结束进程，`ps` 查看正在运行的进程，`top` 和 `htop` 提供系统资源使用的实时视图。
    
- **系统监控**：这些命令帮助你查看系统状态，如 `uptime` 显示系统运行时间，`free` 查看内存使用情况，`df` 查看磁盘空间。
    
- **磁盘操作**：这些命令帮助你管理磁盘和文件系统，如 `fdisk` 用于磁盘分区，`mount` 和 `umount` 用于挂载和卸载文件系统。
    
- **包管理工具**：与软件安装相关的工具，`dpkg` 和 `apt-get` 是 Debian 系列的常见工具。
    
- **文件查找与文本处理**：这些命令处理文本文件，`grep` 用于搜索，`awk` 和 `sed` 是文本处理的强大工具。
    
- **其他**：包含一些实用命令，如 `tar` 用于压缩和解压，`man` 查看帮助文档，`echo` 输出文本。
    
- **脚本与自动化**：这类命令帮助你进行任务自动化，`cron` 用于设置定时任务，`alias` 用于创建命令别名，`bash` 用于执行脚本。

### 为什么理解比记住更重要？

1. **逻辑驱动问题解决**：  
    学会理解和分析问题，了解系统如何工作，能帮助你在面对新问题时快速找到解决方案。例如，知道如何查看进程、如何调整系统设置、如何查看日志等，能帮助你通过组合不同的命令解决复杂问题。
    
2. **灵活使用工具**：  
    Linux 系统中有非常多的工具和命令，但它们都遵循一定的规则和模式。一旦你理解了这些工具的基本用法，你就能灵活地组合它们来完成工作，而不需要死记硬背。
    
3. **文档与搜索能力**：  
    你不可能记住所有命令，但你可以 **学会如何查阅手册**（`man`）和搜索工具（如 `apropos`、`--help`）。通过这种方式，你可以在需要时快速找到所需的命令和选项。
    
4. **动手实践**：  
    真正掌握这些工具和命令的方式是通过实践。当你不断遇到问题并尝试用命令行解决时，你会渐渐掌握它们的用法。**通过实践加深理解**，而不是死记硬背。
    

### 如何高效学习？

- **理解命令背后的原理**：例如，`cp` 命令是用来复制文件的，它背后遵循了“源”与“目标”的规则，理解了这个，其他类似的命令（如 `mv`, `rsync`）你就能很快上手。
    
- **学习“组合命令”的思维**：Linux 中的许多操作是通过 **组合命令**（使用管道 `|` 或重定向 `>`）来实现的。了解这个模式，你就能应对更多复杂场景。
    
- **掌握搜索和调试**：遇到新命令时，先 **查找文档**，通过 `man` 或 `--help` 查看命令详情，结合实际场景实践和调试。
    
- **实践和总结**：每次用到一个新命令时，可以做个简短总结，记下它的用法和选项，之后回顾这些总结，逐渐在实际操作中形成直觉。

### 记住一点：

你不必记住每个命令，但一定要 **理解** 命令如何工作、如何在不同场景下应用它们，并学会 **灵活组合使用**，最重要的是知道如何 **找到正确的工具和资源** 来解决问题。

[[Bash From beginner to Master]] 

- **命令速查网站**：[devhints.io](https://devhints.io/)（按场景分类）
- 高手更擅长通过管道和重定向组合简单命令

#### Master 15 Commands + Options

1. **导航**：`cd` `ls` `pwd`
2. **文件操作**：`cat` `vim` `cp/mv/rm`
3. **诊断**：`grep` `find` `top/htop`
4. **开发**：`git` `ssh` `curl/wget`
5. **权限**：`sudo` `chmod` `chown`

[[The Bash Command DNA Intuition]] Most Linux commands have the same “DNA” structure:
```
command   [options]   parameters   object(s)
```

**🎇Pro workflow:** 
1. **Learn the core options** you see in most tutorials/examples
2. **Use `--help` and `man`** to check new ones only when needed
3. **Practice in small real cases** (muscle memory beats rote memory)
4. **Make a personal cheat sheet** for commands you use a lot

[[Linux Command Option Patterns Map]] 

#### 提效的10个组合技

```
# 1. 快速定位错误
tail -f /var/log/nginx/error.log | grep -C 5 "500"

# 2. 批量处理文件
find . -type f -name "*.bak" -exec rm {} +

# 3. 端口占用检查
netstat -tulnp | grep 3306
```

**📌 附加图解：操作系统体系分类** 

```
            操作系统
            ├── 桌面系统（Windows, macOS, Linux桌面）
            ├── 移动系统（Android, iOS）
            ├── 服务器系统（Ubuntu Server, CentOS）
            ├── 嵌入式系统（RTOS, FreeRTOS）
            └── 特种系统（科研/定制：NixOS, Gentoo, Arch）
```

## 阶段详解


| 层级     | 阶段目标        | 关键词                 | 所需时长  | 支撑项目             |
| ------ | ----------- | ------------------- | ----- | ---------------- |
| **L1** | 熟悉基础操作      | 文件/权限/终端            | 3~5天  | 全项目操作基础          |
| **L2** | 掌握开发环境      | GCC/Make/GDB/VSCode | 5~7天  | CSAPP Labs 编译与调试 |
| **L3** | 熟练系统工具链     | Git/SSH/Grep/Pipe   | 5~7天  | MLIR 项目 & 网络代理服务 |
| **L4** | 高效系统配置      | alias/zsh/权限管理      | 7~10天 | 开源协作、论文项目        |
| **L5** | 进阶开发调试      | Docker/Perf/Strace  | 7~15天 | 性能优化、系统调试        |
| **L6** | 编译器 & 分布式基础 | LLVM/MLIR/Net tools | 15+天  | 三项目终端融合目标        |

📌 建议学习顺序（从现在开始）

| 时间段     | 要做的事情                                  |
| ------- | -------------------------------------- |
| 第 1 周   | 适应 Bash + 常用命令 + vi 编辑器 + APT 安装包      |
| 第 2~3 周 | 学习 Shell 脚本语法、重定向、组合管道、脚本参数传递          |
| 第 4~5 周 | 实战：写项目构建脚本、配置 Nginx、系统调试工具             |
| 第 6~8 周 | 写一个完整的“自动部署 + 日志监控 + 编译测试”的 Shell 脚本项目 |

### 🔰 **L1 - Ubuntu 基础操作入门（文件、终端、权限）**

| 模块 [[bash_L1-Ubuntu]]      | 内容                                                                                      | 示例命令                                    |
| -------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------- |
| 📁 文件导航<br>[[文件导航系统化思路]]   | `ls`, `cd`, `pwd`, `mkdir`, `rm`, `tree`                                                | `cd ~/Documents`, `ls -lah`             |
| 🔐 权限与用户<br>[[权限与用户系统化思路]] | `chmod`, `chown`, `sudo`, `adduser`                                                     | `chmod +x script.sh`, `sudo apt update` |
| 📦 [[包管理-下载&安装]]           | **包格式**（RPM、DEB、Snap…）<br>**包管理器**（yum、dnf、apt、snap、`dpkg`…） **下载工具**（wget、curl、aria2c） | `sudo apt install make gcc`             |
| 🔧 常用工具                    | `nano`, `vim`, `cat`, `echo`, `less`                                                    | `nano config.txt`, `cat a.c`            |
| 📚 帮助系统                    | `man`, `--help`, `tldr`                                                                 | `man ls`, `tldr grep`                   |

> 📌 推荐任务：搭建个人文件结构 + 安装 curl、wget、vim、tree、git、zsh

dnf 命令的基本语法格式为：
```
dnf [选项] <命令> [参数]
```


[[Ubuntu 下载失败场景总结]]  
[[沙盒和 沙盒技术]] (Sandboxing) 
> 沙盒就是给应用程序建一个“围栏”，让它只能在里面活动，保护外面的系统安全。

 [[Linux VS Unix  --Similarities and Differences]] 

## Linux command line and bash scripting encyclopedia

### Part I chapter 1

2025.8.22 学习了该书的第一章至第三章 文件管理：cd ls touch cp ln | mv rm  | mkdir rmdir | cat more less


 ---

 🎗️Welcome to follow my GitHub : https://github.com/ArlesZhang/
