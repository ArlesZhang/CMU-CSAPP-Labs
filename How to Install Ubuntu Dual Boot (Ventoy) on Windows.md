### Windows 上安装 Ubuntu 双系统 (Ventoy )全流程
```
1️⃣ 制作 Ventoy 启动盘  
    ├─ 下载 Ventoy（官方推荐）  
    ├─ 安装 Ventoy 到 U 盘（格式化 U 盘）  
    └─ 拖入 Ubuntu ISO 文件到 U 盘根目录  

2️⃣  启动 Ubuntu 安装程序  
    ├─ 进入 BIOS → 设置 UEFI 模式（关闭 Secure Boot，如必要）  
    ├─ 设置 U 盘为首选启动项  
    └─ 重启 → Ventoy 菜单 → 选择 Ubuntu 镜像启动   

3️⃣ 安装 Ubuntu  
    ├─ 选择 “Interactive Installation” → “Default Selection”  
    ├─ 安装推荐驱动（第三方 Wi-Fi / 显卡 驱动）  
    └─ 分区安装：  
        ├─ 自动使用空闲空间，或手动设置：  
        │   ├─ `/` 根目录（50GB+）  
        │   ├─ `/home` 用户目录（可选）  
        │   └─ `swap` 交换空间（4-8GB）  
        └─ 引导项：安装 GRUB 引导器 

	分区准备（这一步在步骤3一起完成，很简单）
    ├─ 保留原有 Windows 分区（如 C、D）  
    └─ 缩减空间，为 Ubuntu 预留空白分区（建议 100GB+）

4️⃣ 安装完成后（注意：先拔U盘 → 再重启）  
    ├─ 系统提示：拔出安装介质（即拔出 U 盘）  
    └─ 重启电脑，GRUB 菜单出现，支持选择 Ubuntu 或 Windows 启动  

✅ 成功切换双系统！
```

### 使用 Ventoy 制作启动 U 盘（详细步骤）

#### 步骤 1：准备工作

1. **下载 Ventoy**：
    
    - 访问 [Ventoy 官网](http://ventoy.net/en/download.html) 下载适用于 Windows 系统的版本（通常是一个 `.zip` 文件）。
    - 解压并运行 **Ventoy**。
        
2. **下载 Ubuntu ISO 文件**：
    
    - 访问 [Ubuntu 官方下载页面](https://ubuntu.com/download) 下载最新版本的 Ubuntu ISO 文件（建议下载 LTS 版本，长期支持版）。
        
3. **准备 U 盘**：
    
    - 准备一个 **8GB 或更大容量的 U 盘**，并确保里面没有重要数据，因为操作会格式化 U 盘。
  
---

#### 步骤 2：使用 Ventoy 制作启动 U 盘

1. **插入 U 盘**：
    
    - 将你的 U 盘插入电脑的 USB 端口。
        
2. **运行 Ventoy**：
    
    - 双击打开 **Ventoy** 程序（通常是 `Ventoy2Disk.exe`）。
        
3. **选择 U 盘**：
    
    - 在 Ventoy 界面的 **设备** 选项中，选择你的 U 盘。
        
4. **安装 Ventoy 到 U 盘**：
    
    - 点击 **安装** 按钮，Ventoy 会将 U 盘格式化并安装启动环境。
    - 安装完成后，Ventoy 会提示你 U 盘已准备好，直接点击 **确定**。
        
5. **将 Ubuntu ISO 文件拖入 U 盘**：
    
    - 打开你的 U 盘目录（在 Windows 文件资源管理器中）。
    - 将下载好的 **Ubuntu ISO 文件** 拖入 U 盘中（Ventoy 会自动识别该文件）。
    
    这样，U 盘就可以直接启动 Ubuntu 了。
    

以上是前置程序的安装：↑

---

以下是电脑环境的设置：↓

#### **步骤 3：进入 BIOS 设置并启动 Ubuntu 安装程序**

1. **重启电脑**：
    
    - 重启你的电脑，并在启动时按下进入 BIOS 设置的快捷键（常见的有**dell 电脑： F2**、其他电脑：**Del** 或 **ESC**，具体按键可以参考你的主板手册或在开机时看启动画面提示）。
    
2. **进入 BIOS 设置**：
	
    - 在 BIOS 中，找到 **Boot** 或 **启动设置** 菜单，开始下面三步：
    
	1. **设置 UEFI 启动模式**：
    
	    - 确保 **UEFI** 启动模式已经启用。如果你的 BIOS 还支持传统的 **Legacy（CSM）** 启动模式，请确保禁用 **CSM**（即禁用传统启动模式），选择 **UEFI** 启动。
        
	2. **禁用 Secure Boot：** 
    
	    - 在某些系统中，Ubuntu 可能无法在启用了 **Secure Boot**（安全启动）的情况下启动。在 BIOS 中禁用 **Secure Boot** 
    
	3. **选择从 U 盘启动**：
    
	    - 在 BIOS 启动菜单中，选择你的 **U 盘** 作为启动设备。
        
        - 如果你有多个 U 盘插入，确保选择正确的 U 盘（你放置 Ubuntu ISO 文件的那个 U 盘）。
        - 选择后，保存并退出 BIOS。
            
3. **进入 Ubuntu 安装界面**：
    
    - 电脑会从 U 盘启动并进入 Ubuntu 安装界面，接下来你就可以按照提示开始安装 Ubuntu 系统了。
	
- 如果你已经将 Ubuntu ISO 文件放入 U 盘中并完成了 Ventoy 设置，接下来就是从 U 盘启动并开始安装 Ubuntu。

---

#### **步骤 4：安装 Ubuntu（选择双系统）**

1. **启动 Ubuntu 安装程序**：
    
    - 当 U 盘启动时，你将看到 Ubuntu 的安装界面，选择 **“安装 Ubuntu”**。
    - 进入 Ubuntu 安装界面，选择 **Try Ubuntu** 或 **Install Ubuntu** 开始安装流程。
    
2. **选择安装语言**：
    
    - 在安装过程中，选择你希望使用的语言，例如 **中文** 或 **英语**。

  Forlow My GitHub：https://github.com/ArlesZhang/ 
