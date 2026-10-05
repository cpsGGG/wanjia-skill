# 如何工作

玩家.skill由人物指南、资料库和本地检索工具组成。模型负责理解你的情境、比较材料并形成回答；Python脚本负责查找与回读，不会独立生成完整建议。

## 从问题到回答

1. 追问会改变判断的信息：情境、已做行为、对方反馈和你想解决的问题。
2. 拆词检索相关知识，再读取完整理由、条件和限制。
3. 回读连续原文，区分提问、本人观点、嘉宾观点、转述和假设。
4. 比较不同来源中的共同点、差异和先后关系。
5. 依照已审定的具体范围形成模拟回答；需要时给出动作与观察点，附出处。

入口是 `wanjia-skill/SKILL.md`。无需每次加载全部资料，也不依赖制作时使用的网页账号或研究目录。

## 手动使用工具

在 `wanjia-skill` 目录中运行：

```sh
python scripts/search.py "聊天" --limit 5
python scripts/search.py "照片" --action-only --limit 5
python scripts/search.py --id "action-pilot-visible-photo-selection" --full
python scripts/action.py --id "action-pilot-visible-photo-selection"
```

命中结果提供 `read_context_args`；依照其来源和SID运行 `read_context.py`。若使用有限子条，传入精确 `--knowledge-id` 绑定对应的回读范围。`--before` 和 `--after` 是文字段数，不是秒。

`--persona-only` 筛选当前允许有限模拟表达的对象；`--action-only` 筛选有效动作载荷。普通搜索用于发现资料，命中本身不授予模拟或建议权限。

## 转写与校正

原始自动稿继续保留。已有校正候选在回读结果中单列，显示真实状态与未决原因；遇到 `correction_review_required=true`，不能只看裸 `text` 下结论。网页音频支持、独立本地听校、人物身份和准确引语分别记录。

## 验证和打包

在仓库或安装包根目录运行：

```sh
python -B tools/verify_package.py
python -B tools/smoke_check.py
python -B tools/package_release.py --output dist/wanjia-skill-v0.2.1.zip
```

校验检查文件清单、字节哈希、来源关系、本地资源与当前许可；运行检查覆盖校正提醒及动作拒绝路线。文件和运行通过不代替思想准确性、音画核验、人物身份或实际效果验收。
