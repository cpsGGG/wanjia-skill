# 安装与使用 玩家.skill

## 运行要求

使用能够读取本地技能文件并执行 Python 的 Codex 环境。需要 Python **3.10或更新版本**；本次打包前实测 Python 3.13.5。技能的运行脚本和本版校验工具仅使用标准库，不需要安装第三方Python包。回答需要由模型按技能说明检索与理解，Python脚本自身不会自动生成完整建议。

本包是本地技能目录分发包。把ZIP附到一个没有本地执行能力的普通聊天窗口，不会自动安装技能，也不会自动启用本地检索。

## 安装到 Codex

解压后，**完整复制 `wanjia-skill` 文件夹**，包含其 `references`、`history`、`scripts` 和 `agents`；不要只复制 `SKILL.md`。

可选择一个位置：

- 仅当前项目使用：`<你的项目>/.agents/skills/wanjia-skill/`。
- 个人所有项目使用：`~/.agents/skills/wanjia-skill/`。Windows通常为 `%USERPROFILE%\.agents\skills\wanjia-skill\`。

如果已有同名技能，先备份旧目录再更换，避免把新目录复制到旧目录里面形成两层嵌套。本版不会替你写入全局目录或覆盖已安装技能。

Codex会自动发现技能变化；未出现时重新启动 Codex。界面名称为“玩家.skill”，显式调用名为 `$wanjia-skill`。路径、发现方式及界面字段依据 [OpenAI官方技能文档](https://learn.chatgpt.com/docs/build-skills)（核对日期2026-10-05）。

## 无需安装也可在项目里试用

保留解压目录，并向 Codex 说明：“先读取这个包的 `wanjia-skill/SKILL.md`，按其中方法分析我的问题。”这会明确入口；是否自动发现仍取决于目录是否位于上述技能位置。

## 手动检索与回读

以下命令在 `wanjia-skill` 目录中运行。Windows也可将 `python` 换成已配置好的 `py -3`，macOS/Linux可用 `python3`。脚本以自身位置找到数据，因此也可以传入脚本绝对路径，在其他目录执行。

```text
python scripts/search.py "吸引力" --limit 5
python scripts/search.py --id "o6fS0sTCYcU:K01" --full
python scripts/read_context.py --source-id "o6fS0sTCYcU" --sid "S01108" --before 3 --after 3 --knowledge-id "o6fS0sTCYcU:K01"
python scripts/action.py --id "action-pilot-basic-visible-presentation"
```

回读示例的SID表示定位到原文，不授予模拟口吻或动作许可。实际回答应使用命中结果的 `read_context_args`，必要时加精确 `--knowledge-id` 绑定当前可用 payload；先回读再下结论。`--before` 与 `--after` 的单位是连续文字段，不是秒。

普通检索用于发现和解释资料；`--persona-only` 只保留当前允许的模拟观点，`--action-only` 只保留有效有限动作 payload。`--posts-only` 搜社区文字证据，社区来源本身不能绕过知识使用约束。空结果时拆词、换词或按来源补搜。

## 验证包

在解压包根目录运行 `python tools/verify_package.py`，通过后再复制技能目录。验证会检查清单中每个文件的SHA-256、正式数据计数、知识来源对应、全文/分析路径及资源映射哈希。新生成的Python缓存不参与发布清单。

发布包中 `change-manifest.json` 和部分参考文件保留制作时的候选/构建状态。它们是原始阶段记录；本次打包状态以 `release.json` 和 `package-manifest.json` 为准。旧状态不能用来扩大回答许可。
