# Ubuntu From Beginner to Master

----系统开发指南（配合CSAPP & 顶会计划）

## 🗂 总览结构图

### Ubuntu 新手知识地图-图解

#### Bash From beginner to Master
```txt
终端命令
├── 文件操作：ls, cd, mv, cp, rm, mkdir
├── 权限管理：sudo, chmod, chown
├── 软件安装：apt, dpkg, snap
├── 编辑器：nano, vim, code
├── 编译工具：gcc, make, gdb
├── 网络命令：ping, curl, ssh
├── 进程控制：ps, top, kill, htop
└── 其他：man（帮助文档）, echo, cat,less,grep,egrep
```

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
