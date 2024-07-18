**内容贡献者：** 寂静的羽夏

- [如何参与该项目](#%E5%A6%82%E4%BD%95%E5%8F%82%E4%B8%8E%E8%AF%A5%E9%A1%B9%E7%9B%AE)
- [项目结构](#%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84)
  - [递交注释格式](#%E9%80%92%E4%BA%A4%E6%B3%A8%E9%87%8A%E6%A0%BC%E5%BC%8F)
  - [回退分支](#%E5%9B%9E%E9%80%80%E5%88%86%E6%94%AF)
  - [类型](#%E7%B1%BB%E5%9E%8B)
  - [范围](#%E8%8C%83%E5%9B%B4)
  - [主题](#%E4%B8%BB%E9%A2%98)
  - [正文](#%E6%AD%A3%E6%96%87)
  - [脚注](#%E8%84%9A%E6%B3%A8)
- [注意事项](#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)
- [FAQ](#faq)
  - [软件使用](#%E8%BD%AF%E4%BB%B6%E4%BD%BF%E7%94%A8)
  - [编译相关](#%E7%BC%96%E8%AF%91%E7%9B%B8%E5%85%B3)
  - [其他](#%E5%85%B6%E4%BB%96)

## 如何参与该项目

&emsp;&emsp;目前该项目由寂静的羽夏主导且是唯一开发者，我首先表达对你想要参与开源贡献的行为表示感谢。

&emsp;&emsp;如果你是短期参与贡献或者不想和作者联系，你可以自己 fork 该仓库，并修改完毕代码之后保证与我的最新仓库仅仅提前一次 commit，然后向该仓库提 Pull requests，我会亲自审核并及时做出反应。

&emsp;&emsp;如果你想要长期和作者（我）一起开发项目，并且你和我在现实世界很熟悉的话，你可以向我索要仓库权限，我可以给你放开。

## 项目结构

&emsp;&emsp;该仓库之后将会保持`main`和`release`两个分支，第一个分支是不稳定分支，我会根据我的空余时间会持续更新软件。后者是稳定发行版分支，到了我预定冻结功能和发行的时候，我会将`main`的修改合并到`release`分支。

项目目录结构详细分类如下：

- `3rdparty`：使用的第三方库会放到这里面。
- `images`: 程序使用的图片资源。
- `lang`: 程序的语言本地化文件，里面文件夹以国际标准化代码来指示一种语言支持。
- `mkinstaller`: 打包发行版工具，里面的文件夹以生成的文件为名表示支持的安装包类型。
- `src`: 软件源码。
  - `class`: 所有的通用功能代码类。
  - `control`: 控件相关代码。
  - `dialog`: 界面类。
  - `model`: `Model-View`中使用的数据模型。
  - `plugin`: 插件相关的类。
  - `scriptaddon`: 为`AngelScript`提供额外功能的绑定类。
  - `settings`: 设置相关代码。
  - `widgetframe`: 和无边框界面标题栏相关的代码。
- `theme`: 软件主题文件，里面每个文件夹以主题名命名（必须英文）。

### 递交注释格式

&emsp;&emsp;每条提交消息都由**标题（header）**、**正文（body）**和**页脚（footer）**组成。标题具有特殊格式，其中包括**类型（type）**、**范围（scope）**和**主题（subject）**：

```bash
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

&emsp;&emsp;**标题（header）** 是强制性的，而 **范围（scope）** 是可选的。提交消息的任何一行都不能超过 100 个字符！这使得消息在 GitHub 以及各种 git 工具中更容易阅读。如果 **正文（body）** 存在， **空行（BLANK LINE）** 是必须的。

&emsp;&emsp;如果有的话，页脚（footer）应包含 [将拉取请求链接到议题](https://help.github.com/articles/closing-issues-via-commit-messages/)。

&emsp;&emsp;举个例子：

```bash
docs(changelog): update changelog to beta.5
```

```bash
fix(release): need to depend on latest qt5

The version in our package.json gets copied to the one we publish, and users need the latest of these.
```

### 回退分支

&emsp;&emsp;如果提交撤销了之前的提交，则它应该以`revert:`开头，后跟撤销的提交的标题。在正文中，它应该写着：`这将撤销提交 <hash>`，其中哈希是被撤销的提交的 SHA。

### 类型

&emsp;&emsp;必须是下列之一：

- **build**: 影响构建系统或外部依赖项的更改
- **ci**: 更改 CI 配置文件和脚本
- **docs**: 仅文档更改
- **feat**: 新功能
- **fix**: 缺陷修复
- **perf**: 修改代码得到性能提升
- **refactor**: 代码更改既没有修复错误也没有添加功能
- **style**: 不影响代码含义的更改（空格、格式、缺少分号等）
- **test**: 添加缺失的测试或更正现有的测试

### 范围

&emsp;&emsp;范围是可选的，它通常会更加详细的指示了影响的范围，可以是分支名，也可以是版本号（比如 v1.0.0），也可以是如下几种类型：

- **changelog**: 用于更新 CHANGELOG.md 中的发布说明 / used for updating the release notes in CHANGELOG.md
- **readme**: 用于更新 README 中的内容 / used for updating the contents of README
- **license**: 用于更新 LICENSE 中的内容 / used for updating the contents of LICENSE

### 主题

&emsp;&emsp;主题包含对变更的简洁描述。

### 正文

&emsp;&emsp;正文应该包括改变的目的并将其与之前的行为进行对比。如果在一次提交中有多种类型的修改内容，也可以按照标题的形式写到 **正文（body）** 里面。

### 脚注

&emsp;&emsp;页脚应包含有关**重大变更**的任何信息，也是引用此提交**关闭**的 GitHub 问题的地方。

&emsp;&emsp;**重大变更** 应以单词 `BREAKING CHANGE:` 开头，中间有一个空格或两个换行符。提交消息的其余部分将用于此目的。

## 注意事项

&emsp;&emsp;您提供的代码将会遵守`AGPL-3.0`协议，第三方库将会遵守作者的开源协议。开源虽无国界，但您提供的代码来源请一定确保可靠性，不违反法律法规，不包含政治相关内容，不包含侵犯其他人或公司合法权益的代码。否则开源就是个笑话。**当你向仓库提交任何形式的代码，默认表示同意以上声明，且自愿承担因为自己的代码提交的一切责任。**

&emsp;&emsp;所有的 PR 合并都需要通过 CI 检查，请注意你的**代码格式化规范**和代码提交说明是否遵循**最基础的约定式提交标准**。

&emsp;&emsp;最后，再次感谢您对开源的支持和帮助。

## FAQ

### 软件使用

1. 为啥不在搜索结果增加筛选排列功能（其他表格类控件同理）：

    答：功能很好，但是在数据量很大的情况下，很卡，但我没有精力和经验来处理这个事情。

2. 在 Linux 下我直接 clone 仓库编译不通过：

    答：如果你 QT 和 CMake 都装好的话，本软件使用的布局组件 Qt-Advanced-Docking-System 有依赖需要装好，请详细看一下它的 ReadMe。当然你也要注意你的 QT 版本。

3. 该软件和 WingHexExplorer 有什么区别，我还可以继续使用 WingHexExplorer 这个软件吗？

    答：新版软件具有更强大的布局组件、跨平台和 UI 统一性。功能上自带 AngelScript 脚本引擎，相比于 Python 可能会有更好的 API 兼容性和速度（未测试），并且可以具有更好的 API 权限管控，会更安全一些。还有它更擅长处理多文件编辑，你可以对同一个文件同时在不同位置进行预览/编辑，这就是“克隆”功能。十六进制编辑器还增加了 Ctrl + 鼠标滚轮原生缩放支持。该软件对任意编辑中的文件窗体隐藏，哈希值计算，对书签更好的可视化以及标记的可视化和更好的插件支持，以及进一步的 Bug 修复。在 v2.0.0 规划完成发布之后，还会有深度配合的代码编辑器和调试器，正好是一个小型的 AngelScript IDE。这些都是 WingHexExplorer 软件所不具备的功能，这里还有很多小细节没说，这个软件会更加专业，也会更加好用。

    WingHexExplorer 这个软件仍旧是能用的，但还是有点小 Bug，只要你不是深度使用是不会有问题的，比如预览和简单的编辑普通文件。但它有 Bug，我也不会去修了。

4. 该软件和 WingHexExplorer 兼容吗？

    答：项目文件是可以兼容的，但插件还是按照老约定，采用不兼容处理，因为变化太大了。

5. 为什么不能够在有标注的情况下增删字节？

    答：因为内部是通过偏移决定标注的渲染，你增删了但我没有额外处理肯定会偏移导致不准了，这需要你手动修改了。不过在 v3.0.0 规划中决定完善这个功能，解除这个限制提醒。

### 编译相关

1. 使用版本较低的编译器，发现默认项目配置下编译不通过，报错如下：

   ```cpp
    ~/WingHexExplorer2/3rdparty/qwindowkit/qmsetup/src/corecmd/main.cpp: In function 'void copyDirectory(const std::filesystem::__cxx11::path&, const std::filesystem::__cxx11::path&, const std::filesystem::__cxx11::path&, bool, bool, const std::function<bool(const std::filesystem::__cxx11::path&)>&)':
    ~/WingHexExplorer2/3rdparty/qwindowkit/qmsetup/src/corecmd/main.cpp:173:40: error: 'std::__cxx11::string' {aka 'class std::__cxx11::basic_string<char>'} has no member named 'starts_with'
                      linkPath.string().starts_with(srcRootDir.string())
                                        ^~~~~~~~~~~
    make[2]: *** [src/corecmd/CMakeFiles/qmcorecmd.dir/build.make:76: src/corecmd/CMakeFiles/qmcorecmd.dir/main.cpp.o] Error 1
   ```

    答：该模块是用于无边框模块，用于保证 UI 一致性的。可以解决某系统的标题栏大额头问题以及其他系统提供标题栏不好看问题。你可以将选项`WINGHEX_USE_FRAMELESS`关闭清除缓存并重新执行 CMake，这样之后仅仅会使用系统标题栏。如果你实在想整上这功能，请升级编译器。当然你可以试试向原作者提个 issue 寻求支持一下。

### 其他

1. 这个软件作者（寂静的羽夏）是不是个大鸽子？
  
    答：通常情况是的。但有时候他会很勤奋，会日更一段时间。有时候迫于生活，销声匿迹一段时间。

2. 请问我想打包，需要作者（寂静的羽夏）授权吗？

    答：不需要，甚至你不需要告诉我，但需要遵守一些约定。详情请看仓库 README

---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="images/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可。
