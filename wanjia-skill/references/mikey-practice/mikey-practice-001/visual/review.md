# mikey-practice-001 正式视觉复核记录

## 范围

- 来源：`shizhan/1.搭讪西装正妹，快速带回家.mp4`，容器时长 `351.712993` 秒。
- 本正式分析引用此前视觉小样的实际检查：50个低清候选、1张标准联系表、3张大联系表全部查看；另回抽6个原尺寸节点，最终只保留2张脱敏帧。
- 这是静帧序列与原帧检查。没有连续播放任何片段，也没有听原音，所以 `audio=pending`、`visual=sampled`，连续视觉核验秒数为0。
- 证据目录：`research/shizhan/visual-pilot/items/mikey-practice-001/visual/`。正式 `items/mikey-practice-001/visual/` 中的另一批候选没有被本任务冒称为已看。

```jsonl
{"review_id": "mikey-practice-001-V0001", "source_id": "mikey-practice-001", "source_revision": "sha256:fae6740d9f1fcf6d17a8dd23bcbcf619d81d945abdcca7740409c557993165e9", "start": 0.0, "end": 351.712993, "method": "contact_sheet", "frame_ids": ["survey/survey-0001.jpg", "survey-large/survey-large-001.jpg", "survey-large/survey-large-002.jpg", "survey-large/survey-large-003.jpg"], "reviewer": "local_subagent", "status": "checked", "finding": "查看全部50个候选，最长候选间隔10秒；用于场景与剪切定位，不支持连续动作。", "affected_event_ids": ["mikey-practice-001-E0001", "mikey-practice-001-E0002", "mikey-practice-001-E0003", "mikey-practice-001-E0004", "mikey-practice-001-E0005", "mikey-practice-001-E0006", "mikey-practice-001-E0007", "mikey-practice-001-E0008", "mikey-practice-001-E0009"]}
{"review_id": "mikey-practice-001-V0002", "source_id": "mikey-practice-001", "source_revision": "sha256:fae6740d9f1fcf6d17a8dd23bcbcf619d81d945abdcca7740409c557993165e9", "start": 38.0, "end": 38.0, "method": "original_frame", "frame_ids": ["research/shizhan/items/mikey-practice-001/visual/selected-fullres-redacted/001-00-00-38-opening-space-and-distance-redacted.jpg"], "reviewer": "local_subagent", "status": "checked", "finding": "双方在墙边面对面停留，通道开放；不能证明真实开场。", "affected_event_ids": ["mikey-practice-001-E0002"]}
{"review_id": "mikey-practice-001-V0003", "source_id": "mikey-practice-001", "source_revision": "sha256:fae6740d9f1fcf6d17a8dd23bcbcf619d81d945abdcca7740409c557993165e9", "start": 158.0, "end": 158.0, "method": "original_frame", "frame_ids": ["research/shizhan/items/mikey-practice-001/visual/selected-fullres-redacted/002-00-02-38-contact-exchange-redacted.jpg"], "reviewer": "local_subagent", "status": "checked", "finding": "双方同时操作手机，屏幕不可读。", "affected_event_ids": ["mikey-practice-001-E0005"]}
{"review_id": "mikey-practice-001-V0004", "source_id": "mikey-practice-001", "source_revision": "sha256:fae6740d9f1fcf6d17a8dd23bcbcf619d81d945abdcca7740409c557993165e9", "start": 309.0, "end": 309.0, "method": "original_frame", "frame_ids": [], "reviewer": "local_subagent", "status": "checked", "finding": "女方转身沿街离开；未遮挡临时帧在核对后删除。", "affected_event_ids": ["mikey-practice-001-E0009"]}
{"review_id": "mikey-practice-001-V0005", "source_id": "mikey-practice-001", "source_revision": "sha256:fae6740d9f1fcf6d17a8dd23bcbcf619d81d945abdcca7740409c557993165e9", "start": 311.0, "end": 342.0, "method": "original_frame", "frame_ids": [], "reviewer": "local_subagent", "status": "checked", "finding": "抽查确认街景后硬切到结果宣称、聊天拼图和品牌片尾；敏感画面未保存或描述。", "affected_event_ids": ["mikey-practice-001-E0009"]}
```

## 场景／切换

文件0秒已经在交谈。00:16—00:28插入带“次日约会结束”编辑字样的片段，随后回到墙边长谈；约05:09女方离场，约05:11切到结果宣传。发布文件没有连续展示陌生接近、移动到约会场所或“带回家”过程。

## 角色

画面可区分男性发起者 `P01` 与女性参与者 `P02`。没有完成声音锚定或现实身份确认；现场男性不能自动当作Mikey，事件中的说话人状态全部保持 tentative／unknown。

## 重点动作／消息

- 00:38：双方在临街墙边面对面停留，空间未封堵通道。
- 02:38：双方同时低头操作手机。画面支持手机操作节点，不支持具体账号、屏幕内容或添加成功。
- 05:09：女方转身离开，随后切营销画面。
- 尾段聊天拼图字号不足且含隐私，没有读取角色顺序或具体内容。

## 画面对文字的新增或纠正

1. 片名和结果文案不能代替过程证据：现场主体只显示街边长谈、手机操作和分开离场。
2. 00:16—00:28是编辑插片，现实时间顺序被重排。
3. 静帧可见对方持续停留，但不能据此把每句回应都判作强兴趣。
4. “陌生人之间不要这么亲密”是关键边界句；静帧无法确认触发动作，必须保留待核。

## 隐私

只保留两张方法理解所需的脱敏帧，脸、联系方式和手机屏幕均已遮挡。未遮挡原尺寸临时帧已删除。尾段私密空间与聊天拼图只登记其编辑功能，不保存、不描述露骨内容，也不导出。

## 待核

详见 `review-needed.md`：优先回看93—113秒的边界触发与调整、143—171秒的手机操作目的，以及确认308秒后营销素材是否属于同一案例。未解决前不得把片名结果或现场者身份写成确定事实。
