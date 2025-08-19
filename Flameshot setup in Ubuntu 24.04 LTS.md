在 Ubuntu 24.04 LTS 中，Flameshot 的截图功能失效问题通常与 **Wayland 兼容性**或 **屏幕录制权限**有关。以下是针对你的问题的 **完整解决方案**：

---

### **1. 检查并安装 `xdg-desktop-portal` 组件**
确保 Wayland 下必需的组件已安装：
```bash
sudo apt update
sudo apt install xdg-desktop-portal xdg-desktop-portal-gnome xdg-desktop-portal-gtk
```
验证安装：
```bash
sudo dpkg -l | grep xdg-desktop  # 应显示已安装的组件
```

---

### **2. 禁用 Wayland（关键步骤）**
Ubuntu 24.04 默认使用 Wayland，而 Flameshot 在 Wayland 下可能不稳定。  
**永久切换至 Xorg**：
```bash
sudo nano /etc/gdm3/custom.conf
```
找到以下行并取消注释（删除 `#`）：
```ini
WaylandEnable=false
```
保存后重启：
```bash
sudo systemctl restart gdm3  # 或直接重启电脑
```
**注意**：登录时选择 **"Ubuntu on Xorg"** 会话（如有提示）。

---

### **3. 授予屏幕录制权限**
即使切换到 Xorg，仍需确保权限：
1. 打开 **Settings** → **Privacy** → **Screen Lock**。
2. 检查是否有 **"Screen Recording"** 选项，并允许 Flameshot。
   - 如果选项缺失，通过终端授权：
     ```bash
     gsettings set org.gnome.desktop.privacy disable-screencast false
     ```

---

### **4. 设置快捷键**
在 **Settings** → **Keyboard Shortcuts** 中添加自定义快捷键：
- **名称**: `Flameshot Screenshot`
- **命令**: `flameshot gui`
- **快捷键**: 例如 `F1` 或 `Ctrl+Shift+P`。

---

### **5. 验证修复**
- **终端测试**：
  ```bash
  flameshot gui  # 应正常弹出截图界面
  ```
- **快捷键测试**：按下设定的快捷键检查是否生效。

---

### **6. 其他可能问题**
- **Flatpak 版本冲突**：如果通过 Flatpak 安装，运行：
  ```bash
  flatpak override org.flameshot.Flameshot --talk-name=org.freedesktop.portal.Screenshot
  ```
- **依赖缺失**：修复依赖关系：
  ```bash
  sudo apt --fix-broken install
  ```

---

### **总结**
| 步骤 | 操作 | 命令/路径 |
|------|------|-----------|
| 1 | 安装必要组件 | `sudo apt install xdg-desktop-portal*` |
| 2 | 禁用 Wayland | `/etc/gdm3/custom.conf` → `WaylandEnable=false` |
| 3 | 设置权限 | `gsettings` 或图形界面 |
| 4 | 配置快捷键 | `Settings` → `Keyboard Shortcuts` |

---

Welcome to follow my GitHub : https://github.com/ArlesZhang/
