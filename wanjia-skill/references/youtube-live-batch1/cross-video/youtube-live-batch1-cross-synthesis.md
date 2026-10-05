# YouTube 公开直播第01批跨期思想综合（post-audit 修订版）

## 使用说明与证据边界

本文件以 `youtube-live-batch1-cross-input-post-audit.json` 为唯一逐期知识基线，并使用 `cross-audit.json` 记录审计加固。没有听原音，没有连续观看视频，也没有修改任何本地 skill。输入中的自动稿、稀疏视觉巡查、人物注册、事件、知识对象与待核对象保持原有证据等级；跨期综合只做编辑归纳，不能把机械追溯、跨期重复或稀疏画面升级成真实逐字录音、连续画面事实、因果关系或人物归属证明。

运行时的硬规则是：只有本综合 `knowledge_index.use_level=direct` 的知识，才可支撑“Mikey 会怎么判断/怎么做”的第一人称行动部分。`context_only` 只能解释背景；`hold`、`do_not_generalize`、`mixed_speakers`、`attributed_other` 或关联 open blocking 的知识不能作为第一人称建议证据。Mikey 代读观众问题时，声音可以是 Mikey，但问题作者仍是观众；caller、guest、viewer、screen material、unknown/mixed voice 的独有内容不能写成 Mikey 的经历或观点。

## 批次范围、审计状态与运行时统计

- 输入范围：10 期；自动稿段 25936；事件 351；知识 266；knowledge quotes 1501。
- 待核：178；其中 blocking 78；major 99。
- post-audit 逐期状态：candidate_only 196；hold 66；do_not_generalize 4。人物归属：explicit_mikey 229；mixed_speakers 36；attributed_other 1。
- 本跨期运行时分级：direct 68；context_only 71；hold 123；do_not_generalize 4；合计 266。
- 审计加固记录：claims 未改写；candidate_only→hold 记为 35 条；explicit_mikey→mixed_speakers 记为 16 条；全部 78 个 blocking review 仍为 open。
- 跨期成稿实际 `use_level` 变化 17 条；该数与逐期基线的 35 条 release 加固不是同一个口径，因为上一版跨期稿已提前把部分 mixed/blocking 知识放在 hold。

### 各来源运行时分级

| source_id | direct | context_only | hold | do_not_generalize | total |
|---|---:|---:|---:|---:|---:|
| `mikey-youtube-live-001` | 11 | 8 | 8 | 0 | 27 |
| `mikey-youtube-live-002` | 11 | 3 | 28 | 4 | 46 |
| `mikey-youtube-live-003` | 0 | 0 | 16 | 0 | 16 |
| `mikey-youtube-live-004` | 13 | 0 | 7 | 0 | 20 |
| `mikey-youtube-live-005` | 0 | 15 | 4 | 0 | 19 |
| `mikey-youtube-live-006` | 16 | 1 | 7 | 0 | 24 |
| `mikey-youtube-live-007` | 0 | 23 | 6 | 0 | 29 |
| `mikey-youtube-live-008` | 0 | 20 | 5 | 0 | 25 |
| `mikey-youtube-live-009` | 19 | 0 | 7 | 0 | 26 |
| `mikey-youtube-live-010` | 15 | 0 | 19 | 0 | 34 |

### 10 个来源

- `mikey-youtube-live-001`｜直播5：内部群的电话会议 mikey在线解答兄弟们的把妹问题，认真回答不敷衍。 丨dating in china丨恋爱丨约会丨搭讪丨自我提升丨脱单｜27 知识｜31 事件｜published_date `2024-01-07`。
- `mikey-youtube-live-002`｜直播9：内部群的电话会议 mikey在线解答兄弟们的把妹问题，认真回答不敷衍。 丨網聊丨dating in china丨恋爱丨约炮丨搭讪丨自然流丨脱单｜46 知识｜77 事件｜published_date `2024-02-29`。
- `mikey-youtube-live-003`｜直播11： Mikey：内部直播群会议，认真答疑不敷衍，快进来唠嗑！｜16 知识｜29 事件｜published_date `2024-04-04`。
- `mikey-youtube-live-004`｜直播19：mikey与兄弟们见见面｜约会｜搭讪 ｜两性｜20 知识｜32 事件｜published_date `2024-07-10`。
- `mikey-youtube-live-005`｜直播29：泡妞问题答疑 看看有没有你需要的知识｜19 知识｜20 事件｜published_date `2024-10-31`。
- `mikey-youtube-live-006`｜直播30：调动情绪｜24 知识｜31 事件｜published_date `2024-11-07`。
- `mikey-youtube-live-007`｜直播36：如何跟女人聊天 答疑解惑｜29 知识｜40 事件｜published_date `2024-12-29`。
- `mikey-youtube-live-008`｜直播44：两性情感 泡妞 搭讪 约会丨搭讪玩家TV｜25 知识｜38 事件｜published_date `2025-03-06`。
- `mikey-youtube-live-009`｜直播45：Mikey 撩妹答疑丨搭讪玩家TV｜26 知识｜28 事件｜published_date `2025-03-08`。
- `mikey-youtube-live-010`｜直播46：兩性情感 泡妞 搭訕 約會丨搭訕玩家TV｜34 知识｜25 事件｜published_date `2025-03-09`。

## post-audit 加固对跨期使用的直接影响

本轮不是重写逐期 claim，而是收紧“谁说的、能不能直接用”。特别是 `mikey-youtube-live-003` 的 16 条知识全部为 `mixed_speakers / hold`，直到全片 blocking 人物归属复核完成；它们仍可用于说明本期涉及过哪些主题，但不能支持“Mikey 会这样做”的第一人称回答。直播001、002、006、010中审计加固的条目同样按新基线传播。

- `mikey-youtube-live-001-K007`：`context_only` → `hold`；新基线 release=`hold`，attribution=`explicit_mikey`；blocking=无。
- `mikey-youtube-live-001-K008`：`direct` → `hold`；新基线 release=`hold`，attribution=`explicit_mikey`；blocking=无。
- `mikey-youtube-live-001-K017`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-001-K024`：`context_only` → `hold`；新基线 release=`hold`，attribution=`attributed_other`；blocking=无。
- `mikey-youtube-live-002-K011`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K014`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K015`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K022`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K027`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K028`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K034`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K035`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K036`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K037`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K043`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K044`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。
- `mikey-youtube-live-002-K045`：`context_only` → `hold`；新基线 release=`hold`，attribution=`mixed_speakers`；blocking=无。

## direct-major 语义抽查

本轮逐条抽查 35 条 direct-major 交叉项：保留 direct 18 条，降为 context_only 1 条，降为 hold 16 条。

第009、010期的多条观点可在原始可引用稿其他位置找到，但当前事件或 claim_evidence_refs 指到无关句子；这些条目在重新定位、重绑证据并复核 major 边界前不得支撑第一人称建议。逐条理由见 `direct-major-semantic-audit.md/json`。
## 跨期核心主题

### T01 · 自我接纳、状态与内在稳定

**判断：** 先处理对当下状态的抵抗，再行动；稳定不是持续高能量，而是能在焦虑、低能量、冷场或失败时仍保持自我支持。

**理由：** 把焦虑、紧张、低能量和失败从“必须先消除”改成“先承认、再行动”；通过日常专注、冥想或小任务辅助回到当下。

**方法顺序：** 识别当下状态 → 停止自我攻击 → 允许状态存在 → 完成一个可执行动作 → 根据结果复盘

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 若建议需要把未核人物归属、数字结果、法律/医疗判断或案例结果当事实，则停止并转入待核。

**运行时证据分层：** direct 13；context_only 22；hold 26；do_not_generalize 0。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-001-K010`, `mikey-youtube-live-001-K020`, `mikey-youtube-live-002-K008`, `mikey-youtube-live-002-K017`, `mikey-youtube-live-004-K0017`, `mikey-youtube-live-004-K0019`, `mikey-youtube-live-006-K0009`, `mikey-youtube-live-006-K0016`, `mikey-youtube-live-009-K0010`, `mikey-youtube-live-009-K0026`, `mikey-youtube-live-010-K0005`, `mikey-youtube-live-010-K0007`, `mikey-youtube-live-010-K0008`

**受限知识：** context_only=`mikey-youtube-live-001-K018`, `mikey-youtube-live-001-K019`, `mikey-youtube-live-005-K002`, `mikey-youtube-live-005-K007`, `mikey-youtube-live-005-K008`, `mikey-youtube-live-005-K011`, `mikey-youtube-live-005-K015`, `mikey-youtube-live-005-K018`, `mikey-youtube-live-007-K002`, `mikey-youtube-live-007-K005`, `mikey-youtube-live-007-K007`, `mikey-youtube-live-007-K009`, `mikey-youtube-live-007-K012`, `mikey-youtube-live-007-K013`, `mikey-youtube-live-007-K026`, `mikey-youtube-live-007-K028`, `mikey-youtube-live-007-K029`, `mikey-youtube-live-008-K006`, `mikey-youtube-live-008-K007`, `mikey-youtube-live-008-K012`, `mikey-youtube-live-008-K015`, `mikey-youtube-live-008-K021`；hold=`mikey-youtube-live-002-K001`, `mikey-youtube-live-002-K003`, `mikey-youtube-live-002-K015`, `mikey-youtube-live-002-K028`, `mikey-youtube-live-002-K035`, `mikey-youtube-live-002-K039`, `mikey-youtube-live-002-K040`, `mikey-youtube-live-004-K0003`, `mikey-youtube-live-005-K017`, `mikey-youtube-live-006-K0022`, `mikey-youtube-live-007-K020`, `mikey-youtube-live-007-K025`, `mikey-youtube-live-009-K0007`, `mikey-youtube-live-009-K0014`, `mikey-youtube-live-009-K0019`, `mikey-youtube-live-010-K0001`, `mikey-youtube-live-010-K0002`, `mikey-youtube-live-010-K0006`, `mikey-youtube-live-010-K0009`, `mikey-youtube-live-010-K0014`, `mikey-youtube-live-010-K0016`, `mikey-youtube-live-010-K0018`, `mikey-youtube-live-010-K0020`, `mikey-youtube-live-010-K0022`, `mikey-youtube-live-010-K0026`, `mikey-youtube-live-010-K0032`；do_not_generalize=无。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-001-K010` → `mikey-youtube-live-001-E0014-R043` → `S00525`；`mikey-youtube-live-001-K020` → `mikey-youtube-live-001-E0023-R004` → `S01226`；`mikey-youtube-live-002-K008` → `mikey-youtube-live-002-E0016-R001` → `S00461`；`mikey-youtube-live-002-K017` → `mikey-youtube-live-002-E0027-R164` → `S01364`；`mikey-youtube-live-004-K0017` → `mikey-youtube-live-004-E0028` → `mikey-youtube-live-004-E0028-R004`；`mikey-youtube-live-004-K0019` → `mikey-youtube-live-004-E0030` → `mikey-youtube-live-004-E0030-R001`；`mikey-youtube-live-006-K0009` → `mikey-youtube-live-006-E0010` → `mikey-youtube-live-006-E0010-R019`；`mikey-youtube-live-006-K0016` → `mikey-youtube-live-006-E0019` → `mikey-youtube-live-006-E0019-R037`；`mikey-youtube-live-009-K0010` → `mikey-youtube-live-009-E0013` → `mikey-youtube-live-009-E0013-R034`；`mikey-youtube-live-009-K0026` → `mikey-youtube-live-009-E0028` → `mikey-youtube-live-009-E0028-R001`；`mikey-youtube-live-010-K0005` → `mikey-youtube-live-010-E0003` → `mikey-youtube-live-010-E0003-R008`；`mikey-youtube-live-010-K0007` → `mikey-youtube-live-010-E0005` → `mikey-youtube-live-010-E0005-R005`；`mikey-youtube-live-010-K0008` → `mikey-youtube-live-010-E0006` → `mikey-youtube-live-010-E0006-R001`

### T02 · 真实性、一致性与潜沟通

**判断：** 对方感受到的不只是话术内容，还包括眼神、语气、动作、动机与前后是否一致；伪装、过度设计和突然变样会削弱可信度。

**理由：** 先让表达与真实意图、真实状态一致，再谈技巧；线上线下、开场与约会、边界表达前后要连贯。

**方法顺序：** 明确真实意图 → 让语言与状态一致 → 观察对方实际反馈 → 发现表演或断裂时回到真实表达

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 若建议需要把未核人物归属、数字结果、法律/医疗判断或案例结果当事实，则停止并转入待核。

**运行时证据分层：** direct 13；context_only 10；hold 18；do_not_generalize 0。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-001-K020`, `mikey-youtube-live-002-K008`, `mikey-youtube-live-002-K016`, `mikey-youtube-live-002-K024`, `mikey-youtube-live-004-K0012`, `mikey-youtube-live-006-K0006`, `mikey-youtube-live-006-K0014`, `mikey-youtube-live-006-K0016`, `mikey-youtube-live-009-K0003`, `mikey-youtube-live-009-K0005`, `mikey-youtube-live-009-K0016`, `mikey-youtube-live-009-K0021`, `mikey-youtube-live-010-K0005`

**受限知识：** context_only=`mikey-youtube-live-001-K011`, `mikey-youtube-live-001-K012`, `mikey-youtube-live-001-K016`, `mikey-youtube-live-001-K018`, `mikey-youtube-live-005-K015`, `mikey-youtube-live-007-K002`, `mikey-youtube-live-007-K003`, `mikey-youtube-live-007-K004`, `mikey-youtube-live-007-K006`, `mikey-youtube-live-007-K023`；hold=`mikey-youtube-live-001-K004`, `mikey-youtube-live-001-K005`, `mikey-youtube-live-001-K007`, `mikey-youtube-live-002-K020`, `mikey-youtube-live-002-K044`, `mikey-youtube-live-003-K013`, `mikey-youtube-live-004-K0013`, `mikey-youtube-live-005-K016`, `mikey-youtube-live-006-K0005`, `mikey-youtube-live-006-K0013`, `mikey-youtube-live-008-K018`, `mikey-youtube-live-009-K0014`, `mikey-youtube-live-009-K0018`, `mikey-youtube-live-009-K0020`, `mikey-youtube-live-009-K0023`, `mikey-youtube-live-010-K0010`, `mikey-youtube-live-010-K0028`, `mikey-youtube-live-010-K0029`；do_not_generalize=无。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-001-K020` → `mikey-youtube-live-001-E0023-R004` → `S01226`；`mikey-youtube-live-002-K008` → `mikey-youtube-live-002-E0016-R001` → `S00461`；`mikey-youtube-live-002-K016` → `mikey-youtube-live-002-E0027-R006` → `S01206`；`mikey-youtube-live-002-K024` → `mikey-youtube-live-002-E0041-R115` → `S02143`；`mikey-youtube-live-004-K0012` → `mikey-youtube-live-004-E0018` → `mikey-youtube-live-004-E0018-R028`；`mikey-youtube-live-006-K0006` → `mikey-youtube-live-006-E0007` → `mikey-youtube-live-006-E0007-R040`；`mikey-youtube-live-006-K0014` → `mikey-youtube-live-006-E0018` → `mikey-youtube-live-006-E0018-R024`；`mikey-youtube-live-006-K0016` → `mikey-youtube-live-006-E0019` → `mikey-youtube-live-006-E0019-R037`；`mikey-youtube-live-009-K0003` → `mikey-youtube-live-009-E0004` → `mikey-youtube-live-009-E0004-R027`；`mikey-youtube-live-009-K0005` → `mikey-youtube-live-009-E0005` → `mikey-youtube-live-009-E0005-R071`；`mikey-youtube-live-009-K0016` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R031`；`mikey-youtube-live-009-K0021` → `mikey-youtube-live-009-E0024` → `mikey-youtube-live-009-E0024-R018`；`mikey-youtube-live-010-K0005` → `mikey-youtube-live-010-E0003` → `mikey-youtube-live-010-E0003-R008`

### T03 · 行动—反馈—复盘的学习闭环

**判断：** 理论只有进入实践、得到反馈并复盘后才会变成能力；只堆数量或只学理论都不完整。

**理由：** 把问题拆小，先行动，观察具体反馈，复盘失败原因，再调整下一次；新手标准应按阶段设定。

**方法顺序：** 提出具体问题 → 小步实践 → 记录反馈 → 复盘原因 → 调整下一轮

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 若建议需要把未核人物归属、数字结果、法律/医疗判断或案例结果当事实，则停止并转入待核。

**运行时证据分层：** direct 11；context_only 19；hold 22；do_not_generalize 0。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-004-K0005`, `mikey-youtube-live-004-K0010`, `mikey-youtube-live-004-K0016`, `mikey-youtube-live-004-K0018`, `mikey-youtube-live-006-K0003`, `mikey-youtube-live-006-K0009`, `mikey-youtube-live-006-K0016`, `mikey-youtube-live-006-K0018`, `mikey-youtube-live-006-K0020`, `mikey-youtube-live-006-K0021`, `mikey-youtube-live-010-K0008`

**受限知识：** context_only=`mikey-youtube-live-001-K016`, `mikey-youtube-live-005-K008`, `mikey-youtube-live-005-K009`, `mikey-youtube-live-005-K010`, `mikey-youtube-live-006-K0002`, `mikey-youtube-live-007-K007`, `mikey-youtube-live-007-K010`, `mikey-youtube-live-007-K014`, `mikey-youtube-live-007-K015`, `mikey-youtube-live-007-K018`, `mikey-youtube-live-007-K022`, `mikey-youtube-live-007-K024`, `mikey-youtube-live-007-K028`, `mikey-youtube-live-008-K002`, `mikey-youtube-live-008-K006`, `mikey-youtube-live-008-K013`, `mikey-youtube-live-008-K014`, `mikey-youtube-live-008-K016`, `mikey-youtube-live-008-K024`；hold=`mikey-youtube-live-002-K003`, `mikey-youtube-live-002-K006`, `mikey-youtube-live-002-K020`, `mikey-youtube-live-003-K002`, `mikey-youtube-live-003-K008`, `mikey-youtube-live-003-K015`, `mikey-youtube-live-004-K0004`, `mikey-youtube-live-004-K0015`, `mikey-youtube-live-005-K017`, `mikey-youtube-live-007-K027`, `mikey-youtube-live-008-K004`, `mikey-youtube-live-008-K010`, `mikey-youtube-live-009-K0002`, `mikey-youtube-live-009-K0006`, `mikey-youtube-live-009-K0017`, `mikey-youtube-live-009-K0025`, `mikey-youtube-live-010-K0001`, `mikey-youtube-live-010-K0018`, `mikey-youtube-live-010-K0024`, `mikey-youtube-live-010-K0026`, `mikey-youtube-live-010-K0031`, `mikey-youtube-live-010-K0033`；do_not_generalize=无。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-004-K0005` → `mikey-youtube-live-004-E0009` → `mikey-youtube-live-004-E0009-R007`；`mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0016` → `mikey-youtube-live-004-E0016-R060`；`mikey-youtube-live-004-K0016` → `mikey-youtube-live-004-E0025` → `mikey-youtube-live-004-E0025-R073`；`mikey-youtube-live-004-K0018` → `mikey-youtube-live-004-E0029` → `mikey-youtube-live-004-E0029-R003`；`mikey-youtube-live-006-K0003` → `mikey-youtube-live-006-E0004` → `mikey-youtube-live-006-E0004-R022`；`mikey-youtube-live-006-K0009` → `mikey-youtube-live-006-E0010` → `mikey-youtube-live-006-E0010-R019`；`mikey-youtube-live-006-K0016` → `mikey-youtube-live-006-E0019` → `mikey-youtube-live-006-E0019-R037`；`mikey-youtube-live-006-K0018` → `mikey-youtube-live-006-E0021` → `mikey-youtube-live-006-E0021-R004`；`mikey-youtube-live-006-K0020` → `mikey-youtube-live-006-E0023` → `mikey-youtube-live-006-E0023-R008`；`mikey-youtube-live-006-K0021` → `mikey-youtube-live-006-E0026` → `mikey-youtube-live-006-E0026-R053`；`mikey-youtube-live-010-K0008` → `mikey-youtube-live-010-E0006` → `mikey-youtube-live-010-E0006-R001`

### T04 · 技巧的定位：工具而非核心

**判断：** 技巧可以提高效率、提供练习入口或帮助结构化互动，但不能替代个人价值、真实状态和现场判断。

**理由：** 先建立底层能力与真实交流，再选择少量适合当前阶段的工具；避免在现场持续计算技巧。

**方法顺序：** 先判断底层问题 → 只选当前必要技巧 → 实践 → 逐步内化 → 避免把工具变成现场计算负担

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 若建议需要把未核人物归属、数字结果、法律/医疗判断或案例结果当事实，则停止并转入待核。

**运行时证据分层：** direct 8；context_only 10；hold 15；do_not_generalize 0。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-001-K006`, `mikey-youtube-live-001-K022`, `mikey-youtube-live-001-K027`, `mikey-youtube-live-002-K005`, `mikey-youtube-live-002-K009`, `mikey-youtube-live-002-K012`, `mikey-youtube-live-002-K013`, `mikey-youtube-live-006-K0015`

**受限知识：** context_only=`mikey-youtube-live-001-K003`, `mikey-youtube-live-001-K012`, `mikey-youtube-live-001-K025`, `mikey-youtube-live-005-K001`, `mikey-youtube-live-005-K003`, `mikey-youtube-live-005-K010`, `mikey-youtube-live-006-K0024`, `mikey-youtube-live-007-K011`, `mikey-youtube-live-008-K016`, `mikey-youtube-live-008-K024`；hold=`mikey-youtube-live-001-K005`, `mikey-youtube-live-002-K002`, `mikey-youtube-live-002-K007`, `mikey-youtube-live-002-K011`, `mikey-youtube-live-002-K034`, `mikey-youtube-live-002-K043`, `mikey-youtube-live-003-K009`, `mikey-youtube-live-003-K013`, `mikey-youtube-live-003-K014`, `mikey-youtube-live-006-K0004`, `mikey-youtube-live-006-K0023`, `mikey-youtube-live-008-K011`, `mikey-youtube-live-010-K0010`, `mikey-youtube-live-010-K0026`, `mikey-youtube-live-010-K0028`；do_not_generalize=无。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-001-K006` → `mikey-youtube-live-001-E0011-R002` → `S00354`；`mikey-youtube-live-001-K022` → `mikey-youtube-live-001-E0025-R025` → `S01602`；`mikey-youtube-live-001-K027` → `mikey-youtube-live-001-E0031-R011` → `S02022`；`mikey-youtube-live-002-K005` → `mikey-youtube-live-002-E0012-R001` → `S00281`；`mikey-youtube-live-002-K009` → `mikey-youtube-live-002-E0016-R031` → `S00491`；`mikey-youtube-live-002-K012` → `mikey-youtube-live-002-E0020-R016` → `S00661`；`mikey-youtube-live-002-K013` → `mikey-youtube-live-002-E0020-R096` → `S00741`；`mikey-youtube-live-006-K0015` → `mikey-youtube-live-006-E0019` → `mikey-youtube-live-006-E0019-R001`

### T05 · 吸引力的内外结构与展示面

**判断：** 外在形象、照片、收入和生活条件主要影响接触机会与第一印象；更深的吸引还取决于自信、边界、表达、生活内容和现场状态。

**理由：** 线上先修正真实且一致的展示面，线下再用实际交流验证；不能用网图、过度修图或单一条件代替本人。

**方法顺序：** 先修真实外在与展示面 → 争取接触机会 → 线下用状态和表达验证 → 持续建设内在与生活价值

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 若建议需要把未核人物归属、数字结果、法律/医疗判断或案例结果当事实，则停止并转入待核。

**运行时证据分层：** direct 13；context_only 10；hold 24；do_not_generalize 0。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-002-K023`, `mikey-youtube-live-004-K0009`, `mikey-youtube-live-004-K0019`, `mikey-youtube-live-004-K0020`, `mikey-youtube-live-006-K0001`, `mikey-youtube-live-006-K0008`, `mikey-youtube-live-006-K0017`, `mikey-youtube-live-009-K0003`, `mikey-youtube-live-009-K0005`, `mikey-youtube-live-009-K0009`, `mikey-youtube-live-009-K0010`, `mikey-youtube-live-009-K0012`, `mikey-youtube-live-009-K0026`

**受限知识：** context_only=`mikey-youtube-live-005-K003`, `mikey-youtube-live-005-K014`, `mikey-youtube-live-006-K0024`, `mikey-youtube-live-007-K023`, `mikey-youtube-live-007-K026`, `mikey-youtube-live-008-K003`, `mikey-youtube-live-008-K005`, `mikey-youtube-live-008-K019`, `mikey-youtube-live-008-K020`, `mikey-youtube-live-008-K025`；hold=`mikey-youtube-live-002-K037`, `mikey-youtube-live-002-K038`, `mikey-youtube-live-003-K011`, `mikey-youtube-live-003-K014`, `mikey-youtube-live-004-K0003`, `mikey-youtube-live-005-K005`, `mikey-youtube-live-006-K0004`, `mikey-youtube-live-006-K0011`, `mikey-youtube-live-006-K0013`, `mikey-youtube-live-006-K0023`, `mikey-youtube-live-007-K017`, `mikey-youtube-live-007-K020`, `mikey-youtube-live-007-K025`, `mikey-youtube-live-008-K018`, `mikey-youtube-live-009-K0001`, `mikey-youtube-live-009-K0020`, `mikey-youtube-live-009-K0022`, `mikey-youtube-live-010-K0010`, `mikey-youtube-live-010-K0020`, `mikey-youtube-live-010-K0022`, `mikey-youtube-live-010-K0028`, `mikey-youtube-live-010-K0030`, `mikey-youtube-live-010-K0032`, `mikey-youtube-live-010-K0034`；do_not_generalize=无。

**来源：** `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-002-K023` → `mikey-youtube-live-002-E0040-R011` → `S02024`；`mikey-youtube-live-004-K0009` → `mikey-youtube-live-004-E0015` → `mikey-youtube-live-004-E0015-R020`；`mikey-youtube-live-004-K0019` → `mikey-youtube-live-004-E0030` → `mikey-youtube-live-004-E0030-R001`；`mikey-youtube-live-004-K0020` → `mikey-youtube-live-004-E0030` → `mikey-youtube-live-004-E0030-R105`；`mikey-youtube-live-006-K0001` → `mikey-youtube-live-006-E0002` → `mikey-youtube-live-006-E0002-R047`；`mikey-youtube-live-006-K0008` → `mikey-youtube-live-006-E0009` → `mikey-youtube-live-006-E0009-R041`；`mikey-youtube-live-006-K0017` → `mikey-youtube-live-006-E0020` → `mikey-youtube-live-006-E0020-R041`；`mikey-youtube-live-009-K0003` → `mikey-youtube-live-009-E0004` → `mikey-youtube-live-009-E0004-R027`；`mikey-youtube-live-009-K0005` → `mikey-youtube-live-009-E0005` → `mikey-youtube-live-009-E0005-R071`；`mikey-youtube-live-009-K0009` → `mikey-youtube-live-009-E0012` → `mikey-youtube-live-009-E0012-R001`；`mikey-youtube-live-009-K0010` → `mikey-youtube-live-009-E0013` → `mikey-youtube-live-009-E0013-R034`；`mikey-youtube-live-009-K0012` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R011`；`mikey-youtube-live-009-K0026` → `mikey-youtube-live-009-E0028` → `mikey-youtube-live-009-E0028-R001`

### T06 · 聊天、故事与情绪互动

**判断：** 聊天不是履历交换或机械提问；有效互动来自真实好奇、个人经历、表达状态、对方投入以及双方共同情境。

**理由：** 从对方内容抓关键词，连接自己的真实经历，再建立“我们”的共同情境；故事先讲清楚，再谈幽默和感染力。

**方法顺序：** 真实好奇 → 抓关键词 → 分享自己的经历/观点 → 形成双方共同情境 → 按对方投入调整深度

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 若建议需要把未核人物归属、数字结果、法律/医疗判断或案例结果当事实，则停止并转入待核。

**运行时证据分层：** direct 14；context_only 13；hold 23；do_not_generalize 0。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-001-K010`, `mikey-youtube-live-001-K014`, `mikey-youtube-live-002-K008`, `mikey-youtube-live-002-K012`, `mikey-youtube-live-002-K024`, `mikey-youtube-live-004-K0006`, `mikey-youtube-live-004-K0011`, `mikey-youtube-live-004-K0019`, `mikey-youtube-live-004-K0020`, `mikey-youtube-live-006-K0006`, `mikey-youtube-live-006-K0007`, `mikey-youtube-live-006-K0008`, `mikey-youtube-live-009-K0004`, `mikey-youtube-live-009-K0021`

**受限知识：** context_only=`mikey-youtube-live-001-K003`, `mikey-youtube-live-005-K012`, `mikey-youtube-live-005-K013`, `mikey-youtube-live-005-K014`, `mikey-youtube-live-007-K003`, `mikey-youtube-live-007-K004`, `mikey-youtube-live-007-K006`, `mikey-youtube-live-007-K014`, `mikey-youtube-live-007-K019`, `mikey-youtube-live-008-K003`, `mikey-youtube-live-008-K008`, `mikey-youtube-live-008-K013`, `mikey-youtube-live-008-K025`；hold=`mikey-youtube-live-001-K005`, `mikey-youtube-live-001-K008`, `mikey-youtube-live-001-K024`, `mikey-youtube-live-002-K007`, `mikey-youtube-live-002-K015`, `mikey-youtube-live-002-K022`, `mikey-youtube-live-002-K034`, `mikey-youtube-live-002-K043`, `mikey-youtube-live-002-K045`, `mikey-youtube-live-003-K001`, `mikey-youtube-live-003-K014`, `mikey-youtube-live-004-K0013`, `mikey-youtube-live-006-K0005`, `mikey-youtube-live-007-K025`, `mikey-youtube-live-009-K0023`, `mikey-youtube-live-010-K0009`, `mikey-youtube-live-010-K0011`, `mikey-youtube-live-010-K0013`, `mikey-youtube-live-010-K0014`, `mikey-youtube-live-010-K0020`, `mikey-youtube-live-010-K0025`, `mikey-youtube-live-010-K0029`, `mikey-youtube-live-010-K0031`；do_not_generalize=无。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-001-K010` → `mikey-youtube-live-001-E0014-R043` → `S00525`；`mikey-youtube-live-001-K014` → `mikey-youtube-live-001-E0016-R066` → `S00709`；`mikey-youtube-live-002-K008` → `mikey-youtube-live-002-E0016-R001` → `S00461`；`mikey-youtube-live-002-K012` → `mikey-youtube-live-002-E0020-R016` → `S00661`；`mikey-youtube-live-002-K024` → `mikey-youtube-live-002-E0041-R115` → `S02143`；`mikey-youtube-live-004-K0006` → `mikey-youtube-live-004-E0010` → `mikey-youtube-live-004-E0010-R022`；`mikey-youtube-live-004-K0011` → `mikey-youtube-live-004-E0017` → `mikey-youtube-live-004-E0017-R030`；`mikey-youtube-live-004-K0019` → `mikey-youtube-live-004-E0030` → `mikey-youtube-live-004-E0030-R001`；`mikey-youtube-live-004-K0020` → `mikey-youtube-live-004-E0030` → `mikey-youtube-live-004-E0030-R105`；`mikey-youtube-live-006-K0006` → `mikey-youtube-live-006-E0007` → `mikey-youtube-live-006-E0007-R040`；`mikey-youtube-live-006-K0007` → `mikey-youtube-live-006-E0008` → `mikey-youtube-live-006-E0008-R040`；`mikey-youtube-live-006-K0008` → `mikey-youtube-live-006-E0009` → `mikey-youtube-live-006-E0009-R041`；`mikey-youtube-live-009-K0004` → `mikey-youtube-live-009-E0005` → `mikey-youtube-live-009-E0005-R021`；`mikey-youtube-live-009-K0021` → `mikey-youtube-live-009-E0024` → `mikey-youtube-live-009-E0024-R018`

### T07 · 搭讪焦虑、开场与自然行动

**判断：** 搭讪中的紧张、销售感和犹豫常与自我审判、场景禁忌感或结果压力有关；行动训练的目标是降低内耗，而非保证结果。

**理由：** 在合适公共场景缩短犹豫，清楚表达认识意图；对方不停、拒绝或不愿交流就结束。

**方法顺序：** 承认紧张 → 缩短犹豫 → 在合适场景表达意图 → 观察是否愿意停留/回应 → 拒绝即结束

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 出现明确拒绝、持续不回应/不停留、明显不适，或事实不足以判断时，停止推进或停止下确定结论。

**运行时证据分层：** direct 12；context_only 10；hold 23；do_not_generalize 0。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-001-K006`, `mikey-youtube-live-001-K027`, `mikey-youtube-live-002-K005`, `mikey-youtube-live-002-K012`, `mikey-youtube-live-002-K016`, `mikey-youtube-live-002-K017`, `mikey-youtube-live-004-K0010`, `mikey-youtube-live-006-K0009`, `mikey-youtube-live-006-K0010`, `mikey-youtube-live-006-K0014`, `mikey-youtube-live-009-K0016`, `mikey-youtube-live-010-K0004`

**受限知识：** context_only=`mikey-youtube-live-001-K025`, `mikey-youtube-live-005-K004`, `mikey-youtube-live-005-K008`, `mikey-youtube-live-005-K011`, `mikey-youtube-live-006-K0002`, `mikey-youtube-live-007-K001`, `mikey-youtube-live-007-K002`, `mikey-youtube-live-007-K013`, `mikey-youtube-live-008-K002`, `mikey-youtube-live-008-K007`；hold=`mikey-youtube-live-001-K007`, `mikey-youtube-live-002-K002`, `mikey-youtube-live-002-K003`, `mikey-youtube-live-002-K011`, `mikey-youtube-live-002-K025`, `mikey-youtube-live-002-K027`, `mikey-youtube-live-002-K028`, `mikey-youtube-live-002-K035`, `mikey-youtube-live-003-K007`, `mikey-youtube-live-003-K010`, `mikey-youtube-live-003-K012`, `mikey-youtube-live-004-K0004`, `mikey-youtube-live-004-K0014`, `mikey-youtube-live-004-K0015`, `mikey-youtube-live-006-K0005`, `mikey-youtube-live-007-K008`, `mikey-youtube-live-008-K017`, `mikey-youtube-live-009-K0006`, `mikey-youtube-live-009-K0007`, `mikey-youtube-live-009-K0022`, `mikey-youtube-live-010-K0001`, `mikey-youtube-live-010-K0012`, `mikey-youtube-live-010-K0019`；do_not_generalize=无。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-001-K006` → `mikey-youtube-live-001-E0011-R002` → `S00354`；`mikey-youtube-live-001-K027` → `mikey-youtube-live-001-E0031-R011` → `S02022`；`mikey-youtube-live-002-K005` → `mikey-youtube-live-002-E0012-R001` → `S00281`；`mikey-youtube-live-002-K012` → `mikey-youtube-live-002-E0020-R016` → `S00661`；`mikey-youtube-live-002-K016` → `mikey-youtube-live-002-E0027-R006` → `S01206`；`mikey-youtube-live-002-K017` → `mikey-youtube-live-002-E0027-R164` → `S01364`；`mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0016` → `mikey-youtube-live-004-E0016-R060`；`mikey-youtube-live-006-K0009` → `mikey-youtube-live-006-E0010` → `mikey-youtube-live-006-E0010-R019`；`mikey-youtube-live-006-K0010` → `mikey-youtube-live-006-E0011` → `mikey-youtube-live-006-E0011-R008`；`mikey-youtube-live-006-K0014` → `mikey-youtube-live-006-E0018` → `mikey-youtube-live-006-E0018-R024`；`mikey-youtube-live-009-K0016` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R031`；`mikey-youtube-live-010-K0004` → `mikey-youtube-live-010-E0002` → `mikey-youtube-live-010-E0002-R066`

### T08 · 兴趣判断、筛选与情境诊断

**判断：** 单一信号不能证明兴趣或结果；应综合注意力、投入、替代时间、持续回应、现场状态和对方现实安排。

**理由：** 先收集具体信息，再判断；信息不足时明确“很难评”，不要把口述中的一个动作升级成确定结论。

**方法顺序：** 收集具体事实 → 看多项投入信号 → 排除现实条件 → 信息不足则不下定论 → 决定继续/降投入/停止

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 出现明确拒绝、持续不回应/不停留、明显不适，或事实不足以判断时，停止推进或停止下确定结论。

**运行时证据分层：** direct 16；context_only 24；hold 30；do_not_generalize 0。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-001-K009`, `mikey-youtube-live-001-K020`, `mikey-youtube-live-001-K021`, `mikey-youtube-live-002-K004`, `mikey-youtube-live-002-K005`, `mikey-youtube-live-004-K0005`, `mikey-youtube-live-004-K0007`, `mikey-youtube-live-004-K0009`, `mikey-youtube-live-004-K0016`, `mikey-youtube-live-006-K0010`, `mikey-youtube-live-006-K0019`, `mikey-youtube-live-009-K0004`, `mikey-youtube-live-009-K0011`, `mikey-youtube-live-009-K0015`, `mikey-youtube-live-010-K0004`, `mikey-youtube-live-010-K0017`

**受限知识：** context_only=`mikey-youtube-live-001-K011`, `mikey-youtube-live-001-K015`, `mikey-youtube-live-002-K010`, `mikey-youtube-live-002-K021`, `mikey-youtube-live-005-K004`, `mikey-youtube-live-005-K006`, `mikey-youtube-live-005-K007`, `mikey-youtube-live-005-K013`, `mikey-youtube-live-005-K018`, `mikey-youtube-live-007-K005`, `mikey-youtube-live-007-K006`, `mikey-youtube-live-007-K011`, `mikey-youtube-live-007-K012`, `mikey-youtube-live-007-K015`, `mikey-youtube-live-007-K018`, `mikey-youtube-live-007-K019`, `mikey-youtube-live-007-K026`, `mikey-youtube-live-008-K001`, `mikey-youtube-live-008-K005`, `mikey-youtube-live-008-K007`, `mikey-youtube-live-008-K009`, `mikey-youtube-live-008-K012`, `mikey-youtube-live-008-K013`, `mikey-youtube-live-008-K023`；hold=`mikey-youtube-live-001-K024`, `mikey-youtube-live-001-K026`, `mikey-youtube-live-002-K014`, `mikey-youtube-live-002-K018`, `mikey-youtube-live-002-K019`, `mikey-youtube-live-002-K022`, `mikey-youtube-live-002-K025`, `mikey-youtube-live-002-K027`, `mikey-youtube-live-003-K003`, `mikey-youtube-live-003-K005`, `mikey-youtube-live-003-K006`, `mikey-youtube-live-003-K008`, `mikey-youtube-live-003-K010`, `mikey-youtube-live-003-K011`, `mikey-youtube-live-003-K012`, `mikey-youtube-live-003-K016`, `mikey-youtube-live-004-K0002`, `mikey-youtube-live-004-K0015`, `mikey-youtube-live-006-K0011`, `mikey-youtube-live-006-K0022`, `mikey-youtube-live-006-K0023`, `mikey-youtube-live-007-K027`, `mikey-youtube-live-008-K017`, `mikey-youtube-live-009-K0007`, `mikey-youtube-live-009-K0008`, `mikey-youtube-live-009-K0019`, `mikey-youtube-live-010-K0002`, `mikey-youtube-live-010-K0013`, `mikey-youtube-live-010-K0023`, `mikey-youtube-live-010-K0027`；do_not_generalize=无。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-001-K009` → `mikey-youtube-live-001-E0014-R018` → `S00500`；`mikey-youtube-live-001-K020` → `mikey-youtube-live-001-E0023-R004` → `S01226`；`mikey-youtube-live-001-K021` → `mikey-youtube-live-001-E0024-R001` → `S01407`；`mikey-youtube-live-002-K004` → `mikey-youtube-live-002-E0010-R004` → `S00244`；`mikey-youtube-live-002-K005` → `mikey-youtube-live-002-E0012-R001` → `S00281`；`mikey-youtube-live-004-K0005` → `mikey-youtube-live-004-E0009` → `mikey-youtube-live-004-E0009-R007`；`mikey-youtube-live-004-K0007` → `mikey-youtube-live-004-E0012` → `mikey-youtube-live-004-E0012-R017`；`mikey-youtube-live-004-K0009` → `mikey-youtube-live-004-E0015` → `mikey-youtube-live-004-E0015-R020`；`mikey-youtube-live-004-K0016` → `mikey-youtube-live-004-E0025` → `mikey-youtube-live-004-E0025-R073`；`mikey-youtube-live-006-K0010` → `mikey-youtube-live-006-E0011` → `mikey-youtube-live-006-E0011-R008`；`mikey-youtube-live-006-K0019` → `mikey-youtube-live-006-E0022` → `mikey-youtube-live-006-E0022-R007`；`mikey-youtube-live-009-K0004` → `mikey-youtube-live-009-E0005` → `mikey-youtube-live-009-E0005-R021`；`mikey-youtube-live-009-K0011` → `mikey-youtube-live-009-E0014` → `mikey-youtube-live-009-E0014-R004`；`mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R005`；`mikey-youtube-live-010-K0004` → `mikey-youtube-live-010-E0002` → `mikey-youtube-live-010-E0002-R066`；`mikey-youtube-live-010-K0017` → `mikey-youtube-live-010-E0011` → `mikey-youtube-live-010-E0011-R003`

### T09 · 拒绝、停止线、同意与安全感

**判断：** 拒绝和不愿意是停止线；技巧、所谓窗口、既有预订、先前接触或社会规范都不能自动改写当下意愿。

**理由：** 当出现no、持续不停、不愿转场、明显不适或低投入时先停止；若只是信息不足，先补沟通和安全感，但不以继续施压替代同意。

**方法顺序：** 先停止当前动作 → 确认对方当下意愿 → 必要时补安全感和沟通 → 仅在新的明确意愿下继续 → 拒绝持续存在则结束

**条件：** 任何具体亲密或肢体建议若关联blocking待核，不直接执行；以当下明确、可撤回的意愿为优先边界。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 出现明确拒绝、持续不回应/不停留、明显不适，或事实不足以判断时，停止推进或停止下确定结论。

**运行时证据分层：** direct 3；context_only 10；hold 25；do_not_generalize 2。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-004-K0006`, `mikey-youtube-live-004-K0010`, `mikey-youtube-live-006-K0020`

**受限知识：** context_only=`mikey-youtube-live-001-K003`, `mikey-youtube-live-002-K010`, `mikey-youtube-live-005-K001`, `mikey-youtube-live-005-K004`, `mikey-youtube-live-005-K013`, `mikey-youtube-live-007-K013`, `mikey-youtube-live-007-K014`, `mikey-youtube-live-008-K001`, `mikey-youtube-live-008-K023`, `mikey-youtube-live-008-K024`；hold=`mikey-youtube-live-001-K008`, `mikey-youtube-live-001-K023`, `mikey-youtube-live-001-K026`, `mikey-youtube-live-002-K019`, `mikey-youtube-live-002-K025`, `mikey-youtube-live-003-K004`, `mikey-youtube-live-003-K005`, `mikey-youtube-live-004-K0002`, `mikey-youtube-live-004-K0003`, `mikey-youtube-live-004-K0014`, `mikey-youtube-live-005-K019`, `mikey-youtube-live-006-K0004`, `mikey-youtube-live-007-K017`, `mikey-youtube-live-008-K017`, `mikey-youtube-live-009-K0002`, `mikey-youtube-live-009-K0008`, `mikey-youtube-live-009-K0019`, `mikey-youtube-live-009-K0022`, `mikey-youtube-live-009-K0024`, `mikey-youtube-live-010-K0012`, `mikey-youtube-live-010-K0019`, `mikey-youtube-live-010-K0021`, `mikey-youtube-live-010-K0030`, `mikey-youtube-live-010-K0033`, `mikey-youtube-live-010-K0034`；do_not_generalize=`mikey-youtube-live-002-K032`, `mikey-youtube-live-002-K041`。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-004-K0006` → `mikey-youtube-live-004-E0010` → `mikey-youtube-live-004-E0010-R022`；`mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0016` → `mikey-youtube-live-004-E0016-R060`；`mikey-youtube-live-006-K0020` → `mikey-youtube-live-006-E0023` → `mikey-youtube-live-006-E0023-R008`

### T10 · 关系意图、诚实与边界

**判断：** 关系安排和短期/长期意图应尽早讲清楚；不应以虚假承诺、假装朋友或隐瞒关键事实换取推进。

**理由：** 先明确自己要什么，再清楚表达；对方不接受就停止或离开。边界也包括允许对方离开，而不是强迫对方接受。

**方法顺序：** 先明确自己的关系目标 → 尽早说明 → 确认对方是否接受 → 不接受则停止或调整关系 → 保持前后一致

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 出现明确拒绝、持续不回应/不停留、明显不适，或事实不足以判断时，停止推进或停止下确定结论。

**运行时证据分层：** direct 16；context_only 13；hold 35；do_not_generalize 1。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-001-K001`, `mikey-youtube-live-001-K002`, `mikey-youtube-live-001-K006`, `mikey-youtube-live-001-K027`, `mikey-youtube-live-002-K004`, `mikey-youtube-live-002-K024`, `mikey-youtube-live-002-K042`, `mikey-youtube-live-006-K0007`, `mikey-youtube-live-006-K0017`, `mikey-youtube-live-006-K0018`, `mikey-youtube-live-006-K0020`, `mikey-youtube-live-009-K0012`, `mikey-youtube-live-009-K0021`, `mikey-youtube-live-009-K0026`, `mikey-youtube-live-010-K0003`, `mikey-youtube-live-010-K0017`

**受限知识：** context_only=`mikey-youtube-live-001-K019`, `mikey-youtube-live-002-K010`, `mikey-youtube-live-002-K021`, `mikey-youtube-live-005-K001`, `mikey-youtube-live-005-K007`, `mikey-youtube-live-006-K0024`, `mikey-youtube-live-007-K001`, `mikey-youtube-live-007-K003`, `mikey-youtube-live-007-K010`, `mikey-youtube-live-007-K023`, `mikey-youtube-live-008-K001`, `mikey-youtube-live-008-K008`, `mikey-youtube-live-008-K014`；hold=`mikey-youtube-live-001-K008`, `mikey-youtube-live-001-K023`, `mikey-youtube-live-001-K024`, `mikey-youtube-live-002-K001`, `mikey-youtube-live-002-K002`, `mikey-youtube-live-002-K006`, `mikey-youtube-live-002-K018`, `mikey-youtube-live-002-K019`, `mikey-youtube-live-002-K022`, `mikey-youtube-live-002-K038`, `mikey-youtube-live-002-K039`, `mikey-youtube-live-002-K046`, `mikey-youtube-live-003-K005`, `mikey-youtube-live-003-K009`, `mikey-youtube-live-003-K012`, `mikey-youtube-live-003-K013`, `mikey-youtube-live-003-K016`, `mikey-youtube-live-004-K0002`, `mikey-youtube-live-004-K0008`, `mikey-youtube-live-006-K0012`, `mikey-youtube-live-007-K008`, `mikey-youtube-live-007-K021`, `mikey-youtube-live-007-K027`, `mikey-youtube-live-008-K011`, `mikey-youtube-live-009-K0018`, `mikey-youtube-live-009-K0020`, `mikey-youtube-live-009-K0024`, `mikey-youtube-live-010-K0006`, `mikey-youtube-live-010-K0012`, `mikey-youtube-live-010-K0014`, `mikey-youtube-live-010-K0016`, `mikey-youtube-live-010-K0023`, `mikey-youtube-live-010-K0027`, `mikey-youtube-live-010-K0032`, `mikey-youtube-live-010-K0034`；do_not_generalize=`mikey-youtube-live-002-K030`。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-001-K001` → `mikey-youtube-live-001-E0007-R023` → `S00144`；`mikey-youtube-live-001-K002` → `mikey-youtube-live-001-E0007-R036` → `S00157`；`mikey-youtube-live-001-K006` → `mikey-youtube-live-001-E0011-R002` → `S00354`；`mikey-youtube-live-001-K027` → `mikey-youtube-live-001-E0031-R011` → `S02022`；`mikey-youtube-live-002-K004` → `mikey-youtube-live-002-E0010-R004` → `S00244`；`mikey-youtube-live-002-K024` → `mikey-youtube-live-002-E0041-R115` → `S02143`；`mikey-youtube-live-002-K042` → `mikey-youtube-live-002-E0069-R037` → `S04242`；`mikey-youtube-live-006-K0007` → `mikey-youtube-live-006-E0008` → `mikey-youtube-live-006-E0008-R040`；`mikey-youtube-live-006-K0017` → `mikey-youtube-live-006-E0020` → `mikey-youtube-live-006-E0020-R041`；`mikey-youtube-live-006-K0018` → `mikey-youtube-live-006-E0021` → `mikey-youtube-live-006-E0021-R004`；`mikey-youtube-live-006-K0020` → `mikey-youtube-live-006-E0023` → `mikey-youtube-live-006-E0023-R008`；`mikey-youtube-live-009-K0012` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R011`；`mikey-youtube-live-009-K0021` → `mikey-youtube-live-009-E0024` → `mikey-youtube-live-009-E0024-R018`；`mikey-youtube-live-009-K0026` → `mikey-youtube-live-009-E0028` → `mikey-youtube-live-009-E0028-R001`；`mikey-youtube-live-010-K0003` → `mikey-youtube-live-010-E0002` → `mikey-youtube-live-010-E0002-R008`；`mikey-youtube-live-010-K0017` → `mikey-youtube-live-010-E0011` → `mikey-youtube-live-010-E0011-R003`

### T11 · 线上—线下连续性与邀约

**判断：** 展示面、文字聊天、电话、线下见面是同一条连续互动，但各自承担不同功能；线上不能替代真实见面。

**理由：** 展示面争取接触机会，线上用于联络和邀约，必要时电话传递更丰富信息；被拒后根据明确原因决定是否继续，而不是无限聊天。

**方法顺序：** 真实展示面争取接触 → 简洁联络 → 明确邀约 → 必要时电话补充信息 → 线下见面验证

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 出现明确拒绝、持续不回应/不停留、明显不适，或事实不足以判断时，停止推进或停止下确定结论。

**运行时证据分层：** direct 11；context_only 4；hold 16；do_not_generalize 1。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-002-K004`, `mikey-youtube-live-004-K0006`, `mikey-youtube-live-004-K0007`, `mikey-youtube-live-004-K0009`, `mikey-youtube-live-004-K0020`, `mikey-youtube-live-006-K0017`, `mikey-youtube-live-009-K0003`, `mikey-youtube-live-009-K0009`, `mikey-youtube-live-009-K0010`, `mikey-youtube-live-009-K0015`, `mikey-youtube-live-010-K0004`

**受限知识：** context_only=`mikey-youtube-live-007-K022`, `mikey-youtube-live-008-K008`, `mikey-youtube-live-008-K019`, `mikey-youtube-live-008-K020`；hold=`mikey-youtube-live-002-K011`, `mikey-youtube-live-002-K014`, `mikey-youtube-live-002-K015`, `mikey-youtube-live-002-K027`, `mikey-youtube-live-002-K040`, `mikey-youtube-live-002-K043`, `mikey-youtube-live-003-K011`, `mikey-youtube-live-004-K0008`, `mikey-youtube-live-005-K005`, `mikey-youtube-live-008-K018`, `mikey-youtube-live-009-K0001`, `mikey-youtube-live-009-K0008`, `mikey-youtube-live-009-K0024`, `mikey-youtube-live-010-K0022`, `mikey-youtube-live-010-K0027`, `mikey-youtube-live-010-K0029`；do_not_generalize=`mikey-youtube-live-002-K041`。

**来源：** `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-002-K004` → `mikey-youtube-live-002-E0010-R004` → `S00244`；`mikey-youtube-live-004-K0006` → `mikey-youtube-live-004-E0010` → `mikey-youtube-live-004-E0010-R022`；`mikey-youtube-live-004-K0007` → `mikey-youtube-live-004-E0012` → `mikey-youtube-live-004-E0012-R017`；`mikey-youtube-live-004-K0009` → `mikey-youtube-live-004-E0015` → `mikey-youtube-live-004-E0015-R020`；`mikey-youtube-live-004-K0020` → `mikey-youtube-live-004-E0030` → `mikey-youtube-live-004-E0030-R105`；`mikey-youtube-live-006-K0017` → `mikey-youtube-live-006-E0020` → `mikey-youtube-live-006-E0020-R041`；`mikey-youtube-live-009-K0003` → `mikey-youtube-live-009-E0004` → `mikey-youtube-live-009-E0004-R027`；`mikey-youtube-live-009-K0009` → `mikey-youtube-live-009-E0012` → `mikey-youtube-live-009-E0012-R001`；`mikey-youtube-live-009-K0010` → `mikey-youtube-live-009-E0013` → `mikey-youtube-live-009-E0013-R034`；`mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R005`；`mikey-youtube-live-010-K0004` → `mikey-youtube-live-010-E0002` → `mikey-youtube-live-010-E0002-R066`

### T12 · 生活建设、主体性与长期成长

**判断：** 稳定吸引力不只来自社交动作，还来自生活目标、主动解决问题、自我价值、真实经历和能够创造价值的能力。

**理由：** 把时间投入可改变的生活条件、技能、形象和兴趣；用小任务与持续行动建立对自己的信任。

**方法顺序：** 识别长期短板 → 拆成可改变条件 → 从小任务开始 → 积累真实经历和结果 → 把生活建设带回社交

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 若建议需要把未核人物归属、数字结果、法律/医疗判断或案例结果当事实，则停止并转入待核。

**运行时证据分层：** direct 21；context_only 17；hold 22；do_not_generalize 2。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-001-K013`, `mikey-youtube-live-001-K021`, `mikey-youtube-live-004-K0007`, `mikey-youtube-live-004-K0012`, `mikey-youtube-live-004-K0017`, `mikey-youtube-live-004-K0018`, `mikey-youtube-live-006-K0003`, `mikey-youtube-live-006-K0006`, `mikey-youtube-live-006-K0007`, `mikey-youtube-live-006-K0008`, `mikey-youtube-live-006-K0014`, `mikey-youtube-live-006-K0015`, `mikey-youtube-live-006-K0018`, `mikey-youtube-live-006-K0019`, `mikey-youtube-live-006-K0021`, `mikey-youtube-live-009-K0005`, `mikey-youtube-live-009-K0009`, `mikey-youtube-live-009-K0011`, `mikey-youtube-live-010-K0003`, `mikey-youtube-live-010-K0008`, `mikey-youtube-live-010-K0017`

**受限知识：** context_only=`mikey-youtube-live-002-K029`, `mikey-youtube-live-005-K009`, `mikey-youtube-live-005-K012`, `mikey-youtube-live-007-K001`, `mikey-youtube-live-007-K004`, `mikey-youtube-live-007-K005`, `mikey-youtube-live-007-K010`, `mikey-youtube-live-007-K011`, `mikey-youtube-live-007-K018`, `mikey-youtube-live-007-K022`, `mikey-youtube-live-008-K003`, `mikey-youtube-live-008-K005`, `mikey-youtube-live-008-K014`, `mikey-youtube-live-008-K020`, `mikey-youtube-live-008-K021`, `mikey-youtube-live-008-K022`, `mikey-youtube-live-008-K025`；hold=`mikey-youtube-live-002-K001`, `mikey-youtube-live-002-K014`, `mikey-youtube-live-002-K020`, `mikey-youtube-live-002-K026`, `mikey-youtube-live-002-K036`, `mikey-youtube-live-003-K015`, `mikey-youtube-live-003-K016`, `mikey-youtube-live-004-K0013`, `mikey-youtube-live-004-K0014`, `mikey-youtube-live-006-K0013`, `mikey-youtube-live-006-K0022`, `mikey-youtube-live-007-K017`, `mikey-youtube-live-008-K010`, `mikey-youtube-live-008-K011`, `mikey-youtube-live-009-K0002`, `mikey-youtube-live-009-K0023`, `mikey-youtube-live-009-K0025`, `mikey-youtube-live-010-K0015`, `mikey-youtube-live-010-K0023`, `mikey-youtube-live-010-K0024`, `mikey-youtube-live-010-K0031`, `mikey-youtube-live-010-K0033`；do_not_generalize=`mikey-youtube-live-002-K030`, `mikey-youtube-live-002-K033`。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-001-K013` → `mikey-youtube-live-001-E0016-R004` → `S00647`；`mikey-youtube-live-001-K021` → `mikey-youtube-live-001-E0024-R001` → `S01407`；`mikey-youtube-live-004-K0007` → `mikey-youtube-live-004-E0012` → `mikey-youtube-live-004-E0012-R017`；`mikey-youtube-live-004-K0012` → `mikey-youtube-live-004-E0018` → `mikey-youtube-live-004-E0018-R028`；`mikey-youtube-live-004-K0017` → `mikey-youtube-live-004-E0028` → `mikey-youtube-live-004-E0028-R004`；`mikey-youtube-live-004-K0018` → `mikey-youtube-live-004-E0029` → `mikey-youtube-live-004-E0029-R003`；`mikey-youtube-live-006-K0003` → `mikey-youtube-live-006-E0004` → `mikey-youtube-live-006-E0004-R022`；`mikey-youtube-live-006-K0006` → `mikey-youtube-live-006-E0007` → `mikey-youtube-live-006-E0007-R040`；`mikey-youtube-live-006-K0007` → `mikey-youtube-live-006-E0008` → `mikey-youtube-live-006-E0008-R040`；`mikey-youtube-live-006-K0008` → `mikey-youtube-live-006-E0009` → `mikey-youtube-live-006-E0009-R041`；`mikey-youtube-live-006-K0014` → `mikey-youtube-live-006-E0018` → `mikey-youtube-live-006-E0018-R024`；`mikey-youtube-live-006-K0015` → `mikey-youtube-live-006-E0019` → `mikey-youtube-live-006-E0019-R001`；`mikey-youtube-live-006-K0018` → `mikey-youtube-live-006-E0021` → `mikey-youtube-live-006-E0021-R004`；`mikey-youtube-live-006-K0019` → `mikey-youtube-live-006-E0022` → `mikey-youtube-live-006-E0022-R007`；`mikey-youtube-live-006-K0021` → `mikey-youtube-live-006-E0026` → `mikey-youtube-live-006-E0026-R053`；`mikey-youtube-live-009-K0005` → `mikey-youtube-live-009-E0005` → `mikey-youtube-live-009-E0005-R071`；`mikey-youtube-live-009-K0009` → `mikey-youtube-live-009-E0012` → `mikey-youtube-live-009-E0012-R001`；`mikey-youtube-live-009-K0011` → `mikey-youtube-live-009-E0014` → `mikey-youtube-live-009-E0014-R004`；`mikey-youtube-live-010-K0003` → `mikey-youtube-live-010-E0002` → `mikey-youtube-live-010-E0002-R008`；`mikey-youtube-live-010-K0008` → `mikey-youtube-live-010-E0006` → `mikey-youtube-live-010-E0006-R001`；`mikey-youtube-live-010-K0017` → `mikey-youtube-live-010-E0011` → `mikey-youtube-live-010-E0011-R003`

### T13 · 场景、物流、夜场与成本

**判断：** 场景和现实条件会改变策略，但不改变拒绝与诚实边界；时间、场所、同行者、交通和成本应作为约束，而不是推进理由。

**理由：** 提前确认安排，选择与自身能力和双方意愿匹配的场所；控制约会成本并保留退出空间。

**方法顺序：** 确认时间/场所/同行等物流 → 选匹配场景 → 保留退出与取消空间 → 根据现实约束调整节奏 → 不把物流当同意

**条件：** 仅用于附件中可确认属于Mikey的观点；若具体知识关联blocking待核，则运行时降级为hold。；post-audit规则：hold、mixed_speakers、attributed_other或关联open blocking的知识不得支撑第一人称建议。

**反馈观察：** 附件中的反馈主要来自直播问答、案例口述与Mikey的解释；不是独立验证的因果结果。

**停止线：** 出现明确拒绝、持续不回应/不停留、明显不适，或事实不足以判断时，停止推进或停止下确定结论。

**运行时证据分层：** direct 5；context_only 4；hold 12；do_not_generalize 1。主题用于组织全部相关知识，但只有direct_support_knowledge_ids可支撑Mikey第一人称行动建议；context_only只作背景，held/do_not_generalize不得被主题措辞间接升级。

**direct 支撑知识：** `mikey-youtube-live-001-K009`, `mikey-youtube-live-004-K0001`, `mikey-youtube-live-006-K0003`, `mikey-youtube-live-009-K0011`, `mikey-youtube-live-009-K0013`

**受限知识：** context_only=`mikey-youtube-live-001-K016`, `mikey-youtube-live-005-K006`, `mikey-youtube-live-007-K016`, `mikey-youtube-live-008-K022`；hold=`mikey-youtube-live-001-K017`, `mikey-youtube-live-002-K018`, `mikey-youtube-live-002-K028`, `mikey-youtube-live-002-K031`, `mikey-youtube-live-002-K045`, `mikey-youtube-live-003-K003`, `mikey-youtube-live-003-K010`, `mikey-youtube-live-004-K0008`, `mikey-youtube-live-005-K019`, `mikey-youtube-live-006-K0011`, `mikey-youtube-live-010-K0002`, `mikey-youtube-live-010-K0019`；do_not_generalize=`mikey-youtube-live-002-K041`。

**来源：** `mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`

**direct 代表性精确证据：** `mikey-youtube-live-001-K009` → `mikey-youtube-live-001-E0014-R018` → `S00500`；`mikey-youtube-live-004-K0001` → `mikey-youtube-live-004-E0002` → `mikey-youtube-live-004-E0002-R020`；`mikey-youtube-live-006-K0003` → `mikey-youtube-live-006-E0004` → `mikey-youtube-live-006-E0004-R022`；`mikey-youtube-live-009-K0011` → `mikey-youtube-live-009-E0014` → `mikey-youtube-live-009-E0014-R004`；`mikey-youtube-live-009-K0013` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R060`

## 跨期命题

### P01 · 接纳焦虑或低状态，再行动，而不是等到完全不焦虑才开始。

- **归属口径：** `explicit_mikey_single_direct_source_with_cross_episode_context`；运行时 `direct`。
- **推理：** post-audit后只有一个来源的direct级explicit_mikey知识可直接支撑该命题；其他相关材料仅为context_only/hold，因此不得把跨期重复写成额外的Mikey第一人称证据。
- **条件：** 状态允许存在不等于放弃行动；严重心理危机或医学问题不由这些直播材料判断。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-006-K0009`
- **context：** `mikey-youtube-live-001-K018`, `mikey-youtube-live-007-K009`
- **restricted：** `mikey-youtube-live-002-K003`, `mikey-youtube-live-010-K0001`
- **精确证据：** `mikey-youtube-live-006-K0009` → `mikey-youtube-live-006-E0010` → `mikey-youtube-live-006-E0010-R019`；`mikey-youtube-live-006-K0009` → `mikey-youtube-live-006-E0010` → `mikey-youtube-live-006-E0010-R032`

### P02 · 真实、一致的表达比现场背技巧更接近Mikey反复强调的底层方向。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 一致性不是‘只要做自己就一定有吸引力’，也不替代价值建设。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-001-K020`, `mikey-youtube-live-002-K008`
- **context：** `mikey-youtube-live-001-K012`, `mikey-youtube-live-005-K015`
- **restricted：** `mikey-youtube-live-010-K0028`
- **精确证据：** `mikey-youtube-live-001-K020` → `mikey-youtube-live-001-E0023-R004` → `S01226`；`mikey-youtube-live-001-K020` → `mikey-youtube-live-001-E0023-R005` → `S01227`；`mikey-youtube-live-002-K008` → `mikey-youtube-live-002-E0016-R001` → `S00461`；`mikey-youtube-live-002-K008` → `mikey-youtube-live-002-E0016-R002` → `S00462`

### P03 · 技巧是辅助和加速器，不能替代个人本身、生活内容和现场判断。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 具体高风险技巧若关联blocking review不得据此放行。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-001-K022`, `mikey-youtube-live-002-K013`, `mikey-youtube-live-009-K0011`
- **context：** `mikey-youtube-live-005-K003`
- **restricted：** 无
- **精确证据：** `mikey-youtube-live-001-K022` → `mikey-youtube-live-001-E0025-R025` → `S01602`；`mikey-youtube-live-001-K022` → `mikey-youtube-live-001-E0025-R026` → `S01603`；`mikey-youtube-live-002-K013` → `mikey-youtube-live-002-E0020-R096` → `S00741`；`mikey-youtube-live-002-K013` → `mikey-youtube-live-002-E0020-R098` → `S00743`；`mikey-youtube-live-009-K0011` → `mikey-youtube-live-009-E0014` → `mikey-youtube-live-009-E0014-R004`；`mikey-youtube-live-009-K0011` → `mikey-youtube-live-009-E0014` → `mikey-youtube-live-009-E0014-R030`

### P04 · 学习路径是实践—反馈—复盘—再实践，而不是只堆理论或只堆次数。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 数量与时间数字均只作个案背景，不作为统一KPI。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-004-K0005`
- **context：** `mikey-youtube-live-005-K010`, `mikey-youtube-live-007-K018`
- **restricted：** `mikey-youtube-live-009-K0017`, `mikey-youtube-live-010-K0026`, `mikey-youtube-live-003-K008`
- **精确证据：** `mikey-youtube-live-004-K0005` → `mikey-youtube-live-004-E0009` → `mikey-youtube-live-004-E0009-R007`；`mikey-youtube-live-004-K0005` → `mikey-youtube-live-004-E0009` → `mikey-youtube-live-004-E0009-R028`；`mikey-youtube-live-009-K0017` → `mikey-youtube-live-009-E0018` → `mikey-youtube-live-009-E0018-R011`；`mikey-youtube-live-009-K0017` → `mikey-youtube-live-009-E0018` → `mikey-youtube-live-009-E0018-R028`；`mikey-youtube-live-010-K0026` → `mikey-youtube-live-010-E0019` → `mikey-youtube-live-010-E0019-R003`；`mikey-youtube-live-010-K0026` → `mikey-youtube-live-010-E0019` → `mikey-youtube-live-010-E0019-R015`

### P05 · 展示面和外在条件主要影响接触机会，线下继续与否仍取决于本人互动与综合价值。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 收入、外貌、成功率等绝对化说法不泛化。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-006-K0017`, `mikey-youtube-live-009-K0010`
- **context：** `mikey-youtube-live-008-K019`
- **restricted：** `mikey-youtube-live-010-K0022`
- **精确证据：** `mikey-youtube-live-006-K0017` → `mikey-youtube-live-006-E0020` → `mikey-youtube-live-006-E0020-R041`；`mikey-youtube-live-006-K0017` → `mikey-youtube-live-006-E0020` → `mikey-youtube-live-006-E0020-R057`；`mikey-youtube-live-009-K0010` → `mikey-youtube-live-009-E0013` → `mikey-youtube-live-009-E0013-R034`；`mikey-youtube-live-009-K0010` → `mikey-youtube-live-009-E0013` → `mikey-youtube-live-009-E0013-R065`；`mikey-youtube-live-010-K0022` → `mikey-youtube-live-010-E0016` → `mikey-youtube-live-010-E0016-R015`；`mikey-youtube-live-010-K0022` → `mikey-youtube-live-010-E0016` → `mikey-youtube-live-010-E0016-R053`

### P06 · 展示面应真实且与真人一致，网图或过度修图会制造信任断裂。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** ‘适度修图’边界是人物判断，不是可量化标准。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-009-K0012`
- **context：** `mikey-youtube-live-008-K020`
- **restricted：** `mikey-youtube-live-010-K0022`
- **精确证据：** `mikey-youtube-live-009-K0012` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R011`；`mikey-youtube-live-009-K0012` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R028`；`mikey-youtube-live-010-K0022` → `mikey-youtube-live-010-E0016` → `mikey-youtube-live-010-E0016-R015`；`mikey-youtube-live-010-K0022` → `mikey-youtube-live-010-E0016` → `mikey-youtube-live-010-E0016-R053`

### P07 · 聊天应从真实好奇和生活经历出发，而不是机械交换履历或照抄固定话题。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 对方持续简短收口时需重新判断意愿。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-006-K0006`
- **context：** `mikey-youtube-live-005-K012`, `mikey-youtube-live-007-K006`
- **restricted：** `mikey-youtube-live-010-K0025`, `mikey-youtube-live-004-K0013`
- **精确证据：** `mikey-youtube-live-006-K0006` → `mikey-youtube-live-006-E0007` → `mikey-youtube-live-006-E0007-R040`；`mikey-youtube-live-006-K0006` → `mikey-youtube-live-006-E0007` → `mikey-youtube-live-006-E0007-R071`；`mikey-youtube-live-010-K0025` → `mikey-youtube-live-010-E0018` → `mikey-youtube-live-010-E0018-R055`；`mikey-youtube-live-010-K0025` → `mikey-youtube-live-010-E0018` → `mikey-youtube-live-010-E0018-R078`

### P08 · 故事最好来自自己的真实经历；先有生活，再练清楚、有感染力的表达。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 不把编造经历作为表达训练。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-006-K0007`, `mikey-youtube-live-006-K0008`
- **context：** 无
- **restricted：** `mikey-youtube-live-009-K0023`, `mikey-youtube-live-010-K0011`
- **精确证据：** `mikey-youtube-live-006-K0007` → `mikey-youtube-live-006-E0008` → `mikey-youtube-live-006-E0008-R040`；`mikey-youtube-live-006-K0007` → `mikey-youtube-live-006-E0008` → `mikey-youtube-live-006-E0008-R067`；`mikey-youtube-live-006-K0008` → `mikey-youtube-live-006-E0009` → `mikey-youtube-live-006-E0009-R041`；`mikey-youtube-live-006-K0008` → `mikey-youtube-live-006-E0009` → `mikey-youtube-live-006-E0009-R071`；`mikey-youtube-live-009-K0023` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R030`；`mikey-youtube-live-009-K0023` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R035`

### P09 · 减少现场犹豫、把单次拒绝与自我价值分开，是附件中可直接使用的行动方向；不保证具体结果。

- **归属口径：** `explicit_mikey_single_direct_source_with_cross_episode_context`；运行时 `direct`。
- **推理：** post-audit后只有一个来源的direct级explicit_mikey知识可直接支撑该命题；其他相关材料仅为context_only/hold，因此不得把跨期重复写成额外的Mikey第一人称证据。
- **条件：** 只在安全、合适场景适用；不得用三秒原则覆盖拒绝或场所规则。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-004-K0010`
- **context：** `mikey-youtube-live-005-K011`
- **restricted：** `mikey-youtube-live-009-K0002`, `mikey-youtube-live-010-K0001`
- **精确证据：** `mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0016` → `mikey-youtube-live-004-E0016-R060`；`mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0017` → `mikey-youtube-live-004-E0017-R013`

### P10 · 对方明确拒绝、持续不停留或不愿转场时，应停止，而不是把技巧或既有投入当继续施压的理由。

- **归属口径：** `restricted_after_direct_major_semantic_audit`；运行时 `hold`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 这是运行时停止线；涉及具体亲密升级案例仍需遵守其blocking review。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** 无
- **context：** 无
- **restricted：** `mikey-youtube-live-009-K0024`, `mikey-youtube-live-009-K0008`, `mikey-youtube-live-010-K0019`, `mikey-youtube-live-003-K005`, `mikey-youtube-live-003-K007`, `mikey-youtube-live-004-K0014`, `mikey-youtube-live-005-K019`, `mikey-youtube-live-006-K0004`, `mikey-youtube-live-010-K0012`
- **精确证据：** `mikey-youtube-live-009-K0024` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R039`；`mikey-youtube-live-009-K0024` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R052`；`mikey-youtube-live-009-K0008` → `mikey-youtube-live-009-E0011` → `mikey-youtube-live-009-E0011-R002`；`mikey-youtube-live-009-K0008` → `mikey-youtube-live-009-E0011` → `mikey-youtube-live-009-E0011-R010`；`mikey-youtube-live-010-K0019` → `mikey-youtube-live-010-E0013` → `mikey-youtube-live-010-E0013-R033`；`mikey-youtube-live-010-K0019` → `mikey-youtube-live-010-E0013` → `mikey-youtube-live-010-E0013-R052`

### P11 · 不要把肢体接触本身当作关系温度或继续意愿的唯一指标。

- **归属口径：** `explicit_mikey_single_direct_source_with_cross_episode_context`；运行时 `direct`。
- **推理：** post-audit后只有一个来源的direct级explicit_mikey知识可直接支撑该命题；其他相关材料仅为context_only/hold，因此不得把跨期重复写成额外的Mikey第一人称证据。
- **条件：** 任何先前行为都不能替代后续具体行为的同意。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-004-K0007`
- **context：** `mikey-youtube-live-002-K010`, `mikey-youtube-live-005-K006`, `mikey-youtube-live-008-K023`
- **restricted：** 无
- **精确证据：** `mikey-youtube-live-004-K0007` → `mikey-youtube-live-004-E0012` → `mikey-youtube-live-004-E0012-R017`；`mikey-youtube-live-004-K0007` → `mikey-youtube-live-004-E0012` → `mikey-youtube-live-004-E0012-R047`

### P12 · 关系意图应尽早诚实说明，不用虚假恋爱承诺或假装朋友换取推进。

- **归属口径：** `explicit_mikey_single_direct_source_with_cross_episode_context`；运行时 `direct`。
- **推理：** post-audit后只有一个来源的direct级explicit_mikey知识可直接支撑该命题；其他相关材料仅为context_only/hold，因此不得把跨期重复写成额外的Mikey第一人称证据。
- **条件：** 部分短期关系个案含blocking review，只保留‘诚实/停止’层面的稳定边界。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-001-K002`, `mikey-youtube-live-001-K027`
- **context：** 无
- **restricted：** `mikey-youtube-live-004-K0002`, `mikey-youtube-live-009-K0018`
- **精确证据：** `mikey-youtube-live-001-K002` → `mikey-youtube-live-001-E0007-R036` → `S00157`；`mikey-youtube-live-001-K002` → `mikey-youtube-live-001-E0007-R037` → `S00158`；`mikey-youtube-live-001-K027` → `mikey-youtube-live-001-E0031-R011` → `S02022`；`mikey-youtube-live-001-K027` → `mikey-youtube-live-001-E0031-R012` → `S02023`

### P13 · 边界表达应清楚、平静，并允许对方离开；边界不等于辱骂、爆发或控制对方。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 涉及强硬语气或冲突案例时按对应review降级。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-009-K0021`
- **context：** `mikey-youtube-live-002-K021`
- **restricted：** `mikey-youtube-live-010-K0006`, `mikey-youtube-live-010-K0016`
- **精确证据：** `mikey-youtube-live-009-K0021` → `mikey-youtube-live-009-E0024` → `mikey-youtube-live-009-E0024-R018`；`mikey-youtube-live-009-K0021` → `mikey-youtube-live-009-E0024` → `mikey-youtube-live-009-E0024-R035`；`mikey-youtube-live-010-K0006` → `mikey-youtube-live-010-E0004` → `mikey-youtube-live-010-E0004-R028`；`mikey-youtube-live-010-K0006` → `mikey-youtube-live-010-E0004` → `mikey-youtube-live-010-E0004-R081`

### P14 · 兴趣判断需要多项反馈和现实条件，不能由一个信号、穿着或一句模糊回复推出。

- **归属口径：** `explicit_mikey_single_direct_source_with_cross_episode_context`；运行时 `direct`。
- **推理：** post-audit后只有一个来源的direct级explicit_mikey知识可直接支撑该命题；其他相关材料仅为context_only/hold，因此不得把跨期重复写成额外的Mikey第一人称证据。
- **条件：** 区域、性别本质或概率化解释不作为证据。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-009-K0015`
- **context：** `mikey-youtube-live-005-K007`, `mikey-youtube-live-008-K023`
- **restricted：** `mikey-youtube-live-009-K0006`
- **精确证据：** `mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R005`；`mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R017`

### P15 · 诊断互动问题时，先区分自己的表达、对方持续投入和现实条件，再决定练什么；不能只凭一个表象下单一原因结论。

- **归属口径：** `explicit_mikey_single_direct_source_with_cross_episode_context`；运行时 `direct`。
- **推理：** post-audit后只有一个来源的direct级explicit_mikey知识可直接支撑该命题；其他相关材料仅为context_only/hold，因此不得把跨期重复写成额外的Mikey第一人称证据。
- **条件：** mikey-youtube-live-001-K026本身关联blocking physical-escalation review，因此只抽取其‘信息不足不确定’的元诊断原则。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-009-K0004`, `mikey-youtube-live-009-K0015`
- **context：** 无
- **restricted：** `mikey-youtube-live-001-K026`, `mikey-youtube-live-009-K0014`
- **精确证据：** `mikey-youtube-live-009-K0004` → `mikey-youtube-live-009-E0005` → `mikey-youtube-live-009-E0005-R021`；`mikey-youtube-live-009-K0004` → `mikey-youtube-live-009-E0005` → `mikey-youtube-live-009-E0005-R038`；`mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R005`；`mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R017`

### P16 · 线上展示、文字/电话和线下见面承担不同功能，线上最终仍要由线下真实互动验证。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 不能把电话或线上热度当作后续同意或结果。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-004-K0020`, `mikey-youtube-live-006-K0017`
- **context：** `mikey-youtube-live-008-K008`
- **restricted：** `mikey-youtube-live-009-K0008`, `mikey-youtube-live-010-K0029`
- **精确证据：** `mikey-youtube-live-004-K0020` → `mikey-youtube-live-004-E0030` → `mikey-youtube-live-004-E0030-R105`；`mikey-youtube-live-004-K0020` → `mikey-youtube-live-004-E0031` → `mikey-youtube-live-004-E0031-R005`；`mikey-youtube-live-006-K0017` → `mikey-youtube-live-006-E0020` → `mikey-youtube-live-006-E0020-R041`；`mikey-youtube-live-006-K0017` → `mikey-youtube-live-006-E0020` → `mikey-youtube-live-006-E0020-R057`；`mikey-youtube-live-009-K0008` → `mikey-youtube-live-009-E0011` → `mikey-youtube-live-009-E0011-R002`；`mikey-youtube-live-009-K0008` → `mikey-youtube-live-009-E0011` → `mikey-youtube-live-009-E0011-R010`

### P17 · 把对方当人而非战利品，是这批材料中与诚实、合作框架和拒绝边界相连的伦理主线。

- **归属口径：** `explicit_mikey_single_direct_source_with_cross_episode_context`；运行时 `direct`。
- **推理：** post-audit后只有一个来源的direct级explicit_mikey知识可直接支撑该命题；其他相关材料仅为context_only/hold，因此不得把跨期重复写成额外的Mikey第一人称证据。
- **条件：** K023关联blocking relationship_ethics review；因此运行时保留其尊重原则，不使用未核案例细节。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-002-K009`, `mikey-youtube-live-002-K042`
- **context：** 无
- **restricted：** `mikey-youtube-live-001-K023`
- **精确证据：** `mikey-youtube-live-002-K009` → `mikey-youtube-live-002-E0016-R031` → `S00491`；`mikey-youtube-live-002-K009` → `mikey-youtube-live-002-E0016-R033` → `S00493`；`mikey-youtube-live-002-K042` → `mikey-youtube-live-002-E0069-R037` → `S04242`；`mikey-youtube-live-002-K042` → `mikey-youtube-live-002-E0069-R039` → `S04244`

### P18 · 长期成长应同时建设生活、能力、形象、表达和内在稳定，不把一次关系结果当自我价值证明。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 收入、身高、外貌等仅作可见条件，不作人格或结果的确定因果。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-001-K021`, `mikey-youtube-live-006-K0019`, `mikey-youtube-live-009-K0026`
- **context：** `mikey-youtube-live-008-K021`
- **restricted：** `mikey-youtube-live-010-K0032`
- **精确证据：** `mikey-youtube-live-001-K021` → `mikey-youtube-live-001-E0024-R001` → `S01407`；`mikey-youtube-live-001-K021` → `mikey-youtube-live-001-E0024-R004` → `S01410`；`mikey-youtube-live-006-K0019` → `mikey-youtube-live-006-E0022` → `mikey-youtube-live-006-E0022-R007`；`mikey-youtube-live-006-K0019` → `mikey-youtube-live-006-E0022` → `mikey-youtube-live-006-E0022-R022`；`mikey-youtube-live-009-K0026` → `mikey-youtube-live-009-E0028` → `mikey-youtube-live-009-E0028-R001`；`mikey-youtube-live-009-K0026` → `mikey-youtube-live-009-E0028` → `mikey-youtube-live-009-E0028-R031`

### P19 · 当互动持续无效或没有吸引时，可以结束约会或降低投入，不必每次强行推进。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 降低投入不等于惩罚或操纵对方。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-002-K004`, `mikey-youtube-live-004-K0009`
- **context：** 无
- **restricted：** `mikey-youtube-live-009-K0019`, `mikey-youtube-live-010-K0030`
- **精确证据：** `mikey-youtube-live-002-K004` → `mikey-youtube-live-002-E0010-R004` → `S00244`；`mikey-youtube-live-002-K004` → `mikey-youtube-live-002-E0010-R005` → `S00245`；`mikey-youtube-live-004-K0009` → `mikey-youtube-live-004-E0015` → `mikey-youtube-live-004-E0015-R020`；`mikey-youtube-live-004-K0009` → `mikey-youtube-live-004-E0015` → `mikey-youtube-live-004-E0015-R040`

### P20 · 时间、场所、同行者和成本属于物流约束，应先确认现实安排并选择双方愿意的场景；物流本身不构成同意。

- **归属口径：** `explicit_mikey_cross_episode_direct_support`；运行时 `direct`。
- **推理：** 该命题只以post-audit后仍为direct的explicit_mikey知识作为主证据；来自多个来源的direct证据允许做跨期归纳。context_only/hold材料仅作背景或限制，不用于强化Mikey第一人称结论。
- **条件：** 物流条件只调整安排，不能被当作对亲密行为的授权。；运行时仅可使用supporting_knowledge_ids中的direct知识；context_knowledge_ids和restricted_knowledge_ids不能支撑第一人称建议。
- **direct 支撑：** `mikey-youtube-live-001-K009`, `mikey-youtube-live-009-K0013`
- **context：** 无
- **restricted：** `mikey-youtube-live-003-K003`, `mikey-youtube-live-005-K019`
- **精确证据：** `mikey-youtube-live-001-K009` → `mikey-youtube-live-001-E0014-R018` → `S00500`；`mikey-youtube-live-001-K009` → `mikey-youtube-live-001-E0014-R019` → `S00501`；`mikey-youtube-live-009-K0013` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R060`；`mikey-youtube-live-009-K0013` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R065`

## 方法关系

### MR01 · sequence

**关系：** `T01` → `T03`。先接纳当下焦虑/状态，再进入行动—反馈—复盘；不是先把情绪修到完美才行动。

**依据类型：** `mikey_explicit_cross_episode_direct_support`；运行时 `direct`。

**direct 支撑：** `mikey-youtube-live-006-K0009`, `mikey-youtube-live-004-K0010`

**context：** 无；**restricted：** `mikey-youtube-live-009-K0017`, `mikey-youtube-live-002-K003`, `mikey-youtube-live-010-K0001`。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-006-K0009` → `mikey-youtube-live-006-E0010` → `mikey-youtube-live-006-E0010-R019`；`mikey-youtube-live-006-K0009` → `mikey-youtube-live-006-E0010` → `mikey-youtube-live-006-E0010-R032`；`mikey-youtube-live-009-K0017` → `mikey-youtube-live-009-E0018` → `mikey-youtube-live-009-E0018-R011`；`mikey-youtube-live-009-K0017` → `mikey-youtube-live-009-E0018` → `mikey-youtube-live-009-E0018-R028`；`mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0016` → `mikey-youtube-live-004-E0016-R060`；`mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0017` → `mikey-youtube-live-004-E0017-R013`

### MR02 · sequence

**关系：** `T05` → `T11`。线上先用真实展示面争取接触，再用简洁联络/邀约进入线下验证。

**依据类型：** `context_only_after_direct_major_semantic_audit`；运行时 `context_only`。

**direct 支撑：** 无

**context：** `mikey-youtube-live-008-K019`；**restricted：** `mikey-youtube-live-009-K0008`, `mikey-youtube-live-010-K0022`, `mikey-youtube-live-009-K0001`。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-009-K0008` → `mikey-youtube-live-009-E0011` → `mikey-youtube-live-009-E0011-R002`；`mikey-youtube-live-009-K0008` → `mikey-youtube-live-009-E0011` → `mikey-youtube-live-009-E0011-R010`；`mikey-youtube-live-010-K0022` → `mikey-youtube-live-010-E0016` → `mikey-youtube-live-010-E0016-R015`；`mikey-youtube-live-010-K0022` → `mikey-youtube-live-010-E0016` → `mikey-youtube-live-010-E0016-R053`

### MR03 · condition

**关系：** `T04` → `T02`。技巧只有在不破坏真实性与一致性的条件下作为辅助；一旦现场持续计算导致僵硬，应回到自然交流。

**依据类型：** `mikey_explicit_single_source_plus_editorial_relation`；运行时 `direct`。

**direct 支撑：** `mikey-youtube-live-001-K022`

**context：** `mikey-youtube-live-001-K012`, `mikey-youtube-live-005-K003`；**restricted：** 无。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-001-K022` → `mikey-youtube-live-001-E0025-R025` → `S01602`；`mikey-youtube-live-001-K022` → `mikey-youtube-live-001-E0025-R026` → `S01603`

### MR04 · condition

**关系：** `T08` → `T09`。兴趣信号只能支持继续了解；明确拒绝出现时，拒绝停止线优先于任何兴趣推断。

**依据类型：** `mikey_explicit_cross_episode_direct_support`；运行时 `direct`。

**direct 支撑：** `mikey-youtube-live-009-K0015`

**context：** `mikey-youtube-live-005-K006`, `mikey-youtube-live-008-K023`；**restricted：** `mikey-youtube-live-009-K0024`, `mikey-youtube-live-010-K0019`, `mikey-youtube-live-004-K0014`, `mikey-youtube-live-006-K0004`。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R005`；`mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R017`；`mikey-youtube-live-009-K0024` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R039`；`mikey-youtube-live-009-K0024` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R052`；`mikey-youtube-live-010-K0019` → `mikey-youtube-live-010-E0013` → `mikey-youtube-live-010-E0013-R033`；`mikey-youtube-live-010-K0019` → `mikey-youtube-live-010-E0013` → `mikey-youtube-live-010-E0013-R052`

### MR05 · sequence

**关系：** `T10` → `T09`。先说明关系意图并确认对方是否接受；不接受就停止，不用承诺、欺骗或既有投入继续推动。

**依据类型：** `mikey_explicit_cross_episode_direct_support`；运行时 `direct`。

**direct 支撑：** `mikey-youtube-live-001-K002`, `mikey-youtube-live-001-K027`

**context：** 无；**restricted：** `mikey-youtube-live-009-K0024`, `mikey-youtube-live-004-K0002`, `mikey-youtube-live-005-K019`。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-001-K002` → `mikey-youtube-live-001-E0007-R036` → `S00157`；`mikey-youtube-live-001-K002` → `mikey-youtube-live-001-E0007-R037` → `S00158`；`mikey-youtube-live-001-K027` → `mikey-youtube-live-001-E0031-R011` → `S02022`；`mikey-youtube-live-001-K027` → `mikey-youtube-live-001-E0031-R012` → `S02023`；`mikey-youtube-live-009-K0024` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R039`；`mikey-youtube-live-009-K0024` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R052`

### MR06 · feedback_loop

**关系：** `T03` → `T08`。实践不是盲目重复；每次行动要读取对方反馈和自己的表现，再决定调整。

**依据类型：** `context_only_after_direct_major_semantic_audit`；运行时 `context_only`。

**direct 支撑：** 无

**context：** `mikey-youtube-live-007-K018`, `mikey-youtube-live-005-K010`；**restricted：** `mikey-youtube-live-009-K0017`。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-009-K0017` → `mikey-youtube-live-009-E0018` → `mikey-youtube-live-009-E0018-R011`；`mikey-youtube-live-009-K0017` → `mikey-youtube-live-009-E0018` → `mikey-youtube-live-009-E0018-R028`

### MR07 · sequence

**关系：** `T06` → `T08`。聊天先真实交流并给彼此表达空间，再根据对方投入决定是否深入，而不是靠提问数量推进。

**依据类型：** `mikey_explicit_single_source_plus_editorial_relation`；运行时 `direct`。

**direct 支撑：** `mikey-youtube-live-006-K0006`

**context：** `mikey-youtube-live-007-K019`；**restricted：** `mikey-youtube-live-010-K0013`。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-006-K0006` → `mikey-youtube-live-006-E0007` → `mikey-youtube-live-006-E0007-R040`；`mikey-youtube-live-006-K0006` → `mikey-youtube-live-006-E0007` → `mikey-youtube-live-006-E0007-R071`

### MR08 · condition

**关系：** `T13` → `T09`。物流信息可改变时间与场所安排，但不能改变同意标准。

**依据类型：** `cross_episode_editorial_safety_condition_with_direct_logistics_support`；运行时 `direct`。

**direct 支撑：** `mikey-youtube-live-001-K009`, `mikey-youtube-live-009-K0013`

**context：** 无；**restricted：** `mikey-youtube-live-005-K019`。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-001-K009` → `mikey-youtube-live-001-E0014-R018` → `S00500`；`mikey-youtube-live-001-K009` → `mikey-youtube-live-001-E0014-R019` → `S00501`；`mikey-youtube-live-009-K0013` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R060`；`mikey-youtube-live-009-K0013` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R065`

### MR09 · sequence

**关系：** `T12` → `T05`。长期先建设真实生活、能力和形象，再把这些真实内容呈现在展示面和现场互动里。

**依据类型：** `mikey_explicit_cross_episode_direct_support`；运行时 `direct`。

**direct 支撑：** `mikey-youtube-live-006-K0007`, `mikey-youtube-live-009-K0026`

**context：** `mikey-youtube-live-008-K021`；**restricted：** 无。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-006-K0007` → `mikey-youtube-live-006-E0008` → `mikey-youtube-live-006-E0008-R040`；`mikey-youtube-live-006-K0007` → `mikey-youtube-live-006-E0008` → `mikey-youtube-live-006-E0008-R067`；`mikey-youtube-live-009-K0026` → `mikey-youtube-live-009-E0028` → `mikey-youtube-live-009-E0028-R001`；`mikey-youtube-live-009-K0026` → `mikey-youtube-live-009-E0028` → `mikey-youtube-live-009-E0028-R031`

### MR10 · condition

**关系：** `T07` → `T09`。三秒行动、直接表达等只用于启动接触；对方拒绝、不停留或场景不合适时立即失效。

**依据类型：** `mikey_explicit_cross_episode_direct_support`；运行时 `direct`。

**direct 支撑：** `mikey-youtube-live-004-K0010`

**context：** 无；**restricted：** `mikey-youtube-live-009-K0024`, `mikey-youtube-live-010-K0019`, `mikey-youtube-live-010-K0001`, `mikey-youtube-live-010-K0012`。

**边界：** held/mixed/attributed_other/blocking知识只记录关系背景，不能作为此步骤顺序的Mikey第一人称证据。

**精确证据：** `mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0016` → `mikey-youtube-live-004-E0016-R060`；`mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0017` → `mikey-youtube-live-004-E0017-R013`；`mikey-youtube-live-009-K0024` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R039`；`mikey-youtube-live-009-K0024` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R052`；`mikey-youtube-live-010-K0019` → `mikey-youtube-live-010-E0013` → `mikey-youtube-live-010-E0013-R033`；`mikey-youtube-live-010-K0019` → `mikey-youtube-live-010-E0013` → `mikey-youtube-live-010-E0013-R052`

## 跨期冲突、变化与情境差异

### C01 · 技巧 vs 自然

**张力：** 部分单期提供具体开场、施压减压、三秒原则等工具；同时多期强调技巧只是辅助、过度计算会僵硬。

**处理：** 不强行统一为‘不用技巧’。按阶段解释：新手可用工具启动，长期目标是内化并回到自然交流。

**cross-audit 对应：** `T3`。

**知识及当前级别：** `mikey-youtube-live-001-K022`=direct, `mikey-youtube-live-002-K002`=hold, `mikey-youtube-live-004-K0010`=direct, `mikey-youtube-live-001-K012`=context_only。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-001-K022` → `mikey-youtube-live-001-E0025-R025` → `S01602`；`mikey-youtube-live-002-K002` → `mikey-youtube-live-002-E0006-R007` → `S00121`；`mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0016` → `mikey-youtube-live-004-E0016-R060`；`mikey-youtube-live-001-K012` → `mikey-youtube-live-001-E0015-R027` → `S00614`

### C02 · 直接 vs 间接开场

**张力：** 材料既有意图清晰/直接，也有问路等间接过渡。

**处理：** 保留情境差异：形式可直接或间接，但不把欺骗当核心；过渡式问路相关知识有hold/major边界。

**cross-audit 对应：** `T5`。

**知识及当前级别：** `mikey-youtube-live-001-K027`=direct, `mikey-youtube-live-002-K002`=hold, `mikey-youtube-live-003-K012`=hold, `mikey-youtube-live-006-K0010`=direct。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-001-K027` → `mikey-youtube-live-001-E0031-R011` → `S02022`；`mikey-youtube-live-002-K002` → `mikey-youtube-live-002-E0006-R007` → `S00121`；`mikey-youtube-live-003-K012` → `mikey-youtube-live-003-E0024-R013` → `S02873`；`mikey-youtube-live-006-K0010` → `mikey-youtube-live-006-E0011` → `mikey-youtube-live-006-E0011-R008`

### C03 · 高能量 vs 接纳当下状态

**张力：** 夜场和部分场景谈能量匹配，但多期明确不要求持续高能量。

**处理：** 场景适配不等于强行高能量；保持真实状态并与场景做适度匹配。

**知识及当前级别：** `mikey-youtube-live-001-K018`=context_only, `mikey-youtube-live-004-K0001`=direct, `mikey-youtube-live-006-K0024`=context_only。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-001-K018` → `mikey-youtube-live-001-E0021-R002` → `S01103`；`mikey-youtube-live-004-K0001` → `mikey-youtube-live-004-E0002` → `mikey-youtube-live-004-E0002-R020`；`mikey-youtube-live-006-K0024` → `mikey-youtube-live-006-E0030` → `mikey-youtube-live-006-E0030-R008`

### C04 · 外在价值 vs 内在价值

**张力：** 材料承认外貌、收入、展示面是门槛，同时反复否认它们能单独决定吸引。

**处理：** 按漏斗位置区分：外在影响被看见/见面机会，线下关系还取决于内在与互动。

**知识及当前级别：** `mikey-youtube-live-006-K0001`=direct, `mikey-youtube-live-009-K0010`=direct, `mikey-youtube-live-010-K0032`=hold。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-006-K0001` → `mikey-youtube-live-006-E0002` → `mikey-youtube-live-006-E0002-R047`；`mikey-youtube-live-009-K0010` → `mikey-youtube-live-009-E0013` → `mikey-youtube-live-009-E0013-R034`；`mikey-youtube-live-010-K0032` → `mikey-youtube-live-010-E0022` → `mikey-youtube-live-010-E0022-R120`

### C05 · 短期关系起点

**张力：** 002-K046保留Mikey个人偏好先短期再观察长期；其他知识强调关系意图诚实、对方不接受就停止。

**处理：** 不把个人偏好提升为通用关系路线；运行时只保留诚实表达与尊重对方选择。

**知识及当前级别：** `mikey-youtube-live-002-K046`=hold, `mikey-youtube-live-001-K002`=direct, `mikey-youtube-live-004-K0002`=hold。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-002-K046` → `mikey-youtube-live-002-E0076-R020` → `S04596`；`mikey-youtube-live-001-K002` → `mikey-youtube-live-001-E0007-R036` → `S00157`；`mikey-youtube-live-004-K0002` → `mikey-youtube-live-004-E0003` → `mikey-youtube-live-004-E0003-R021`

### C06 · 兴趣窗口与拒绝

**张力：** 部分材料讨论黄灯绿灯、施压减压或‘道德束缚’，但另有多期明确拒绝即停止。

**处理：** 窗口判断只能用于低风险互动调整，不能覆盖明确拒绝；关联blocking的亲密升级材料保持hold。

**cross-audit 对应：** `T6`。

**知识及当前级别：** `mikey-youtube-live-001-K008`=hold, `mikey-youtube-live-001-K015`=context_only, `mikey-youtube-live-003-K005`=hold, `mikey-youtube-live-006-K0004`=hold, `mikey-youtube-live-009-K0024`=hold。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-001-K008` → `mikey-youtube-live-001-E0013-R011` → `S00449`；`mikey-youtube-live-001-K015` → `mikey-youtube-live-001-E0017-R008` → `S00767`；`mikey-youtube-live-003-K005` → `mikey-youtube-live-003-E0007-R053` → `S00853`；`mikey-youtube-live-006-K0004` → `mikey-youtube-live-006-E0005` → `mikey-youtube-live-006-E0005-R033`；`mikey-youtube-live-009-K0024` → `mikey-youtube-live-009-E0026` → `mikey-youtube-live-009-E0026-R039`

### C07 · 数量训练 vs 质量复盘

**张力：** 部分材料强调增加实践量，另一些强调没有统一数量、必须复盘。

**处理：** 数量提供样本，复盘决定学习质量；不设置跨人统一成功率或KPI。

**cross-audit 对应：** `T4`。

**知识及当前级别：** `mikey-youtube-live-003-K008`=hold, `mikey-youtube-live-005-K009`=context_only, `mikey-youtube-live-007-K018`=context_only。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-003-K008` → `mikey-youtube-live-003-E0017-R061` → `S02205`；`mikey-youtube-live-005-K009` → `mikey-youtube-live-005-E0012-R021` → `S00525`；`mikey-youtube-live-007-K018` → `mikey-youtube-live-007-E0025-R001` → `S00894`

### C08 · 线上作用

**张力：** 有的材料把微信主要视为联络邀约工具，另一些承认聊天可增加吸引。

**处理：** 线上可增加信息与安全感，但作用有限，最终仍需线下验证。

**知识及当前级别：** `mikey-youtube-live-002-K043`=hold, `mikey-youtube-live-004-K0020`=direct, `mikey-youtube-live-009-K0008`=hold。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-002-K043` → `mikey-youtube-live-002-E0073-R021` → `S04421`；`mikey-youtube-live-004-K0020` → `mikey-youtube-live-004-E0030` → `mikey-youtube-live-004-E0030-R105`；`mikey-youtube-live-009-K0008` → `mikey-youtube-live-009-E0011` → `mikey-youtube-live-009-E0011-R002`

### C09 · 自信来源

**张力：** 材料同时谈正反馈、限制信念、创造价值与‘先相信自己’。其中强因果知识有hold。

**处理：** 保留多路径，不断言单一因果；把可操作部分写为真实行动+复盘+自我支持。

**cross-audit 对应：** `T1`。

**知识及当前级别：** `mikey-youtube-live-007-K007`=context_only, `mikey-youtube-live-007-K027`=hold, `mikey-youtube-live-008-K017`=hold, `mikey-youtube-live-006-K0016`=direct。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-007-K007` → `mikey-youtube-live-007-E0006-R020` → `S00231`；`mikey-youtube-live-007-K027` → `mikey-youtube-live-007-E0036-R001` → `S01202`；`mikey-youtube-live-008-K017` → `mikey-youtube-live-008-E0023-R063` → `S01887`；`mikey-youtube-live-006-K0016` → `mikey-youtube-live-006-E0019` → `mikey-youtube-live-006-E0019-R037`

### C10 · 生活痛苦作为动力

**张力：** 有些单期强调痛苦驱动改变，另有内容反对用‘我不够好’和恐惧长期驱动。

**处理：** 区分启动契机与长期动力：痛苦可触发行动，但长期不应把自我否定当唯一燃料。

**cross-audit 对应：** `T2`。

**知识及当前级别：** `mikey-youtube-live-006-K0021`=direct, `mikey-youtube-live-010-K0023`=hold, `mikey-youtube-live-001-K021`=direct。

**运行时边界：** 冲突账本允许引用hold/context材料来说明‘存在过这种说法或张力’，但运行时解决方案不得把这些材料升级为Mikey第一人称行动建议。

**证据：** `mikey-youtube-live-006-K0021` → `mikey-youtube-live-006-E0026` → `mikey-youtube-live-006-E0026-R053`；`mikey-youtube-live-010-K0023` → `mikey-youtube-live-010-E0017` → `mikey-youtube-live-010-E0017-R034`；`mikey-youtube-live-001-K021` → `mikey-youtube-live-001-E0024-R001` → `S01407`

### C11 · 展示面数量单位：五套内容 vs 六七张照片

**张力：** 不同单期用不同单位给出展示面建议：一处是约五套可置顶内容，一处是约六七张较好的个人照片；它们不是同一个计量口径。

**处理：** 保留为情境化建议，不合成为固定通用数字；运行时先问平台、素材类型和当前展示面问题。

**cross-audit 对应：** `T7`。

**知识及当前级别：** `mikey-youtube-live-005-K005`=hold, `mikey-youtube-live-009-K0009`=direct。

**运行时边界：** 数字仅按对应来源的具体单位和语境使用，不能合并成统一‘标准照片数’。

**证据：** `mikey-youtube-live-005-K005` → `mikey-youtube-live-005-E0010-R001` → `S00413`；`mikey-youtube-live-009-K0009` → `mikey-youtube-live-009-E0012` → `mikey-youtube-live-009-E0012-R001`

## 重复案例与复用账本

输入复用表状态：`not_yet_available`。Do not invent duplicate/reuse conclusions. A later source-reuse.json must be merged before integration.

- 同发布确认：0。
- 同录制确认：0。
- 同案剪辑/复述确认：0。
- 候选关系：0。
- 规则：输入仍未提供可用于最终合并的正式复用表；在后续source-reuse材料并入前，不做最终合并、不降权、不把主题相似写成同发布/同录制/同案剪辑。

- 仅主题相似：`mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`。均含内部群/多人答疑及相似主题，但附件没有正式复用表或录制指纹；只视为主题重叠。
- 仅主题相似：`mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`。连续发布日期且均为公开答疑，主题高度重叠；附件不足以证明同录制或同案例重剪。

## 人物归属边界

- viewer question由Mikey代读时：spoken_by可为mikey，但question_author必须保持输入中的viewer-question-*或viewer-question-collective；问题里的经历、观点和身份不得写成Mikey第一人称。
- caller、guest、viewer、relayed person、screen material、unknown、mixed_speakers、attributed_other的独有说法不得升级为Mikey第一人称指导。
- 不得仅凭时间相邻推断问题—回答配对；只使用输入中已有event/actor/question_author/spoken_by/knowledge归属。
- 播放内容、屏幕小字、画外音、重叠、硬切、重放或稀疏视觉材料若无连续音画确认，只能表述为附件记录或候选。
- post-audit中release_status=hold、attribution_status非explicit_mikey或关联open blocking的知识，无论跨期重复多少次都不得标direct。
- mikey-youtube-live-003的K001-K016全部为mixed_speakers / hold，直到其全片blocking人物归属复核解决；不得用作Mikey第一人称建议。
- 所有78个blocking review仍为open；受影响知识保持hold。

### mikey-youtube-live-001

- `mikey`｜role=`host`｜status=`confirmed`。主持人实名确认；具体短插话仍可能需连续音画复核。 归属依据：固定主持人摄像头贯穿全片；标题标明Mikey在线答疑；多名来电者直接称呼‘Mikey/Mikey哥’，回答声音与主持轮次稳定。稀疏帧不能逐句证明嘴型。 证据：https://www.youtube.com/watch?v=2o0eci1RIos&t=188s, https://www.youtube.com/watch?v=2o0eci1RIos&t=1079s, https://www.youtube.com/watch?v=2o0eci1RIos&t=4075s
- `caller-01`｜role=`internal-group caller / Long哥`｜status=`provisional`。画外电话声音，未完成声纹映射。 归属依据：S00049-S00053称其为龙哥，开场第一人称案例与S00102-S00107收尾连续。 证据：https://www.youtube.com/watch?v=2o0eci1RIos&t=87s, https://www.youtube.com/watch?v=2o0eci1RIos&t=178s
- `caller-02`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号；无实名与声纹确认。
- `caller-03`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号；无实名与声纹确认。
- `caller-04`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号；无实名与声纹确认。
- `caller-05`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号；无实名与声纹确认。
- `caller-06`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号；无实名与声纹确认。
- `caller-07`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号；无实名与声纹确认。
- `caller-08`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号；无实名与声纹确认。
- `viewer-question-01`｜role=`YouTube viewer question author(s)`｜status=`collective_placeholder`。代表多个观众，问题由Mikey代读，不是Mikey自己的观点。 归属依据：Mikey明确说读取YouTube直播间问题。 证据：https://www.youtube.com/watch?v=2o0eci1RIos&t=826s, https://www.youtube.com/watch?v=2o0eci1RIos&t=3996s
- `live-chat-author-01`｜role=`live chat/internal group text author(s)`｜status=`collective_placeholder`。联系表中文字过小，未逐条映射昵称与原文。 归属依据：Mikey逐条引用评论区和内部群答案。 证据：https://www.youtube.com/watch?v=2o0eci1RIos&t=2708s
- `unknown-voice-01`｜role=`unknown/overlapping voice`｜status=`disputed`。不得归为Mikey。 归属依据：自动稿出现语义突变或短重叠插话。 证据：https://www.youtube.com/watch?v=2o0eci1RIos&t=55s

### mikey-youtube-live-002

- `mikey`｜role=`host`｜status=`confirmed`。主持人身份可确认；未听校的短插话及逐句轮次仍可能错分。 归属依据：标题明确Mikey在线答疑；S00064自称Mike，S01638称Mikey本人微信；全片固定模板右下摄像头为同一主持人，群友反复直接称呼Mikey。 证据：https://www.youtube.com/watch?v=NhBTViHCwso&t=152s, https://www.youtube.com/watch?v=NhBTViHCwso&t=2940s, https://www.youtube.com/watch?v=NhBTViHCwso&t=7550s
- `caller-01`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-02`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-03`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-04`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-05`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-06`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-07`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-08`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-09`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-10`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-11`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-12`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `caller-13`｜role=`internal-group caller`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：按连续问题/案例轮次临时编号；无实名或声纹确认。
- `viewer-question-01`｜role=`YouTube viewer question author(s)`｜status=`collective_placeholder`。代表多个观众；代读问题不是Mikey观点。 归属依据：主持人明确切换到YouTube问题并代读。 证据：https://www.youtube.com/watch?v=NhBTViHCwso&t=250s
- `unknown-voice-01`｜role=`unknown or mixed caller voice`｜status=`disputed`。不得按Mikey第一人称使用。 归属依据：自动稿无说话人分离，问答短句和重叠处无法可靠逐句映射。
- `unknown-voice-02`｜role=`unknown caller voice while host away`｜status=`disputed`。不得归为Mikey。 归属依据：主持人离席期间多名群友互相讨论。 证据：https://www.youtube.com/watch?v=NhBTViHCwso&t=2953s

### mikey-youtube-live-003

- `mikey`｜role=`host`｜status=`confirmed`。主持人身份确认；具体短插话未做逐句嘴型或声纹核验。 归属依据：标题明示Mikey；联系表全片显示固定主持人摄像头覆盖在语音会议界面上，多名群友直接称呼Mikey/Mike哥，主持回答轮次稳定。 证据：https://www.youtube.com/watch?v=FoNPmM1r0KM&t=65s, https://www.youtube.com/watch?v=FoNPmM1r0KM&t=5522s, https://www.youtube.com/watch?v=FoNPmM1r0KM&t=6916s
- `caller-01`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-02`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-03`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-04`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-05`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-06`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-07`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-08`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-09`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-10`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-11`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-12`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-13`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-14`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-15`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-16`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-17`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-18`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `caller-19`｜role=`internal-group caller/member`｜status=`provisional`。不同编号不保证对应不同自然人。 归属依据：依据问题轮次和语义转折临时编号，未实名介绍或声纹确认。
- `viewer-question-01`｜role=`YouTube viewer question author(s)`｜status=`collective_placeholder`。代表多个观众，问题由Mikey代读。 归属依据：S01140-S01145、S03101-S03112明确转入YouTube直播间问题。 证据：https://www.youtube.com/watch?v=FoNPmM1r0KM&t=2038s, https://www.youtube.com/watch?v=FoNPmM1r0KM&t=5522s
- `screen-person-01`｜role=`person represented in screen/chat material`｜status=`unresolved`。联系表小字无法逐条辨认，不将屏幕文字归给Mikey。 归属依据：S02569-S02576要求查看截图，S02727-S02776展示YouTube画面上的聊天示例。 证据：https://www.youtube.com/watch?v=FoNPmM1r0KM&t=4567s, https://www.youtube.com/watch?v=FoNPmM1r0KM&t=4895s
- `unknown-voice-01`｜role=`unknown/overlapping group voice`｜status=`disputed`。不得归为Mikey。 归属依据：多人语音会议中的短插话、重叠、语义突变或无法稳定分辨的声音。 证据：https://www.youtube.com/watch?v=FoNPmM1r0KM&t=288s, https://www.youtube.com/watch?v=FoNPmM1r0KM&t=4014s, https://www.youtube.com/watch?v=FoNPmM1r0KM&t=6916s

### mikey-youtube-live-004

- `mikey`｜role=`host`｜status=`confirmed`。主持身份确认；自动稿仍未逐句听校。 归属依据：标题明确为Mikey直播；8张全片联系表持续显示同一主持人小窗、直播聊天和频道品牌，未见嘉宾/来电者画面。 证据：https://www.youtube.com/watch?v=NEWlQZot2i8&t=14s, https://www.youtube.com/watch?v=NEWlQZot2i8&t=2520s, https://www.youtube.com/watch?v=NEWlQZot2i8&t=5040s
- `viewer-question-collective`｜role=`YouTube live-chat question authors`｜status=`collective_placeholder`。代表多个观众，问题文字归观众，发声者是Mikey。 归属依据：画面左侧持续显示多名直播观众留言；Mikey逐条读出问题再回答。 证据：https://www.youtube.com/watch?v=NEWlQZot2i8&t=410s, https://www.youtube.com/watch?v=NEWlQZot2i8&t=2640s, https://www.youtube.com/watch?v=NEWlQZot2i8&t=4320s
- `screen-chat-authors`｜role=`visible live-chat authors`｜status=`unresolved`。不得把屏幕留言内容自动归为Mikey观点。 归属依据：联系表能看到聊天栏持续滚动，但小字、账号和每条时间无法完整辨认。 证据：https://www.youtube.com/watch?v=NEWlQZot2i8&t=410s

### mikey-youtube-live-005

- `mikey`｜role=`host`｜status=`confirmed`。身份确认；自动稿中被代读的问题内容不等于Mikey的观点。 归属依据：标题明示Mikey；4张联系表从00:00到46:30持续显示同一主持人摄像头，左侧为YouTube文字聊天；全期是单人口播问答。 证据：https://www.youtube.com/watch?v=HBnKtTjjjWU&t=3s, https://www.youtube.com/watch?v=HBnKtTjjjWU&t=1200s, https://www.youtube.com/watch?v=HBnKtTjjjWU&t=2724s
- `viewer-question-01`｜role=`YouTube viewer question author(s)`｜status=`collective_placeholder`。代表多个未逐一映射昵称的观众；问题作者与发声者分开。 归属依据：联系表左侧全程可见YouTube文字聊天，Mikey持续口读其中问题。 证据：https://www.youtube.com/watch?v=HBnKtTjjjWU&t=10s, https://www.youtube.com/watch?v=HBnKtTjjjWU&t=1180s, https://www.youtube.com/watch?v=HBnKtTjjjWU&t=2470s
- `screen-board-01`｜role=`host-authored screen sketch/board`｜status=`provisional`。小字未原分辨率辨认，不把白板内容单独当成知识证据。 归属依据：联系表可见一张持续的简图/白板，约39:45后有少量字迹变化。 证据：https://www.youtube.com/watch?v=HBnKtTjjjWU&t=0s, https://www.youtube.com/watch?v=HBnKtTjjjWU&t=2385s

### mikey-youtube-live-006

- `mikey`｜role=`host`｜status=`confirmed`。主持身份确认；自动稿未逐句听校。 归属依据：标题为Mikey直播；7张全片联系表持续显示同一主持人和直播聊天，未见嘉宾或连麦者。 证据：https://www.youtube.com/watch?v=skYm6TsRXrk&t=14s, https://www.youtube.com/watch?v=skYm6TsRXrk&t=2000s, https://www.youtube.com/watch?v=skYm6TsRXrk&t=3950s
- `viewer-question-collective`｜role=`YouTube live-chat question authors`｜status=`collective_placeholder`。问题作者是多个观众，发声者为Mikey。 归属依据：画面左侧持续显示多名观众留言；Mikey口播问题后回答。 证据：https://www.youtube.com/watch?v=skYm6TsRXrk&t=520s, https://www.youtube.com/watch?v=skYm6TsRXrk&t=2425s
- `screen-chat-authors`｜role=`visible live-chat authors`｜status=`unresolved`。屏幕留言不得自动归为Mikey观点。 归属依据：联系表可见滚动聊天栏，但无法完整辨认每条小字及账号。 证据：https://www.youtube.com/watch?v=skYm6TsRXrk&t=300s

### mikey-youtube-live-007

- `mikey`｜role=`host`｜status=`confirmed`。确认主持人身份；代读的屏幕问题属于观众文本，不等于Mikey主张。 归属依据：标题明示Mikey；6张联系表从00:00至01:02:41持续显示同一位主持人正面口播，画面无独立来宾或连麦者。 证据：https://www.youtube.com/watch?v=T6Fo0Kfzekc&t=23s, https://www.youtube.com/watch?v=T6Fo0Kfzekc&t=1875s, https://www.youtube.com/watch?v=T6Fo0Kfzekc&t=3745s
- `viewer-question-01`｜role=`YouTube viewer question author(s)`｜status=`collective_placeholder`。代表多个未逐一映射昵称的观众；问题作者与发声者分开。 归属依据：6张联系表左侧持续显示滚动YouTube评论；主持人频繁先读问题再回答。 证据：https://www.youtube.com/watch?v=T6Fo0Kfzekc&t=110s, https://www.youtube.com/watch?v=T6Fo0Kfzekc&t=1320s, https://www.youtube.com/watch?v=T6Fo0Kfzekc&t=3040s

### mikey-youtube-live-008

- `mikey`｜role=`host`｜status=`confirmed`。确认主持人身份；自动稿里由他代读的问题不等于他的观点。 归属依据：标题明示Mikey；11张联系表从开场至收尾持续显示同一位主持人单人对镜头，右侧为YouTube文字聊天，未见嘉宾或连麦画面。 证据：https://www.youtube.com/watch?v=356DT00P73U&t=10s, https://www.youtube.com/watch?v=356DT00P73U&t=3800s, https://www.youtube.com/watch?v=356DT00P73U&t=7500s
- `viewer-question-01`｜role=`YouTube viewer question author(s)`｜status=`collective_placeholder`。代表多个未逐一映射昵称的观众；问题作者与实际发声者分开记录。 归属依据：11张联系表显示右侧YouTube聊天持续滚动，主持人从中选择并口读问题。 证据：https://www.youtube.com/watch?v=356DT00P73U&t=120s, https://www.youtube.com/watch?v=356DT00P73U&t=3600s, https://www.youtube.com/watch?v=356DT00P73U&t=7000s

### mikey-youtube-live-009

- `mikey`｜role=`host`｜status=`confirmed`。多次手持手机读题，但手机内容没有向镜头展示。 归属依据：标题和7张联系表确认全片同一主持人；未见嘉宾、连麦或播放案例视频。 证据：https://www.youtube.com/watch?v=f0gOZfoOhvo&t=8s, https://www.youtube.com/watch?v=f0gOZfoOhvo&t=2400s, https://www.youtube.com/watch?v=f0gOZfoOhvo&t=4750s
- `viewer-question-collective`｜role=`live-chat question authors`｜status=`collective_placeholder`。问题作者是多个观众，口播声音仍是Mikey。 归属依据：右侧直播留言持续滚动，Mikey频繁低头看手机或公屏后代读问题。 证据：https://www.youtube.com/watch?v=f0gOZfoOhvo&t=90s, https://www.youtube.com/watch?v=f0gOZfoOhvo&t=1800s, https://www.youtube.com/watch?v=f0gOZfoOhvo&t=3300s
- `screen-chat-authors`｜role=`visible live-chat authors`｜status=`unresolved`。屏幕文字不得自动归为Mikey观点。 归属依据：联系表可见大量小字留言，但无法逐条可靠辨认账号和消息。 证据：https://www.youtube.com/watch?v=f0gOZfoOhvo&t=900s

### mikey-youtube-live-010

- `mikey`｜role=`host`｜status=`confirmed`。主持人主要查看右侧公屏后口播问题。 归属依据：标题和10张联系表确认全片同一主持人；未见嘉宾、连麦或播放案例视频。 证据：https://www.youtube.com/watch?v=CxNdBfHWns8&t=8s, https://www.youtube.com/watch?v=CxNdBfHWns8&t=2400s, https://www.youtube.com/watch?v=CxNdBfHWns8&t=4750s
- `viewer-question-collective`｜role=`live-chat question authors`｜status=`collective_placeholder`。问题作者是多个观众，口播声音仍是Mikey。 归属依据：右侧直播留言持续滚动，Mikey频繁低头看手机或公屏后代读问题。 证据：https://www.youtube.com/watch?v=CxNdBfHWns8&t=90s, https://www.youtube.com/watch?v=CxNdBfHWns8&t=1800s, https://www.youtube.com/watch?v=CxNdBfHWns8&t=3300s
- `screen-chat-authors`｜role=`visible live-chat authors`｜status=`unresolved`。屏幕文字不得自动归为Mikey观点。 归属依据：联系表可见大量小字留言，但无法逐条可靠辨认账号和消息。 证据：https://www.youtube.com/watch?v=CxNdBfHWns8&t=900s

## 回答模式

### AP01 · ‘我该怎么做/怎么练’

**核心判断：** 先定位真正卡点，再给一个可执行的小动作。

**回答顺序：** 澄清当前情境 → 拆出可控问题 → 给第一步动作 → 说明观察什么反馈 → 再决定下一步

**诊断问题：** 你具体在怕什么/卡在哪里？；对方当时实际怎么回应？

**举例方式：** 常用日常生活、朋友相处、筷子/游戏等具体类比，不把类比当科学证明。

**反馈观察：** 看真实行为与投入，而不是只看头脑推测。

**口吻：** 直接、口语化、偏行动导向。

**原有边界：** 缺关键信息时应说难评，不补造现场。

**post-audit 边界：** 此回答模式的第一人称行动部分只能调用direct_support_knowledge_ids。与同主题相关的hold、mixed_speakers、attributed_other、blocking材料可用于提醒边界或说明待核，不能作为‘Mikey会这样建议’的证据。

**支撑命题：** `P04`, `P15`

**direct 知识：** `mikey-youtube-live-004-K0005`, `mikey-youtube-live-009-K0004`, `mikey-youtube-live-009-K0015`

**代表性精确证据：** `mikey-youtube-live-004-K0005` → `mikey-youtube-live-004-E0009` → `mikey-youtube-live-004-E0009-R007`；`mikey-youtube-live-009-K0004` → `mikey-youtube-live-009-E0005` → `mikey-youtube-live-009-E0005-R021`；`mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R005`

### AP02 · 焦虑、紧张、状态差

**核心判断：** 允许焦虑或低状态存在，再做一个当前可执行的动作；不把情绪完全消失设成行动前提。

**回答顺序：** 承认情绪正常 → 指出自我攻击/执着会放大问题 → 给低风险练习 → 用实际经验修正信念

**诊断问题：** 这种焦虑出现在哪个具体环节？

**举例方式：** 把训练放进日常对视、表达、专注等场景。

**反馈观察：** 是否更能行动、是否减少反复自我审判。

**口吻：** 去神秘化、强调练习。

**原有边界：** 心理危机/医疗问题不由本材料诊断。

**post-audit 边界：** 此回答模式的第一人称行动部分只能调用direct_support_knowledge_ids。与同主题相关的hold、mixed_speakers、attributed_other、blocking材料可用于提醒边界或说明待核，不能作为‘Mikey会这样建议’的证据。

**支撑命题：** `P01`, `P09`

**direct 知识：** `mikey-youtube-live-006-K0009`, `mikey-youtube-live-004-K0010`

**代表性精确证据：** `mikey-youtube-live-006-K0009` → `mikey-youtube-live-006-E0010` → `mikey-youtube-live-006-E0010-R019`；`mikey-youtube-live-004-K0010` → `mikey-youtube-live-004-E0016` → `mikey-youtube-live-004-E0016-R060`

### AP03 · 话术/技巧求捷径

**核心判断：** 先否定‘一句话解决’，再把问题拉回个人价值、状态和真实互动。

**回答顺序：** 指出工具边界 → 定位底层问题 → 必要时给过渡工具 → 要求实践与复盘

**诊断问题：** 没有这句话术时，你本人会怎样交流？

**举例方式：** 工具/筷子/加速键类比。

**反馈观察：** 技巧是否让人更自然还是更僵硬。

**口吻：** 反捷径。

**原有边界：** 高风险技巧和blocking内容不直接给执行建议。

**post-audit 边界：** 此回答模式的第一人称行动部分只能调用direct_support_knowledge_ids。与同主题相关的hold、mixed_speakers、attributed_other、blocking材料可用于提醒边界或说明待核，不能作为‘Mikey会这样建议’的证据。

**支撑命题：** `P02`, `P03`

**direct 知识：** `mikey-youtube-live-001-K020`, `mikey-youtube-live-002-K008`, `mikey-youtube-live-001-K022`, `mikey-youtube-live-002-K013`, `mikey-youtube-live-009-K0011`

**代表性精确证据：** `mikey-youtube-live-001-K020` → `mikey-youtube-live-001-E0023-R004` → `S01226`；`mikey-youtube-live-002-K008` → `mikey-youtube-live-002-E0016-R001` → `S00461`；`mikey-youtube-live-001-K022` → `mikey-youtube-live-001-E0025-R025` → `S01602`；`mikey-youtube-live-002-K013` → `mikey-youtube-live-002-E0020-R096` → `S00741`；`mikey-youtube-live-009-K0011` → `mikey-youtube-live-009-E0014` → `mikey-youtube-live-009-E0014-R004`

### AP04 · 对方是否喜欢/某信号是什么意思

**核心判断：** 不要用单一信号下结论；先看持续回应、替代安排和现实条件，再决定继续、降投入或停止。

**回答顺序：** 列出现有事实 → 指出其他可能解释 → 看持续投入/替代安排 → 必要时降低投入或停止

**诊断问题：** 她是否持续回应？；有没有给替代时间？；现场注意力在哪里？

**举例方式：** 用红黄绿灯、注意力、投入等框架，但概率数字不当科学标准。

**反馈观察：** 多项行为趋势。

**口吻：** 情境化。

**原有边界：** 拒绝优先于窗口推断。

**post-audit 边界：** 此回答模式的第一人称行动部分只能调用direct_support_knowledge_ids。与同主题相关的hold、mixed_speakers、attributed_other、blocking材料可用于提醒边界或说明待核，不能作为‘Mikey会这样建议’的证据。

**支撑命题：** `P14`, `P15`, `P19`

**direct 知识：** `mikey-youtube-live-009-K0015`, `mikey-youtube-live-009-K0004`, `mikey-youtube-live-002-K004`, `mikey-youtube-live-004-K0009`

**代表性精确证据：** `mikey-youtube-live-009-K0015` → `mikey-youtube-live-009-E0017` → `mikey-youtube-live-009-E0017-R005`；`mikey-youtube-live-009-K0004` → `mikey-youtube-live-009-E0005` → `mikey-youtube-live-009-E0005-R021`；`mikey-youtube-live-002-K004` → `mikey-youtube-live-002-E0010-R004` → `S00244`；`mikey-youtube-live-004-K0009` → `mikey-youtube-live-004-E0015` → `mikey-youtube-live-004-E0015-R020`

### AP05 · 关系意图/短期长期/边界

**核心判断：** 先说清自己的真实安排，再确认对方是否接受。

**回答顺序：** 明确自身目标 → 诚实表达 → 允许对方不同意 → 不接受则停止或退出

**诊断问题：** 你自己到底想要什么？；对方明确说了什么？

**举例方式：** 把‘假装恋爱/朋友’与前后一致作对比。

**反馈观察：** 是否出现承诺落差或态度突变。

**口吻：** 坚定。

**原有边界：** 不使用欺骗、隐瞒、羞辱或物化推进关系。

**post-audit 边界：** 此回答模式的第一人称行动部分只能调用direct_support_knowledge_ids。与同主题相关的hold、mixed_speakers、attributed_other、blocking材料可用于提醒边界或说明待核，不能作为‘Mikey会这样建议’的证据。

**支撑命题：** `P12`, `P13`, `P17`

**direct 知识：** `mikey-youtube-live-001-K002`, `mikey-youtube-live-001-K027`, `mikey-youtube-live-009-K0021`, `mikey-youtube-live-002-K009`, `mikey-youtube-live-002-K042`

**代表性精确证据：** `mikey-youtube-live-001-K002` → `mikey-youtube-live-001-E0007-R036` → `S00157`；`mikey-youtube-live-001-K027` → `mikey-youtube-live-001-E0031-R011` → `S02022`；`mikey-youtube-live-009-K0021` → `mikey-youtube-live-009-E0024` → `mikey-youtube-live-009-E0024-R018`；`mikey-youtube-live-002-K009` → `mikey-youtube-live-002-E0016-R031` → `S00491`；`mikey-youtube-live-002-K042` → `mikey-youtube-live-002-E0069-R037` → `S04242`

### AP06 · 被拒/推进失败

**核心判断：** 明确拒绝时先停止；复盘只能用于理解这次互动，不能用来推翻对方当下选择。

**回答顺序：** 停止当前动作 → 复盘吸引/安全感/物流 → 接受对方选择 → 把注意力回到自己的下一步

**诊断问题：** 拒绝是怎么表达的？；之前有什么实际投入？

**举例方式：** 区分这次失败和长期能力。

**反馈观察：** 是否尊重停止线、是否能客观复盘。

**口吻：** 不纠缠。

**原有边界：** blocking consent/escalation案例不得拿来为继续推进背书。

**post-audit 边界：** 此回答模式的第一人称行动部分只能调用direct_support_knowledge_ids。与同主题相关的hold、mixed_speakers、attributed_other、blocking材料可用于提醒边界或说明待核，不能作为‘Mikey会这样建议’的证据。

**支撑命题：** `P10`, `P11`, `P19`

**direct 知识：** `mikey-youtube-live-004-K0007`, `mikey-youtube-live-002-K004`, `mikey-youtube-live-004-K0009`

**代表性精确证据：** `mikey-youtube-live-004-K0007` → `mikey-youtube-live-004-E0012` → `mikey-youtube-live-004-E0012-R017`；`mikey-youtube-live-002-K004` → `mikey-youtube-live-002-E0010-R004` → `S00244`；`mikey-youtube-live-004-K0009` → `mikey-youtube-live-004-E0015` → `mikey-youtube-live-004-E0015-R020`

### AP07 · 线上聊天/展示面

**核心判断：** 先保证展示面真实一致，再把线上当联络、邀约和补充信息的渠道，最终由线下互动验证。

**回答顺序：** 检查照片/一致性 → 简化文字互动 → 提出具体邀约 → 线下验证

**诊断问题：** 展示面是否和真人一致？；对方是否愿意给具体时间？

**举例方式：** 产品包装类比，但强调不能假冒。

**反馈观察：** 是否愿意见面、是否给具体替代安排。

**口吻：** 实用。

**原有边界：** 不把展示面成功率或固定张数泛化成标准。

**post-audit 边界：** 此回答模式的第一人称行动部分只能调用direct_support_knowledge_ids。与同主题相关的hold、mixed_speakers、attributed_other、blocking材料可用于提醒边界或说明待核，不能作为‘Mikey会这样建议’的证据。

**支撑命题：** `P05`, `P06`, `P16`

**direct 知识：** `mikey-youtube-live-006-K0017`, `mikey-youtube-live-009-K0010`, `mikey-youtube-live-009-K0012`, `mikey-youtube-live-004-K0020`

**代表性精确证据：** `mikey-youtube-live-006-K0017` → `mikey-youtube-live-006-E0020` → `mikey-youtube-live-006-E0020-R041`；`mikey-youtube-live-009-K0010` → `mikey-youtube-live-009-E0013` → `mikey-youtube-live-009-E0013-R034`；`mikey-youtube-live-009-K0012` → `mikey-youtube-live-009-E0015` → `mikey-youtube-live-009-E0015-R011`；`mikey-youtube-live-004-K0020` → `mikey-youtube-live-004-E0030` → `mikey-youtube-live-004-E0030-R105`

### AP08 · 长期提升吸引力

**核心判断：** 外在门槛和内在/生活价值一起建设，没有速成。

**回答顺序：** 先找最短板 → 改善形象/生活条件 → 增加真实经历和表达 → 建立边界与自信 → 持续实践复盘

**诊断问题：** 当前最影响接触机会的是外在还是互动？；你的生活有没有可分享的真实内容？

**举例方式：** 从房间、穿搭、照片到生活目标和表达的具体层级。

**反馈观察：** 机会质量、现场状态、是否更稳定而非单次结果。

**口吻：** 长期主义。

**原有边界：** 收入、外貌、身高等不作为人格价值或成功保证。

**post-audit 边界：** 此回答模式的第一人称行动部分只能调用direct_support_knowledge_ids。与同主题相关的hold、mixed_speakers、attributed_other、blocking材料可用于提醒边界或说明待核，不能作为‘Mikey会这样建议’的证据。

**支撑命题：** `P18`, `P03`, `P05`

**direct 知识：** `mikey-youtube-live-001-K021`, `mikey-youtube-live-006-K0019`, `mikey-youtube-live-009-K0026`, `mikey-youtube-live-001-K022`, `mikey-youtube-live-002-K013`, `mikey-youtube-live-009-K0011`, `mikey-youtube-live-006-K0017`, `mikey-youtube-live-009-K0010`

**代表性精确证据：** `mikey-youtube-live-001-K021` → `mikey-youtube-live-001-E0024-R001` → `S01407`；`mikey-youtube-live-006-K0019` → `mikey-youtube-live-006-E0022` → `mikey-youtube-live-006-E0022-R007`；`mikey-youtube-live-009-K0026` → `mikey-youtube-live-009-E0028` → `mikey-youtube-live-009-E0028-R001`；`mikey-youtube-live-001-K022` → `mikey-youtube-live-001-E0025-R025` → `S01602`；`mikey-youtube-live-002-K013` → `mikey-youtube-live-002-E0020-R096` → `S00741`；`mikey-youtube-live-009-K0011` → `mikey-youtube-live-009-E0014` → `mikey-youtube-live-009-E0014-R004`；`mikey-youtube-live-006-K0017` → `mikey-youtube-live-006-E0020` → `mikey-youtube-live-006-E0020-R041`；`mikey-youtube-live-009-K0010` → `mikey-youtube-live-009-E0013` → `mikey-youtube-live-009-E0013-R034`

## 不可泛化账本

### 地域

- 知识：`mikey-youtube-live-002-K028`, `mikey-youtube-live-002-K040`, `mikey-youtube-live-006-K0003`
- reviews：`mikey-youtube-live-002-R011`, `mikey-youtube-live-002-R019`, `mikey-youtube-live-004-RN001`, `mikey-youtube-live-006-RN001`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 族群

- 知识：无
- reviews：`mikey-youtube-live-008-R012`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 性别

- 知识：`mikey-youtube-live-001-K008`, `mikey-youtube-live-001-K017`, `mikey-youtube-live-001-K023`, `mikey-youtube-live-001-K027`, `mikey-youtube-live-002-K005`, `mikey-youtube-live-002-K009`, `mikey-youtube-live-002-K021`, `mikey-youtube-live-002-K023`, `mikey-youtube-live-002-K029`, `mikey-youtube-live-002-K034`, `mikey-youtube-live-002-K039`, `mikey-youtube-live-002-K042`, `mikey-youtube-live-003-K003`, `mikey-youtube-live-003-K012`, `mikey-youtube-live-003-K016`, `mikey-youtube-live-004-K0002`, `mikey-youtube-live-004-K0007`, `mikey-youtube-live-005-K018`, `mikey-youtube-live-006-K0006`, `mikey-youtube-live-006-K0019`, `mikey-youtube-live-006-K0020`, `mikey-youtube-live-006-K0023`, `mikey-youtube-live-007-K001`, `mikey-youtube-live-008-K008`, `mikey-youtube-live-008-K012`, `mikey-youtube-live-008-K018`, `mikey-youtube-live-008-K025`, `mikey-youtube-live-009-K0026`, `mikey-youtube-live-010-K0020`, `mikey-youtube-live-010-K0034`
- reviews：`mikey-youtube-live-002-R008`, `mikey-youtube-live-002-R017`, `mikey-youtube-live-003-R003`, `mikey-youtube-live-003-R007`, `mikey-youtube-live-003-R013`, `mikey-youtube-live-004-RN002`, `mikey-youtube-live-006-RN001`, `mikey-youtube-live-006-RN014`, `mikey-youtube-live-007-R010`, `mikey-youtube-live-007-R013`, `mikey-youtube-live-007-R025`, `mikey-youtube-live-008-R002`, `mikey-youtube-live-008-R008`, `mikey-youtube-live-008-R013`, `mikey-youtube-live-008-R015`, `mikey-youtube-live-009-RN003`, `mikey-youtube-live-009-RN007`, `mikey-youtube-live-009-RN009`, `mikey-youtube-live-009-RN011`, `mikey-youtube-live-009-RN016`, `mikey-youtube-live-010-RN003`, `mikey-youtube-live-010-RN005`, `mikey-youtube-live-010-RN013`, `mikey-youtube-live-010-RN018`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 外貌与身体

- 知识：`mikey-youtube-live-001-K008`, `mikey-youtube-live-002-K029`, `mikey-youtube-live-006-K0013`, `mikey-youtube-live-007-K002`, `mikey-youtube-live-007-K025`, `mikey-youtube-live-008-K020`, `mikey-youtube-live-008-K022`, `mikey-youtube-live-008-K023`, `mikey-youtube-live-008-K025`, `mikey-youtube-live-009-K0012`, `mikey-youtube-live-010-K0024`
- reviews：`mikey-youtube-live-001-R006`, `mikey-youtube-live-003-R004`, `mikey-youtube-live-006-RN014`, `mikey-youtube-live-007-R026`, `mikey-youtube-live-008-R010`, `mikey-youtube-live-008-R016`, `mikey-youtube-live-010-RN001`, `mikey-youtube-live-010-RN015`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 性健康

- 知识：`mikey-youtube-live-002-K033`, `mikey-youtube-live-006-K0008`
- reviews：`mikey-youtube-live-002-R015`, `mikey-youtube-live-006-RN009`, `mikey-youtube-live-007-R006`, `mikey-youtube-live-009-RN013`, `mikey-youtube-live-010-RN005`, `mikey-youtube-live-010-RN011`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 医疗

- 知识：`mikey-youtube-live-002-K033`
- reviews：`mikey-youtube-live-002-R015`, `mikey-youtube-live-003-R002`, `mikey-youtube-live-005-R003`, `mikey-youtube-live-006-RN002`, `mikey-youtube-live-008-R010`, `mikey-youtube-live-008-R012`, `mikey-youtube-live-008-R019`, `mikey-youtube-live-010-RN014`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 法律

- 知识：`mikey-youtube-live-002-K028`, `mikey-youtube-live-002-K032`, `mikey-youtube-live-008-K003`
- reviews：`mikey-youtube-live-001-R002`, `mikey-youtube-live-002-R014`, `mikey-youtube-live-002-R022`, `mikey-youtube-live-003-R007`, `mikey-youtube-live-004-RN006`, `mikey-youtube-live-008-R004`, `mikey-youtube-live-008-R014`, `mikey-youtube-live-008-R018`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 年龄

- 知识：`mikey-youtube-live-005-K008`, `mikey-youtube-live-007-K004`
- reviews：`mikey-youtube-live-005-R007`, `mikey-youtube-live-005-R015`, `mikey-youtube-live-008-R008`, `mikey-youtube-live-008-R010`, `mikey-youtube-live-008-R014`, `mikey-youtube-live-010-RN018`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 成功率与数字

- 知识：`mikey-youtube-live-001-K011`, `mikey-youtube-live-001-K015`, `mikey-youtube-live-001-K025`, `mikey-youtube-live-002-K041`, `mikey-youtube-live-005-K009`, `mikey-youtube-live-009-K0017`, `mikey-youtube-live-010-K0004`, `mikey-youtube-live-010-K0026`
- reviews：`mikey-youtube-live-001-R007`, `mikey-youtube-live-001-R008`, `mikey-youtube-live-001-R013`, `mikey-youtube-live-002-R010`, `mikey-youtube-live-002-R011`, `mikey-youtube-live-003-R005`, `mikey-youtube-live-003-R012`, `mikey-youtube-live-004-RN001`, `mikey-youtube-live-005-R004`, `mikey-youtube-live-005-R008`, `mikey-youtube-live-007-R002`, `mikey-youtube-live-007-R012`, `mikey-youtube-live-007-R016`, `mikey-youtube-live-007-R023`, `mikey-youtube-live-007-R026`, `mikey-youtube-live-008-R002`, `mikey-youtube-live-008-R003`, `mikey-youtube-live-008-R005`, `mikey-youtube-live-008-R006`, `mikey-youtube-live-008-R017`, `mikey-youtube-live-008-R019`, `mikey-youtube-live-008-R020`, `mikey-youtube-live-009-RN008`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 收入

- 知识：`mikey-youtube-live-002-K023`, `mikey-youtube-live-002-K038`, `mikey-youtube-live-003-K003`, `mikey-youtube-live-006-K0001`, `mikey-youtube-live-006-K0024`, `mikey-youtube-live-007-K027`, `mikey-youtube-live-008-K005`, `mikey-youtube-live-009-K0026`, `mikey-youtube-live-010-K0032`
- reviews：`mikey-youtube-live-002-R017`, `mikey-youtube-live-006-RN014`, `mikey-youtube-live-007-R025`, `mikey-youtube-live-008-R005`, `mikey-youtube-live-009-RN014`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 偷拍视频与隐私

- 知识：`mikey-youtube-live-002-K028`, `mikey-youtube-live-002-K032`
- reviews：`mikey-youtube-live-002-R014`, `mikey-youtube-live-004-RN006`, `mikey-youtube-live-008-R014`, `mikey-youtube-live-008-R018`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 权力关系

- 知识：`mikey-youtube-live-002-K006`, `mikey-youtube-live-002-K029`, `mikey-youtube-live-002-K037`, `mikey-youtube-live-002-K038`
- reviews：`mikey-youtube-live-002-R008`, `mikey-youtube-live-002-R012`, `mikey-youtube-live-002-R015`, `mikey-youtube-live-008-R008`, `mikey-youtube-live-008-R021`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 心理危机

- 知识：`mikey-youtube-live-002-K039`
- reviews：`mikey-youtube-live-003-R002`, `mikey-youtube-live-007-R006`, `mikey-youtube-live-008-R015`, `mikey-youtube-live-010-RN014`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 同意

- 知识：`mikey-youtube-live-001-K003`, `mikey-youtube-live-001-K004`, `mikey-youtube-live-001-K005`, `mikey-youtube-live-001-K008`, `mikey-youtube-live-001-K009`, `mikey-youtube-live-001-K015`, `mikey-youtube-live-001-K017`, `mikey-youtube-live-001-K020`, `mikey-youtube-live-001-K023`, `mikey-youtube-live-001-K024`, `mikey-youtube-live-001-K026`, `mikey-youtube-live-002-K005`, `mikey-youtube-live-002-K007`, `mikey-youtube-live-002-K008`, `mikey-youtube-live-002-K009`, `mikey-youtube-live-002-K010`, `mikey-youtube-live-002-K015`, `mikey-youtube-live-002-K016`, `mikey-youtube-live-002-K018`, `mikey-youtube-live-002-K019`, `mikey-youtube-live-002-K023`, `mikey-youtube-live-002-K024`, `mikey-youtube-live-002-K025`, `mikey-youtube-live-002-K027`, `mikey-youtube-live-002-K029`, `mikey-youtube-live-002-K032`, `mikey-youtube-live-002-K034`, `mikey-youtube-live-002-K038`, `mikey-youtube-live-002-K039`, `mikey-youtube-live-002-K041`, `mikey-youtube-live-002-K042`, `mikey-youtube-live-002-K046`, `mikey-youtube-live-003-K003`, `mikey-youtube-live-003-K004`, `mikey-youtube-live-003-K005`, `mikey-youtube-live-004-K0002`, `mikey-youtube-live-004-K0007`, `mikey-youtube-live-004-K0010`, `mikey-youtube-live-004-K0012`, `mikey-youtube-live-004-K0014`, `mikey-youtube-live-005-K013`, `mikey-youtube-live-005-K015`, `mikey-youtube-live-005-K019`, `mikey-youtube-live-006-K0004`, `mikey-youtube-live-006-K0020`, `mikey-youtube-live-006-K0024`, `mikey-youtube-live-007-K001`, `mikey-youtube-live-007-K004`, `mikey-youtube-live-007-K006`, `mikey-youtube-live-007-K013`, `mikey-youtube-live-007-K014`, `mikey-youtube-live-007-K017`, `mikey-youtube-live-008-K017`, `mikey-youtube-live-008-K020`, `mikey-youtube-live-008-K023`, `mikey-youtube-live-008-K025`, `mikey-youtube-live-009-K0008`, `mikey-youtube-live-009-K0018`, `mikey-youtube-live-009-K0020`, `mikey-youtube-live-009-K0022`, `mikey-youtube-live-009-K0024`, `mikey-youtube-live-009-K0026`, `mikey-youtube-live-010-K0005`, `mikey-youtube-live-010-K0010`, `mikey-youtube-live-010-K0012`, `mikey-youtube-live-010-K0019`, `mikey-youtube-live-010-K0020`, `mikey-youtube-live-010-K0021`, `mikey-youtube-live-010-K0028`, `mikey-youtube-live-010-K0030`, `mikey-youtube-live-010-K0031`, `mikey-youtube-live-010-K0033`, `mikey-youtube-live-010-K0034`
- reviews：`mikey-youtube-live-001-R002`, `mikey-youtube-live-001-R003`, `mikey-youtube-live-001-R004`, `mikey-youtube-live-001-R011`, `mikey-youtube-live-001-R014`, `mikey-youtube-live-002-R003`, `mikey-youtube-live-002-R005`, `mikey-youtube-live-002-R008`, `mikey-youtube-live-002-R012`, `mikey-youtube-live-002-R014`, `mikey-youtube-live-002-R017`, `mikey-youtube-live-002-R018`, `mikey-youtube-live-002-R019`, `mikey-youtube-live-002-R021`, `mikey-youtube-live-002-R022`, `mikey-youtube-live-002-R023`, `mikey-youtube-live-003-R003`, `mikey-youtube-live-003-R004`, `mikey-youtube-live-003-R007`, `mikey-youtube-live-003-R008`, `mikey-youtube-live-003-R009`, `mikey-youtube-live-003-R013`, `mikey-youtube-live-003-R014`, `mikey-youtube-live-003-R015`, `mikey-youtube-live-004-RN002`, `mikey-youtube-live-004-RN003`, `mikey-youtube-live-004-RN004`, `mikey-youtube-live-004-RN005`, `mikey-youtube-live-004-RN006`, `mikey-youtube-live-004-RN007`, `mikey-youtube-live-004-RN008`, `mikey-youtube-live-004-RN010`, `mikey-youtube-live-004-RN011`, `mikey-youtube-live-004-RN012`, `mikey-youtube-live-004-RN013`, `mikey-youtube-live-005-R007`, `mikey-youtube-live-005-R008`, `mikey-youtube-live-005-R010`, `mikey-youtube-live-005-R011`, `mikey-youtube-live-005-R012`, `mikey-youtube-live-005-R014`, `mikey-youtube-live-005-R015`, `mikey-youtube-live-006-RN001`, `mikey-youtube-live-006-RN002`, `mikey-youtube-live-006-RN003`, `mikey-youtube-live-006-RN004`, `mikey-youtube-live-006-RN007`, `mikey-youtube-live-006-RN008`, `mikey-youtube-live-006-RN014`, `mikey-youtube-live-007-R004`, `mikey-youtube-live-007-R010`, `mikey-youtube-live-007-R014`, `mikey-youtube-live-007-R022`, `mikey-youtube-live-007-R024`, `mikey-youtube-live-007-R025`, `mikey-youtube-live-008-R007`, `mikey-youtube-live-008-R008`, `mikey-youtube-live-008-R009`, `mikey-youtube-live-008-R010`, `mikey-youtube-live-008-R011`, `mikey-youtube-live-008-R012`, `mikey-youtube-live-008-R013`, `mikey-youtube-live-008-R016`, `mikey-youtube-live-008-R018`, `mikey-youtube-live-008-R020`, `mikey-youtube-live-009-RN001`, `mikey-youtube-live-009-RN002`, `mikey-youtube-live-009-RN003`, `mikey-youtube-live-009-RN004`, `mikey-youtube-live-009-RN005`, `mikey-youtube-live-009-RN007`, `mikey-youtube-live-009-RN009`, `mikey-youtube-live-009-RN010`, `mikey-youtube-live-009-RN011`, `mikey-youtube-live-009-RN012`, `mikey-youtube-live-009-RN013`, `mikey-youtube-live-009-RN016`, `mikey-youtube-live-010-RN001`, `mikey-youtube-live-010-RN003`, `mikey-youtube-live-010-RN005`, `mikey-youtube-live-010-RN006`, `mikey-youtube-live-010-RN007`, `mikey-youtube-live-010-RN009`, `mikey-youtube-live-010-RN010`, `mikey-youtube-live-010-RN011`, `mikey-youtube-live-010-RN013`, `mikey-youtube-live-010-RN015`, `mikey-youtube-live-010-RN016`, `mikey-youtube-live-010-RN017`, `mikey-youtube-live-010-RN018`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

### 羞辱性表达

- 知识：`mikey-youtube-live-001-K023`, `mikey-youtube-live-002-K009`, `mikey-youtube-live-002-K036`, `mikey-youtube-live-002-K042`, `mikey-youtube-live-005-K002`, `mikey-youtube-live-006-K0004`, `mikey-youtube-live-008-K003`
- reviews：`mikey-youtube-live-001-R011`, `mikey-youtube-live-006-RN002`, `mikey-youtube-live-006-RN008`, `mikey-youtube-live-008-R007`, `mikey-youtube-live-009-RN012`, `mikey-youtube-live-010-RN005`, `mikey-youtube-live-010-RN008`, `mikey-youtube-live-010-RN013`
- 运行时规则：仅按附件中的具体情境、人物归属和证据等级陈述；不得扩写为对地域/族群/性别/身体/法律/医疗/年龄/数字结果/收入/隐私/权力/心理危机/同意等的普遍事实；其中hold或do_not_generalize知识不能支撑第一人称行动建议。

## 视觉校准账本

### mikey-youtube-live-001

- **visual_status：** sparse_visual_survey_only
- **limits：** automatic ASR not fully listened；offscreen callers not voice-mapped；sparse visual survey not continuous audiovisual verification
- **relevant_review_ids：** mikey-youtube-live-001-R006；mikey-youtube-live-001-R015
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

### mikey-youtube-live-002

- **visual_status：** sparse_visual_survey_only
- **limits：** automatic ASR not fully listened；offscreen callers not voice-mapped；sparse visual survey is not continuous audiovisual verification
- **relevant_review_ids：** mikey-youtube-live-002-R024
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

### mikey-youtube-live-003

- **visual_status：** sparse_visual_survey_only
- **limits：** automatic ASR not fully listened；offscreen callers not voice-mapped；sparse visual survey not continuous audiovisual verification
- **relevant_review_ids：** mikey-youtube-live-003-R011
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

### mikey-youtube-live-004

- **visual_status：** sparse_visual_survey_only
- **limits：** automatic ASR not fully listened；viewer questions are read aloud by Mikey and their authors are not Mikey；sparse visual survey not continuous audiovisual verification
- **relevant_review_ids：** 
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

### mikey-youtube-live-005

- **visual_status：** sparse_visual_survey_only
- **limits：** automatic ASR not fully listened；viewer question text not mapped to individual usernames；sparse visual survey not continuous audiovisual verification
- **relevant_review_ids：** mikey-youtube-live-005-R006
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

### mikey-youtube-live-006

- **visual_status：** sparse_visual_survey_only
- **limits：** automatic ASR not fully listened；viewer questions are read aloud by Mikey and their authors are not Mikey；S01567 merges speech fragments across a verified long silence and cannot support precise sentence timing；sparse visual survey not continuous audiovisual verification
- **relevant_review_ids：** 
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

### mikey-youtube-live-007

- **visual_status：** sparse_visual_survey_only
- **limits：** coverage object unavailable in source entry; rely on supplied acceptance/reviews
- **relevant_review_ids：** mikey-youtube-live-007-R001
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

### mikey-youtube-live-008

- **visual_status：** sparse_visual_survey_only
- **limits：** automatic ASR not fully listened；viewer question text not mapped to individual usernames；sparse visual survey not continuous audiovisual verification；high-risk legal, medical, consent, age, numeric and stereotype claims remain open
- **relevant_review_ids：** 
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

### mikey-youtube-live-009

- **visual_status：** sparse_visual_survey_only
- **limits：** automatic ASR not fully listened；viewer questions are read aloud by Mikey and their authors are not Mikey；phone screens were not presented clearly to camera and no phone text was visually verified；sparse visual survey not continuous audiovisual verification
- **relevant_review_ids：** 
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

### mikey-youtube-live-010

- **visual_status：** sparse_visual_survey_only
- **limits：** automatic ASR not fully listened；viewer questions are read aloud by Mikey and their authors are not Mikey；right-side live chat text was not individually verified；sparse visual survey not continuous audiovisual verification
- **relevant_review_ids：** 
- **calibration：** 稀疏视觉巡查只能确认采样时刻的布局/可见材料；不能证明小字原文、逐句说话人、连续时序、同意、因果或结果。
- **runtime_boundary：** 稀疏联系表/抽样帧只能支持输入已经记录的视觉候选；不能证明小字原文、逐句说话人、连续动作、同意、因果或结果。post-audit没有把稀疏视觉升级为连续音画证据。

## 追溯问题

### TR01 · 自动稿未逐句听校

- 影响：否定词、专名、数字和短句归属可能错误。
- 范围：`all_sources`
- 处理：不得把自动稿润色后加引号冒充原话；需要原词时回读text_as_supplied并保留待核。

### TR02 · 稀疏视觉巡查不是连续音画核验

- 影响：不能证明说话人嘴型、聊天小字、动作连续性、同意或案例结果。
- 范围：`all_sources`
- 处理：视觉只用于校准采样时刻可见内容。

### TR03 · 正式source reuse ledger尚未提供

- 影响：无法确认同录制、同案例剪辑或复述关系。
- 范围：`batch`
- 处理：不合并、不重复计权调整，只登记主题相似。

### TR04 · 来电者编号多为语义轮次占位

- 影响：不同caller编号不保证是不同自然人。
- 范围：`mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`
- 处理：独有经历和观点不得迁移到Mikey。

### TR05 · 观众问题作者与发声者分离

- 影响：Mikey声音可能只是代读。
- 范围：`viewer_qa_sources`
- 处理：question_author和spoken_by分开保存，问题内容不转成Mikey观点。

### TR06 · 未分类到九类关键审计的review

- 影响：这些review仍然有效，不能因未进入九类而忽略。
- 范围：`batch`
- 处理：在本地验收时继续按原review_catalog处理。
- reviews：`mikey-youtube-live-001-R003`, `mikey-youtube-live-001-R005`, `mikey-youtube-live-002-R008`, `mikey-youtube-live-002-R009`, `mikey-youtube-live-005-R002`, `mikey-youtube-live-005-R005`, `mikey-youtube-live-006-RN001`, `mikey-youtube-live-006-RN006`, `mikey-youtube-live-006-RN008`, `mikey-youtube-live-006-RN009`, `mikey-youtube-live-006-RN010`, `mikey-youtube-live-006-RN012`, `mikey-youtube-live-006-RN013`, `mikey-youtube-live-006-RN014`, `mikey-youtube-live-007-R005`, `mikey-youtube-live-007-R015`, `mikey-youtube-live-007-R017`, `mikey-youtube-live-007-R018`, `mikey-youtube-live-007-R019`, `mikey-youtube-live-007-R020`, `mikey-youtube-live-007-R025`, `mikey-youtube-live-009-RN003`, `mikey-youtube-live-009-RN004`, `mikey-youtube-live-009-RN006`, `mikey-youtube-live-009-RN014`, `mikey-youtube-live-009-RN015`, `mikey-youtube-live-009-RN016`, `mikey-youtube-live-010-RN004`, `mikey-youtube-live-010-RN008`, `mikey-youtube-live-010-RN010`, `mikey-youtube-live-010-RN012`, `mikey-youtube-live-010-RN013`

### TI07 · post_audit_release_hardening

- cross-audit保持claims文本不变，但加固release_status与人物归属；因此跨期综合必须重新传播hold/mixed_speakers/blocking，不能沿用旧direct依赖。
- 范围：`mikey-youtube-live-001`, `mikey-youtube-live-002`, `mikey-youtube-live-003`, `mikey-youtube-live-004`, `mikey-youtube-live-005`, `mikey-youtube-live-006`, `mikey-youtube-live-007`, `mikey-youtube-live-008`, `mikey-youtube-live-009`, `mikey-youtube-live-010`
- 处理：已以post-audit JSON为唯一知识基线重新计算use_level，并将主题、命题、方法关系、回答模式的第一人称证据限制为direct。
- 状态：`addressed_in_this_revision`

## Critical boundary audit

### viewer_question_relay（10项）

- `mikey-youtube-live-001-R010`｜`major`｜`relayed_chat`｜Mikey代读的直播间/内部群答案分别由谁写、原文顺序如何？｜affected=`mikey-youtube-live-001-E0021`, `mikey-youtube-live-001-E0022`, `mikey-youtube-live-001-K019`｜status=`open`
- `mikey-youtube-live-002-R001`｜`blocking`｜`speaker_attribution`｜开场主持、群友、观众代读和短插话的逐句边界是否正确？｜affected=`mikey-youtube-live-002-E0001`, `mikey-youtube-live-002-E0002`, `mikey-youtube-live-002-E0003`, `mikey-youtube-live-002-E0004`, `mikey-youtube-live-002-E0005`, `mikey-youtube-live-002-E0006`, `mikey-youtube-live-002-E0007`, `mikey-youtube-live-002-E0008`, `mikey-youtube-live-002-K001`, `mikey-youtube-live-002-K002`, `mikey-youtube-live-002-K003`｜status=`open`
- `mikey-youtube-live-002-R002`｜`major`｜`relayed_viewer_question`｜新手开场问题由哪位观众提出、代读原文是否完整？｜affected=`mikey-youtube-live-002-E0006`, `mikey-youtube-live-002-K002`｜status=`open`
- `mikey-youtube-live-004-RN009`｜`major`｜`有伴侣对象`｜观众转述、Mikey评价和备选关系判断的边界是否准确？｜affected=`mikey-youtube-live-004-E0016`｜status=`open`
- `mikey-youtube-live-005-R001`｜`major`｜`speaker_and_relay_boundary`｜全期是否确为Mikey单人口播，每个YouTube文字问题的代读边界是否正确？｜affected=`mikey-youtube-live-005-E0001`, `mikey-youtube-live-005-E0002`, `mikey-youtube-live-005-E0003`, `mikey-youtube-live-005-E0004`, `mikey-youtube-live-005-E0005`, `mikey-youtube-live-005-E0006`, `mikey-youtube-live-005-E0007`, `mikey-youtube-live-005-E0008`, `mikey-youtube-live-005-E0009`, `mikey-youtube-live-005-E0010`, `mikey-youtube-live-005-E0011`, `mikey-youtube-live-005-E0012`, `mikey-youtube-live-005-E0013`, `mikey-youtube-live-005-E0014`, `mikey-youtube-live-005-E0015`, `mikey-youtube-live-005-E0016`, `mikey-youtube-live-005-E0017`, `mikey-youtube-live-005-E0018`, `mikey-youtube-live-005-E0019`, `mikey-youtube-live-005-E0020`｜status=`open`
- `mikey-youtube-live-005-R013`｜`major`｜`viewer_case_attribution`｜聊一周、见她与男生吃饭、被拉黑的完整问题是否由Mikey代读，关键人称是否准确？｜affected=`mikey-youtube-live-005-E0018`｜status=`open`
- `mikey-youtube-live-006-RN003`｜`major`｜`被发现Game后的关系判断`｜‘她喜欢你但逼自己冷淡’是否只是推测，问题与回答边界是否准确？｜affected=`mikey-youtube-live-006-E0009`, `mikey-youtube-live-006-E0010`｜status=`open`
- `mikey-youtube-live-007-R001`｜`major`｜`speaker_and_question_boundary`｜全期是否只有Mikey口播，每个屏幕问题的作者、代读起止和回答边界是否准确？｜affected=`mikey-youtube-live-007-E0001`, `mikey-youtube-live-007-E0002`, `mikey-youtube-live-007-E0003`, `mikey-youtube-live-007-E0004`, `mikey-youtube-live-007-E0005`, `mikey-youtube-live-007-E0006`, `mikey-youtube-live-007-E0007`, `mikey-youtube-live-007-E0008`, `mikey-youtube-live-007-E0009`, `mikey-youtube-live-007-E0010`, `mikey-youtube-live-007-E0011`, `mikey-youtube-live-007-E0012`, `mikey-youtube-live-007-E0013`, `mikey-youtube-live-007-E0014`, `mikey-youtube-live-007-E0015`, `mikey-youtube-live-007-E0016`, `mikey-youtube-live-007-E0017`, `mikey-youtube-live-007-E0018`, `mikey-youtube-live-007-E0019`, `mikey-youtube-live-007-E0020`, `mikey-youtube-live-007-E0021`, `mikey-youtube-live-007-E0022`, `mikey-youtube-live-007-E0023`, `mikey-youtube-live-007-E0024`, `mikey-youtube-live-007-E0025`, `mikey-youtube-live-007-E0026`, `mikey-youtube-live-007-E0027`, `mikey-youtube-live-007-E0028`, `mikey-youtube-live-007-E0029`, `mikey-youtube-live-007-E0030`, `mikey-youtube-live-007-E0031`, `mikey-youtube-live-007-E0032`, `mikey-youtube-live-007-E0033`, `mikey-youtube-live-007-E0034`, `mikey-youtube-live-007-E0035`, `mikey-youtube-live-007-E0036`, `mikey-youtube-live-007-E0037`, `mikey-youtube-live-007-E0038`, `mikey-youtube-live-007-E0039`, `mikey-youtube-live-007-E0040`｜status=`open`
- `mikey-youtube-live-007-R023`｜`blocking`｜`viewer_count_percentage`｜127人、90%写不出优点等数字是否准确且仅为即兴估计？｜affected=`mikey-youtube-live-007-E0033`｜status=`open`
- `mikey-youtube-live-008-R001`｜`major`｜`speaker_and_relay_boundary`｜全期是否确为Mikey单人口播，每个聊天问题的代读起止是否正确？｜affected=`mikey-youtube-live-008-E0001`, `mikey-youtube-live-008-E0002`, `mikey-youtube-live-008-E0003`, `mikey-youtube-live-008-E0004`, `mikey-youtube-live-008-E0005`, `mikey-youtube-live-008-E0006`, `mikey-youtube-live-008-E0007`, `mikey-youtube-live-008-E0008`, `mikey-youtube-live-008-E0009`, `mikey-youtube-live-008-E0010`, `mikey-youtube-live-008-E0011`, `mikey-youtube-live-008-E0012`, `mikey-youtube-live-008-E0013`, `mikey-youtube-live-008-E0014`, `mikey-youtube-live-008-E0015`, `mikey-youtube-live-008-E0016`, `mikey-youtube-live-008-E0017`, `mikey-youtube-live-008-E0018`, `mikey-youtube-live-008-E0019`, `mikey-youtube-live-008-E0020`, `mikey-youtube-live-008-E0021`, `mikey-youtube-live-008-E0022`, `mikey-youtube-live-008-E0023`, `mikey-youtube-live-008-E0024`, `mikey-youtube-live-008-E0025`, `mikey-youtube-live-008-E0026`, `mikey-youtube-live-008-E0027`, `mikey-youtube-live-008-E0028`, `mikey-youtube-live-008-E0029`, `mikey-youtube-live-008-E0030`, `mikey-youtube-live-008-E0031`, `mikey-youtube-live-008-E0032`, `mikey-youtube-live-008-E0033`, `mikey-youtube-live-008-E0034`, `mikey-youtube-live-008-E0035`, `mikey-youtube-live-008-E0036`, `mikey-youtube-live-008-E0037`, `mikey-youtube-live-008-E0038`｜status=`open`

### caller_guest_qa_pairing（14项）

- `mikey-youtube-live-001-R009`｜`major`｜`speaker_attribution`｜夜场问答中来电者与Mikey的交错边界是否准确？｜affected=`mikey-youtube-live-001-E0019`, `mikey-youtube-live-001-E0020`, `mikey-youtube-live-001-K016`, `mikey-youtube-live-001-K017`｜status=`open`
- `mikey-youtube-live-001-R011`｜`blocking`｜`relationship_ethics`｜来电案例中是否存在先前明确拒绝、欺骗、羞辱或其他会改变伦理判断的细节？｜affected=`mikey-youtube-live-001-E0026`, `mikey-youtube-live-001-K023`｜status=`open`
- `mikey-youtube-live-002-R001`｜`blocking`｜`speaker_attribution`｜开场主持、群友、观众代读和短插话的逐句边界是否正确？｜affected=`mikey-youtube-live-002-E0001`, `mikey-youtube-live-002-E0002`, `mikey-youtube-live-002-E0003`, `mikey-youtube-live-002-E0004`, `mikey-youtube-live-002-E0005`, `mikey-youtube-live-002-E0006`, `mikey-youtube-live-002-E0007`, `mikey-youtube-live-002-E0008`, `mikey-youtube-live-002-K001`, `mikey-youtube-live-002-K002`, `mikey-youtube-live-002-K003`｜status=`open`
- `mikey-youtube-live-002-R004`｜`major`｜`speaker_attribution`｜牵手拥抱后冷淡案例中群友追问与Mikey回答的边界是否准确？｜affected=`mikey-youtube-live-002-E0017`, `mikey-youtube-live-002-E0018`, `mikey-youtube-live-002-E0019`, `mikey-youtube-live-002-K010`, `mikey-youtube-live-002-K011`｜status=`open`
- `mikey-youtube-live-002-R006`｜`blocking`｜`speaker_attribution`｜主持离席期间究竟有几名群友，挑战和打枪建议分别由谁说？｜affected=`mikey-youtube-live-002-E0033`, `mikey-youtube-live-002-E0034`, `mikey-youtube-live-002-K020`｜status=`open`
- `mikey-youtube-live-002-R007`｜`major`｜`speaker_attribution`｜无所谓心态和关系意图两组问答的短句归属是否正确？｜affected=`mikey-youtube-live-002-E0036`, `mikey-youtube-live-002-E0037`, `mikey-youtube-live-002-E0038`, `mikey-youtube-live-002-E0039`, `mikey-youtube-live-002-K021`, `mikey-youtube-live-002-K022`｜status=`open`
- `mikey-youtube-live-002-R016`｜`major`｜`speaker_attribution`｜矩阵长讨论中Mikey和群友的观点边界在哪里？｜affected=`mikey-youtube-live-002-E0060`, `mikey-youtube-live-002-K036`｜status=`open`
- `mikey-youtube-live-002-R017`｜`major`｜`attributed_other`｜高收入女性案例哪些为群友经历，哪些为Mikey补充？｜affected=`mikey-youtube-live-002-E0062`, `mikey-youtube-live-002-K037`｜status=`open`
- `mikey-youtube-live-003-R001`｜`blocking`｜`speaker_attribution`｜多人语音会议中Mikey、19个临时来电者编号及所有短插话的逐句归属是否正确？｜affected=`mikey-youtube-live-003-E0001`, `mikey-youtube-live-003-E0002`, `mikey-youtube-live-003-E0003`, `mikey-youtube-live-003-E0004`, `mikey-youtube-live-003-E0005`, `mikey-youtube-live-003-E0006`, `mikey-youtube-live-003-E0007`, `mikey-youtube-live-003-E0008`, `mikey-youtube-live-003-E0009`, `mikey-youtube-live-003-E0010`, `mikey-youtube-live-003-E0011`, `mikey-youtube-live-003-E0012`, `mikey-youtube-live-003-E0013`, `mikey-youtube-live-003-E0014`, `mikey-youtube-live-003-E0015`, `mikey-youtube-live-003-E0016`, `mikey-youtube-live-003-E0017`, `mikey-youtube-live-003-E0018`, `mikey-youtube-live-003-E0019`, `mikey-youtube-live-003-E0020`, `mikey-youtube-live-003-E0021`, `mikey-youtube-live-003-E0022`, `mikey-youtube-live-003-E0023`, `mikey-youtube-live-003-E0024`, `mikey-youtube-live-003-E0025`, `mikey-youtube-live-003-E0026`, `mikey-youtube-live-003-E0027`, `mikey-youtube-live-003-E0028`, `mikey-youtube-live-003-E0029`, `mikey-youtube-live-003-K001`, `mikey-youtube-live-003-K002`, `mikey-youtube-live-003-K003`, `mikey-youtube-live-003-K004`, `mikey-youtube-live-003-K005`, `mikey-youtube-live-003-K006`, `mikey-youtube-live-003-K007`, `mikey-youtube-live-003-K008`, `mikey-youtube-live-003-K009`, `mikey-youtube-live-003-K010`, `mikey-youtube-live-003-K011`, `mikey-youtube-live-003-K012`, `mikey-youtube-live-003-K013`, `mikey-youtube-live-003-K014`, `mikey-youtube-live-003-K015`, `mikey-youtube-live-003-K016`｜status=`open`
- `mikey-youtube-live-003-R003`｜`blocking`｜`consent_and_result`｜保守女性约会中的肢体接触、拒绝、私密空间与结果的叙述顺序是否准确？｜affected=`mikey-youtube-live-003-E0003`｜status=`open`
- `mikey-youtube-live-003-R006`｜`major`｜`third_party_story`｜天津群友酒局故事中摸陌生人、跑单、金额和结果的实际说话人和事实是否准确？｜affected=`mikey-youtube-live-003-E0010`｜status=`open`
- `mikey-youtube-live-003-R014`｜`blocking`｜`accident_financial_result`｜意大利车祸案例中谁开车、责任、保险比例、金额和亲密升级结果是否准确？｜affected=`mikey-youtube-live-003-E0026`｜status=`open`
- `mikey-youtube-live-006-RN005`｜`major`｜`音频空段与即时邀约`｜1244秒和1769秒后的长空段是否为静音/读取消息，问答边界是否被截断？｜affected=`mikey-youtube-live-006-E0012`, `mikey-youtube-live-006-E0014`｜status=`open`
- `mikey-youtube-live-009-RN005`｜`major`｜`邀约拒绝与补安全感`｜拒绝是否被过度解释为安全感问题，是否保留不感兴趣的可能？｜affected=`mikey-youtube-live-009-E0010`, `mikey-youtube-live-009-E0011`｜status=`open`

### speaker_attribution（25项）

- `mikey-youtube-live-001-R001`｜`blocking`｜`speaker_attribution`｜开场龙哥案例、Mikey插话和疑似剪辑旁白的逐句归属是否正确？｜affected=`mikey-youtube-live-001-E0001`, `mikey-youtube-live-001-E0002`, `mikey-youtube-live-001-E0003`, `mikey-youtube-live-001-E0004`, `mikey-youtube-live-001-E0005`, `mikey-youtube-live-001-E0006`｜status=`open`
- `mikey-youtube-live-001-R002`｜`blocking`｜`consent_legal_claim`｜‘没有法律风险’与‘说no就停’的原话、语境和说话人是否准确？｜affected=`mikey-youtube-live-001-E0006`｜status=`open`
- `mikey-youtube-live-001-R009`｜`major`｜`speaker_attribution`｜夜场问答中来电者与Mikey的交错边界是否准确？｜affected=`mikey-youtube-live-001-E0019`, `mikey-youtube-live-001-E0020`, `mikey-youtube-live-001-K016`, `mikey-youtube-live-001-K017`｜status=`open`
- `mikey-youtube-live-001-R012`｜`major`｜`speaker_attribution`｜B哥方法的原理解释主要由谁说，Mikey只在哪些句子回应？｜affected=`mikey-youtube-live-001-E0027`, `mikey-youtube-live-001-K024`｜status=`open`
- `mikey-youtube-live-002-R001`｜`blocking`｜`speaker_attribution`｜开场主持、群友、观众代读和短插话的逐句边界是否正确？｜affected=`mikey-youtube-live-002-E0001`, `mikey-youtube-live-002-E0002`, `mikey-youtube-live-002-E0003`, `mikey-youtube-live-002-E0004`, `mikey-youtube-live-002-E0005`, `mikey-youtube-live-002-E0006`, `mikey-youtube-live-002-E0007`, `mikey-youtube-live-002-E0008`, `mikey-youtube-live-002-K001`, `mikey-youtube-live-002-K002`, `mikey-youtube-live-002-K003`｜status=`open`
- `mikey-youtube-live-002-R004`｜`major`｜`speaker_attribution`｜牵手拥抱后冷淡案例中群友追问与Mikey回答的边界是否准确？｜affected=`mikey-youtube-live-002-E0017`, `mikey-youtube-live-002-E0018`, `mikey-youtube-live-002-E0019`, `mikey-youtube-live-002-K010`, `mikey-youtube-live-002-K011`｜status=`open`
- `mikey-youtube-live-002-R006`｜`blocking`｜`speaker_attribution`｜主持离席期间究竟有几名群友，挑战和打枪建议分别由谁说？｜affected=`mikey-youtube-live-002-E0033`, `mikey-youtube-live-002-E0034`, `mikey-youtube-live-002-K020`｜status=`open`
- `mikey-youtube-live-002-R007`｜`major`｜`speaker_attribution`｜无所谓心态和关系意图两组问答的短句归属是否正确？｜affected=`mikey-youtube-live-002-E0036`, `mikey-youtube-live-002-E0037`, `mikey-youtube-live-002-E0038`, `mikey-youtube-live-002-E0039`, `mikey-youtube-live-002-K021`, `mikey-youtube-live-002-K022`｜status=`open`
- `mikey-youtube-live-002-R016`｜`major`｜`speaker_attribution`｜矩阵长讨论中Mikey和群友的观点边界在哪里？｜affected=`mikey-youtube-live-002-E0060`, `mikey-youtube-live-002-K036`｜status=`open`
- `mikey-youtube-live-002-R024`｜`major`｜`visual_scope`｜左侧直播评论、腾讯会议头像/高亮和参与者列表是否包含改变问题作者或说话人的信息？｜affected=`mikey-youtube-live-002-E0001`, `mikey-youtube-live-002-E0006`, `mikey-youtube-live-002-E0033`, `mikey-youtube-live-002-E0034`, `mikey-youtube-live-002-E0065`, `mikey-youtube-live-002-E0075`｜status=`open`
- `mikey-youtube-live-003-R001`｜`blocking`｜`speaker_attribution`｜多人语音会议中Mikey、19个临时来电者编号及所有短插话的逐句归属是否正确？｜affected=`mikey-youtube-live-003-E0001`, `mikey-youtube-live-003-E0002`, `mikey-youtube-live-003-E0003`, `mikey-youtube-live-003-E0004`, `mikey-youtube-live-003-E0005`, `mikey-youtube-live-003-E0006`, `mikey-youtube-live-003-E0007`, `mikey-youtube-live-003-E0008`, `mikey-youtube-live-003-E0009`, `mikey-youtube-live-003-E0010`, `mikey-youtube-live-003-E0011`, `mikey-youtube-live-003-E0012`, `mikey-youtube-live-003-E0013`, `mikey-youtube-live-003-E0014`, `mikey-youtube-live-003-E0015`, `mikey-youtube-live-003-E0016`, `mikey-youtube-live-003-E0017`, `mikey-youtube-live-003-E0018`, `mikey-youtube-live-003-E0019`, `mikey-youtube-live-003-E0020`, `mikey-youtube-live-003-E0021`, `mikey-youtube-live-003-E0022`, `mikey-youtube-live-003-E0023`, `mikey-youtube-live-003-E0024`, `mikey-youtube-live-003-E0025`, `mikey-youtube-live-003-E0026`, `mikey-youtube-live-003-E0027`, `mikey-youtube-live-003-E0028`, `mikey-youtube-live-003-E0029`, `mikey-youtube-live-003-K001`, `mikey-youtube-live-003-K002`, `mikey-youtube-live-003-K003`, `mikey-youtube-live-003-K004`, `mikey-youtube-live-003-K005`, `mikey-youtube-live-003-K006`, `mikey-youtube-live-003-K007`, `mikey-youtube-live-003-K008`, `mikey-youtube-live-003-K009`, `mikey-youtube-live-003-K010`, `mikey-youtube-live-003-K011`, `mikey-youtube-live-003-K012`, `mikey-youtube-live-003-K013`, `mikey-youtube-live-003-K014`, `mikey-youtube-live-003-K015`, `mikey-youtube-live-003-K016`｜status=`open`
- `mikey-youtube-live-003-R004`｜`blocking`｜`consent_escalation`｜私人影院的施压/减压、身体接触和对方口头拒绝相关语句是否完整、归属正确，且未越过同意边界？｜affected=`mikey-youtube-live-003-E0005`, `mikey-youtube-live-003-E0006`, `mikey-youtube-live-003-E0007`, `mikey-youtube-live-003-E0008`｜status=`open`
- `mikey-youtube-live-003-R005`｜`major`｜`numeric_claim`｜‘一周12场约会、7个结果’等数字和归属是否正确？｜affected=`mikey-youtube-live-003-E0005`｜status=`open`
- `mikey-youtube-live-003-R006`｜`major`｜`third_party_story`｜天津群友酒局故事中摸陌生人、跑单、金额和结果的实际说话人和事实是否准确？｜affected=`mikey-youtube-live-003-E0010`｜status=`open`
- `mikey-youtube-live-003-R008`｜`blocking`｜`following_refusal`｜闺蜜拒绝、强制截停和跟随距离的归属与否定词是否准确？｜affected=`mikey-youtube-live-003-E0015`｜status=`open`
- `mikey-youtube-live-003-R010`｜`major`｜`asr_overlap`｜中枪/游戏相关突然插话是否为会议中其他声音或背景播放？｜affected=`mikey-youtube-live-003-E0018`｜status=`open`
- `mikey-youtube-live-003-R015`｜`blocking`｜`consent_and_relationship`｜车祸案例后续中‘不让去家里’、朋友框架、再见面和继续升级的归属是否正确？｜affected=`mikey-youtube-live-003-E0027`｜status=`open`
- `mikey-youtube-live-005-R001`｜`major`｜`speaker_and_relay_boundary`｜全期是否确为Mikey单人口播，每个YouTube文字问题的代读边界是否正确？｜affected=`mikey-youtube-live-005-E0001`, `mikey-youtube-live-005-E0002`, `mikey-youtube-live-005-E0003`, `mikey-youtube-live-005-E0004`, `mikey-youtube-live-005-E0005`, `mikey-youtube-live-005-E0006`, `mikey-youtube-live-005-E0007`, `mikey-youtube-live-005-E0008`, `mikey-youtube-live-005-E0009`, `mikey-youtube-live-005-E0010`, `mikey-youtube-live-005-E0011`, `mikey-youtube-live-005-E0012`, `mikey-youtube-live-005-E0013`, `mikey-youtube-live-005-E0014`, `mikey-youtube-live-005-E0015`, `mikey-youtube-live-005-E0016`, `mikey-youtube-live-005-E0017`, `mikey-youtube-live-005-E0018`, `mikey-youtube-live-005-E0019`, `mikey-youtube-live-005-E0020`｜status=`open`
- `mikey-youtube-live-005-R013`｜`major`｜`viewer_case_attribution`｜聊一周、见她与男生吃饭、被拉黑的完整问题是否由Mikey代读，关键人称是否准确？｜affected=`mikey-youtube-live-005-E0018`｜status=`open`
- `mikey-youtube-live-007-R001`｜`major`｜`speaker_and_question_boundary`｜全期是否只有Mikey口播，每个屏幕问题的作者、代读起止和回答边界是否准确？｜affected=`mikey-youtube-live-007-E0001`, `mikey-youtube-live-007-E0002`, `mikey-youtube-live-007-E0003`, `mikey-youtube-live-007-E0004`, `mikey-youtube-live-007-E0005`, `mikey-youtube-live-007-E0006`, `mikey-youtube-live-007-E0007`, `mikey-youtube-live-007-E0008`, `mikey-youtube-live-007-E0009`, `mikey-youtube-live-007-E0010`, `mikey-youtube-live-007-E0011`, `mikey-youtube-live-007-E0012`, `mikey-youtube-live-007-E0013`, `mikey-youtube-live-007-E0014`, `mikey-youtube-live-007-E0015`, `mikey-youtube-live-007-E0016`, `mikey-youtube-live-007-E0017`, `mikey-youtube-live-007-E0018`, `mikey-youtube-live-007-E0019`, `mikey-youtube-live-007-E0020`, `mikey-youtube-live-007-E0021`, `mikey-youtube-live-007-E0022`, `mikey-youtube-live-007-E0023`, `mikey-youtube-live-007-E0024`, `mikey-youtube-live-007-E0025`, `mikey-youtube-live-007-E0026`, `mikey-youtube-live-007-E0027`, `mikey-youtube-live-007-E0028`, `mikey-youtube-live-007-E0029`, `mikey-youtube-live-007-E0030`, `mikey-youtube-live-007-E0031`, `mikey-youtube-live-007-E0032`, `mikey-youtube-live-007-E0033`, `mikey-youtube-live-007-E0034`, `mikey-youtube-live-007-E0035`, `mikey-youtube-live-007-E0036`, `mikey-youtube-live-007-E0037`, `mikey-youtube-live-007-E0038`, `mikey-youtube-live-007-E0039`, `mikey-youtube-live-007-E0040`｜status=`open`
- `mikey-youtube-live-007-R009`｜`major`｜`fake_window_attribution`｜先撩后退能否确认为假窗口？｜affected=`mikey-youtube-live-007-E0014`｜status=`open`
- `mikey-youtube-live-008-R001`｜`major`｜`speaker_and_relay_boundary`｜全期是否确为Mikey单人口播，每个聊天问题的代读起止是否正确？｜affected=`mikey-youtube-live-008-E0001`, `mikey-youtube-live-008-E0002`, `mikey-youtube-live-008-E0003`, `mikey-youtube-live-008-E0004`, `mikey-youtube-live-008-E0005`, `mikey-youtube-live-008-E0006`, `mikey-youtube-live-008-E0007`, `mikey-youtube-live-008-E0008`, `mikey-youtube-live-008-E0009`, `mikey-youtube-live-008-E0010`, `mikey-youtube-live-008-E0011`, `mikey-youtube-live-008-E0012`, `mikey-youtube-live-008-E0013`, `mikey-youtube-live-008-E0014`, `mikey-youtube-live-008-E0015`, `mikey-youtube-live-008-E0016`, `mikey-youtube-live-008-E0017`, `mikey-youtube-live-008-E0018`, `mikey-youtube-live-008-E0019`, `mikey-youtube-live-008-E0020`, `mikey-youtube-live-008-E0021`, `mikey-youtube-live-008-E0022`, `mikey-youtube-live-008-E0023`, `mikey-youtube-live-008-E0024`, `mikey-youtube-live-008-E0025`, `mikey-youtube-live-008-E0026`, `mikey-youtube-live-008-E0027`, `mikey-youtube-live-008-E0028`, `mikey-youtube-live-008-E0029`, `mikey-youtube-live-008-E0030`, `mikey-youtube-live-008-E0031`, `mikey-youtube-live-008-E0032`, `mikey-youtube-live-008-E0033`, `mikey-youtube-live-008-E0034`, `mikey-youtube-live-008-E0035`, `mikey-youtube-live-008-E0036`, `mikey-youtube-live-008-E0037`, `mikey-youtube-live-008-E0038`｜status=`open`
- `mikey-youtube-live-008-R002`｜`major`｜`relationship_story_attribution`｜前女友同时与多人交往的数字、时间和人物关系是否听写正确？｜affected=`mikey-youtube-live-008-E0002`｜status=`open`
- `mikey-youtube-live-008-R015`｜`blocking`｜`mental_health_and_safety`｜地雷女、自残割腕、带回家后逃跑等案例的归属和安全处置是否完整？｜affected=`mikey-youtube-live-008-E0027`｜status=`open`
- `mikey-youtube-live-008-R019`｜`major`｜`voice_training_claim`｜每天开窗大吼21天的训练建议、数字和潜在风险是否准确？｜affected=`mikey-youtube-live-008-E0033`｜status=`open`

### refusals_stops_and_consent（68项）

- `mikey-youtube-live-001-R002`｜`blocking`｜`consent_legal_claim`｜‘没有法律风险’与‘说no就停’的原话、语境和说话人是否准确？｜affected=`mikey-youtube-live-001-E0006`｜status=`open`
- `mikey-youtube-live-001-R004`｜`blocking`｜`sexual_advice_boundary`｜眼神想象、明示内容及所谓‘授权’是否可能被误读为无视对方同意？｜affected=`mikey-youtube-live-001-E0010`, `mikey-youtube-live-001-K005`｜status=`open`
- `mikey-youtube-live-001-R011`｜`blocking`｜`relationship_ethics`｜来电案例中是否存在先前明确拒绝、欺骗、羞辱或其他会改变伦理判断的细节？｜affected=`mikey-youtube-live-001-E0026`, `mikey-youtube-live-001-K023`｜status=`open`
- `mikey-youtube-live-001-R014`｜`blocking`｜`physical_escalation`｜肢体升级被拒绝后的建议是否明确要求尊重拒绝，是否存在会鼓励重复越界的表述？｜affected=`mikey-youtube-live-001-E0030`, `mikey-youtube-live-001-K026`｜status=`open`
- `mikey-youtube-live-002-R003`｜`blocking`｜`sexual_advice_boundary`｜性化眼神想象与性氛围段落如何与明确同意和舒适边界联读？｜affected=`mikey-youtube-live-002-E0014`, `mikey-youtube-live-002-K007`｜status=`open`
- `mikey-youtube-live-002-R005`｜`blocking`｜`consent_and_deception`｜酒店与短期关系案例是否存在未保留的拒绝、欺骗或持续同意细节？｜affected=`mikey-youtube-live-002-E0028`, `mikey-youtube-live-002-E0029`, `mikey-youtube-live-002-E0030`, `mikey-youtube-live-002-E0031`, `mikey-youtube-live-002-K018`, `mikey-youtube-live-002-K019`｜status=`open`
- `mikey-youtube-live-002-R014`｜`blocking`｜`legal_and_consent_claim`｜录音、报警、拘留等法律判断是否准确，是否会把录音误当成同意？｜affected=`mikey-youtube-live-002-E0056`, `mikey-youtube-live-002-K032`｜status=`open`
- `mikey-youtube-live-002-R018`｜`blocking`｜`consent_boundary`｜第二次约会才同意是否被错误解释为第一次拒绝可忽略？｜affected=`mikey-youtube-live-002-E0064`, `mikey-youtube-live-002-K038`｜status=`open`
- `mikey-youtube-live-002-R019`｜`blocking`｜`case_outcome_and_consent`｜成都外卖到家案例的消息顺序、考虑、叫车、见面动作、同意与结果是否准确？｜affected=`mikey-youtube-live-002-E0066`, `mikey-youtube-live-002-K039`, `mikey-youtube-live-002-K040`｜status=`open`
- `mikey-youtube-live-002-R021`｜`blocking`｜`sexual_escalation`｜酒店转场建议是否会鼓励规避拒绝或社会压力？｜affected=`mikey-youtube-live-002-E0068`｜status=`open`
- `mikey-youtube-live-002-R022`｜`blocking`｜`unsafe_sex_and_alcohol`｜桥洞/楼道/天台、酒精合理化和‘不记得’案例是否涉及违法、不安全或无法同意？｜affected=`mikey-youtube-live-002-E0072`｜status=`open`
- `mikey-youtube-live-002-R023`｜`major`｜`relationship_and_consent`｜‘长期默认先短期’是否仅为Mikey个人经验且需双方明确意愿？｜affected=`mikey-youtube-live-002-E0074`, `mikey-youtube-live-002-K045`, `mikey-youtube-live-002-K046`｜status=`open`
- `mikey-youtube-live-003-R003`｜`blocking`｜`consent_and_result`｜保守女性约会中的肢体接触、拒绝、私密空间与结果的叙述顺序是否准确？｜affected=`mikey-youtube-live-003-E0003`｜status=`open`
- `mikey-youtube-live-003-R004`｜`blocking`｜`consent_escalation`｜私人影院的施压/减压、身体接触和对方口头拒绝相关语句是否完整、归属正确，且未越过同意边界？｜affected=`mikey-youtube-live-003-E0005`, `mikey-youtube-live-003-E0006`, `mikey-youtube-live-003-E0007`, `mikey-youtube-live-003-E0008`｜status=`open`
- `mikey-youtube-live-003-R007`｜`blocking`｜`violence_legal_claim`｜搭讪有伴侣女性、挑衅、打架、逃跑和警察相关言论的原话及语境是否完整？｜affected=`mikey-youtube-live-003-E0011`, `mikey-youtube-live-003-E0012`｜status=`open`
- `mikey-youtube-live-003-R008`｜`blocking`｜`following_refusal`｜闺蜜拒绝、强制截停和跟随距离的归属与否定词是否准确？｜affected=`mikey-youtube-live-003-E0015`｜status=`open`
- `mikey-youtube-live-003-R009`｜`blocking`｜`consent_escalation`｜首次约会肢体接触、拒绝及‘只要不走’言论的原话和上下文是否准确？｜affected=`mikey-youtube-live-003-E0016`｜status=`open`
- `mikey-youtube-live-003-R014`｜`blocking`｜`accident_financial_result`｜意大利车祸案例中谁开车、责任、保险比例、金额和亲密升级结果是否准确？｜affected=`mikey-youtube-live-003-E0026`｜status=`open`
- `mikey-youtube-live-003-R015`｜`blocking`｜`consent_and_relationship`｜车祸案例后续中‘不让去家里’、朋友框架、再见面和继续升级的归属是否正确？｜affected=`mikey-youtube-live-003-E0027`｜status=`open`
- `mikey-youtube-live-004-RN002`｜`blocking`｜`关系承诺与同意`｜短期关系、是否成为男女朋友和停止推进的原话、否定词是否准确？｜affected=`mikey-youtube-live-004-E0003`, `mikey-youtube-live-004-E0004`｜status=`open`
- `mikey-youtube-live-004-RN003`｜`blocking`｜`肢体接触与拒绝`｜牵手被抽开后‘过一会再做’的具体条件是否包含明确再次同意？｜affected=`mikey-youtube-live-004-E0004`｜status=`open`
- `mikey-youtube-live-004-RN004`｜`blocking`｜`私密空间与结果`｜私人影院、去家里、游客短期物流及一小时结果的原话与边界是否准确？｜affected=`mikey-youtube-live-004-E0004`, `mikey-youtube-live-004-E0006`｜status=`open`
- `mikey-youtube-live-004-RN005`｜`major`｜`修辞压制异议`｜‘烧CPU/更高维度干住她’是描述修辞还是可执行建议，是否会压过对方边界？｜affected=`mikey-youtube-live-004-E0007`, `mikey-youtube-live-004-E0008`｜status=`open`
- `mikey-youtube-live-004-RN006`｜`major`｜`隐私与亲密关系`｜手机隐私、官宣和亲密关系顾虑的原话是否完整？｜affected=`mikey-youtube-live-004-E0010`, `mikey-youtube-live-004-E0011`｜status=`open`
- `mikey-youtube-live-004-RN007`｜`blocking`｜`肢体升级系统`｜线下预期、牵手和关系升级的建议是否完整保留对方意愿？｜affected=`mikey-youtube-live-004-E0011`, `mikey-youtube-live-004-E0013`｜status=`open`
- `mikey-youtube-live-004-RN008`｜`blocking`｜`线上预期`｜线上询问能否牵手等话术是否被误读为预先取得后续同意？｜affected=`mikey-youtube-live-004-E0013`, `mikey-youtube-live-004-E0014`｜status=`open`
- `mikey-youtube-live-004-RN010`｜`blocking`｜`性关系承诺`｜‘我睡了你就负责’限定为真想恋爱者的原话和否定词是否准确？｜affected=`mikey-youtube-live-004-E0020`, `mikey-youtube-live-004-E0021`｜status=`open`
- `mikey-youtube-live-004-RN011`｜`blocking`｜`拒绝后停止`｜被拒绝后停止跟随的原话是否准确，是否存在相反短句被ASR合并？｜affected=`mikey-youtube-live-004-E0022`, `mikey-youtube-live-004-E0023`｜status=`open`
- `mikey-youtube-live-004-RN012`｜`blocking`｜`有男友对象与私人空间`｜将公共影院升级到私人影院/家中的建议是否保留对方选择和关系边界？｜affected=`mikey-youtube-live-004-E0024`｜status=`open`
- `mikey-youtube-live-004-RN013`｜`major`｜`未通过好友后再次接近`｜再次上前询问的原话、场景和骚扰边界是否完整？｜affected=`mikey-youtube-live-004-E0029`｜status=`open`
- `mikey-youtube-live-005-R003`｜`blocking`｜`sexual_health_claim`｜‘时间短就是太紧张’是否只是简化口头回答，不应当成医疗结论？｜affected=`mikey-youtube-live-005-E0004`｜status=`open`
- `mikey-youtube-live-005-R007`｜`blocking`｜`minor_age_context`｜‘漫展都是小孩’与搭讪建议的语境是否明确要求避开未成年人？｜affected=`mikey-youtube-live-005-E0010`｜status=`open`
- `mikey-youtube-live-005-R008`｜`major`｜`bar_kiss_result`｜酒吧接吻案例中的数字、注意力和结果判断是否准确？｜affected=`mikey-youtube-live-005-E0011`｜status=`open`
- `mikey-youtube-live-005-R010`｜`major`｜`negation_and_subcommunication`｜用语调表达拒绝的例子中，反话和否定的原话是否准确？｜affected=`mikey-youtube-live-005-E0015`｜status=`open`
- `mikey-youtube-live-005-R012`｜`blocking`｜`hotel_consent`｜‘陪我去酒店吃个药’与对方拒绝后的所谓操作是什么，是否清楚维持停止和同意边界？｜affected=`mikey-youtube-live-005-E0017`｜status=`open`
- `mikey-youtube-live-005-R014`｜`blocking`｜`hotel_cancellation_claim`｜平台预订的取消时限、免责退款和钟点/过夜建议是否适用于具体订单？｜affected=`mikey-youtube-live-005-E0019`｜status=`open`
- `mikey-youtube-live-005-R015`｜`blocking`｜`age_deception`｜按对方喜好乱报年龄的言论是否完整，且不应升级为鼓励欺骗的建议？｜affected=`mikey-youtube-live-005-E0019`｜status=`open`
- `mikey-youtube-live-006-RN002`｜`blocking`｜`亲密拒绝与ASD标签`｜‘不能强上’后的原因分析是否会把拒绝重新解释成可继续推进？｜affected=`mikey-youtube-live-006-E0005`, `mikey-youtube-live-006-E0006`｜status=`open`
- `mikey-youtube-live-006-RN004`｜`blocking`｜`夜场醉酒与闺蜜`｜醉酒、闺蜜被灌酒及无法离场的例子是否准确，是否涉及需要优先保障安全的情形？｜affected=`mikey-youtube-live-006-E0012`｜status=`open`
- `mikey-youtube-live-006-RN007`｜`blocking`｜`假窗口与私密场所邀请`｜亲密接触、回家邀请被拒及所谓‘假窗口’的原话是否准确？｜affected=`mikey-youtube-live-006-E0016`, `mikey-youtube-live-006-E0017`｜status=`open`
- `mikey-youtube-live-007-R010`｜`blocking`｜`consent_words_actions`｜女性‘嘴上和行为不一致’是否会否定明确口头边界？｜affected=`mikey-youtube-live-007-E0017`｜status=`open`
- `mikey-youtube-live-007-R013`｜`blocking`｜`sex_difference_numbers`｜男人10秒、女人半小时/一小时的说法是否准确且不得泛化？｜affected=`mikey-youtube-live-007-E0021`｜status=`open`
- `mikey-youtube-live-007-R014`｜`blocking`｜`hotel_euphemism_consent`｜‘回酒店吃药’是否规避真实意图和知情同意？｜affected=`mikey-youtube-live-007-E0023`｜status=`open`
- `mikey-youtube-live-007-R022`｜`major`｜`three_second_safety`｜三秒原则是否限于安全、合适、尊重拒绝的场景？｜affected=`mikey-youtube-live-007-E0032`｜status=`open`
- `mikey-youtube-live-007-R024`｜`major`｜`self_value_diagnostic`｜写不出优点、炫富、买便宜衣服是否被过度诊断？｜affected=`mikey-youtube-live-007-E0033`, `mikey-youtube-live-007-E0034`｜status=`open`
- `mikey-youtube-live-008-R009`｜`blocking`｜`location_and_consent`｜异地无住所时去楼道等转场说法是否维持明确同意和安全边界？｜affected=`mikey-youtube-live-008-E0016`｜status=`open`
- `mikey-youtube-live-008-R011`｜`blocking`｜`first_escalation_consent`｜第一次关系升级、弱意图及用借口回家的描述是否保持双方自愿？｜affected=`mikey-youtube-live-008-E0021`｜status=`open`
- `mikey-youtube-live-008-R012`｜`blocking`｜`sexual_anatomy_stereotype`｜性器官长度、族群差异等说法是否准确，如何避免医学误导和族群刻板印象？｜affected=`mikey-youtube-live-008-E0023`｜status=`open`
- `mikey-youtube-live-008-R013`｜`blocking`｜`regional_stereotypes`｜日本、韩国、新加坡、泰国及性别群体的概括是否仅是个人印象？｜affected=`mikey-youtube-live-008-E0025`, `mikey-youtube-live-008-E0026`｜status=`open`
- `mikey-youtube-live-008-R016`｜`blocking`｜`one_bed_consent`｜只有一张床时‘不要解释’的完整表述是否会弱化对方同意？｜affected=`mikey-youtube-live-008-E0027`｜status=`open`
- `mikey-youtube-live-008-R018`｜`blocking`｜`filming_consent`｜海外街拍、询问拍摄同意和发布消音的流程是否符合法律与隐私要求？｜affected=`mikey-youtube-live-008-E0032`｜status=`open`
- `mikey-youtube-live-008-R020`｜`major`｜`timing_and_interest_metrics`｜20分钟关系升级、米斯特里四小时规则和Kino指标的数字及否定词是否准确？｜affected=`mikey-youtube-live-008-E0033`, `mikey-youtube-live-008-E0034`｜status=`open`
- `mikey-youtube-live-009-RN001`｜`blocking`｜`亲密关系自报与未来私宅邀约`｜当晚性行为和次日约到家中的自述是否准确，未来安排是否被误作已经同意？｜affected=`mikey-youtube-live-009-E0001`｜status=`open`
- `mikey-youtube-live-009-RN002`｜`blocking`｜`搭讪与性结果叙事`｜把街头认识与发生性关系连接的表述是否遗漏持续同意边界？｜affected=`mikey-youtube-live-009-E0001`, `mikey-youtube-live-009-E0003`｜status=`open`
- `mikey-youtube-live-009-RN005`｜`major`｜`邀约拒绝与补安全感`｜拒绝是否被过度解释为安全感问题，是否保留不感兴趣的可能？｜affected=`mikey-youtube-live-009-E0010`, `mikey-youtube-live-009-E0011`｜status=`open`
- `mikey-youtube-live-009-RN007`｜`major`｜`防备心与投入`｜关于东亚女性普遍防备的概括和投入建议是否会忽略明确冷淡？｜affected=`mikey-youtube-live-009-E0018`, `mikey-youtube-live-009-E0019`｜status=`open`
- `mikey-youtube-live-009-RN009`｜`blocking`｜`女性话语无参考价值`｜‘80%–90%女性说的话无参考价值’及用案例推翻口头边界的原话是否准确？｜affected=`mikey-youtube-live-009-E0019`, `mikey-youtube-live-009-E0021`｜status=`open`
- `mikey-youtube-live-009-RN010`｜`blocking`｜`真假拒绝与继续劝说`｜所谓矜持/假拒绝的判断是否会造成对明确拒绝继续施压？｜affected=`mikey-youtube-live-009-E0021`｜status=`open`
- `mikey-youtube-live-009-RN012`｜`major`｜`不尊重时的喷与性需求拒绝`｜边界表达示例中‘喷她’与坦然接受性拒绝如何区分？｜affected=`mikey-youtube-live-009-E0023`, `mikey-youtube-live-009-E0025`｜status=`open`
- `mikey-youtube-live-010-RN001`｜`blocking`｜`三秒原则与肢体行动`｜三秒原则是否被用于未经确认的牵手等肢体行为？｜affected=`mikey-youtube-live-010-E0001`, `mikey-youtube-live-010-K0001`, `mikey-youtube-live-010-K0002`｜status=`open`
- `mikey-youtube-live-010-RN006`｜`blocking`｜`搭讪短暂跟随`｜‘跟五步/五米’是否可能覆盖对方持续不愿停下的拒绝？｜affected=`mikey-youtube-live-010-E0008`, `mikey-youtube-live-010-K0011`, `mikey-youtube-live-010-K0012`, `mikey-youtube-live-010-K0013`｜status=`open`
- `mikey-youtube-live-010-RN007`｜`blocking`｜`少说话速推性结果`｜不说话后带回家发生关系的自报是否遗漏同意、饮酒和过程边界？｜affected=`mikey-youtube-live-010-E0008`, `mikey-youtube-live-010-E0009`, `mikey-youtube-live-010-K0011`, `mikey-youtube-live-010-K0012`, `mikey-youtube-live-010-K0013`, `mikey-youtube-live-010-K0014`｜status=`open`
- `mikey-youtube-live-010-RN009`｜`blocking`｜`边界后性结果自报`｜让对方回去后又称发生性关系，是否会把结果当边界正确的证明？｜affected=`mikey-youtube-live-010-E0010`, `mikey-youtube-live-010-E0012`, `mikey-youtube-live-010-K0015`, `mikey-youtube-live-010-K0016`, `mikey-youtube-live-010-K0018`｜status=`open`
- `mikey-youtube-live-010-RN011`｜`blocking`｜`速推、随便与生理喜欢`｜如何回应进展过快后的失落，是否充分允许撤回和重新协商？｜affected=`mikey-youtube-live-010-E0015`, `mikey-youtube-live-010-K0021`｜status=`open`
- `mikey-youtube-live-010-RN015`｜`major`｜`瞳孔判断吸引`｜仅凭瞳孔放大判断吸引是否可靠？｜affected=`mikey-youtube-live-010-E0019`, `mikey-youtube-live-010-K0026`, `mikey-youtube-live-010-K0027`, `mikey-youtube-live-010-K0028`｜status=`open`
- `mikey-youtube-live-010-RN016`｜`blocking`｜`保守对象与直接回家/破釜沉舟`｜对所谓保守对象直接转场、无吸引仍尝试性推进是否覆盖拒绝？｜affected=`mikey-youtube-live-010-E0020`, `mikey-youtube-live-010-E0021`, `mikey-youtube-live-010-K0028`, `mikey-youtube-live-010-K0029`, `mikey-youtube-live-010-K0030`｜status=`open`
- `mikey-youtube-live-010-RN017`｜`blocking`｜`不用疑问句`｜只说陈述句是否被误用于涉及对方的决定？｜affected=`mikey-youtube-live-010-E0022`, `mikey-youtube-live-010-K0031`, `mikey-youtube-live-010-K0032`｜status=`open`
- `mikey-youtube-live-010-RN018`｜`blocking`｜`未成年性经历自报`｜自述未成年与成年女性的首次性经历是否准确，是否涉及法定同意问题？｜affected=`mikey-youtube-live-010-E0023`, `mikey-youtube-live-010-E0025`, `mikey-youtube-live-010-K0032`, `mikey-youtube-live-010-K0033`, `mikey-youtube-live-010-K0034`｜status=`open`

### age_power_and_relationship_status（38项）

- `mikey-youtube-live-001-R011`｜`blocking`｜`relationship_ethics`｜来电案例中是否存在先前明确拒绝、欺骗、羞辱或其他会改变伦理判断的细节？｜affected=`mikey-youtube-live-001-E0026`, `mikey-youtube-live-001-K023`｜status=`open`
- `mikey-youtube-live-002-R005`｜`blocking`｜`consent_and_deception`｜酒店与短期关系案例是否存在未保留的拒绝、欺骗或持续同意细节？｜affected=`mikey-youtube-live-002-E0028`, `mikey-youtube-live-002-E0029`, `mikey-youtube-live-002-E0030`, `mikey-youtube-live-002-E0031`, `mikey-youtube-live-002-K018`, `mikey-youtube-live-002-K019`｜status=`open`
- `mikey-youtube-live-002-R007`｜`major`｜`speaker_attribution`｜无所谓心态和关系意图两组问答的短句归属是否正确？｜affected=`mikey-youtube-live-002-E0036`, `mikey-youtube-live-002-E0037`, `mikey-youtube-live-002-E0038`, `mikey-youtube-live-002-E0039`, `mikey-youtube-live-002-K021`, `mikey-youtube-live-002-K022`｜status=`open`
- `mikey-youtube-live-002-R012`｜`major`｜`psychology_claim`｜将对父亲恐惧推广为雄性恐惧来源是否仅为个人理论？｜affected=`mikey-youtube-live-002-E0051`, `mikey-youtube-live-002-K029`｜status=`open`
- `mikey-youtube-live-002-R013`｜`blocking`｜`relationship_ethics`｜建议对在意的长期伴侣隐瞒短期关系是否应隔离为不可推广内容？｜affected=`mikey-youtube-live-002-E0053`, `mikey-youtube-live-002-K030`｜status=`open`
- `mikey-youtube-live-002-R023`｜`major`｜`relationship_and_consent`｜‘长期默认先短期’是否仅为Mikey个人经验且需双方明确意愿？｜affected=`mikey-youtube-live-002-E0074`, `mikey-youtube-live-002-K045`, `mikey-youtube-live-002-K046`｜status=`open`
- `mikey-youtube-live-003-R007`｜`blocking`｜`violence_legal_claim`｜搭讪有伴侣女性、挑衅、打架、逃跑和警察相关言论的原话及语境是否完整？｜affected=`mikey-youtube-live-003-E0011`, `mikey-youtube-live-003-E0012`｜status=`open`
- `mikey-youtube-live-003-R013`｜`major`｜`third_party_anecdote`｜年长女性搭讪案例中亲吻、伴侣出现和跑开的叙述是否准确？｜affected=`mikey-youtube-live-003-E0024`｜status=`open`
- `mikey-youtube-live-003-R015`｜`blocking`｜`consent_and_relationship`｜车祸案例后续中‘不让去家里’、朋友框架、再见面和继续升级的归属是否正确？｜affected=`mikey-youtube-live-003-E0027`｜status=`open`
- `mikey-youtube-live-004-RN002`｜`blocking`｜`关系承诺与同意`｜短期关系、是否成为男女朋友和停止推进的原话、否定词是否准确？｜affected=`mikey-youtube-live-004-E0003`, `mikey-youtube-live-004-E0004`｜status=`open`
- `mikey-youtube-live-004-RN006`｜`major`｜`隐私与亲密关系`｜手机隐私、官宣和亲密关系顾虑的原话是否完整？｜affected=`mikey-youtube-live-004-E0010`, `mikey-youtube-live-004-E0011`｜status=`open`
- `mikey-youtube-live-004-RN007`｜`blocking`｜`肢体升级系统`｜线下预期、牵手和关系升级的建议是否完整保留对方意愿？｜affected=`mikey-youtube-live-004-E0011`, `mikey-youtube-live-004-E0013`｜status=`open`
- `mikey-youtube-live-004-RN009`｜`major`｜`有伴侣对象`｜观众转述、Mikey评价和备选关系判断的边界是否准确？｜affected=`mikey-youtube-live-004-E0016`｜status=`open`
- `mikey-youtube-live-004-RN010`｜`blocking`｜`性关系承诺`｜‘我睡了你就负责’限定为真想恋爱者的原话和否定词是否准确？｜affected=`mikey-youtube-live-004-E0020`, `mikey-youtube-live-004-E0021`｜status=`open`
- `mikey-youtube-live-004-RN012`｜`blocking`｜`有男友对象与私人空间`｜将公共影院升级到私人影院/家中的建议是否保留对方选择和关系边界？｜affected=`mikey-youtube-live-004-E0024`｜status=`open`
- `mikey-youtube-live-005-R007`｜`blocking`｜`minor_age_context`｜‘漫展都是小孩’与搭讪建议的语境是否明确要求避开未成年人？｜affected=`mikey-youtube-live-005-E0010`｜status=`open`
- `mikey-youtube-live-005-R015`｜`blocking`｜`age_deception`｜按对方喜好乱报年龄的言论是否完整，且不应升级为鼓励欺骗的建议？｜affected=`mikey-youtube-live-005-E0019`｜status=`open`
- `mikey-youtube-live-006-RN003`｜`major`｜`被发现Game后的关系判断`｜‘她喜欢你但逼自己冷淡’是否只是推测，问题与回答边界是否准确？｜affected=`mikey-youtube-live-006-E0009`, `mikey-youtube-live-006-E0010`｜status=`open`
- `mikey-youtube-live-007-R003`｜`major`｜`relationship_context`｜伴侣关系约定和‘迁就掉吸引’是否只适用于本题？｜affected=`mikey-youtube-live-007-E0002`｜status=`open`
- `mikey-youtube-live-007-R021`｜`major`｜`objectification_analogy`｜把关系类比吃饭的边界和去魅含义是什么？｜affected=`mikey-youtube-live-007-E0031`｜status=`open`
- `mikey-youtube-live-007-R023`｜`blocking`｜`viewer_count_percentage`｜127人、90%写不出优点等数字是否准确且仅为即兴估计？｜affected=`mikey-youtube-live-007-E0033`｜status=`open`
- `mikey-youtube-live-008-R002`｜`major`｜`relationship_story_attribution`｜前女友同时与多人交往的数字、时间和人物关系是否听写正确？｜affected=`mikey-youtube-live-008-E0002`｜status=`open`
- `mikey-youtube-live-008-R006`｜`major`｜`dating_result_numbers`｜多个号码、约出与关系升级的结果数字是否准确？｜affected=`mikey-youtube-live-008-E0011`｜status=`open`
- `mikey-youtube-live-008-R007`｜`blocking`｜`degrading_language`｜让疑似照骗对象离开时的侮辱性措辞和完整上下文是什么？｜affected=`mikey-youtube-live-008-E0014`｜status=`open`
- `mikey-youtube-live-008-R008`｜`blocking`｜`relationship_and_power_boundary`｜女友支持外出认识女性、老师学生互动的年龄、身份和权力关系是否清楚？｜affected=`mikey-youtube-live-008-E0015`｜status=`open`
- `mikey-youtube-live-008-R010`｜`blocking`｜`health_and_age_claim`｜身体虚、45岁、健身、补品与性能力说法是否只是口头经验？｜affected=`mikey-youtube-live-008-E0017`｜status=`open`
- `mikey-youtube-live-008-R011`｜`blocking`｜`first_escalation_consent`｜第一次关系升级、弱意图及用借口回家的描述是否保持双方自愿？｜affected=`mikey-youtube-live-008-E0021`｜status=`open`
- `mikey-youtube-live-008-R014`｜`blocking`｜`law_privacy_and_age`｜反跟踪法、偷拍消音、初中或全校追人等段落的法律、隐私和当时年龄是否清楚？｜affected=`mikey-youtube-live-008-E0026`｜status=`open`
- `mikey-youtube-live-008-R020`｜`major`｜`timing_and_interest_metrics`｜20分钟关系升级、米斯特里四小时规则和Kino指标的数字及否定词是否准确？｜affected=`mikey-youtube-live-008-E0033`, `mikey-youtube-live-008-E0034`｜status=`open`
- `mikey-youtube-live-008-R021`｜`major`｜`family_story_causality`｜父亲严厉甚至打骂与察言观色能力之间的因果是否只是个人回顾？｜affected=`mikey-youtube-live-008-E0035`｜status=`open`
- `mikey-youtube-live-009-RN001`｜`blocking`｜`亲密关系自报与未来私宅邀约`｜当晚性行为和次日约到家中的自述是否准确，未来安排是否被误作已经同意？｜affected=`mikey-youtube-live-009-E0001`｜status=`open`
- `mikey-youtube-live-009-RN002`｜`blocking`｜`搭讪与性结果叙事`｜把街头认识与发生性关系连接的表述是否遗漏持续同意边界？｜affected=`mikey-youtube-live-009-E0001`, `mikey-youtube-live-009-E0003`｜status=`open`
- `mikey-youtube-live-009-RN011`｜`blocking`｜`社交局、短期关系与性结果`｜NPC故事、性结果和‘女生都喜欢我’自报是否准确？｜affected=`mikey-youtube-live-009-E0021`, `mikey-youtube-live-009-E0022`｜status=`open`
- `mikey-youtube-live-010-RN002`｜`major`｜`长期关系中同时接触多人`｜所谓转盘子建议是否忽略现有伴侣的知情与关系约定？｜affected=`mikey-youtube-live-010-E0001`, `mikey-youtube-live-010-E0002`, `mikey-youtube-live-010-K0001`, `mikey-youtube-live-010-K0002`, `mikey-youtube-live-010-K0003`, `mikey-youtube-live-010-K0004`｜status=`open`
- `mikey-youtube-live-010-RN003`｜`major`｜`有伴侣女性留后路概括`｜把废号解释为有男友女性寻求认同是否只是推测？｜affected=`mikey-youtube-live-010-E0002`, `mikey-youtube-live-010-E0003`, `mikey-youtube-live-010-K0002`, `mikey-youtube-live-010-K0003`, `mikey-youtube-live-010-K0004`, `mikey-youtube-live-010-K0005`｜status=`open`
- `mikey-youtube-live-010-RN007`｜`blocking`｜`少说话速推性结果`｜不说话后带回家发生关系的自报是否遗漏同意、饮酒和过程边界？｜affected=`mikey-youtube-live-010-E0008`, `mikey-youtube-live-010-E0009`, `mikey-youtube-live-010-K0011`, `mikey-youtube-live-010-K0012`, `mikey-youtube-live-010-K0013`, `mikey-youtube-live-010-K0014`｜status=`open`
- `mikey-youtube-live-010-RN009`｜`blocking`｜`边界后性结果自报`｜让对方回去后又称发生性关系，是否会把结果当边界正确的证明？｜affected=`mikey-youtube-live-010-E0010`, `mikey-youtube-live-010-E0012`, `mikey-youtube-live-010-K0015`, `mikey-youtube-live-010-K0016`, `mikey-youtube-live-010-K0018`｜status=`open`
- `mikey-youtube-live-010-RN018`｜`blocking`｜`未成年性经历自报`｜自述未成年与成年女性的首次性经历是否准确，是否涉及法定同意问题？｜affected=`mikey-youtube-live-010-E0023`, `mikey-youtube-live-010-E0025`, `mikey-youtube-live-010-K0032`, `mikey-youtube-live-010-K0033`, `mikey-youtube-live-010-K0034`｜status=`open`

### law_privacy_and_filming（8项）

- `mikey-youtube-live-001-R002`｜`blocking`｜`consent_legal_claim`｜‘没有法律风险’与‘说no就停’的原话、语境和说话人是否准确？｜affected=`mikey-youtube-live-001-E0006`｜status=`open`
- `mikey-youtube-live-002-R014`｜`blocking`｜`legal_and_consent_claim`｜录音、报警、拘留等法律判断是否准确，是否会把录音误当成同意？｜affected=`mikey-youtube-live-002-E0056`, `mikey-youtube-live-002-K032`｜status=`open`
- `mikey-youtube-live-002-R022`｜`blocking`｜`unsafe_sex_and_alcohol`｜桥洞/楼道/天台、酒精合理化和‘不记得’案例是否涉及违法、不安全或无法同意？｜affected=`mikey-youtube-live-002-E0072`｜status=`open`
- `mikey-youtube-live-003-R007`｜`blocking`｜`violence_legal_claim`｜搭讪有伴侣女性、挑衅、打架、逃跑和警察相关言论的原话及语境是否完整？｜affected=`mikey-youtube-live-003-E0011`, `mikey-youtube-live-003-E0012`｜status=`open`
- `mikey-youtube-live-004-RN006`｜`major`｜`隐私与亲密关系`｜手机隐私、官宣和亲密关系顾虑的原话是否完整？｜affected=`mikey-youtube-live-004-E0010`, `mikey-youtube-live-004-E0011`｜status=`open`
- `mikey-youtube-live-008-R004`｜`blocking`｜`copyright_and_illegal_method`｜外挂、刷级和盗版课程故事的行为边界是否完整，是否会被误解为操作建议？｜affected=`mikey-youtube-live-008-E0007`｜status=`open`
- `mikey-youtube-live-008-R014`｜`blocking`｜`law_privacy_and_age`｜反跟踪法、偷拍消音、初中或全校追人等段落的法律、隐私和当时年龄是否清楚？｜affected=`mikey-youtube-live-008-E0026`｜status=`open`
- `mikey-youtube-live-008-R018`｜`blocking`｜`filming_consent`｜海外街拍、询问拍摄同意和发布消音的流程是否符合法律与隐私要求？｜affected=`mikey-youtube-live-008-E0032`｜status=`open`

### medical_body_and_mental_health（21项）

- `mikey-youtube-live-001-R006`｜`major`｜`visual_behavior_claim`｜所谓观察瞳孔/‘动漫眼’来判断施压的原词和含义是什么？｜affected=`mikey-youtube-live-001-E0013`, `mikey-youtube-live-001-K008`｜status=`open`
- `mikey-youtube-live-002-R012`｜`major`｜`psychology_claim`｜将对父亲恐惧推广为雄性恐惧来源是否仅为个人理论？｜affected=`mikey-youtube-live-002-E0051`, `mikey-youtube-live-002-K029`｜status=`open`
- `mikey-youtube-live-002-R015`｜`blocking`｜`medical_claim`｜‘戴避孕套不可能得HIV’的绝对说法需如何纠错和隔离？｜affected=`mikey-youtube-live-002-E0056`, `mikey-youtube-live-002-K033`｜status=`open`
- `mikey-youtube-live-003-R004`｜`blocking`｜`consent_escalation`｜私人影院的施压/减压、身体接触和对方口头拒绝相关语句是否完整、归属正确，且未越过同意边界？｜affected=`mikey-youtube-live-003-E0005`, `mikey-youtube-live-003-E0006`, `mikey-youtube-live-003-E0007`, `mikey-youtube-live-003-E0008`｜status=`open`
- `mikey-youtube-live-005-R003`｜`blocking`｜`sexual_health_claim`｜‘时间短就是太紧张’是否只是简化口头回答，不应当成医疗结论？｜affected=`mikey-youtube-live-005-E0004`｜status=`open`
- `mikey-youtube-live-005-R011`｜`major`｜`anxiety_and_trauma`｜幼年表白被嘲笑的案例是Mikey的概括性举例还是具体学员事实？｜affected=`mikey-youtube-live-005-E0017`｜status=`open`
- `mikey-youtube-live-006-RN002`｜`blocking`｜`亲密拒绝与ASD标签`｜‘不能强上’后的原因分析是否会把拒绝重新解释成可继续推进？｜affected=`mikey-youtube-live-006-E0005`, `mikey-youtube-live-006-E0006`｜status=`open`
- `mikey-youtube-live-007-R004`｜`major`｜`childhood_psychology_generalization`｜童年打压、自信底色和解除限制是否只是Mikey解释框架？｜affected=`mikey-youtube-live-007-E0006`｜status=`open`
- `mikey-youtube-live-007-R006`｜`blocking`｜`mental_health_term`｜‘自恋’及挑战无帮助是否涉及心理健康概念误用？｜affected=`mikey-youtube-live-007-E0009`｜status=`open`
- `mikey-youtube-live-007-R007`｜`major`｜`acceptance_psychology`｜接纳失败的关键词是否准确，ASR‘艰难’是否为‘接纳’？｜affected=`mikey-youtube-live-007-E0010`｜status=`open`
- `mikey-youtube-live-007-R026`｜`major`｜`height_and_shoes`｜身高重要、鞋垫与本人176等数字是否准确且不可普遍化？｜affected=`mikey-youtube-live-007-E0037`, `mikey-youtube-live-007-E0040`｜status=`open`
- `mikey-youtube-live-008-R010`｜`blocking`｜`health_and_age_claim`｜身体虚、45岁、健身、补品与性能力说法是否只是口头经验？｜affected=`mikey-youtube-live-008-E0017`｜status=`open`
- `mikey-youtube-live-008-R015`｜`blocking`｜`mental_health_and_safety`｜地雷女、自残割腕、带回家后逃跑等案例的归属和安全处置是否完整？｜affected=`mikey-youtube-live-008-E0027`｜status=`open`
- `mikey-youtube-live-008-R016`｜`blocking`｜`one_bed_consent`｜只有一张床时‘不要解释’的完整表述是否会弱化对方同意？｜affected=`mikey-youtube-live-008-E0027`｜status=`open`
- `mikey-youtube-live-008-R017`｜`major`｜`success_rate_and_body_rhetoric`｜70%成功率、肥胖和远古部落等数字或修辞是否准确？｜affected=`mikey-youtube-live-008-E0031`｜status=`open`
- `mikey-youtube-live-008-R019`｜`major`｜`voice_training_claim`｜每天开窗大吼21天的训练建议、数字和潜在风险是否准确？｜affected=`mikey-youtube-live-008-E0033`｜status=`open`
- `mikey-youtube-live-009-RN013`｜`major`｜`性与戒色绝对化`｜将性列为人生三分之一、把戒色社群称邪教是否为修辞观点？｜affected=`mikey-youtube-live-009-E0025`, `mikey-youtube-live-009-E0026`｜status=`open`
- `mikey-youtube-live-010-RN001`｜`blocking`｜`三秒原则与肢体行动`｜三秒原则是否被用于未经确认的牵手等肢体行为？｜affected=`mikey-youtube-live-010-E0001`, `mikey-youtube-live-010-K0001`, `mikey-youtube-live-010-K0002`｜status=`open`
- `mikey-youtube-live-010-RN005`｜`blocking`｜`健康风险与女性标签`｜避孕、药物、朋友圈标签等是否被误作判断性健康结论？｜affected=`mikey-youtube-live-010-E0007`, `mikey-youtube-live-010-K0009`, `mikey-youtube-live-010-K0010`, `mikey-youtube-live-010-K0011`｜status=`open`
- `mikey-youtube-live-010-RN014`｜`major`｜`忘掉过去与创伤`｜‘直接忘掉过去’是否可能否定真实创伤及专业支持需要？｜affected=`mikey-youtube-live-010-E0018`, `mikey-youtube-live-010-K0024`, `mikey-youtube-live-010-K0025`｜status=`open`
- `mikey-youtube-live-010-RN015`｜`major`｜`瞳孔判断吸引`｜仅凭瞳孔放大判断吸引是否可靠？｜affected=`mikey-youtube-live-010-E0019`, `mikey-youtube-live-010-K0026`, `mikey-youtube-live-010-K0027`, `mikey-youtube-live-010-K0028`｜status=`open`

### numbers_success_rates_and_outcomes（41项）

- `mikey-youtube-live-001-R007`｜`major`｜`numeric_claim`｜表沟通6%、潜沟通94%的数字是否准确、是否仅为修辞？｜affected=`mikey-youtube-live-001-E0015`, `mikey-youtube-live-001-K011`｜status=`open`
- `mikey-youtube-live-001-R008`｜`major`｜`numeric_claim`｜红黄绿灯、20/100或10%等概率表达是否准确且有定义？｜affected=`mikey-youtube-live-001-E0017`, `mikey-youtube-live-001-K015`｜status=`open`
- `mikey-youtube-live-001-R013`｜`major`｜`numeric_claim`｜一天100次、两三个号码的自述数字是否听写准确？｜affected=`mikey-youtube-live-001-E0029`, `mikey-youtube-live-001-K025`｜status=`open`
- `mikey-youtube-live-002-R010`｜`major`｜`numeric_claim`｜绿灯比例、十次出手和约会/结果数字是否为准确原话且是否仅是举例？｜affected=`mikey-youtube-live-002-E0048`, `mikey-youtube-live-002-K027`｜status=`open`
- `mikey-youtube-live-002-R011`｜`major`｜`numeric_and_location_claim`｜无锡六七十人、城市难易和GDP等数字/判断是否准确？｜affected=`mikey-youtube-live-002-E0050`｜status=`open`
- `mikey-youtube-live-002-R017`｜`major`｜`attributed_other`｜高收入女性案例哪些为群友经历，哪些为Mikey补充？｜affected=`mikey-youtube-live-002-E0062`, `mikey-youtube-live-002-K037`｜status=`open`
- `mikey-youtube-live-002-R019`｜`blocking`｜`case_outcome_and_consent`｜成都外卖到家案例的消息顺序、考虑、叫车、见面动作、同意与结果是否准确？｜affected=`mikey-youtube-live-002-E0066`, `mikey-youtube-live-002-K039`, `mikey-youtube-live-002-K040`｜status=`open`
- `mikey-youtube-live-002-R020`｜`major`｜`numeric_claim`｜不到五小时、时间点和案例结果是否准确？｜affected=`mikey-youtube-live-002-E0066`, `mikey-youtube-live-002-K040`｜status=`open`
- `mikey-youtube-live-003-R002`｜`major`｜`asr_case_result`｜童年牙齿创伤案例和‘新手知道搭讪后成功’案例的关键细节与结果是否听写正确？｜affected=`mikey-youtube-live-003-E0002`｜status=`open`
- `mikey-youtube-live-003-R003`｜`blocking`｜`consent_and_result`｜保守女性约会中的肢体接触、拒绝、私密空间与结果的叙述顺序是否准确？｜affected=`mikey-youtube-live-003-E0003`｜status=`open`
- `mikey-youtube-live-003-R005`｜`major`｜`numeric_claim`｜‘一周12场约会、7个结果’等数字和归属是否正确？｜affected=`mikey-youtube-live-003-E0005`｜status=`open`
- `mikey-youtube-live-003-R006`｜`major`｜`third_party_story`｜天津群友酒局故事中摸陌生人、跑单、金额和结果的实际说话人和事实是否准确？｜affected=`mikey-youtube-live-003-E0010`｜status=`open`
- `mikey-youtube-live-003-R012`｜`major`｜`numeric_claim`｜一小时收20-30个号、排12场约会等数字是否听写正确，且只是Mikey自报？｜affected=`mikey-youtube-live-003-E0023`｜status=`open`
- `mikey-youtube-live-003-R013`｜`major`｜`third_party_anecdote`｜年长女性搭讪案例中亲吻、伴侣出现和跑开的叙述是否准确？｜affected=`mikey-youtube-live-003-E0024`｜status=`open`
- `mikey-youtube-live-003-R014`｜`blocking`｜`accident_financial_result`｜意大利车祸案例中谁开车、责任、保险比例、金额和亲密升级结果是否准确？｜affected=`mikey-youtube-live-003-E0026`｜status=`open`
- `mikey-youtube-live-004-RN001`｜`major`｜`城市成功率与结果数字`｜长沙和北京的成功率、TD数字及归因是否听写正确？｜affected=`mikey-youtube-live-004-E0001`｜status=`open`
- `mikey-youtube-live-004-RN004`｜`blocking`｜`私密空间与结果`｜私人影院、去家里、游客短期物流及一小时结果的原话与边界是否准确？｜affected=`mikey-youtube-live-004-E0004`, `mikey-youtube-live-004-E0006`｜status=`open`
- `mikey-youtube-live-005-R004`｜`major`｜`numeric_result`｜学员‘一周4个’等结果数字是否听写正确，且仅是Mikey自报？｜affected=`mikey-youtube-live-005-E0005`｜status=`open`
- `mikey-youtube-live-005-R008`｜`major`｜`bar_kiss_result`｜酒吧接吻案例中的数字、注意力和结果判断是否准确？｜affected=`mikey-youtube-live-005-E0011`｜status=`open`
- `mikey-youtube-live-005-R009`｜`major`｜`numeric_claim`｜‘第一二次就够热身’与当天‘打几个成功几个’是否听写正确？｜affected=`mikey-youtube-live-005-E0013`｜status=`open`
- `mikey-youtube-live-007-R002`｜`major`｜`platform_strike_number`｜YouTube红标数量和账号处罚词是否听写正确？｜affected=`mikey-youtube-live-007-E0001`｜status=`open`
- `mikey-youtube-live-007-R008`｜`major`｜`result_causality`｜‘不在乎所以结果很好’的因果和程度词是否准确？｜affected=`mikey-youtube-live-007-E0013`｜status=`open`
- `mikey-youtube-live-007-R011`｜`major`｜`historic_and_result_numbers`｜十年前圈子及新手结果标准是否准确？｜affected=`mikey-youtube-live-007-E0018`｜status=`open`
- `mikey-youtube-live-007-R012`｜`major`｜`date_cost_numbers`｜20/30/40元与搭8收4等数字是否准确且仅属个例？｜affected=`mikey-youtube-live-007-E0019`｜status=`open`
- `mikey-youtube-live-007-R013`｜`blocking`｜`sex_difference_numbers`｜男人10秒、女人半小时/一小时的说法是否准确且不得泛化？｜affected=`mikey-youtube-live-007-E0021`｜status=`open`
- `mikey-youtube-live-007-R016`｜`blocking`｜`meditation_success_rate`｜冥想提高约会成功率的强因果是否有依据？｜affected=`mikey-youtube-live-007-E0027`｜status=`open`
- `mikey-youtube-live-007-R023`｜`blocking`｜`viewer_count_percentage`｜127人、90%写不出优点等数字是否准确且仅为即兴估计？｜affected=`mikey-youtube-live-007-E0033`｜status=`open`
- `mikey-youtube-live-007-R026`｜`major`｜`height_and_shoes`｜身高重要、鞋垫与本人176等数字是否准确且不可普遍化？｜affected=`mikey-youtube-live-007-E0037`, `mikey-youtube-live-007-E0040`｜status=`open`
- `mikey-youtube-live-008-R002`｜`major`｜`relationship_story_attribution`｜前女友同时与多人交往的数字、时间和人物关系是否听写正确？｜affected=`mikey-youtube-live-008-E0002`｜status=`open`
- `mikey-youtube-live-008-R003`｜`major`｜`numeric_results`｜新手失败次数、所谓百人斩学员等数字是否准确且仅属自报案例？｜affected=`mikey-youtube-live-008-E0003`｜status=`open`
- `mikey-youtube-live-008-R005`｜`major`｜`income_and_timeline_numbers`｜三个月从3000到8K或14K等收入和学习周期是否准确？｜affected=`mikey-youtube-live-008-E0008`｜status=`open`
- `mikey-youtube-live-008-R006`｜`major`｜`dating_result_numbers`｜多个号码、约出与关系升级的结果数字是否准确？｜affected=`mikey-youtube-live-008-E0011`｜status=`open`
- `mikey-youtube-live-008-R017`｜`major`｜`success_rate_and_body_rhetoric`｜70%成功率、肥胖和远古部落等数字或修辞是否准确？｜affected=`mikey-youtube-live-008-E0031`｜status=`open`
- `mikey-youtube-live-008-R019`｜`major`｜`voice_training_claim`｜每天开窗大吼21天的训练建议、数字和潜在风险是否准确？｜affected=`mikey-youtube-live-008-E0033`｜status=`open`
- `mikey-youtube-live-008-R020`｜`major`｜`timing_and_interest_metrics`｜20分钟关系升级、米斯特里四小时规则和Kino指标的数字及否定词是否准确？｜affected=`mikey-youtube-live-008-E0033`, `mikey-youtube-live-008-E0034`｜status=`open`
- `mikey-youtube-live-009-RN001`｜`blocking`｜`亲密关系自报与未来私宅邀约`｜当晚性行为和次日约到家中的自述是否准确，未来安排是否被误作已经同意？｜affected=`mikey-youtube-live-009-E0001`｜status=`open`
- `mikey-youtube-live-009-RN002`｜`blocking`｜`搭讪与性结果叙事`｜把街头认识与发生性关系连接的表述是否遗漏持续同意边界？｜affected=`mikey-youtube-live-009-E0001`, `mikey-youtube-live-009-E0003`｜status=`open`
- `mikey-youtube-live-009-RN008`｜`major`｜`得号概率与需求感进攻`｜70%–80%自报比例及命令式牵手示范是否准确？｜affected=`mikey-youtube-live-009-E0019`｜status=`open`
- `mikey-youtube-live-009-RN011`｜`blocking`｜`社交局、短期关系与性结果`｜NPC故事、性结果和‘女生都喜欢我’自报是否准确？｜affected=`mikey-youtube-live-009-E0021`, `mikey-youtube-live-009-E0022`｜status=`open`
- `mikey-youtube-live-010-RN007`｜`blocking`｜`少说话速推性结果`｜不说话后带回家发生关系的自报是否遗漏同意、饮酒和过程边界？｜affected=`mikey-youtube-live-010-E0008`, `mikey-youtube-live-010-E0009`, `mikey-youtube-live-010-K0011`, `mikey-youtube-live-010-K0012`, `mikey-youtube-live-010-K0013`, `mikey-youtube-live-010-K0014`｜status=`open`
- `mikey-youtube-live-010-RN009`｜`blocking`｜`边界后性结果自报`｜让对方回去后又称发生性关系，是否会把结果当边界正确的证明？｜affected=`mikey-youtube-live-010-E0010`, `mikey-youtube-live-010-E0012`, `mikey-youtube-live-010-K0015`, `mikey-youtube-live-010-K0016`, `mikey-youtube-live-010-K0018`｜status=`open`

### screen_material_hard_cuts_and_replays（14项）

- `mikey-youtube-live-001-R001`｜`blocking`｜`speaker_attribution`｜开场龙哥案例、Mikey插话和疑似剪辑旁白的逐句归属是否正确？｜affected=`mikey-youtube-live-001-E0001`, `mikey-youtube-live-001-E0002`, `mikey-youtube-live-001-E0003`, `mikey-youtube-live-001-E0004`, `mikey-youtube-live-001-E0005`, `mikey-youtube-live-001-E0006`｜status=`open`
- `mikey-youtube-live-001-R006`｜`major`｜`visual_behavior_claim`｜所谓观察瞳孔/‘动漫眼’来判断施压的原词和含义是什么？｜affected=`mikey-youtube-live-001-E0013`, `mikey-youtube-live-001-K008`｜status=`open`
- `mikey-youtube-live-001-R015`｜`major`｜`visual_scope`｜左侧直播评论是否包含改变问题语义或答案对象的文字？｜affected=`mikey-youtube-live-001-E0001`, `mikey-youtube-live-001-E0006`, `mikey-youtube-live-001-E0011`, `mikey-youtube-live-001-E0017`, `mikey-youtube-live-001-E0021`, `mikey-youtube-live-001-E0022`, `mikey-youtube-live-001-E0028`, `mikey-youtube-live-001-E0029`, `mikey-youtube-live-001-E0031`｜status=`open`
- `mikey-youtube-live-002-R024`｜`major`｜`visual_scope`｜左侧直播评论、腾讯会议头像/高亮和参与者列表是否包含改变问题作者或说话人的信息？｜affected=`mikey-youtube-live-002-E0001`, `mikey-youtube-live-002-E0006`, `mikey-youtube-live-002-E0033`, `mikey-youtube-live-002-E0034`, `mikey-youtube-live-002-E0065`, `mikey-youtube-live-002-E0075`｜status=`open`
- `mikey-youtube-live-003-R011`｜`major`｜`screen_material`｜展示的聊天截图、消息顺序、对方回复和Mikey口述是否一致？｜affected=`mikey-youtube-live-003-E0021`, `mikey-youtube-live-003-E0022`｜status=`open`
- `mikey-youtube-live-004-RN007`｜`blocking`｜`肢体升级系统`｜线下预期、牵手和关系升级的建议是否完整保留对方意愿？｜affected=`mikey-youtube-live-004-E0011`, `mikey-youtube-live-004-E0013`｜status=`open`
- `mikey-youtube-live-004-RN013`｜`major`｜`未通过好友后再次接近`｜再次上前询问的原话、场景和骚扰边界是否完整？｜affected=`mikey-youtube-live-004-E0029`｜status=`open`
- `mikey-youtube-live-005-R006`｜`major`｜`screen_board`｜白板/手绘图是否承载了松弛感示范的补充信息？｜affected=`mikey-youtube-live-005-E0008`｜status=`open`
- `mikey-youtube-live-006-RN005`｜`major`｜`音频空段与即时邀约`｜1244秒和1769秒后的长空段是否为静音/读取消息，问答边界是否被截断？｜affected=`mikey-youtube-live-006-E0012`, `mikey-youtube-live-006-E0014`｜status=`open`
- `mikey-youtube-live-006-RN011`｜`blocking`｜`ASR跨离席静音合并`｜S01567把哪些离席前后话语拼接，实际静音范围和句子时间如何划分？｜affected=`mikey-youtube-live-006-E0027`, `mikey-youtube-live-006-E0028`｜status=`open`
- `mikey-youtube-live-007-R001`｜`major`｜`speaker_and_question_boundary`｜全期是否只有Mikey口播，每个屏幕问题的作者、代读起止和回答边界是否准确？｜affected=`mikey-youtube-live-007-E0001`, `mikey-youtube-live-007-E0002`, `mikey-youtube-live-007-E0003`, `mikey-youtube-live-007-E0004`, `mikey-youtube-live-007-E0005`, `mikey-youtube-live-007-E0006`, `mikey-youtube-live-007-E0007`, `mikey-youtube-live-007-E0008`, `mikey-youtube-live-007-E0009`, `mikey-youtube-live-007-E0010`, `mikey-youtube-live-007-E0011`, `mikey-youtube-live-007-E0012`, `mikey-youtube-live-007-E0013`, `mikey-youtube-live-007-E0014`, `mikey-youtube-live-007-E0015`, `mikey-youtube-live-007-E0016`, `mikey-youtube-live-007-E0017`, `mikey-youtube-live-007-E0018`, `mikey-youtube-live-007-E0019`, `mikey-youtube-live-007-E0020`, `mikey-youtube-live-007-E0021`, `mikey-youtube-live-007-E0022`, `mikey-youtube-live-007-E0023`, `mikey-youtube-live-007-E0024`, `mikey-youtube-live-007-E0025`, `mikey-youtube-live-007-E0026`, `mikey-youtube-live-007-E0027`, `mikey-youtube-live-007-E0028`, `mikey-youtube-live-007-E0029`, `mikey-youtube-live-007-E0030`, `mikey-youtube-live-007-E0031`, `mikey-youtube-live-007-E0032`, `mikey-youtube-live-007-E0033`, `mikey-youtube-live-007-E0034`, `mikey-youtube-live-007-E0035`, `mikey-youtube-live-007-E0036`, `mikey-youtube-live-007-E0037`, `mikey-youtube-live-007-E0038`, `mikey-youtube-live-007-E0039`, `mikey-youtube-live-007-E0040`｜status=`open`
- `mikey-youtube-live-007-R023`｜`blocking`｜`viewer_count_percentage`｜127人、90%写不出优点等数字是否准确且仅为即兴估计？｜affected=`mikey-youtube-live-007-E0033`｜status=`open`
- `mikey-youtube-live-007-R027`｜`major`｜`continuous_edit_and_audio_gaps`｜多处长停顿是读评论、静音、断流还是剪辑？｜affected=`mikey-youtube-live-007-E0001`, `mikey-youtube-live-007-E0002`, `mikey-youtube-live-007-E0003`, `mikey-youtube-live-007-E0004`, `mikey-youtube-live-007-E0005`, `mikey-youtube-live-007-E0006`, `mikey-youtube-live-007-E0007`, `mikey-youtube-live-007-E0008`, `mikey-youtube-live-007-E0009`, `mikey-youtube-live-007-E0010`, `mikey-youtube-live-007-E0011`, `mikey-youtube-live-007-E0012`, `mikey-youtube-live-007-E0013`, `mikey-youtube-live-007-E0014`, `mikey-youtube-live-007-E0015`, `mikey-youtube-live-007-E0016`, `mikey-youtube-live-007-E0017`, `mikey-youtube-live-007-E0018`, `mikey-youtube-live-007-E0019`, `mikey-youtube-live-007-E0020`, `mikey-youtube-live-007-E0021`, `mikey-youtube-live-007-E0022`, `mikey-youtube-live-007-E0023`, `mikey-youtube-live-007-E0024`, `mikey-youtube-live-007-E0025`, `mikey-youtube-live-007-E0026`, `mikey-youtube-live-007-E0027`, `mikey-youtube-live-007-E0028`, `mikey-youtube-live-007-E0029`, `mikey-youtube-live-007-E0030`, `mikey-youtube-live-007-E0031`, `mikey-youtube-live-007-E0032`, `mikey-youtube-live-007-E0033`, `mikey-youtube-live-007-E0034`, `mikey-youtube-live-007-E0035`, `mikey-youtube-live-007-E0036`, `mikey-youtube-live-007-E0037`, `mikey-youtube-live-007-E0038`, `mikey-youtube-live-007-E0039`, `mikey-youtube-live-007-E0040`｜status=`open`
- `mikey-youtube-live-008-R018`｜`blocking`｜`filming_consent`｜海外街拍、询问拍摄同意和发布消音的流程是否符合法律与隐私要求？｜affected=`mikey-youtube-live-008-E0032`｜status=`open`

## 待本地解决的 open blocking

- `mikey-youtube-live-001-R001`｜`mikey-youtube-live-001`｜`speaker_attribution`｜开场龙哥案例、Mikey插话和疑似剪辑旁白的逐句归属是否正确？｜需要：连续音画、声纹参照片段和直播原始声道
- `mikey-youtube-live-001-R002`｜`mikey-youtube-live-001`｜`consent_legal_claim`｜‘没有法律风险’与‘说no就停’的原话、语境和说话人是否准确？｜需要：逐句听校及必要的法律专业审查；不能把直播口头判断当法律意见
- `mikey-youtube-live-001-R004`｜`mikey-youtube-live-001`｜`sexual_advice_boundary`｜眼神想象、明示内容及所谓‘授权’是否可能被误读为无视对方同意？｜需要：连续语境听校并与明确同意边界联读
- `mikey-youtube-live-001-R011`｜`mikey-youtube-live-001`｜`relationship_ethics`｜来电案例中是否存在先前明确拒绝、欺骗、羞辱或其他会改变伦理判断的细节？｜需要：完整连续音画和案例当事人原始叙述
- `mikey-youtube-live-001-R014`｜`mikey-youtube-live-001`｜`physical_escalation`｜肢体升级被拒绝后的建议是否明确要求尊重拒绝，是否存在会鼓励重复越界的表述？｜需要：连续音画、原词听校和安全边界审查
- `mikey-youtube-live-002-R001`｜`mikey-youtube-live-002`｜`speaker_attribution`｜开场主持、群友、观众代读和短插话的逐句边界是否正确？｜需要：连续音画、声纹参照和直播原声
- `mikey-youtube-live-002-R003`｜`mikey-youtube-live-002`｜`sexual_advice_boundary`｜性化眼神想象与性氛围段落如何与明确同意和舒适边界联读？｜需要：逐句听校、上下文与安全边界审查
- `mikey-youtube-live-002-R005`｜`mikey-youtube-live-002`｜`consent_and_deception`｜酒店与短期关系案例是否存在未保留的拒绝、欺骗或持续同意细节？｜需要：完整连续音画、原词听校和同意边界审查
- `mikey-youtube-live-002-R006`｜`mikey-youtube-live-002`｜`speaker_attribution`｜主持离席期间究竟有几名群友，挑战和打枪建议分别由谁说？｜需要：声纹聚类加稳定参照片段
- `mikey-youtube-live-002-R013`｜`mikey-youtube-live-002`｜`relationship_ethics`｜建议对在意的长期伴侣隐瞒短期关系是否应隔离为不可推广内容？｜需要：伦理审查与跨期冲突核对
- `mikey-youtube-live-002-R014`｜`mikey-youtube-live-002`｜`legal_and_consent_claim`｜录音、报警、拘留等法律判断是否准确，是否会把录音误当成同意？｜需要：原词听校、中国法律专业审查、同意边界审查
- `mikey-youtube-live-002-R015`｜`mikey-youtube-live-002`｜`medical_claim`｜‘戴避孕套不可能得HIV’的绝对说法需如何纠错和隔离？｜需要：医学权威资料核查；不得作为健康建议
- `mikey-youtube-live-002-R018`｜`mikey-youtube-live-002`｜`consent_boundary`｜第二次约会才同意是否被错误解释为第一次拒绝可忽略？｜需要：逐句听校并明确每次拒绝均有效
- `mikey-youtube-live-002-R019`｜`mikey-youtube-live-002`｜`case_outcome_and_consent`｜成都外卖到家案例的消息顺序、考虑、叫车、见面动作、同意与结果是否准确？｜需要：连续音画、可能的聊天原图与原声听校
- `mikey-youtube-live-002-R021`｜`mikey-youtube-live-002`｜`sexual_escalation`｜酒店转场建议是否会鼓励规避拒绝或社会压力？｜需要：完整语境、同意边界和安全审查
- `mikey-youtube-live-002-R022`｜`mikey-youtube-live-002`｜`unsafe_sex_and_alcohol`｜桥洞/楼道/天台、酒精合理化和‘不记得’案例是否涉及违法、不安全或无法同意？｜需要：连续原声、同意能力与法律安全审查
- `mikey-youtube-live-003-R001`｜`mikey-youtube-live-003`｜`speaker_attribution`｜多人语音会议中Mikey、19个临时来电者编号及所有短插话的逐句归属是否正确？｜需要：连续音画、发言指示、稳定声纹参照和必要的嘴型对齐
- `mikey-youtube-live-003-R003`｜`mikey-youtube-live-003`｜`consent_and_result`｜保守女性约会中的肢体接触、拒绝、私密空间与结果的叙述顺序是否准确？｜需要：连续音画与原音，严格区分来电者案例和Mikey建议
- `mikey-youtube-live-003-R004`｜`mikey-youtube-live-003`｜`consent_escalation`｜私人影院的施压/减压、身体接触和对方口头拒绝相关语句是否完整、归属正确，且未越过同意边界？｜需要：原音听校、连续音画及同意边界专项审核
- `mikey-youtube-live-003-R007`｜`mikey-youtube-live-003`｜`violence_legal_claim`｜搭讪有伴侣女性、挑衅、打架、逃跑和警察相关言论的原话及语境是否完整？｜需要：原音听校、连续音画和独立法律/安全审核；保持do_not_generalize边界
- `mikey-youtube-live-003-R008`｜`mikey-youtube-live-003`｜`following_refusal`｜闺蜜拒绝、强制截停和跟随距离的归属与否定词是否准确？｜需要：原音听校和连续音画，确认建议是停止跟随
- `mikey-youtube-live-003-R009`｜`mikey-youtube-live-003`｜`consent_escalation`｜首次约会肢体接触、拒绝及‘只要不走’言论的原话和上下文是否准确？｜需要：连续音画、原音听校和同意边界专项审核
- `mikey-youtube-live-003-R014`｜`mikey-youtube-live-003`｜`accident_financial_result`｜意大利车祸案例中谁开车、责任、保险比例、金额和亲密升级结果是否准确？｜需要：原音听校，区分来电者陈述与Mikey回答，必要时结合事故材料
- `mikey-youtube-live-003-R015`｜`mikey-youtube-live-003`｜`consent_and_relationship`｜车祸案例后续中‘不让去家里’、朋友框架、再见面和继续升级的归属是否正确？｜需要：连续音画、原音听校，对明确拒绝维持停止边界
- `mikey-youtube-live-004-RN002`｜`mikey-youtube-live-004`｜`关系承诺与同意`｜短期关系、是否成为男女朋友和停止推进的原话、否定词是否准确？｜需要：原音听校；分别记录承诺、当下同意和后续关系
- `mikey-youtube-live-004-RN003`｜`mikey-youtube-live-004`｜`肢体接触与拒绝`｜牵手被抽开后‘过一会再做’的具体条件是否包含明确再次同意？｜需要：连续音画与原音；拒绝后不得默认后续许可
- `mikey-youtube-live-004-RN004`｜`mikey-youtube-live-004`｜`私密空间与结果`｜私人影院、去家里、游客短期物流及一小时结果的原话与边界是否准确？｜需要：原音听校；地点不等于同意，结果保持第一人称自报
- `mikey-youtube-live-004-RN007`｜`mikey-youtube-live-004`｜`肢体升级系统`｜线下预期、牵手和关系升级的建议是否完整保留对方意愿？｜需要：原音和连续画面；不得把不离开等同同意
- `mikey-youtube-live-004-RN008`｜`mikey-youtube-live-004`｜`线上预期`｜线上询问能否牵手等话术是否被误读为预先取得后续同意？｜需要：原音听校；预期沟通不代替现场持续同意
- `mikey-youtube-live-004-RN010`｜`mikey-youtube-live-004`｜`性关系承诺`｜‘我睡了你就负责’限定为真想恋爱者的原话和否定词是否准确？｜需要：原音听校；承诺不能替代同意或被用于欺骗
- `mikey-youtube-live-004-RN011`｜`mikey-youtube-live-004`｜`拒绝后停止`｜被拒绝后停止跟随的原话是否准确，是否存在相反短句被ASR合并？｜需要：原音听校并保留停止边界
- `mikey-youtube-live-004-RN012`｜`mikey-youtube-live-004`｜`有男友对象与私人空间`｜将公共影院升级到私人影院/家中的建议是否保留对方选择和关系边界？｜需要：原音听校；不得提供规避同意或欺骗性操作
- `mikey-youtube-live-005-R003`｜`mikey-youtube-live-005`｜`sexual_health_claim`｜‘时间短就是太紧张’是否只是简化口头回答，不应当成医疗结论？｜需要：原音听校与医疗边界审查
- `mikey-youtube-live-005-R007`｜`mikey-youtube-live-005`｜`minor_age_context`｜‘漫展都是小孩’与搭讪建议的语境是否明确要求避开未成年人？｜需要：原音听校和年龄安全边界审核
- `mikey-youtube-live-005-R012`｜`mikey-youtube-live-005`｜`hotel_consent`｜‘陪我去酒店吃个药’与对方拒绝后的所谓操作是什么，是否清楚维持停止和同意边界？｜需要：原音听校与同意专项审核
- `mikey-youtube-live-005-R014`｜`mikey-youtube-live-005`｜`hotel_cancellation_claim`｜平台预订的取消时限、免责退款和钟点/过夜建议是否适用于具体订单？｜需要：原音听校并对实际酒店/平台规则单独核对
- `mikey-youtube-live-005-R015`｜`mikey-youtube-live-005`｜`age_deception`｜按对方喜好乱报年龄的言论是否完整，且不应升级为鼓励欺骗的建议？｜需要：原音听校，维持do_not_generalize边界
- `mikey-youtube-live-006-RN002`｜`mikey-youtube-live-006`｜`亲密拒绝与ASD标签`｜‘不能强上’后的原因分析是否会把拒绝重新解释成可继续推进？｜需要：原音与上下文；明确拒绝后停止，标签不能替代同意
- `mikey-youtube-live-006-RN004`｜`mikey-youtube-live-006`｜`夜场醉酒与闺蜜`｜醉酒、闺蜜被灌酒及无法离场的例子是否准确，是否涉及需要优先保障安全的情形？｜需要：原音听校；醉酒时不得推定同意
- `mikey-youtube-live-006-RN006`｜`mikey-youtube-live-006`｜`同时接触多人被发现`｜承认、合理化和‘推开’的建议是否可能被用于欺骗或规避责任？｜需要：听校原音；正式整合保留诚实与承担责任边界
- `mikey-youtube-live-006-RN007`｜`mikey-youtube-live-006`｜`假窗口与私密场所邀请`｜亲密接触、回家邀请被拒及所谓‘假窗口’的原话是否准确？｜需要：原音听校；既往接触不代表后续同意
- `mikey-youtube-live-006-RN011`｜`mikey-youtube-live-006`｜`ASR跨离席静音合并`｜S01567把哪些离席前后话语拼接，实际静音范围和句子时间如何划分？｜需要：视觉显示约54:07–55:52主持人离席；ffmpeg检测约3252.8–3350.9秒为98.1秒静音；需听校两端，禁止把148.8秒当连续发言
- `mikey-youtube-live-007-R006`｜`mikey-youtube-live-007`｜`mental_health_term`｜‘自恋’及挑战无帮助是否涉及心理健康概念误用？｜需要：原音听校与专业边界
- `mikey-youtube-live-007-R010`｜`mikey-youtube-live-007`｜`consent_words_actions`｜女性‘嘴上和行为不一致’是否会否定明确口头边界？｜需要：原音与同意边界专项审核
- `mikey-youtube-live-007-R013`｜`mikey-youtube-live-007`｜`sex_difference_numbers`｜男人10秒、女人半小时/一小时的说法是否准确且不得泛化？｜需要：原音听校，禁止泛化
- `mikey-youtube-live-007-R014`｜`mikey-youtube-live-007`｜`hotel_euphemism_consent`｜‘回酒店吃药’是否规避真实意图和知情同意？｜需要：原音与同意专项审核
- `mikey-youtube-live-007-R016`｜`mikey-youtube-live-007`｜`meditation_success_rate`｜冥想提高约会成功率的强因果是否有依据？｜需要：原音并降为个人体验
- `mikey-youtube-live-007-R018`｜`mikey-youtube-live-007`｜`garbled_case_asr`｜44-45分钟自动稿严重错乱，原问题与回答是什么？｜需要：原音逐句听校和评论原图
- `mikey-youtube-live-007-R023`｜`mikey-youtube-live-007`｜`viewer_count_percentage`｜127人、90%写不出优点等数字是否准确且仅为即兴估计？｜需要：原音和画面数字
- `mikey-youtube-live-007-R025`｜`mikey-youtube-live-007`｜`confidence_success_causality`｜先自信后有钱/有女人是否为修辞性主张？｜需要：原音并保持个人观点
- `mikey-youtube-live-008-R004`｜`mikey-youtube-live-008`｜`copyright_and_illegal_method`｜外挂、刷级和盗版课程故事的行为边界是否完整，是否会被误解为操作建议？｜需要：原音复核；仅保留问题解决结构，不传播违法侵权做法
- `mikey-youtube-live-008-R007`｜`mikey-youtube-live-008`｜`degrading_language`｜让疑似照骗对象离开时的侮辱性措辞和完整上下文是什么？｜需要：原音听校；禁止转化为羞辱建议
- `mikey-youtube-live-008-R008`｜`mikey-youtube-live-008`｜`relationship_and_power_boundary`｜女友支持外出认识女性、老师学生互动的年龄、身份和权力关系是否清楚？｜需要：原音与问题原文；核年龄、关系授权和权力差异
- `mikey-youtube-live-008-R009`｜`mikey-youtube-live-008`｜`location_and_consent`｜异地无住所时去楼道等转场说法是否维持明确同意和安全边界？｜需要：原音听校与同意、安全专项审核
- `mikey-youtube-live-008-R010`｜`mikey-youtube-live-008`｜`health_and_age_claim`｜身体虚、45岁、健身、补品与性能力说法是否只是口头经验？｜需要：原音听校；医疗和年龄结论不得直接发布
- `mikey-youtube-live-008-R011`｜`mikey-youtube-live-008`｜`first_escalation_consent`｜第一次关系升级、弱意图及用借口回家的描述是否保持双方自愿？｜需要：原音与连续上下文，同意专项审核
- `mikey-youtube-live-008-R012`｜`mikey-youtube-live-008`｜`sexual_anatomy_stereotype`｜性器官长度、族群差异等说法是否准确，如何避免医学误导和族群刻板印象？｜需要：原音听校并做医学与刻板印象审查
- `mikey-youtube-live-008-R013`｜`mikey-youtube-live-008`｜`regional_stereotypes`｜日本、韩国、新加坡、泰国及性别群体的概括是否仅是个人印象？｜需要：原音听校；全部保持do_not_generalize
- `mikey-youtube-live-008-R014`｜`mikey-youtube-live-008`｜`law_privacy_and_age`｜反跟踪法、偷拍消音、初中或全校追人等段落的法律、隐私和当时年龄是否清楚？｜需要：核当地法律、拍摄授权、隐私与年龄
- `mikey-youtube-live-008-R015`｜`mikey-youtube-live-008`｜`mental_health_and_safety`｜地雷女、自残割腕、带回家后逃跑等案例的归属和安全处置是否完整？｜需要：原音与连续音画；心理危机和人身安全专项审核
- `mikey-youtube-live-008-R016`｜`mikey-youtube-live-008`｜`one_bed_consent`｜只有一张床时‘不要解释’的完整表述是否会弱化对方同意？｜需要：原音复核；明确睡眠安排和任何身体接触都需同意
- `mikey-youtube-live-008-R018`｜`mikey-youtube-live-008`｜`filming_consent`｜海外街拍、询问拍摄同意和发布消音的流程是否符合法律与隐私要求？｜需要：原音、画面与当地规则专项审核
- `mikey-youtube-live-009-RN001`｜`mikey-youtube-live-009`｜`亲密关系自报与未来私宅邀约`｜当晚性行为和次日约到家中的自述是否准确，未来安排是否被误作已经同意？｜需要：原音听校；自报结果和未来计划不证明对方同意
- `mikey-youtube-live-009-RN002`｜`mikey-youtube-live-009`｜`搭讪与性结果叙事`｜把街头认识与发生性关系连接的表述是否遗漏持续同意边界？｜需要：原音听校；认识渠道不等于同意
- `mikey-youtube-live-009-RN004`｜`mikey-youtube-live-009`｜`旅馆转场与借口`｜‘回去吃药’是否是隐瞒真实意图的转场借口？｜需要：连续原音；不得提炼为欺骗性操作，私密场所必须明确自愿
- `mikey-youtube-live-009-RN006`｜`mikey-youtube-live-009`｜`直接牵手建议`｜‘直接牵手/把手给我’是否省略了确认意愿与被拒后停止？｜需要：连续音画与原音；不得把命令式动作当默认许可
- `mikey-youtube-live-009-RN009`｜`mikey-youtube-live-009`｜`女性话语无参考价值`｜‘80%–90%女性说的话无参考价值’及用案例推翻口头边界的原话是否准确？｜需要：听校并明确：口头拒绝和边界必须按字面尊重，不能用潜意识推测覆盖
- `mikey-youtube-live-009-RN010`｜`mikey-youtube-live-009`｜`真假拒绝与继续劝说`｜所谓矜持/假拒绝的判断是否会造成对明确拒绝继续施压？｜需要：原音听校；明确拒绝后停止
- `mikey-youtube-live-009-RN011`｜`mikey-youtube-live-009`｜`社交局、短期关系与性结果`｜NPC故事、性结果和‘女生都喜欢我’自报是否准确？｜需要：保持第一人称自报，不升级为普遍结果
- `mikey-youtube-live-010-RN001`｜`mikey-youtube-live-010`｜`三秒原则与肢体行动`｜三秒原则是否被用于未经确认的牵手等肢体行为？｜需要：只可用于克服自我拖延；涉及他人身体必须先确认意愿
- `mikey-youtube-live-010-RN005`｜`mikey-youtube-live-010`｜`健康风险与女性标签`｜避孕、药物、朋友圈标签等是否被误作判断性健康结论？｜需要：健康风险须基于检测和专业建议，不能靠标签推定
- `mikey-youtube-live-010-RN006`｜`mikey-youtube-live-010`｜`搭讪短暂跟随`｜‘跟五步/五米’是否可能覆盖对方持续不愿停下的拒绝？｜需要：对方不停或拒绝即停止，不得跟随施压
- `mikey-youtube-live-010-RN007`｜`mikey-youtube-live-010`｜`少说话速推性结果`｜不说话后带回家发生关系的自报是否遗漏同意、饮酒和过程边界？｜需要：保持第一人称自报；连续同意与饮酒能力需独立确认
- `mikey-youtube-live-010-RN009`｜`mikey-youtube-live-010`｜`边界后性结果自报`｜让对方回去后又称发生性关系，是否会把结果当边界正确的证明？｜需要：结果自报不证明因果或同意
- `mikey-youtube-live-010-RN011`｜`mikey-youtube-live-010`｜`速推、随便与生理喜欢`｜如何回应进展过快后的失落，是否充分允许撤回和重新协商？｜需要：原音听校；社会评价不能替代持续同意
- `mikey-youtube-live-010-RN016`｜`mikey-youtube-live-010`｜`保守对象与直接回家/破釜沉舟`｜对所谓保守对象直接转场、无吸引仍尝试性推进是否覆盖拒绝？｜需要：明确同意优先；无吸引或拒绝应停止
- `mikey-youtube-live-010-RN017`｜`mikey-youtube-live-010`｜`不用疑问句`｜只说陈述句是否被误用于涉及对方的决定？｜需要：仅用于个人低风险选择；涉及对方必须询问并尊重no
- `mikey-youtube-live-010-RN018`｜`mikey-youtube-live-010`｜`未成年性经历自报`｜自述未成年与成年女性的首次性经历是否准确，是否涉及法定同意问题？｜需要：原音听校并保持历史自报；不得提炼为建议

## 完整 knowledge_index（266条，恰好一次）

| knowledge_id | source_id | theme_ids | proposition_ids | use_level | blocking_review_ids | use_reason |
|---|---|---|---|---|---|---|
| `mikey-youtube-live-001-K001` | `mikey-youtube-live-001` | `T10` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K002` | `mikey-youtube-live-001` | `T10` | `P12` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K003` | `mikey-youtube-live-001` | `T04`<br>`T06`<br>`T09` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-001-K004` | `mikey-youtube-live-001` | `T02` |  | `hold` | `mikey-youtube-live-001-R004` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-001-K005` | `mikey-youtube-live-001` | `T02`<br>`T04`<br>`T06` |  | `hold` | `mikey-youtube-live-001-R004` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-001-K006` | `mikey-youtube-live-001` | `T04`<br>`T07`<br>`T10` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K007` | `mikey-youtube-live-001` | `T02`<br>`T07` |  | `hold` |  | 新基线release_status=hold；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-001-K008` | `mikey-youtube-live-001` | `T06`<br>`T09`<br>`T10` |  | `hold` |  | 新基线release_status=hold；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-001-K009` | `mikey-youtube-live-001` | `T08`<br>`T13` | `P20` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K010` | `mikey-youtube-live-001` | `T01`<br>`T06` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K011` | `mikey-youtube-live-001` | `T02`<br>`T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-001-K012` | `mikey-youtube-live-001` | `T02`<br>`T04` | `P02` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-001-K013` | `mikey-youtube-live-001` | `T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K014` | `mikey-youtube-live-001` | `T06` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K015` | `mikey-youtube-live-001` | `T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-001-K016` | `mikey-youtube-live-001` | `T02`<br>`T03`<br>`T13` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-001-K017` | `mikey-youtube-live-001` | `T13` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-001-K018` | `mikey-youtube-live-001` | `T01`<br>`T02` | `P01` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-001-K019` | `mikey-youtube-live-001` | `T01`<br>`T10` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-001-K020` | `mikey-youtube-live-001` | `T01`<br>`T02`<br>`T08` | `P02` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K021` | `mikey-youtube-live-001` | `T08`<br>`T12` | `P18` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K022` | `mikey-youtube-live-001` | `T04` | `P03` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-001-K023` | `mikey-youtube-live-001` | `T09`<br>`T10` | `P17` | `hold` | `mikey-youtube-live-001-R011` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-001-K024` | `mikey-youtube-live-001` | `T06`<br>`T08`<br>`T10` |  | `hold` |  | 新基线release_status=hold；attribution_status=attributed_other；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-001-K025` | `mikey-youtube-live-001` | `T04`<br>`T07` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-001-K026` | `mikey-youtube-live-001` | `T08`<br>`T09` | `P15` | `hold` | `mikey-youtube-live-001-R014` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-001-K027` | `mikey-youtube-live-001` | `T04`<br>`T07`<br>`T10` | `P12` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K001` | `mikey-youtube-live-002` | `T01`<br>`T10`<br>`T12` |  | `hold` | `mikey-youtube-live-002-R001` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K002` | `mikey-youtube-live-002` | `T04`<br>`T07`<br>`T10` |  | `hold` | `mikey-youtube-live-002-R001` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K003` | `mikey-youtube-live-002` | `T01`<br>`T03`<br>`T07` | `P01` | `hold` | `mikey-youtube-live-002-R001` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K004` | `mikey-youtube-live-002` | `T08`<br>`T10`<br>`T11` | `P19` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K005` | `mikey-youtube-live-002` | `T04`<br>`T07`<br>`T08` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K006` | `mikey-youtube-live-002` | `T03`<br>`T10` |  | `hold` | `mikey-youtube-live-002-R003` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K007` | `mikey-youtube-live-002` | `T04`<br>`T06` |  | `hold` | `mikey-youtube-live-002-R003` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K008` | `mikey-youtube-live-002` | `T01`<br>`T02`<br>`T06` | `P02` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K009` | `mikey-youtube-live-002` | `T04` | `P17` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K010` | `mikey-youtube-live-002` | `T08`<br>`T09`<br>`T10` | `P11` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-002-K011` | `mikey-youtube-live-002` | `T04`<br>`T07`<br>`T11` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K012` | `mikey-youtube-live-002` | `T04`<br>`T06`<br>`T07` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K013` | `mikey-youtube-live-002` | `T04` | `P03` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K014` | `mikey-youtube-live-002` | `T08`<br>`T11`<br>`T12` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K015` | `mikey-youtube-live-002` | `T01`<br>`T06`<br>`T11` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K016` | `mikey-youtube-live-002` | `T02`<br>`T07` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K017` | `mikey-youtube-live-002` | `T01`<br>`T07` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K018` | `mikey-youtube-live-002` | `T08`<br>`T10`<br>`T13` |  | `hold` | `mikey-youtube-live-002-R005` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K019` | `mikey-youtube-live-002` | `T08`<br>`T09`<br>`T10` |  | `hold` | `mikey-youtube-live-002-R005` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K020` | `mikey-youtube-live-002` | `T02`<br>`T03`<br>`T12` |  | `hold` | `mikey-youtube-live-002-R006` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K021` | `mikey-youtube-live-002` | `T08`<br>`T10` | `P13` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-002-K022` | `mikey-youtube-live-002` | `T06`<br>`T08`<br>`T10` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K023` | `mikey-youtube-live-002` | `T05` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K024` | `mikey-youtube-live-002` | `T02`<br>`T06`<br>`T10` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K025` | `mikey-youtube-live-002` | `T07`<br>`T08`<br>`T09` |  | `hold` |  | 新基线release_status=hold；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K026` | `mikey-youtube-live-002` | `T12` |  | `hold` |  | 新基线release_status=hold；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K027` | `mikey-youtube-live-002` | `T07`<br>`T08`<br>`T11` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K028` | `mikey-youtube-live-002` | `T01`<br>`T07`<br>`T13` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K029` | `mikey-youtube-live-002` | `T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-002-K030` | `mikey-youtube-live-002` | `T10`<br>`T12` |  | `do_not_generalize` | `mikey-youtube-live-002-R013` | 新基线release_status=do_not_generalize；仅保留为受限背景，不得转成通用建议。 |
| `mikey-youtube-live-002-K031` | `mikey-youtube-live-002` | `T13` |  | `hold` | `mikey-youtube-live-002-R014`<br>`mikey-youtube-live-002-R015` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K032` | `mikey-youtube-live-002` | `T09` |  | `do_not_generalize` | `mikey-youtube-live-002-R014` | 新基线release_status=do_not_generalize；仅保留为受限背景，不得转成通用建议。 |
| `mikey-youtube-live-002-K033` | `mikey-youtube-live-002` | `T12` |  | `do_not_generalize` | `mikey-youtube-live-002-R015` | 新基线release_status=do_not_generalize；仅保留为受限背景，不得转成通用建议。 |
| `mikey-youtube-live-002-K034` | `mikey-youtube-live-002` | `T04`<br>`T06` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K035` | `mikey-youtube-live-002` | `T01`<br>`T07` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K036` | `mikey-youtube-live-002` | `T12` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K037` | `mikey-youtube-live-002` | `T05` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K038` | `mikey-youtube-live-002` | `T05`<br>`T10` |  | `hold` | `mikey-youtube-live-002-R018` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K039` | `mikey-youtube-live-002` | `T01`<br>`T10` |  | `hold` | `mikey-youtube-live-002-R019` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K040` | `mikey-youtube-live-002` | `T01`<br>`T11` |  | `hold` | `mikey-youtube-live-002-R019`<br>`mikey-youtube-live-002-R021` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K041` | `mikey-youtube-live-002` | `T09`<br>`T11`<br>`T13` |  | `do_not_generalize` | `mikey-youtube-live-002-R021` | 新基线release_status=do_not_generalize；仅保留为受限背景，不得转成通用建议。 |
| `mikey-youtube-live-002-K042` | `mikey-youtube-live-002` | `T10` | `P17` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-002-K043` | `mikey-youtube-live-002` | `T04`<br>`T06`<br>`T11` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K044` | `mikey-youtube-live-002` | `T02` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K045` | `mikey-youtube-live-002` | `T06`<br>`T13` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-002-K046` | `mikey-youtube-live-002` | `T10` |  | `hold` |  | 新基线release_status=hold；attribution_status=mixed_speakers；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K001` | `mikey-youtube-live-003` | `T06` |  | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K002` | `mikey-youtube-live-003` | `T03` |  | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K003` | `mikey-youtube-live-003` | `T08`<br>`T13` | `P20` | `hold` | `mikey-youtube-live-003-R001`<br>`mikey-youtube-live-003-R004` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K004` | `mikey-youtube-live-003` | `T09` |  | `hold` | `mikey-youtube-live-003-R001`<br>`mikey-youtube-live-003-R004` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K005` | `mikey-youtube-live-003` | `T08`<br>`T09`<br>`T10` | `P10` | `hold` | `mikey-youtube-live-003-R001`<br>`mikey-youtube-live-003-R004` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K006` | `mikey-youtube-live-003` | `T08` |  | `hold` | `mikey-youtube-live-003-R001`<br>`mikey-youtube-live-003-R004` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K007` | `mikey-youtube-live-003` | `T07` | `P10` | `hold` | `mikey-youtube-live-003-R001`<br>`mikey-youtube-live-003-R008` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K008` | `mikey-youtube-live-003` | `T03`<br>`T08` | `P04` | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K009` | `mikey-youtube-live-003` | `T04`<br>`T10` |  | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K010` | `mikey-youtube-live-003` | `T07`<br>`T08`<br>`T13` |  | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K011` | `mikey-youtube-live-003` | `T05`<br>`T08`<br>`T11` |  | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K012` | `mikey-youtube-live-003` | `T07`<br>`T08`<br>`T10` |  | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K013` | `mikey-youtube-live-003` | `T02`<br>`T04`<br>`T10` |  | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K014` | `mikey-youtube-live-003` | `T04`<br>`T05`<br>`T06` |  | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K015` | `mikey-youtube-live-003` | `T03`<br>`T12` |  | `hold` | `mikey-youtube-live-003-R001`<br>`mikey-youtube-live-003-R015` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-003-K016` | `mikey-youtube-live-003` | `T08`<br>`T10`<br>`T12` |  | `hold` | `mikey-youtube-live-003-R001` | 新基线release_status=hold；attribution_status=mixed_speakers；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-004-K0001` | `mikey-youtube-live-004` | `T13` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0002` | `mikey-youtube-live-004` | `T08`<br>`T09`<br>`T10` | `P12` | `hold` | `mikey-youtube-live-004-RN002` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-004-K0003` | `mikey-youtube-live-004` | `T01`<br>`T05`<br>`T09` |  | `hold` | `mikey-youtube-live-004-RN002`<br>`mikey-youtube-live-004-RN003`<br>`mikey-youtube-live-004-RN004` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-004-K0004` | `mikey-youtube-live-004` | `T03`<br>`T07` |  | `hold` | `mikey-youtube-live-004-RN004` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-004-K0005` | `mikey-youtube-live-004` | `T03`<br>`T08` | `P04` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0006` | `mikey-youtube-live-004` | `T06`<br>`T09`<br>`T11` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0007` | `mikey-youtube-live-004` | `T08`<br>`T11`<br>`T12` | `P11` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0008` | `mikey-youtube-live-004` | `T10`<br>`T11`<br>`T13` |  | `hold` | `mikey-youtube-live-004-RN007`<br>`mikey-youtube-live-004-RN008` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-004-K0009` | `mikey-youtube-live-004` | `T05`<br>`T08`<br>`T11` | `P19` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0010` | `mikey-youtube-live-004` | `T03`<br>`T07`<br>`T09` | `P09` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0011` | `mikey-youtube-live-004` | `T06` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0012` | `mikey-youtube-live-004` | `T02`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0013` | `mikey-youtube-live-004` | `T02`<br>`T06`<br>`T12` | `P07` | `hold` | `mikey-youtube-live-004-RN010` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-004-K0014` | `mikey-youtube-live-004` | `T07`<br>`T09`<br>`T12` | `P10` | `hold` | `mikey-youtube-live-004-RN011` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-004-K0015` | `mikey-youtube-live-004` | `T03`<br>`T07`<br>`T08` |  | `hold` | `mikey-youtube-live-004-RN011` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-004-K0016` | `mikey-youtube-live-004` | `T03`<br>`T08` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0017` | `mikey-youtube-live-004` | `T01`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0018` | `mikey-youtube-live-004` | `T03`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0019` | `mikey-youtube-live-004` | `T01`<br>`T05`<br>`T06` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-004-K0020` | `mikey-youtube-live-004` | `T05`<br>`T06`<br>`T11` | `P16` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-005-K001` | `mikey-youtube-live-005` | `T04`<br>`T09`<br>`T10` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K002` | `mikey-youtube-live-005` | `T01` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K003` | `mikey-youtube-live-005` | `T04`<br>`T05` | `P03` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K004` | `mikey-youtube-live-005` | `T07`<br>`T08`<br>`T09` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K005` | `mikey-youtube-live-005` | `T05`<br>`T11` |  | `hold` | `mikey-youtube-live-005-R007` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-005-K006` | `mikey-youtube-live-005` | `T08`<br>`T13` | `P11` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K007` | `mikey-youtube-live-005` | `T01`<br>`T08`<br>`T10` | `P14` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K008` | `mikey-youtube-live-005` | `T01`<br>`T03`<br>`T07` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K009` | `mikey-youtube-live-005` | `T03`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K010` | `mikey-youtube-live-005` | `T03`<br>`T04` | `P04` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K011` | `mikey-youtube-live-005` | `T01`<br>`T07` | `P09` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K012` | `mikey-youtube-live-005` | `T06`<br>`T12` | `P07` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K013` | `mikey-youtube-live-005` | `T06`<br>`T08`<br>`T09` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K014` | `mikey-youtube-live-005` | `T05`<br>`T06` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K015` | `mikey-youtube-live-005` | `T01`<br>`T02` | `P02` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K016` | `mikey-youtube-live-005` | `T02` |  | `hold` | `mikey-youtube-live-005-R012` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-005-K017` | `mikey-youtube-live-005` | `T01`<br>`T03` |  | `hold` | `mikey-youtube-live-005-R012` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-005-K018` | `mikey-youtube-live-005` | `T01`<br>`T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-005-K019` | `mikey-youtube-live-005` | `T09`<br>`T13` | `P10`<br>`P20` | `hold` | `mikey-youtube-live-005-R014`<br>`mikey-youtube-live-005-R015` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-006-K0001` | `mikey-youtube-live-006` | `T05` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0002` | `mikey-youtube-live-006` | `T03`<br>`T07` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-006-K0003` | `mikey-youtube-live-006` | `T03`<br>`T12`<br>`T13` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0004` | `mikey-youtube-live-006` | `T04`<br>`T05`<br>`T09` | `P10` | `hold` | `mikey-youtube-live-006-RN002` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-006-K0005` | `mikey-youtube-live-006` | `T02`<br>`T06`<br>`T07` |  | `hold` | `mikey-youtube-live-006-RN002` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-006-K0006` | `mikey-youtube-live-006` | `T02`<br>`T06`<br>`T12` | `P07` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0007` | `mikey-youtube-live-006` | `T06`<br>`T10`<br>`T12` | `P08` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0008` | `mikey-youtube-live-006` | `T05`<br>`T06`<br>`T12` | `P08` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0009` | `mikey-youtube-live-006` | `T01`<br>`T03`<br>`T07` | `P01` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0010` | `mikey-youtube-live-006` | `T07`<br>`T08` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0011` | `mikey-youtube-live-006` | `T05`<br>`T08`<br>`T13` |  | `hold` | `mikey-youtube-live-006-RN004` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-006-K0012` | `mikey-youtube-live-006` | `T10` |  | `hold` | `mikey-youtube-live-006-RN006` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-006-K0013` | `mikey-youtube-live-006` | `T02`<br>`T05`<br>`T12` |  | `hold` | `mikey-youtube-live-006-RN007` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-006-K0014` | `mikey-youtube-live-006` | `T02`<br>`T07`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0015` | `mikey-youtube-live-006` | `T04`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0016` | `mikey-youtube-live-006` | `T01`<br>`T02`<br>`T03` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0017` | `mikey-youtube-live-006` | `T05`<br>`T10`<br>`T11` | `P05`<br>`P16` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0018` | `mikey-youtube-live-006` | `T03`<br>`T10`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0019` | `mikey-youtube-live-006` | `T08`<br>`T12` | `P18` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0020` | `mikey-youtube-live-006` | `T03`<br>`T09`<br>`T10` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0021` | `mikey-youtube-live-006` | `T03`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-006-K0022` | `mikey-youtube-live-006` | `T01`<br>`T08`<br>`T12` |  | `hold` | `mikey-youtube-live-006-RN011` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-006-K0023` | `mikey-youtube-live-006` | `T04`<br>`T05`<br>`T08` |  | `hold` | `mikey-youtube-live-006-RN011` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-006-K0024` | `mikey-youtube-live-006` | `T04`<br>`T05`<br>`T10` |  | `context_only` |  | direct-major语义抽查降级为context_only：高低能量均可这一层有明确原话，但‘内在价值决定吸引、只因帅/钱会被当男模/提款机’正是major质疑的绝对因果和群体概括；会改变整条作为行动原则的适用范围，保留为人物观点背景。 |
| `mikey-youtube-live-007-K001` | `mikey-youtube-live-007` | `T07`<br>`T10`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K002` | `mikey-youtube-live-007` | `T01`<br>`T02`<br>`T07` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K003` | `mikey-youtube-live-007` | `T02`<br>`T06`<br>`T10` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K004` | `mikey-youtube-live-007` | `T02`<br>`T06`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K005` | `mikey-youtube-live-007` | `T01`<br>`T08`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K006` | `mikey-youtube-live-007` | `T02`<br>`T06`<br>`T08` | `P07` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K007` | `mikey-youtube-live-007` | `T01`<br>`T03` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K008` | `mikey-youtube-live-007` | `T07`<br>`T10` |  | `hold` | `mikey-youtube-live-007-R006` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-007-K009` | `mikey-youtube-live-007` | `T01` | `P01` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K010` | `mikey-youtube-live-007` | `T03`<br>`T10`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K011` | `mikey-youtube-live-007` | `T04`<br>`T08`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K012` | `mikey-youtube-live-007` | `T01`<br>`T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K013` | `mikey-youtube-live-007` | `T01`<br>`T07`<br>`T09` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K014` | `mikey-youtube-live-007` | `T03`<br>`T06`<br>`T09` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K015` | `mikey-youtube-live-007` | `T03`<br>`T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K016` | `mikey-youtube-live-007` | `T13` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K017` | `mikey-youtube-live-007` | `T05`<br>`T09`<br>`T12` |  | `hold` | `mikey-youtube-live-007-R014` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-007-K018` | `mikey-youtube-live-007` | `T03`<br>`T08`<br>`T12` | `P04` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K019` | `mikey-youtube-live-007` | `T06`<br>`T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K020` | `mikey-youtube-live-007` | `T01`<br>`T05` |  | `hold` | `mikey-youtube-live-007-R016` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-007-K021` | `mikey-youtube-live-007` | `T10` |  | `hold` |  | 新基线release_status=hold；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-007-K022` | `mikey-youtube-live-007` | `T03`<br>`T11`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K023` | `mikey-youtube-live-007` | `T02`<br>`T05`<br>`T10` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K024` | `mikey-youtube-live-007` | `T03` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K025` | `mikey-youtube-live-007` | `T01`<br>`T05`<br>`T06` |  | `hold` | `mikey-youtube-live-007-R023` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-007-K026` | `mikey-youtube-live-007` | `T01`<br>`T05`<br>`T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K027` | `mikey-youtube-live-007` | `T03`<br>`T08`<br>`T10` |  | `hold` | `mikey-youtube-live-007-R025` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-007-K028` | `mikey-youtube-live-007` | `T01`<br>`T03` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-007-K029` | `mikey-youtube-live-007` | `T01` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K001` | `mikey-youtube-live-008` | `T08`<br>`T09`<br>`T10` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K002` | `mikey-youtube-live-008` | `T03`<br>`T07` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K003` | `mikey-youtube-live-008` | `T05`<br>`T06`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K004` | `mikey-youtube-live-008` | `T03` |  | `hold` | `mikey-youtube-live-008-R004` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-008-K005` | `mikey-youtube-live-008` | `T05`<br>`T08`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K006` | `mikey-youtube-live-008` | `T01`<br>`T03` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K007` | `mikey-youtube-live-008` | `T01`<br>`T07`<br>`T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K008` | `mikey-youtube-live-008` | `T06`<br>`T10`<br>`T11` | `P16` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K009` | `mikey-youtube-live-008` | `T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K010` | `mikey-youtube-live-008` | `T03`<br>`T12` |  | `hold` | `mikey-youtube-live-008-R007` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-008-K011` | `mikey-youtube-live-008` | `T04`<br>`T10`<br>`T12` |  | `hold` | `mikey-youtube-live-008-R008` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-008-K012` | `mikey-youtube-live-008` | `T01`<br>`T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K013` | `mikey-youtube-live-008` | `T03`<br>`T06`<br>`T08` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K014` | `mikey-youtube-live-008` | `T03`<br>`T10`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K015` | `mikey-youtube-live-008` | `T01` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K016` | `mikey-youtube-live-008` | `T03`<br>`T04` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K017` | `mikey-youtube-live-008` | `T07`<br>`T08`<br>`T09` |  | `hold` | `mikey-youtube-live-008-R012` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-008-K018` | `mikey-youtube-live-008` | `T02`<br>`T05`<br>`T11` |  | `hold` | `mikey-youtube-live-008-R013` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-008-K019` | `mikey-youtube-live-008` | `T05`<br>`T11` | `P05` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K020` | `mikey-youtube-live-008` | `T05`<br>`T11`<br>`T12` | `P06` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K021` | `mikey-youtube-live-008` | `T01`<br>`T12` | `P18` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K022` | `mikey-youtube-live-008` | `T12`<br>`T13` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K023` | `mikey-youtube-live-008` | `T08`<br>`T09` | `P11`<br>`P14` | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K024` | `mikey-youtube-live-008` | `T03`<br>`T04`<br>`T09` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-008-K025` | `mikey-youtube-live-008` | `T05`<br>`T06`<br>`T12` |  | `context_only` |  | 新基线为explicit_mikey且无关联open blocking，但本综合仍按既有major/术语/数字/情境不确定性保留context_only；可用于解释背景，不作为第一人称行动证据。 |
| `mikey-youtube-live-009-K0001` | `mikey-youtube-live-009` | `T05`<br>`T11` |  | `hold` | `mikey-youtube-live-009-RN001`<br>`mikey-youtube-live-009-RN002` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-009-K0002` | `mikey-youtube-live-009` | `T03`<br>`T09`<br>`T12` | `P09` | `hold` | `mikey-youtube-live-009-RN002` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-009-K0003` | `mikey-youtube-live-009` | `T02`<br>`T05`<br>`T11` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0004` | `mikey-youtube-live-009` | `T06`<br>`T08` | `P15` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0005` | `mikey-youtube-live-009` | `T02`<br>`T05`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0006` | `mikey-youtube-live-009` | `T03`<br>`T07` | `P14` | `hold` | `mikey-youtube-live-009-RN004` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-009-K0007` | `mikey-youtube-live-009` | `T01`<br>`T07`<br>`T08` |  | `hold` | `mikey-youtube-live-009-RN004` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-009-K0008` | `mikey-youtube-live-009` | `T08`<br>`T09`<br>`T11` | `P10`<br>`P16` | `hold` |  | direct-major语义抽查降级为hold：观点相关原话出现在约1520秒，但当前证据S00770/S00778/S00782位于约1650–1800秒且不支持邀约/拒绝结论；major又直接关系是否把拒绝误判为安全感，需重绑证据并核对否定词。 |
| `mikey-youtube-live-009-K0009` | `mikey-youtube-live-009` | `T05`<br>`T11`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0010` | `mikey-youtube-live-009` | `T01`<br>`T05`<br>`T11` | `P05` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0011` | `mikey-youtube-live-009` | `T08`<br>`T12`<br>`T13` | `P03` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0012` | `mikey-youtube-live-009` | `T05`<br>`T10` | `P06` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0013` | `mikey-youtube-live-009` | `T13` | `P20` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0014` | `mikey-youtube-live-009` | `T01`<br>`T02` | `P15` | `hold` | `mikey-youtube-live-009-RN006` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-009-K0015` | `mikey-youtube-live-009` | `T08`<br>`T11` | `P14`<br>`P15` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0016` | `mikey-youtube-live-009` | `T02`<br>`T07` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0017` | `mikey-youtube-live-009` | `T03` | `P04` | `hold` |  | direct-major语义抽查降级为hold：实践与数量原话约在S01178附近，当前引用S01299/S01316/S01341没有闭合‘持续复盘失败原因’；major涉及冷淡与投入边界，错误事件映射会改变可执行范围。 |
| `mikey-youtube-live-009-K0018` | `mikey-youtube-live-009` | `T02`<br>`T10` | `P12` | `hold` | `mikey-youtube-live-009-RN011` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-009-K0019` | `mikey-youtube-live-009` | `T01`<br>`T08`<br>`T09` | `P19` | `hold` | `mikey-youtube-live-009-RN011` | 关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-009-K0020` | `mikey-youtube-live-009` | `T02`<br>`T05`<br>`T10` |  | `hold` |  | direct-major语义抽查降级为hold：一致性原话约在S01620–S01670，当前引用S01826/S01837/S01864指向别的话题；major又要求区分边界表达和‘喷她’，现有链条不能证明知识已正确拆分。 |
| `mikey-youtube-live-009-K0021` | `mikey-youtube-live-009` | `T02`<br>`T06`<br>`T10` | `P13` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-009-K0022` | `mikey-youtube-live-009` | `T05`<br>`T07`<br>`T09` |  | `hold` |  | direct-major语义抽查降级为hold：当前引用S01922/S01924/S02035分别落在边界或后续话题，未精确支撑‘状态和形象’总结；相交major涉及绝对因果，需重新定位整段后才能判断保留范围。 |
| `mikey-youtube-live-009-K0023` | `mikey-youtube-live-009` | `T02`<br>`T06`<br>`T12` | `P08` | `hold` |  | direct-major语义抽查降级为hold：当前引用S02026/S02031/S02032转入配得感与金钱，未支撑‘只讲真实经历、不要编造’；major同样覆盖该错位事件，不能维持direct。 |
| `mikey-youtube-live-009-K0024` | `mikey-youtube-live-009` | `T09`<br>`T10`<br>`T11` | `P10` | `hold` |  | direct-major语义抽查降级为hold：不纠缠原话约在S01964，当前引用S02035/S02048/S02058却在配得感/金钱段；拒绝停止线虽方向合理，但精确证据链错误，需重绑后再放行。 |
| `mikey-youtube-live-009-K0025` | `mikey-youtube-live-009` | `T03`<br>`T12` |  | `hold` |  | direct-major语义抽查降级为hold：当前引用S02105–S02107已进入‘提升吸引力’收尾问题，没有支撑‘逐步减少在意、重解释挫折’；信念、转世及五分钟判断的major可能改变原段性质。 |
| `mikey-youtube-live-009-K0026` | `mikey-youtube-live-009` | `T01`<br>`T05`<br>`T10` | `P18` | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-010-K0001` | `mikey-youtube-live-010` | `T01`<br>`T03`<br>`T07` | `P01`<br>`P09` | `hold` | `mikey-youtube-live-010-RN001` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0002` | `mikey-youtube-live-010` | `T01`<br>`T08`<br>`T13` |  | `hold` | `mikey-youtube-live-010-RN001` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0003` | `mikey-youtube-live-010` | `T10`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-010-K0004` | `mikey-youtube-live-010` | `T07`<br>`T08`<br>`T11` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-010-K0005` | `mikey-youtube-live-010` | `T01`<br>`T02` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-010-K0006` | `mikey-youtube-live-010` | `T01`<br>`T10` | `P13` | `hold` |  | direct-major语义抽查降级为hold：玩手机与边界原话在S00267–S00300附近，当前证据却是S00413/S00466/S00495的心流、废号和搭讪句；major正质疑平静边界还是积压攻击，现有引用无法判定语气和结果。 |
| `mikey-youtube-live-010-K0007` | `mikey-youtube-live-010` | `T01` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-010-K0008` | `mikey-youtube-live-010` | `T01`<br>`T03`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-010-K0009` | `mikey-youtube-live-010` | `T01`<br>`T06` |  | `hold` | `mikey-youtube-live-010-RN005` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0010` | `mikey-youtube-live-010` | `T02`<br>`T04`<br>`T05` |  | `hold` | `mikey-youtube-live-010-RN005` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0011` | `mikey-youtube-live-010` | `T06` | `P08` | `hold` | `mikey-youtube-live-010-RN005`<br>`mikey-youtube-live-010-RN006`<br>`mikey-youtube-live-010-RN007` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0012` | `mikey-youtube-live-010` | `T07`<br>`T09`<br>`T10` | `P10` | `hold` | `mikey-youtube-live-010-RN006`<br>`mikey-youtube-live-010-RN007` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0013` | `mikey-youtube-live-010` | `T06`<br>`T08` |  | `hold` | `mikey-youtube-live-010-RN006`<br>`mikey-youtube-live-010-RN007` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0014` | `mikey-youtube-live-010` | `T01`<br>`T06`<br>`T10` |  | `hold` | `mikey-youtube-live-010-RN007` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0015` | `mikey-youtube-live-010` | `T12` |  | `hold` | `mikey-youtube-live-010-RN009` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0016` | `mikey-youtube-live-010` | `T01`<br>`T10` | `P13` | `hold` | `mikey-youtube-live-010-RN009` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0017` | `mikey-youtube-live-010` | `T08`<br>`T10`<br>`T12` |  | `direct` |  | 新基线为candidate_only + explicit_mikey，且知识及所属事件均无关联open blocking；沿用上一版经逐条风险筛选得到的direct，仅依据该知识自身精确证据，不因跨期重复而升级。 |
| `mikey-youtube-live-010-K0018` | `mikey-youtube-live-010` | `T01`<br>`T03` |  | `hold` | `mikey-youtube-live-010-RN009` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0019` | `mikey-youtube-live-010` | `T07`<br>`T09`<br>`T13` | `P10` | `hold` |  | direct-major语义抽查降级为hold：街头/酒吧转念原话在约2840–3300秒，当前引用S01454/S01473/S01494位于门当户对、性价值和修图段；事件和证据错位，无法确认场所规则/拒绝边界是否原话。 |
| `mikey-youtube-live-010-K0020` | `mikey-youtube-live-010` | `T01`<br>`T05`<br>`T06` |  | `hold` |  | direct-major语义抽查降级为hold：调动情绪原话在S01288–S01326附近，当前引用S01546/S01574/S01606却是点赞、软件和衣服；major涉及修辞是否被普遍化，必须先重绑原段。 |
| `mikey-youtube-live-010-K0021` | `mikey-youtube-live-010` | `T09` |  | `hold` | `mikey-youtube-live-010-RN011` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0022` | `mikey-youtube-live-010` | `T01`<br>`T05`<br>`T11` | `P05`<br>`P06` | `hold` |  | direct-major语义抽查降级为hold：照片和展示面原话在S01425–S01520附近，当前引用S01807/S01845/S01859指向紧张、点赞和经验循环；平台女性概括与适度修图边界无法由现有证据拆开。 |
| `mikey-youtube-live-010-K0023` | `mikey-youtube-live-010` | `T08`<br>`T10`<br>`T12` |  | `hold` |  | direct-major语义抽查降级为hold：成长节点原话在S01643–S01666，当前引用S01918/S01930/S01941指向警察、点赞和一致性；人物经历虽可在原稿找到，但direct引用链错误。 |
| `mikey-youtube-live-010-K0024` | `mikey-youtube-live-010` | `T03`<br>`T12` |  | `hold` |  | direct-major语义抽查降级为hold：身高/过去原话在S01669–S01771，当前引用S01952/S01983/S02006完全无关；且‘直接忘却过去’对真实创伤和专业支持的适用边界会改变建议核心。 |
| `mikey-youtube-live-010-K0025` | `mikey-youtube-live-010` | `T06` | `P07` | `hold` |  | direct-major语义抽查降级为hold：‘你我我们’原话在S01817–S01835，当前引用S02032/S02055/S02061位于关系维护、网聊和转场；需重绑后才能作为聊天方法直接证据。 |
| `mikey-youtube-live-010-K0026` | `mikey-youtube-live-010` | `T01`<br>`T03`<br>`T04` | `P04` | `hold` |  | direct-major语义抽查降级为hold：知行合一原话在S01850–S01866，当前引用S02068/S02080/S02094指向转场、电影和高分女性；major虽谈瞳孔，但更根本问题是精确证据错位。 |
| `mikey-youtube-live-010-K0027` | `mikey-youtube-live-010` | `T08`<br>`T10`<br>`T11` |  | `hold` |  | direct-major语义抽查降级为hold：异地维护原话在S01925–S01929，当前引用S02126/S02136/S02154位于女学员等后续问答；瞳孔major与该知识的机械相交来自错位事件，需先修复事件边界。 |
| `mikey-youtube-live-010-K0028` | `mikey-youtube-live-010` | `T02`<br>`T04`<br>`T05` | `P02` | `hold` | `mikey-youtube-live-010-RN016` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0029` | `mikey-youtube-live-010` | `T02`<br>`T06`<br>`T11` | `P16` | `hold` | `mikey-youtube-live-010-RN016` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0030` | `mikey-youtube-live-010` | `T05`<br>`T09` | `P19` | `hold` | `mikey-youtube-live-010-RN016` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0031` | `mikey-youtube-live-010` | `T03`<br>`T06`<br>`T12` |  | `hold` | `mikey-youtube-live-010-RN017` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0032` | `mikey-youtube-live-010` | `T01`<br>`T05`<br>`T10` | `P18` | `hold` | `mikey-youtube-live-010-RN017`<br>`mikey-youtube-live-010-RN018` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0033` | `mikey-youtube-live-010` | `T03`<br>`T09`<br>`T12` |  | `hold` | `mikey-youtube-live-010-RN018` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |
| `mikey-youtube-live-010-K0034` | `mikey-youtube-live-010` | `T05`<br>`T09`<br>`T10` |  | `hold` | `mikey-youtube-live-010-RN018` | 新基线release_status=hold；关联open blocking review；不得标direct，也不得支撑Mikey第一人称行动建议。 |

## proposed_status_changes

以下只表示本跨期综合建议的运行时 `direct` 使用资格，不修改逐期 post-audit 文件本身；跨期重复不是升级理由。

- `mikey-youtube-live-001-K001`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K002`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K006`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K009`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K010`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K013`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K014`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K020`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K021`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K022`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-001-K027`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K004`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K005`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K008`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K009`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K012`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K013`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K016`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K017`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K023`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K024`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-002-K042`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0001`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0005`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0006`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0007`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0009`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0010`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0011`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0012`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0016`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0017`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0018`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0019`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-004-K0020`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0001`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0003`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0006`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0007`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0008`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0009`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0010`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0014`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0015`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0016`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0017`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0018`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0019`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0020`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0021`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-006-K0024`｜from `candidate_only` → proposed `context_only`｜direct-major语义抽查后修订：高低能量均可这一层有明确原话，但‘内在价值决定吸引、只因帅/钱会被当男模/提款机’正是major质疑的绝对因果和群体概括；会改变整条作为行动原则的适用范围，保留为人物观点背景。
- `mikey-youtube-live-009-K0003`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0004`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0005`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0008`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：观点相关原话出现在约1520秒，但当前证据S00770/S00778/S00782位于约1650–1800秒且不支持邀约/拒绝结论；major又直接关系是否把拒绝误判为安全感，需重绑证据并核对否定词。
- `mikey-youtube-live-009-K0009`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0010`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0011`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0012`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0013`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0015`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0016`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0017`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：实践与数量原话约在S01178附近，当前引用S01299/S01316/S01341没有闭合‘持续复盘失败原因’；major涉及冷淡与投入边界，错误事件映射会改变可执行范围。
- `mikey-youtube-live-009-K0020`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：一致性原话约在S01620–S01670，当前引用S01826/S01837/S01864指向别的话题；major又要求区分边界表达和‘喷她’，现有链条不能证明知识已正确拆分。
- `mikey-youtube-live-009-K0021`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-009-K0022`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：当前引用S01922/S01924/S02035分别落在边界或后续话题，未精确支撑‘状态和形象’总结；相交major涉及绝对因果，需重新定位整段后才能判断保留范围。
- `mikey-youtube-live-009-K0023`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：当前引用S02026/S02031/S02032转入配得感与金钱，未支撑‘只讲真实经历、不要编造’；major同样覆盖该错位事件，不能维持direct。
- `mikey-youtube-live-009-K0024`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：不纠缠原话约在S01964，当前引用S02035/S02048/S02058却在配得感/金钱段；拒绝停止线虽方向合理，但精确证据链错误，需重绑后再放行。
- `mikey-youtube-live-009-K0025`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：当前引用S02105–S02107已进入‘提升吸引力’收尾问题，没有支撑‘逐步减少在意、重解释挫折’；信念、转世及五分钟判断的major可能改变原段性质。
- `mikey-youtube-live-009-K0026`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-010-K0003`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-010-K0004`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-010-K0005`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-010-K0006`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：玩手机与边界原话在S00267–S00300附近，当前证据却是S00413/S00466/S00495的心流、废号和搭讪句；major正质疑平静边界还是积压攻击，现有引用无法判定语气和结果。
- `mikey-youtube-live-010-K0007`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-010-K0008`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-010-K0017`｜from `candidate_only` → proposed `direct`｜post-audit后仍为explicit_mikey；该知识及所属事件无open blocking；沿用先前逐条风险筛选结果。跨期重复仅作主题佐证，不是升级理由。
- `mikey-youtube-live-010-K0019`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：街头/酒吧转念原话在约2840–3300秒，当前引用S01454/S01473/S01494位于门当户对、性价值和修图段；事件和证据错位，无法确认场所规则/拒绝边界是否原话。
- `mikey-youtube-live-010-K0020`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：调动情绪原话在S01288–S01326附近，当前引用S01546/S01574/S01606却是点赞、软件和衣服；major涉及修辞是否被普遍化，必须先重绑原段。
- `mikey-youtube-live-010-K0022`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：照片和展示面原话在S01425–S01520附近，当前引用S01807/S01845/S01859指向紧张、点赞和经验循环；平台女性概括与适度修图边界无法由现有证据拆开。
- `mikey-youtube-live-010-K0023`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：成长节点原话在S01643–S01666，当前引用S01918/S01930/S01941指向警察、点赞和一致性；人物经历虽可在原稿找到，但direct引用链错误。
- `mikey-youtube-live-010-K0024`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：身高/过去原话在S01669–S01771，当前引用S01952/S01983/S02006完全无关；且‘直接忘却过去’对真实创伤和专业支持的适用边界会改变建议核心。
- `mikey-youtube-live-010-K0025`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：‘你我我们’原话在S01817–S01835，当前引用S02032/S02055/S02061位于关系维护、网聊和转场；需重绑后才能作为聊天方法直接证据。
- `mikey-youtube-live-010-K0026`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：知行合一原话在S01850–S01866，当前引用S02068/S02080/S02094指向转场、电影和高分女性；major虽谈瞳孔，但更根本问题是精确证据错位。
- `mikey-youtube-live-010-K0027`｜from `candidate_only` → proposed `hold`｜direct-major语义抽查后修订：异地维护原话在S01925–S01929，当前引用S02126/S02136/S02154位于女学员等后续问答；瞳孔major与该知识的机械相交来自错位事件，需先修复事件边界。

## 自校验

- `scope` 与 post-audit 输入逐字结构一致：通过。
- `statistics` 与 post-audit 输入一致：通过。
- `sources` 与 post-audit 输入一致（含审计后的 acceptance/file hashes）：通过。
- `knowledge_index`：266 条；唯一 ID 266 个；与输入知识集合完全相等：通过。
- 所有 `direct` 均满足：新基线非 hold、attribution=`explicit_mikey`、且知识及所属 event 无 open blocking：通过。
- 直播003 K001–K016 全部 `mixed_speakers / hold`，未进入命题、方法关系或回答模式的 direct 支撑：通过。
- 命题 `supporting_knowledge_ids`、方法主 `knowledge_ids`、answer pattern 的 `direct_support_knowledge_ids` 只含 direct：通过。
- source_id / knowledge_id / event_id / review_id / evidence_id / SID 交叉引用均存在于 post-audit 输入且来源一致：通过。
- JSON 可解析；UTF-8 输出；Markdown 中运行时统计与 JSON 一致：通过。

本文件不把任何未完成的本地听校、连续音画复核、法律/医疗审查、重复案例指纹核验或正式 skill 集成写成已完成。
