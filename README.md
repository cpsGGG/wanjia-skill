<p align="center">
  <img src="assets/cover.png" alt="玩家.skill：黑与洋红的原创城市封面，判断、表达、行动" width="100%" />
</p>

<h1 align="center">玩家.skill</h1>
<p align="center"><strong>把 Mikey 的判断和方法，带到你的具体问题里。</strong></p>

<p align="center">
  <a href="https://github.com/cpsGGG/wanjia-skill/releases/latest">下载安装</a> ·
  <a href="#开始提问">开始提问</a> ·
  <a href="docs/how-it-works.md">如何工作</a> ·
  <a href="README_EN.md">English</a>
</p>

玩家.skill 是一个基于「搭讪玩家」Mikey 资料的模拟问答 skill。它把视频、课程与帖子中的思想、判断和方法整理成可检索的知识，让你在面对吸引力、聊天、邀约和关系问题时，直接提问，听懂判断背后的理由，再决定下一步。

回答尽量贴近材料中的思考与表达，同时保留出处。它是依据资料的模拟，不代表 Mikey 本人发言或背书。

## 先看一段回答

**问：照片很多，怎么选出适合交友资料的照片？**

以下为依据材料的模拟示例，非逐字原话：

> 先别被照片数量带着走，关键是每张想让人看见什么。照片要么把你拍得帅、让人觉得你不错，要么传递你想表达的价值；同时要自然，修饰别把五官改成另一副样子。

用到交友资料，可以先挑一组，再逐张检查：这张表达了什么，见面时还能认出你吗？这一步是编者的情境应用，原讨论针对朋友圈，不保证配对结果。

出处：[《直播45：Mikey 撩妹答疑》](https://www.youtube.com/watch?v=f0gOZfoOhvo)，自然感[12:23](https://www.youtube.com/watch?v=f0gOZfoOhvo&t=743)、筛选标准[26:15](https://www.youtube.com/watch?v=f0gOZfoOhvo&t=1575)、修饰边界[34:52](https://www.youtube.com/watch?v=f0gOZfoOhvo&t=2092)。[完整示例与定位](docs/photo-example.md)。

## 它能帮你什么

| 你遇到的问题 | 它会做什么 |
| --- | --- |
| 道理听过很多，遇事还是不会判断 | 找到相关讨论，说明判断、理由和适用条件 |
| 两段建议看起来互相矛盾 | 比较当时的情境、目标和先后次序 |
| 想知道现在可以做什么 | 从已审定的方法里给出具体动作与观察点 |
| 想确认回答从哪里来 | 附来源与定位，支持回读前后文 |

当前资料库包含 **512条来源记录、3,649条知识**，覆盖长短视频、课程、直播与209条社区帖。来源记录包含复用和研究材料；收录量与可直接用于模拟回答的范围不同，具体见[资料与使用范围](docs/scope.md)。

## 三步安装

需要能读取本地文件、运行 Python 的 Codex 环境，以及 **Python 3.10+**。检索工具只用标准库。

1. 下载 [最新安装包](https://github.com/cpsGGG/wanjia-skill/releases/latest)，解压。
2. 将完整的 `wanjia-skill` 文件夹放到 `~/.agents/skills/wanjia-skill/`。Windows 对应 `%USERPROFILE%\.agents\skills\wanjia-skill\`；也可以放到当前项目的 `.agents/skills/`。
3. 在 Codex 中输入 `$wanjia-skill`，开始提问。未出现时重启 Codex。

请复制整个目录，包含知识库和脚本。更多安装方式见[安装说明](INSTALL.md)，发现路径依据[OpenAI官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

## 开始提问

```text
$wanjia-skill

我聊天总像查户口。请先问清会影响判断的信息，
再根据相关材料解释问题，给我一个可以尝试的下一步。
```

也可以从这些问题开始：

- 我自身条件不差，为什么和人互动还是很僵？
- 相册照片很多，怎么挑出适合交友资料的照片？
- 这两段关于需求感的说法看着矛盾，各自适用于什么情境？

把实际情境、你做过什么、对方的反馈一起说清楚，答案更容易落到具体判断。无需先整理一份完整报告。

## 回答如何形成

资料按需检索，相关原文会被回读；观点的理由、条件、人物归属和冲突一并保留。回答区分材料原有观点、跨来源整理和用于你当前情境的推测。有疑点的内容会保留限制，原始转写与校正记录也分开保存。

你可以直接使用，也可以检查它的判断过程、修正知识，或为某个问题补充更好的证据。实现与手动检索见[如何工作](docs/how-it-works.md)，参与改进见[贡献指南](CONTRIBUTING.md)。

## 出处与许可

原创代码和说明采用 [MIT](LICENSE)。人物原始文字、引文与图片保留原作者及第三方权利，详见[出处说明](THIRD_PARTY_NOTICES.md)；运行时允许某种回答，不等于材料获得了新的版权许可。资料仍有转写、身份与案例上下文待核，观点本身的现实效果也没有统一认证。

封面由 AI 生成。完整资料目录见[内容总表](CONTENTS.md)，版本变化见[更新记录](CHANGELOG.md)。
