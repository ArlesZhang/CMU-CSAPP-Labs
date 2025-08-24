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


---


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

---

## Linux command line and bash scripting encyclopedia

——该书能带来的是收益：掌握 Bash/sed/gawk 不是“只能用在 Linux”，而是获得了 一种通用的“文本驱动 & 批处理”思维，可以迁移到：
- Windows（WSL2 / PowerShell）
- 云计算平台（大多数容器、集群都跑 Linux）
- 科研场景（自动化实验 → 复现实验 → 节省人力）
- 个人效率（日常文件/数据处理）

### 2025.8.22 学习日志
学习了该书的第一章至第三章 文件管理：cd ls touch cp ln | mv rm  | mkdir rmdir | cat more less tail head

### 2025.8.23 学习日志

今天的感悟：

- 之前我把 shell 仅仅当成“命令行工具”而不是“编程语言 + 环境”。其实 Bash 不仅仅是操作接口，它是：交互式接口（输入命令 → 系统执行 → 输出结果）。脚本语言（变量、条件、循环、函数、环境作用域…），能写复杂逻辑。
- 粘合剂（Glue Language）：能把 C 程序、Python、系统命令粘在一起，形成自动化流程。换句话说：Linux = 内核 + 用户态工具，而 Shell = 让你“编排”内核和工具的方式。
- Shell 知识以后会成为我学习 Makefile、CMake、Dockerfile、CI/CD 脚本、系统运维 的基石，绝不是“边角料”。

---

#### 1. 为什么说 Shell 是“粘合剂语言”

不同语言有不同定位：

| 语言               | 定位        | 特点                         | 局限                |
| ---------------- | --------- | -------------------------- | ----------------- |
| **C**            | 系统编程      | 高效、贴近硬件、可直接调用系统调用（syscall） | 开发速度慢，写复杂逻辑繁琐     |
| **Python**       | 高层应用      | 开发快、库丰富、易写算法/数据处理          | 性能一般，需要解释器        |
| **Shell (Bash)** | 调度 & glue | 能调度/组合任意可执行程序、做自动化、运维      | 算法和数据结构很弱，不适合复杂计算 |

所以：

* **C 负责造工具（高效二进制程序）**
* **Python 负责写逻辑（算法、脚本、数据分析）**
* **Shell 负责调度和自动化（把一堆工具组织成工作流）**

> 就像工厂流水线：
>
> * C 是造机器的工程师
> * Python 是设计生产工艺的工程师
> * Shell 是车间主任，把机器、工艺、人工协调成一个产线，能按计划自动运转

---

#### 2. 一个实际例子（结合 C、Python、Shell、CSAPP Labs）

假设你在做 **CSAPP 的 `bomb lab` 或 `malloc lab`**，你会遇到这样的场景：

#### **阶段1：C 语言部分**

你写了一个 C 程序（比如 `myprog.c`），编译成二进制：

```bash
gcc -O2 myprog.c -o myprog
```

它很快，但功能单一，比如输入数据 → 输出结果。

---

#### **阶段2：Python 部分**

你需要写个 Python 脚本做数据生成或结果分析，比如：

```python
# gen_input.py
import random
for i in range(10):
    print(random.randint(1, 100))
```

它能快速生成随机测试数据，但效率不如 C。

---

#### **阶段3：Shell 粘合**

你写个 `run.sh` 脚本，把两者串起来：

```bash
#!/bin/bash

# 1. 生成测试数据 (Python)
python3 gen_input.py > input.txt

# 2. 用 C 程序处理数据
./myprog < input.txt > output.txt

# 3. 自动检查结果
grep "ERROR" output.txt && echo "发现错误！" || echo "结果正常"
```

👉 这样，Shell 就把 **数据生成（Python） → 高效计算（C） → 结果检查（Shell 自带工具 grep）** 串成了一条流水线。

---

#### **阶段4：CSAPP Labs 应用**

* 在 `bomblab`，你可能要不断运行 `./bomb`，调试输入。
  Shell 可以写个循环自动化测试：

  ```bash
  for input in $(cat candidates.txt); do
      echo $input | ./bomb
  done
  ```
* 在 `malloc lab`，你可以用 Python 生成随机分配/释放序列，再由 C 程序跑 allocator，最后 Shell 自动收集日志和性能结果。

---

#### 3. 自动化流程的威力

你能靠 Shell + C + Python 搭建小型“流水线”：

📌 **例子：自动化测试 + 性能分析**

```bash
#!/bin/bash

for size in 100 1000 10000; do
    python3 gen_input.py $size > input.txt
    /usr/bin/time -f "%e" ./myprog < input.txt >> perf.log
done

echo "测试完成，结果在 perf.log"
```

这里 Shell 自动化完成了：

1. 调用 Python 生成不同规模输入。
2. 调用 C 程序跑实验。
3. 用 `time` 测试性能。
4. 把结果自动汇总到日志。

这就是科研实验/工程开发里 **最常见的“自动化实验流程”**。

---

#### 4. 和 CSAPP 的联系

CSAPP Labs，这里有几个核心联系：

| CSAPP 内容             | Shell 联系                    | 作用                              |                      |
| -------------------- | --------------------------- | ------------------------------- | -------------------- |
| **进程 & fork/exec**   | Shell 本质就是不断 fork/exec 子进程  | 理解 Shell = 理解操作系统调度             |                      |
| **I/O 重定向**          | `cmd < input > output`      | 实际就是调用 `dup2` 改变文件描述符           |                      |
| **管道 (pipe)**        | \`cmd1                      | cmd2\`                          | 对应 OS 的管道机制，多个进程数据传递 |
| **环境变量**             | `export VAR=value`          | 对应进程的 `environ[]`，和 `execve` 有关 |                      |
| **内存管理**             | Shell 调度的 C 程序用 malloc/free | Shell 是 orchestrator，不直接管内存     |                      |
| **网络编程 (proxy lab)** | Shell 可用 `nc`, `curl` 辅助调试  | 自动化测试网络服务                       |                      |

换句话说：**Shell 是从 CSAPP 理论走向实践的桥梁**。

---

#### 5. 学习路线（把 4 个要素串联起来）

1. **Shell 基础（Glue 能力）**

   * 学变量、条件、循环、函数
   * 学 `stdin/stdout/stderr`、重定向、管道
   * 学环境变量与 PATH

2. **C 程序作为“工具”**

   * 写小工具（比如字符串处理、加密、排序程序）
   * 交给 Shell 调用

3. **Python 作为“助手”**

   * 用 Python 写数据生成器 / 结果分析器
   * Shell 统一调度 Python + C

4. **CSAPP Labs 场景化实践**

   * `bomb lab`: Shell 循环输入测试
   * `malloc lab`: Python 生成 workload + Shell 自动跑
   * `proxy lab`: Shell 调用 `curl` 自动化压力测试

5. **进阶 → 形成科研“实验自动化框架”**

   * 未来做编译器优化实验，可以用 Shell 写一个完整 pipeline：

     * 自动生成测试模型
     * 调用 MLIR/TVM 编译器（C/C++）
     * 调用 Python 脚本跑 benchmark
     * Shell 收集结果、打包、出报告

---

#### 6. 关键结论

* **C**：造轮子，性能好。
* **Python**：做逻辑，开发快。
* **Shell**：粘合剂，把所有轮子组织成系统。
* **CSAPP Labs**：让你理解它们在系统层面的“底层原理”。
* Makefile、CMake、Docker —— 它们是把“能跑通的实验”升级成“别人也能一键复现的项目”的核心工具。

所以未来要做 **AI 编译器优化/系统实验**，一定是 **C/C++ 实现编译器核心** + **Python 调度和实验脚本** + **Shell 自动化管理流程**。

##### Shell 与 AI Agent 的对比与价值

✅ 最终认知：

> Shell 是底层稳定的“执行与编排语言”，不可替代。
> AI Agent 是高层“智能决策与任务分配者”。
> 两者不是竞争，而是上下协同。


#### 🔄 我的目标闭环（完整图景）

```
学习 & 实践 → 工具/实验闭环（C+Python+Shell+CSAPP） → 开源项目 → 技术博客输出（GitHub+Medium+知乎） → 论文产出（顶会） → 行业影响力（开源/社区） → 商业落地（职业/变现）
```
✅ 给自己的建议：
把这种思维落到一个实践框架，即：每学一样技术（比如 Bash、MLIR、分布式系统），都问自己 3 个问题：

- 它能解决哪些现实痛点？
- 我能否用它做一个小 demo/产品？
- 这个 demo 能否写成一篇有传播力的博客/知乎专栏/开源工具？

这样，每一步学习都会兼顾 技术深度 + 商业潜力 + 个人品牌。

### 2025.8.24 学习日志

今天学习了《Linux命令行与shell脚本编程大全》的第二、三部分 shell 脚本编程基础和进阶，大概理解了整体的知识框架和 shell 知识体系，为接下来的实操打下来基础；同时，我也了解到了shell 脚本编程能够给我带来的巨大收益！


 ---

 🎗️Welcome to follow my GitHub : https://github.com/ArlesZhang/
