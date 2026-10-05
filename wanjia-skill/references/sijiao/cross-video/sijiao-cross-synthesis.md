# `sijiao` 私教案例批次跨期综合

> 输入仅使用 `sijiao-cross-input.json/.md` 与 `cross-synthesis-instructions.md`。本文件是跨期综合，不把逐期全文重新复制；需要核对原句时沿知识 ID、事件 ID 与 SID 回读。

## 1. 范围、统计与复用

本批次正式新增来源为 18 个，知识条目恰好 164 条；`mikey-sijiao-007` 是既有来源的重编码复用，形式权重为 0，不产生新的知识或独立案例权重。

### scope（原样保留）

```json
{
  "source_ids": [
    "mikey-sijiao-001",
    "mikey-sijiao-002",
    "mikey-sijiao-003",
    "mikey-sijiao-004",
    "mikey-sijiao-005",
    "mikey-sijiao-006",
    "mikey-sijiao-008",
    "mikey-sijiao-009",
    "mikey-sijiao-010",
    "mikey-sijiao-011",
    "mikey-sijiao-012",
    "mikey-sijiao-013",
    "mikey-sijiao-014",
    "mikey-sijiao-015",
    "mikey-sijiao-016",
    "mikey-sijiao-017",
    "mikey-sijiao-018",
    "mikey-sijiao-019"
  ],
  "duplicate_sources_reused_from_prior": [
    "mikey-sijiao-007"
  ]
}
```

### statistics（原样保留）

```json
{
  "source_count": 18,
  "segments": 9254,
  "events": 197,
  "knowledge": 164,
  "knowledge_quotes": 1967,
  "review_needed": 130
}
```

### source_reuse_ledger（原样保留）

```json
{
  "schema_version": "sijiao-source-reuse-1.0",
  "status": "complete",
  "new_source_ids": [
    "mikey-sijiao-001",
    "mikey-sijiao-002",
    "mikey-sijiao-003",
    "mikey-sijiao-004",
    "mikey-sijiao-005",
    "mikey-sijiao-006",
    "mikey-sijiao-008",
    "mikey-sijiao-009",
    "mikey-sijiao-010",
    "mikey-sijiao-011",
    "mikey-sijiao-012",
    "mikey-sijiao-013",
    "mikey-sijiao-014",
    "mikey-sijiao-015",
    "mikey-sijiao-016",
    "mikey-sijiao-017",
    "mikey-sijiao-018",
    "mikey-sijiao-019"
  ],
  "aliases": [
    {
      "source_id": "mikey-sijiao-007",
      "canonical_source_id": "mikey-approach-027",
      "relationship": "same_release_reencode",
      "formal_weight": 0,
      "basis": "规范化自动稿全文逐字一致"
    }
  ]
}
```

## 2. 来源索引

| source_id | title | content_locator | knowledge |
|---|---|---|---:|
| `mikey-sijiao-001` | 40岁老板三天收尾女大学生 | `items/mikey-sijiao-001/analysis/episode-analysis.md` | 12 |
| `mikey-sijiao-002` | 49岁大叔学员学习搭讪，当你说太晚了的时候，一定要谨慎，它可能是你退缩的借口 | `items/mikey-sijiao-002/analysis/episode-analysis.md` | 7 |
| `mikey-sijiao-003` | 情感导师的生活日记 | `items/mikey-sijiao-003/analysis/episode-analysis.md` | 11 |
| `mikey-sijiao-004` | 为什么学把妹，线下复盘的重要性 | `items/mikey-sijiao-004/analysis/episode-analysis.md` | 15 |
| `mikey-sijiao-005` | 身高一米六能否把妹 | `items/mikey-sijiao-005/analysis/episode-analysis.md` | 8 |
| `mikey-sijiao-006` | 线下学员经典案例 | `items/mikey-sijiao-006/analysis/episode-analysis.md` | 7 |
| `mikey-sijiao-008` | 你的搭讪有一致性么 | `items/mikey-sijiao-008/analysis/episode-analysis.md` | 6 |
| `mikey-sijiao-009` | 搭讪从零到一，线下三天拥有松弛感（纯享版）丨线下学员案例丨个性样本丨自我提升丨搭讪丨自然流丨脱单 | `items/mikey-sijiao-009/analysis/episode-analysis.md` | 5 |
| `mikey-sijiao-010` | 你们常犯的约会错误丨怎么传递个性样本丨自我提升丨搭讪丨约会丨自然流丨脱单丨dating in | `items/mikey-sijiao-010/analysis/episode-analysis.md` | 8 |
| `mikey-sijiao-011` | 是什么毁了你的搭讪丨自我提升丨搭讪丨约会丨自然流丨脱单丨dating in china_108 | `items/mikey-sijiao-011/analysis/episode-analysis.md` | 11 |
| `mikey-sijiao-012` | 怎麽game女同事丨線上聊天案例講解丨聊天丨網聊方法丨約會丨情感丨戀愛丨dating in c | `items/mikey-sijiao-012/analysis/episode-analysis.md` | 10 |
| `mikey-sijiao-013` | 報名一周，學員收獲自己的心儀女生丨線上聊天案例講解丨聊天丨網聊方法丨約會丨情感丨戀愛丨dati | `items/mikey-sijiao-013/analysis/episode-analysis.md` | 9 |
| `mikey-sijiao-014` | A9企业家网聊收尾正妹丨线上聊天案例讲解丨聊天丨网聊方法丨恋爱丨dating in china | `items/mikey-sijiao-014/analysis/episode-analysis.md` | 10 |
| `mikey-sijiao-015` | 玩家心态的打磨过程，学员实战复盘（上）丨线上私教案例丨支配游戏丨“术”和“道”丨情感丨恋爱丨d | `items/mikey-sijiao-015/analysis/episode-analysis.md` | 11 |
| `mikey-sijiao-016` | 玩家心态的打磨过程，学员实战复盘（下）丨线上私教案例丨支配游戏丨“术”和“道”丨情感丨恋爱丨d | `items/mikey-sijiao-016/analysis/episode-analysis.md` | 8 |
| `mikey-sijiao-017` | 一个月的时间把学员约不出来的女生变成母丨线上聊天案例讲解丨聊天丨网聊方法丨恋爱丨情感丨搭讪丨约 | `items/mikey-sijiao-017/analysis/episode-analysis.md` | 10 |
| `mikey-sijiao-018` | 前女友多人运动，老实人的逆袭丨我对她那么好，她玩我就跟玩一样丨线上聊天案例讲解丨聊天丨网聊方法 | `items/mikey-sijiao-018/analysis/episode-analysis.md` | 8 |
| `mikey-sijiao-019` | 女人拒絕出門，如何外賣到家丨20s的語音，讓你區別其他男人丨線上聊天案例講解丨自我提升丨約會丨搭訕丨 | `items/mikey-sijiao-019/analysis/episode-analysis.md` | 8 |

## 3. 总体跨期判断

这批私教案例跨期后最稳定的结构，不是一套固定话术，而是一个反复出现的判断循环：**先判断当前阶段与场景 → 做最小可执行动作 → 看真实反馈 → 及时减压或继续 → 复盘真正卡点 → 再把具体技术抽象成可迁移原则**。线下搭讪部分反复围绕行动、松弛、一致性、注意力、真实来意、浅沟通和复盘；网聊与约会部分则逐渐把同一套逻辑延伸到热度、邀约、物流、安全感、约会体验、修复与维护。

同时，批次里确实存在另一条彼此冲突的内容线：命令式带领、制造嫉妒、沉没成本、把人视为 NPC、酒精推进、冒犯自动美化、百分百拿下等。它们没有被跨期综合成可直接调用的方法，而被放入 `conflicts`、`critical_boundary_audit` 和 `hold/do_not_generalize`。结果层同样严格拆开：**Mikey 教学判断 ≠ 学员自述 ≠ 现场可见行为 ≠ 聊天截图 ≠ 发布标题/后期包装 ≠ 镜头外结果主张**。

## 4. 主题综合

### T01｜训练与复盘：先行动，再把状态和错误练稳定

**判断：** 这批私教材料把进步定义成一个循环：先把可控行动做出来，再用现场/录像复盘定位真正卡点，一次改一个可观察问题；短期兴奋或数字变化不能直接等同于永久改变。

**理由：**
- 只学碎片理论并未自动消除行动焦虑。
- 语速、假笑、逃离感和基础表达能力是比复杂话术更先要处理的变量。
- 机械增加次数可能固化同一个错误，及时反馈才让练习产生方向。

**步骤：**
1. 按当前阶段定义一个可完成目标，例如出手、完成一轮真实交流。
2. 观察最明显的状态问题，必要时先放慢和减少动作。
3. 回看现场或录像，找一个关键变量。
4. 下一批练习只盯这个变量，再比较反馈。

**适用条件：**
- 目标会随训练阶段变化。
- 即时自评、课程证言和课后兴奋不作为长期效果证明。

**观察反馈：**
- 是否更能停留在对话中而不是急于逃离。
- 语速、停顿、表情和身体是否更自然。
- 同一错误是否在下一轮减少。

**限制：**
- 不把课程效果数字或一次高状态推广成普遍成功率。

**命题：** `P01`、`P02`、`P03`

**知识依据：** `mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0003`、`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`、`mikey-sijiao-005-K0005`、`mikey-sijiao-011-K0009`、`mikey-sijiao-002-K0002`、`mikey-sijiao-003-K0001`、`mikey-sijiao-003-K0002`、`mikey-sijiao-003-K0004`、`mikey-sijiao-004-K0008`、`mikey-sijiao-005-K0001`、`mikey-sijiao-005-K0007`、`mikey-sijiao-011-K0008`、`mikey-sijiao-011-K0010`、`mikey-sijiao-012-K0006`、`mikey-sijiao-003-K0011`、`mikey-sijiao-004-K0001`、`mikey-sijiao-004-K0009`、`mikey-sijiao-004-K0011`、`mikey-sijiao-004-K0012`、`mikey-sijiao-006-K0005`、`mikey-sijiao-002-K0006`

**来源：** `mikey-sijiao-002`、`mikey-sijiao-005`、`mikey-sijiao-011`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-012`、`mikey-sijiao-006`

### T02｜一致性与节奏：让语言、声音、身体和日常人格对得上

**判断：** Mikey反复把‘不一致’放在比一句话术更高的位置：字面强硬但声音退缩、平时正常而搭讪突然迎合，都会让表达显得假。稳定不是永远一种状态，而是能主动选择坚定、放松、幽默，并给交流留空间。

**理由：**
- 浅沟通会让对方感到字面内容之外的状态。
- 怕失去会让人加速、抢话和填满空白。
- 自然切换状态比临场扮演一个固定角色更可持续。

**步骤：**
1. 先看自己平时说话状态，再看搭讪/约会时发生了什么变化。
2. 把语速和动作降到能正常表达。
3. 句子后留停顿，让对方有参与空间。
4. 只保留清楚目的，已练会的细节尽量自然发生。

**适用条件：**
- 非言语判断需要连续音画才能确认。
- 一致性不能用来合理化命令、强迫或无视反馈。

**观察反馈：**
- 声音和身体是否与所表达的意图一致。
- 对方是否获得说话空间。
- 自己是否能容纳空白和被截停。

**限制：**
- 006/008等条目人物和外景声音仍有待核，主要作上下文。

**命题：** `P04`、`P06`

**知识依据：** `mikey-sijiao-003-K0001`、`mikey-sijiao-004-K0008`、`mikey-sijiao-004-K0009`、`mikey-sijiao-006-K0001`、`mikey-sijiao-006-K0003`、`mikey-sijiao-006-K0007`、`mikey-sijiao-008-K0001`、`mikey-sijiao-008-K0004`、`mikey-sijiao-008-K0006`、`mikey-sijiao-009-K0002`、`mikey-sijiao-015-K0002`、`mikey-sijiao-015-K0008`、`mikey-sijiao-015-K0010`、`mikey-sijiao-017-K0004`、`mikey-sijiao-002-K0002`、`mikey-sijiao-005-K0001`、`mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0005`、`mikey-sijiao-011-K0006`、`mikey-sijiao-011-K0008`、`mikey-sijiao-011-K0010`、`mikey-sijiao-013-K0004`、`mikey-sijiao-006-K0006`

**来源：** `mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-006`、`mikey-sijiao-008`、`mikey-sijiao-009`、`mikey-sijiao-015`、`mikey-sijiao-017`、`mikey-sijiao-002`、`mikey-sijiao-005`、`mikey-sijiao-011`、`mikey-sijiao-013`

### T03｜开场、内容与意图：先让对方知道你是谁、为什么过来

**判断：** 跨期方法不是背一段完整开场，而是先取得注意力、减少销售感，随后用真实来意、当下场景和个人经历展开；兴趣要清楚但强度要匹配关系阶段。

**理由：**
- 对方没注意你时继续高速输出容易像销售。
- 当下场景和真实经历能自然生成内容，减少背稿感。
- 过度隐藏兴趣会拖成普通朋友，过早性暗示又可能越级。

**步骤：**
1. 先确认对方有注意力且方便交流。
2. 用与本人一致的方式说明真实来意。
3. 从现场和自己的真实经历展开，而非搜索固定题目。
4. 按当前关系阶段表达适量兴趣。

**适用条件：**
- 同事、路上、夜场等关系成本不同。
- 对方拒绝、继续忙或离开时结束。

**观察反馈：**
- 对方是否听清来意并开始参与。
- 交流是否形成自然来回。
- 兴趣表达是否让关系更清楚而非让压力陡增。

**限制：**
- ‘命令取得注意力’等高风险版本不纳入通用执行。

**命题：** `P05`、`P07`、`P09`

**知识依据：** `mikey-sijiao-004-K0002`、`mikey-sijiao-004-K0007`、`mikey-sijiao-005-K0002`、`mikey-sijiao-008-K0002`、`mikey-sijiao-009-K0001`、`mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0002`、`mikey-sijiao-011-K0007`、`mikey-sijiao-004-K0004`、`mikey-sijiao-008-K0005`、`mikey-sijiao-009-K0003`、`mikey-sijiao-009-K0004`、`mikey-sijiao-010-K0003`、`mikey-sijiao-010-K0006`、`mikey-sijiao-001-K0009`、`mikey-sijiao-003-K0006`、`mikey-sijiao-004-K0003`、`mikey-sijiao-005-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-012-K0003`、`mikey-sijiao-013-K0002`、`mikey-sijiao-013-K0003`、`mikey-sijiao-013-K0006`、`mikey-sijiao-015-K0004`、`mikey-sijiao-016-K0002`、`mikey-sijiao-016-K0003`、`mikey-sijiao-017-K0001`、`mikey-sijiao-018-K0001`、`mikey-sijiao-019-K0001`、`mikey-sijiao-019-K0003`

**来源：** `mikey-sijiao-004`、`mikey-sijiao-005`、`mikey-sijiao-008`、`mikey-sijiao-009`、`mikey-sijiao-011`、`mikey-sijiao-010`、`mikey-sijiao-001`、`mikey-sijiao-003`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-019`

### T04｜个性样本与共振：不要只围着对方问，也不要把自己包装成简历

**判断：** 约会或长互动里，吸引之外还需要让对方在逻辑和体验上知道你是什么样的人。真实好奇可以保留，但要把自己的经历、兴趣和状态放进双向交流。

**理由：**
- 只问对方会让对方结束时仍不了解你。
- 真实经历既提供内容，也让声音和情绪有现实感。
- 分享自己并不等于炫耀条件或单向独白。

**步骤：**
1. 区分真好奇与没话说式提问。
2. 每轮互动给出一些自己的真实信息。
3. 用对方可回应、可追问的细节，而非履历展示。
4. 观察是否形成双方投入，而不是只计算时长。

**适用条件：**
- 不能从讲者对对象心理的判断直接证明吸引。
- 双方投入才是比聊多久更有意义的观察。

**观察反馈：**
- 对方是否开始追问或主动分享。
- 是否不再只有一方连续提问。
- 对方是否在交流中获得对你的具体认识。

**限制：**
- 结果与吸引强度仍需对象本人或连续证据支持。

**命题：** `P08`

**知识依据：** `mikey-sijiao-006-K0006`、`mikey-sijiao-009-K0002`、`mikey-sijiao-009-K0003`、`mikey-sijiao-010-K0001`、`mikey-sijiao-010-K0002`、`mikey-sijiao-010-K0003`、`mikey-sijiao-010-K0004`、`mikey-sijiao-010-K0005`、`mikey-sijiao-010-K0006`、`mikey-sijiao-011-K0011`、`mikey-sijiao-015-K0002`、`mikey-sijiao-018-K0001`

**来源：** `mikey-sijiao-006`、`mikey-sijiao-009`、`mikey-sijiao-010`、`mikey-sijiao-011`、`mikey-sijiao-015`、`mikey-sijiao-018`

### T05｜反馈校准、拒绝与停止：任何推进都必须保留回退机制

**判断：** 这批材料最稳定的上位边界是：对方后退、明确拒绝、不想入镜、已有伴侣或表现明显不适时，先停止当前推进或退一步减压；任何‘隐藏兴趣’解释都不能覆盖这些信号。

**理由：**
- 001/003明确把不及时减压视为失败原因。
- 多期强调动作应随现场反馈而变，而不是复制课程动作。
- 行为信号可以作为信息，但不能覆盖明确拒绝。

**步骤：**
1. 先识别是否存在明确停止信号。
2. 有则停止当前动作、拉开距离或结束互动。
3. 没有明确拒绝但反馈变差时降低压力并观察。
4. 只有新的、清楚的正向反馈出现后才重新判断。

**适用条件：**
- 后续重新互动是新的判断，不会把之前拒绝改写成同意。
- 亲密行为另受持续同意要求约束。

**观察反馈：**
- 对方是否重新主动参与而非仅礼貌停留。
- 距离、语气、回应是否持续改善。
- 是否出现新的明确拒绝或退出。

**限制：**
- 停留、微笑、手机操作、同行都不能单独证明接受。

**命题：** `P10`、`P11`

**知识依据：** `mikey-sijiao-001-K0001`、`mikey-sijiao-001-K0005`、`mikey-sijiao-003-K0005`、`mikey-sijiao-003-K0007`、`mikey-sijiao-004-K0010`、`mikey-sijiao-005-K0008`、`mikey-sijiao-008-K0003`、`mikey-sijiao-012-K0005`、`mikey-sijiao-012-K0010`、`mikey-sijiao-017-K0005`、`mikey-sijiao-019-K0002`、`mikey-sijiao-001-K0003`、`mikey-sijiao-001-K0004`、`mikey-sijiao-006-K0003`、`mikey-sijiao-006-K0006`、`mikey-sijiao-008-K0004`、`mikey-sijiao-011-K0002`、`mikey-sijiao-015-K0009`、`mikey-sijiao-015-K0010`、`mikey-sijiao-016-K0006`、`mikey-sijiao-019-K0004`

**来源：** `mikey-sijiao-001`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-005`、`mikey-sijiao-008`、`mikey-sijiao-012`、`mikey-sijiao-017`、`mikey-sijiao-019`、`mikey-sijiao-006`、`mikey-sijiao-011`、`mikey-sijiao-015`、`mikey-sijiao-016`

### T06｜联系方式、网聊与邀约：把信号、工具、物流和真正见面拆开

**判断：** 收号不是关系结果；网聊也不是单纯追热度。更完整的链条是先建立足够的互动和安全感，再把联系方式作为连接工具，按关系阶段观察整体行为，最后提出清楚、真实、可拒绝的邀约并处理物流问题。

**理由：**
- 多期指出急于收号常来自想逃离现场压力。
- 回复速度、照片、单次分享等都不足以单独证明兴趣。
- 邀约需要时间、地点、同行者、安全、身体状况等现实条件。

**步骤：**
1. 先判断现场/线上互动是否已有基本投入。
2. 区分提出联系方式、答应、手机操作和真正完成。
3. 网聊按关系阶段和整体热度判断，不因单一信号脑补。
4. 邀约时说清真实意图，并解决时间地点、安全和临时变化。

**适用条件：**
- 对方拒绝或安全安排无法满足时允许取消。
- 手机号、位置和叫车信息不等于同意见面或后续亲密。

**观察反馈：**
- 是否真正完成添加并有后续互动。
- 是否对邀约给出明确答复。
- 物流问题是否被实际解决，而不是靠话术掩盖。

**限制：**
- 所有截图顺序、账号身份和完成状态仍按视觉/原音证据等级处理。

**命题：** `P12`、`P13`、`P14`

**知识依据：** `mikey-sijiao-006-K0002`、`mikey-sijiao-005-K0006`、`mikey-sijiao-009-K0005`、`mikey-sijiao-011-K0011`、`mikey-sijiao-019-K0006`、`mikey-sijiao-004-K0003`、`mikey-sijiao-004-K0005`、`mikey-sijiao-005-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-013-K0002`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0006`、`mikey-sijiao-015-K0004`、`mikey-sijiao-016-K0002`、`mikey-sijiao-016-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-017-K0005`、`mikey-sijiao-018-K0004`、`mikey-sijiao-019-K0001`、`mikey-sijiao-019-K0002`、`mikey-sijiao-012-K0003`、`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0005`、`mikey-sijiao-013-K0004`、`mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0003`、`mikey-sijiao-014-K0004`、`mikey-sijiao-015-K0005`、`mikey-sijiao-016-K0004`、`mikey-sijiao-017-K0001`、`mikey-sijiao-017-K0002`、`mikey-sijiao-017-K0003`、`mikey-sijiao-019-K0004`

**来源：** `mikey-sijiao-006`、`mikey-sijiao-005`、`mikey-sijiao-009`、`mikey-sijiao-011`、`mikey-sijiao-019`、`mikey-sijiao-004`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-014`

### T07｜约会与亲密推进：体验优先，结果与同意分开

**判断：** 约会的核心不是把当晚结果变成硬任务，而是看双方体验、环境、投入和当下反馈；任何亲密推进都不能由地点、酒精、过夜、停留或既往信号自动推导。

**理由：**
- 强求结果会让人急于推进并增加压力。
- 高温、环境、关系位置等会直接影响体验。
- 当场接受部分接触也不代表事后或下一步自动接受。

**步骤：**
1. 先保证基本交流、舒适和现实环境。
2. 表达当下意图并观察明确反馈。
3. 每一步亲密推进独立判断。
4. 出现迟疑、后退或拒绝立即停止/减压。

**适用条件：**
- 酒精不用于削弱判断。
- 到家、酒店、门禁、过夜或继续聊天不等于同意进一步行为。

**观察反馈：**
- 对方是否持续主动参与。
- 是否存在清楚、持续的正向反馈。
- 事后沟通是否出现反悔、冷却或重新评估。

**限制：**
- 多数高影响结果只有截图、旁白或学员单方材料。

**命题：** `P15`、`P16`

**知识依据：** `mikey-sijiao-001-K0002`、`mikey-sijiao-001-K0005`、`mikey-sijiao-003-K0008`、`mikey-sijiao-004-K0006`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0006`、`mikey-sijiao-018-K0004`、`mikey-sijiao-001-K0001`、`mikey-sijiao-001-K0003`、`mikey-sijiao-001-K0004`、`mikey-sijiao-001-K0011`、`mikey-sijiao-003-K0005`、`mikey-sijiao-004-K0010`、`mikey-sijiao-005-K0008`、`mikey-sijiao-012-K0008`、`mikey-sijiao-012-K0010`、`mikey-sijiao-013-K0007`、`mikey-sijiao-013-K0008`、`mikey-sijiao-015-K0007`、`mikey-sijiao-015-K0011`、`mikey-sijiao-016-K0007`、`mikey-sijiao-016-K0008`、`mikey-sijiao-017-K0005`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0006`、`mikey-sijiao-019-K0006`、`mikey-sijiao-019-K0007`

**来源：** `mikey-sijiao-001`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-013`、`mikey-sijiao-018`、`mikey-sijiao-005`、`mikey-sijiao-012`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-019`

### T08｜冷却、冲突与修复：先解决真正问题，而不是继续证明自己

**判断：** 对方冷淡、质疑或关系搞砸后，Mikey较稳定的可用部分是先稳住自己、减少追发和解释，识别真正问题；修复时停止礼物补偿和死缠烂打，必要时只提供一次低负担、可退出的沟通机会。

**理由：**
- 焦虑追赶会让互动进一步失衡。
- 大量解释往往是在处理自己的不安，而不是对方顾虑。
- 对方软化后继续强硬同样会显得不近人情。

**步骤：**
1. 停止连续追问、证明和礼物补偿。
2. 判断是现实问题、误解、冷却还是明确拒绝。
3. 只解释必要信息，或等待/改约。
4. 若仍有修复意愿，给一次边界清楚、成本低的沟通；对方不愿则结束。

**适用条件：**
- 重大关系信息不能用‘少解释’当作隐瞒理由。
- 推开、降温和嫉妒不作为固定操控步骤。

**观察反馈：**
- 对方是否主动恢复交流。
- 是否明确表达真实顾虑。
- 是否继续拒绝或要求停止。

**限制：**
- 修复成功与后续关系在案例中仍是单方结果主张。

**命题：** `P17`、`P18`

**知识依据：** `mikey-sijiao-001-K0006`、`mikey-sijiao-001-K0007`、`mikey-sijiao-001-K0008`、`mikey-sijiao-001-K0009`、`mikey-sijiao-013-K0006`、`mikey-sijiao-019-K0004`、`mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0003`、`mikey-sijiao-015-K0005`、`mikey-sijiao-015-K0009`、`mikey-sijiao-016-K0004`、`mikey-sijiao-016-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-017-K0002`、`mikey-sijiao-017-K0004`、`mikey-sijiao-019-K0002`、`mikey-sijiao-006-K0004`

**来源：** `mikey-sijiao-001`、`mikey-sijiao-013`、`mikey-sijiao-019`、`mikey-sijiao-014`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-006`

### T09｜标准、维护与多线风险：有选择感不等于控制别人

**判断：** Mikey多次强调不要因为外貌、欲望或单一对象失去自己的判断；关系进入持续阶段后靠正常生活连接维护。复杂关系里，材料同时承认多线是高风险策略，也承认无法保证永不暴露。

**理由：**
- 选择感能减少委屈求全和单一对象依赖。
- 普通生活连接比只在想要性结果时联系更像维护。
- 多线、隐瞒和‘被发现后话术’会持续制造风险。

**步骤：**
1. 先明确自己的关系目标和不可接受边界。
2. 对重要关系事实如实披露，保留对方选择。
3. 持续关系用普通联系、分享和约会维护。
4. 若选择多线关系，先处理各方约定、知情和风险，而不是先研究隐藏技巧。

**适用条件：**
- 个人标准不是普遍道德事实。
- 不把‘高位’、财富或男性义务当成强制价值判断。

**观察反馈：**
- 自己是否仍能接受对方拒绝。
- 双方是否清楚关系约定。
- 互动是否靠正常连接而非持续控制与危机制造。

**限制：**
- 长期关系、性结果和所谓稳定多由单方材料描述。

**命题：** `P19`、`P20`、`P21`

**知识依据：** `mikey-sijiao-001-K0009`、`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`、`mikey-sijiao-003-K0009`、`mikey-sijiao-004-K0014`、`mikey-sijiao-014-K0006`、`mikey-sijiao-016-K0001`、`mikey-sijiao-016-K0004`、`mikey-sijiao-017-K0005`、`mikey-sijiao-017-K0006`、`mikey-sijiao-017-K0008`、`mikey-sijiao-018-K0002`、`mikey-sijiao-018-K0003`、`mikey-sijiao-018-K0005`、`mikey-sijiao-019-K0008`、`mikey-sijiao-001-K0010`、`mikey-sijiao-012-K0001`、`mikey-sijiao-012-K0007`、`mikey-sijiao-012-K0008`、`mikey-sijiao-014-K0008`、`mikey-sijiao-014-K0009`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0007`

**来源：** `mikey-sijiao-001`、`mikey-sijiao-002`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-014`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-019`、`mikey-sijiao-012`

### T10｜术与道：先给新手可执行结构，再逐渐转向原理和迁移

**判断：** 跨期学习观不是‘不要技术’，而是技术与原则分阶段：没有经验时需要足够具体的动作和复盘；有经验后要理解为什么做、什么条件下做、什么时候不做，避免把第一次成功复制成僵化套路。

**理由：**
- 碎片资料过多会形成互相冲突的限制。
- 固定技术只能覆盖有限情境。
- 理解心态和原则后才能在新情境生成不同应对。

**步骤：**
1. 先判断用户处于完全不会做、会做但不稳定，还是需要迁移原则的阶段。
2. 新手给最小可执行步骤。
3. 完成后复盘条件和反馈。
4. 逐步减少对固定句子的依赖，保留判断顺序。

**适用条件：**
- 不能把导师权威或‘百分百信任’当作方法有效证据。
- 任何技巧都受拒绝、知情与安全边界约束。

**观察反馈：**
- 是否能解释为什么做，而非只复述句子。
- 换对象/场景后能否根据反馈调整。

**限制：**
- 不模仿Mikey口头禅，也不编造他没说过的原则。

**命题：** `P22`

**知识依据：** `mikey-sijiao-001-K0012`、`mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0006`、`mikey-sijiao-004-K0012`、`mikey-sijiao-006-K0007`、`mikey-sijiao-008-K0006`、`mikey-sijiao-013-K0001`、`mikey-sijiao-014-K0007`、`mikey-sijiao-014-K0010`、`mikey-sijiao-015-K0001`、`mikey-sijiao-015-K0008`、`mikey-sijiao-015-K0009`、`mikey-sijiao-015-K0010`、`mikey-sijiao-017-K0004`、`mikey-sijiao-017-K0009`

**来源：** `mikey-sijiao-001`、`mikey-sijiao-002`、`mikey-sijiao-004`、`mikey-sijiao-006`、`mikey-sijiao-008`、`mikey-sijiao-013`、`mikey-sijiao-014`、`mikey-sijiao-015`、`mikey-sijiao-017`

### T11｜情境策略：夜场、高压、同事、多人与拍摄需要单独判断

**判断：** 部分做法只在特定场景成立：夜场按时段设目标、高压力环境用于练习、同事关系降低意图强度、多人互动照顾每个人、拍摄时尊重不入镜要求。跨期综合不能把这些情境经验升级为万能规则。

**理由：**
- 社会成本、旁人、时间段和拍摄条件会改变同一句话的压力。
- 多人互动中谁被晾着会改变整体氛围。
- 不想入镜是独立边界，不因继续聊天而消失。

**步骤：**
1. 先问清场景与关系。
2. 再选择对应的意图强度、互动目标和分工。
3. 观察现场变化并允许退出。

**适用条件：**
- 情境策略不能用于推导结果保证。
- 拍摄和隐私需单独处理。

**观察反馈：**
- 场景压力是否降低。
- 参与者是否仍有空间和选择。

**限制：**
- 夜场时段与高压训练是经验性观点，不是普遍因果。

**命题：** `P23`

**知识依据：** `mikey-sijiao-003-K0007`、`mikey-sijiao-003-K0008`、`mikey-sijiao-004-K0006`、`mikey-sijiao-011-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-013-K0005`、`mikey-sijiao-016-K0003`、`mikey-sijiao-017-K0005`、`mikey-sijiao-018-K0004`、`mikey-sijiao-019-K0001`

**来源：** `mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-011`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-019`

### T12｜证据与高风险边界：保留Mikey观点，但不把包装和操控升级成事实

**判断：** 这一批跨期整合必须同时服务‘像问Mikey’和‘不伪造证据’：教学判断可作为Mikey观点，学员自述、截图、标题、推广证言、旁白结果分别保留；高风险操控策略只进冲突/边界，不进入直接建议。

**理由：**
- 视觉审查反复发现截图不是连续聊天、回放不是新案例、硬切后结果不明。
- 多个结果与课程效果只有单方证言或营销语。
- 部分来源存在绝对承诺、嫉妒、沉没成本、NPC、酒精推进等与更稳定边界冲突的内容。

**步骤：**
1. 先标归属：Mikey判断/学员自述/现场可见/截图/标题/结果主张。
2. 再判断是否有连续证据、人物确认和完整上下文。
3. 可用原则进入direct/context；结果与高风险内容进入hold/do_not_generalize。

**适用条件：**
- 所有引用只能沿输入知识ID、事件ID和SID回读。
- 不引入网页、常识或旧记忆补洞。

**观察反馈：**
- 运行时回答是否清楚区分观点与事实。
- 是否把结果主张误写成亲历或已验证因果。

**限制：**
- 验证结构闭合不等于方法有效或结果真实。

**命题：** `P24`、`P25`、`P26`

**知识依据：** `mikey-sijiao-001-K0011`、`mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0006`、`mikey-sijiao-002-K0007`、`mikey-sijiao-003-K0003`、`mikey-sijiao-003-K0010`、`mikey-sijiao-003-K0011`、`mikey-sijiao-004-K0009`、`mikey-sijiao-004-K0010`、`mikey-sijiao-004-K0011`、`mikey-sijiao-004-K0012`、`mikey-sijiao-004-K0013`、`mikey-sijiao-004-K0015`、`mikey-sijiao-005-K0004`、`mikey-sijiao-005-K0005`、`mikey-sijiao-005-K0006`、`mikey-sijiao-005-K0007`、`mikey-sijiao-005-K0008`、`mikey-sijiao-012-K0001`、`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0008`、`mikey-sijiao-012-K0009`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0008`、`mikey-sijiao-013-K0009`、`mikey-sijiao-014-K0002`、`mikey-sijiao-014-K0009`、`mikey-sijiao-014-K0010`、`mikey-sijiao-015-K0003`、`mikey-sijiao-015-K0011`、`mikey-sijiao-016-K0008`、`mikey-sijiao-017-K0003`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0006`、`mikey-sijiao-018-K0007`、`mikey-sijiao-018-K0008`、`mikey-sijiao-019-K0006`、`mikey-sijiao-019-K0007`、`mikey-sijiao-010-K0007`、`mikey-sijiao-009-K0005`、`mikey-sijiao-010-K0008`、`mikey-sijiao-003-K0009`、`mikey-sijiao-004-K0014`、`mikey-sijiao-011-K0004`、`mikey-sijiao-012-K0007`、`mikey-sijiao-013-K0007`、`mikey-sijiao-014-K0005`、`mikey-sijiao-014-K0006`、`mikey-sijiao-014-K0008`、`mikey-sijiao-015-K0006`、`mikey-sijiao-015-K0007`、`mikey-sijiao-016-K0007`、`mikey-sijiao-019-K0005`

**来源：** `mikey-sijiao-001`、`mikey-sijiao-002`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-005`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-014`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-019`、`mikey-sijiao-010`、`mikey-sijiao-009`、`mikey-sijiao-011`

## 5. 可核对命题

### P01｜训练先把目标放在可控行动，而不是把收号或性结果当唯一成功

跨期材料反复把新手阶段的首要任务放在愿意出手、完成真实互动和按当前阶段设定可完成目标；结果可记录，但不宜作为唯一训练指标。

**条件：** 适用于因害怕、完美主义或外部高标准而迟迟不行动的阶段。；进入稳定行动后，训练目标应转向质量、反馈和具体薄弱点，而不是永远只刷次数。

**相反/限制材料：** `mikey-sijiao-004-K0013`、`mikey-sijiao-005-K0006`、`mikey-sijiao-002-K0007`

**支持知识：** `mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0003`、`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`、`mikey-sijiao-005-K0005`、`mikey-sijiao-011-K0009`

**编辑说明：** 这是训练目标命题，不等于否认联系方式、约会或关系结果的价值；它强调先区分可控动作与不可控结果。

### P02｜技术要建立在能正常表达的状态上，焦虑时先慢下来

Mikey多次把过快语速、多余动作、假笑、想逃离对话和基础表达能力下降视为状态问题；先让人能正常说话、停顿和承接，再谈更复杂技巧。

**条件：** 先处理明显的慌乱、急促、逃离感，再增加技巧负荷。；松弛不等于失去边界，也不等于任何外部心理方法已经被证明长期有效。

**相反/限制材料：** `mikey-sijiao-003-K0003`、`mikey-sijiao-004-K0013`、`mikey-sijiao-005-K0007`

**支持知识：** `mikey-sijiao-002-K0002`、`mikey-sijiao-003-K0001`、`mikey-sijiao-003-K0002`、`mikey-sijiao-003-K0004`、`mikey-sijiao-004-K0008`、`mikey-sijiao-005-K0001`、`mikey-sijiao-005-K0007`、`mikey-sijiao-011-K0008`、`mikey-sijiao-011-K0010`、`mikey-sijiao-012-K0006`

**编辑说明：** 把‘内核/内在限制’保留为Mikey的解释框架；持续效果没有纵向证据。

### P03｜复盘的价值在于定位真正卡点并及时纠错，而不是机械重复

线下、录像和即时复盘被用来暴露当事人自己难以察觉的语速、姿态、意图、退缩与互动质量；发现问题后一次只改一个可观察点，再回到实战验证。

**条件：** 需要能够对应到具体互动，而不是把不同案例或回放混成一条链。；一次状态变好或课后自评不能直接证明永久改变。

**相反/限制材料：** `mikey-sijiao-003-K0003`、`mikey-sijiao-004-K0013`、`mikey-sijiao-002-K0007`、`mikey-sijiao-003-K0010`

**支持知识：** `mikey-sijiao-003-K0011`、`mikey-sijiao-004-K0001`、`mikey-sijiao-004-K0009`、`mikey-sijiao-004-K0011`、`mikey-sijiao-004-K0012`、`mikey-sijiao-006-K0005`、`mikey-sijiao-011-K0009`、`mikey-sijiao-002-K0006`

**编辑说明：** 复盘循环可以作为方法结构直接使用，但课程长期效果与服务价值仍须单独审计。

### P04｜一致性不是强硬，而是意图、声音、身体和日常人格彼此对得上

多期把‘不一致’解释为字面上很强硬、身体和声音却退缩，或搭讪时突然变成与平时不同的人；更稳定的方向是保留真实人格，并能有意识地切换坚定、放松和幽默。

**条件：** 需结合现场声音、身体距离和日常状态，不能只从一句台词判断。；一致性不授权强迫、命令或无视对方反馈。

**相反/限制材料：** `mikey-sijiao-011-K0004`、`mikey-sijiao-004-K0010`、`mikey-sijiao-005-K0008`

**支持知识：** `mikey-sijiao-003-K0001`、`mikey-sijiao-004-K0008`、`mikey-sijiao-004-K0009`、`mikey-sijiao-006-K0001`、`mikey-sijiao-006-K0003`、`mikey-sijiao-006-K0007`、`mikey-sijiao-008-K0001`、`mikey-sijiao-008-K0004`、`mikey-sijiao-008-K0006`、`mikey-sijiao-009-K0002`、`mikey-sijiao-015-K0002`、`mikey-sijiao-015-K0008`、`mikey-sijiao-015-K0010`、`mikey-sijiao-017-K0004`

**编辑说明：** 006/008等来源说话人仍有部分待核，因此这些来源对命题主要提供上下文支持。

### P05｜开场先取得注意力和可见性，再清楚说明真实来意

当对方没看你、在忙或把你当销售时，材料更支持先进入可见范围、放慢、取得注意力，再用本人一致的方式说明为何过来，而不是高速输出整套开场。

**条件：** 对方明显不方便、拒绝或继续离开时应停止。；‘取得注意力’不能被扩大成命令服从。

**相反/限制材料：** `mikey-sijiao-011-K0004`、`mikey-sijiao-009-K0001`

**支持知识：** `mikey-sijiao-004-K0002`、`mikey-sijiao-004-K0007`、`mikey-sijiao-005-K0002`、`mikey-sijiao-008-K0002`、`mikey-sijiao-009-K0001`、`mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0002`、`mikey-sijiao-011-K0007`

**编辑说明：** ‘看我’式命令在011被单独降级，不纳入该命题的通用执行。

### P06｜给对方说话空间，允许停顿和不完整句子

多期把持续高速输出解释为害怕失去和寻求认同；更好的互动节奏是说完后停顿，让对方有参与空间，接受冷场和截停失败。

**条件：** 适用于语速过快、连续自说自话或急于把整套信息说完的情境。；不能把沉默本身解释成兴趣或同意。

**相反/限制材料：** `mikey-sijiao-013-K0004`、`mikey-sijiao-006-K0006`

**支持知识：** `mikey-sijiao-002-K0002`、`mikey-sijiao-005-K0001`、`mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0005`、`mikey-sijiao-011-K0006`、`mikey-sijiao-011-K0008`、`mikey-sijiao-011-K0010`、`mikey-sijiao-013-K0004`、`mikey-sijiao-006-K0006`

**编辑说明：** 这是节奏控制原则，不是话术模板。

### P07｜自然内容从当下场景和真实个人经历里长出来

与其在脑中搜索固定题目，材料更支持从眼前发生的事情、自己的当天经历、真实兴趣和可被追问的生活细节展开。

**条件：** 内容必须真实且与当前互动有关系。；不是把履历、财富或成就做成价值展示清单。

**相反/限制材料：** `mikey-sijiao-010-K0006`、`mikey-sijiao-009-K0005`

**支持知识：** `mikey-sijiao-004-K0004`、`mikey-sijiao-008-K0005`、`mikey-sijiao-009-K0003`、`mikey-sijiao-009-K0004`、`mikey-sijiao-010-K0003`、`mikey-sijiao-010-K0006`、`mikey-sijiao-011-K0007`

**编辑说明：** 009/010中的片段只支持内容结构，不证明这些内容本身导致了结果。

### P08｜共振不仅是让对方觉得你有吸引，还要让对方真实了解你

约会和长互动里，如果一直只问对方、自己几乎没有可感知内容，对方即使觉得你‘酷’也未必知道你是谁；需要把自己的经历、兴趣和状态放进双向交流。

**条件：** 分享自己与真实好奇可以并存。；对方是否喜欢、投入或被吸引不能仅由讲者心读确认。

**相反/限制材料：** `mikey-sijiao-010-K0007`、`mikey-sijiao-006-K0006`

**支持知识：** `mikey-sijiao-006-K0006`、`mikey-sijiao-009-K0002`、`mikey-sijiao-009-K0003`、`mikey-sijiao-010-K0001`、`mikey-sijiao-010-K0002`、`mikey-sijiao-010-K0003`、`mikey-sijiao-010-K0004`、`mikey-sijiao-010-K0005`、`mikey-sijiao-010-K0006`、`mikey-sijiao-011-K0011`、`mikey-sijiao-015-K0002`、`mikey-sijiao-018-K0001`

**编辑说明：** 吸引与舒适被分开讨论，但具体对象内心判断保持Mikey解释层级。

### P09｜兴趣和邀约意图要按关系阶段清楚表达，既不隐藏也不越级

材料既反对长期把兴趣藏成普通朋友，也反对刚认识就过强性暗示；更稳定的做法是按陌生—熟悉—暧昧—约会等阶段，用可拒绝、不过度施压的方式表达当下真实意图。

**条件：** 同事、路上认识、夜场认识等社会成本和安全感不同，需要调整强度。；‘轻意图’与‘早期表达男女吸引’并不矛盾，关键是阶段、关系和压力水平。

**相反/限制材料：** `mikey-sijiao-013-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-003-K0006`

**支持知识：** `mikey-sijiao-001-K0009`、`mikey-sijiao-003-K0006`、`mikey-sijiao-004-K0003`、`mikey-sijiao-005-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-012-K0003`、`mikey-sijiao-013-K0002`、`mikey-sijiao-013-K0003`、`mikey-sijiao-013-K0006`、`mikey-sijiao-015-K0004`、`mikey-sijiao-016-K0002`、`mikey-sijiao-016-K0003`、`mikey-sijiao-017-K0001`、`mikey-sijiao-018-K0001`、`mikey-sijiao-019-K0001`、`mikey-sijiao-019-K0003`

**编辑说明：** 该命题用来协调003与012/013等来源的表面冲突。

### P10｜后退、明确拒绝、已有伴侣或不想入镜都应先被当作边界

跨期最稳定的停止逻辑是：身体后退、明确说不、不愿加联系方式、不想入镜或表达已有伴侣时，不用隐藏兴趣解释覆盖这些信号，先停止当前推进或退出。

**条件：** 之后若对方重新主动互动，只能重新判断新的互动，不追溯性地把之前拒绝改写成同意。；拒绝后的修复尝试也必须给对方真实退出空间。

**相反/限制材料：** `mikey-sijiao-012-K0005`、`mikey-sijiao-011-K0004`、`mikey-sijiao-019-K0005`

**支持知识：** `mikey-sijiao-001-K0001`、`mikey-sijiao-001-K0005`、`mikey-sijiao-003-K0005`、`mikey-sijiao-003-K0007`、`mikey-sijiao-004-K0010`、`mikey-sijiao-005-K0008`、`mikey-sijiao-008-K0003`、`mikey-sijiao-012-K0005`、`mikey-sijiao-012-K0010`、`mikey-sijiao-017-K0005`、`mikey-sijiao-019-K0002`

**编辑说明：** 这是一条用于限制其他‘行为比言语重要’或‘持续推进’说法的上位边界。

### P11｜所有靠近、升级和推拉都要随当下反馈校准，不能机械复制

Mikey多次反对‘视频里这样做，所以我也这样做’；具体动作只在当前反馈支持时继续，出现不适或压力就回退，理解理由比记时机重要。

**条件：** 反馈要以可观察行为和清楚表达为主，不能靠单方心读。；高影响亲密推进另受持续同意约束。

**相反/限制材料：** `mikey-sijiao-001-K0005`、`mikey-sijiao-016-K0007`、`mikey-sijiao-017-K0003`

**支持知识：** `mikey-sijiao-001-K0003`、`mikey-sijiao-001-K0004`、`mikey-sijiao-006-K0003`、`mikey-sijiao-006-K0006`、`mikey-sijiao-008-K0003`、`mikey-sijiao-008-K0004`、`mikey-sijiao-011-K0002`、`mikey-sijiao-012-K0005`、`mikey-sijiao-015-K0009`、`mikey-sijiao-015-K0010`、`mikey-sijiao-016-K0006`、`mikey-sijiao-019-K0004`

**编辑说明：** 这是‘术’向‘原则’迁移的核心桥梁。

### P12｜联系方式只是后续连接工具，必须拆开提议、答应、手机操作和真正完成

多期都在弱化‘收号=成功’：联系方式的价值取决于当下互动质量和后续可连接性；视觉上看到手机、扫码动作或口头答应也不能直接写成已完成添加。

**条件：** 审核时必须把提出联系方式、口头接受、拿手机、扫码/输入、完成添加、后续回复分层。；对方愿意给号码不等于同意见面或亲密行为。

**相反/限制材料：** `mikey-sijiao-005-K0006`、`mikey-sijiao-009-K0005`、`mikey-sijiao-019-K0006`

**支持知识：** `mikey-sijiao-006-K0002`、`mikey-sijiao-005-K0006`、`mikey-sijiao-009-K0005`、`mikey-sijiao-011-K0011`、`mikey-sijiao-019-K0006`

**编辑说明：** 该命题同时是方法判断和关键证据边界。

### P13｜邀约要清楚、真实、可拒绝，并先解决物流和安全感

有效邀约不是靠含糊试探，也不是靠强硬；材料更支持直接面对自己想见面的意图，同时考虑关系位置、时间、地点、同行者、安全顾虑、临时生病等现实问题。

**条件：** 对方拒绝、称病或提出安全安排时先判断并尊重真实问题。；‘晚上一起玩’等问题只是物流筛选，不是结果保证。

**相反/限制材料：** `mikey-sijiao-004-K0005`、`mikey-sijiao-017-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-019-K0001`

**支持知识：** `mikey-sijiao-004-K0003`、`mikey-sijiao-004-K0005`、`mikey-sijiao-005-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-013-K0002`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0006`、`mikey-sijiao-015-K0004`、`mikey-sijiao-016-K0002`、`mikey-sijiao-016-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-017-K0005`、`mikey-sijiao-018-K0004`、`mikey-sijiao-019-K0001`、`mikey-sijiao-019-K0002`、`mikey-sijiao-019-K0006`

**编辑说明：** 把搭讪后的即时邀约、网聊邀约和二约条件放在同一物流链上，但不合并具体案例。

### P14｜网聊按关系阶段和热度同频，慢回复或单一信号不要过度脑补

后半批案例反复强调别因慢回复、朋友圈照片或一次分享就立刻破防或下结论；看整体关系阶段、连续行为与真实邀约反馈，再决定升温、等待或降低投入。

**条件：** 单个照片、分享、回复速度和‘窗口’都可能有替代解释。；明确拒绝仍优先于任何兴趣推断。

**相反/限制材料：** `mikey-sijiao-017-K0003`、`mikey-sijiao-014-K0004`、`mikey-sijiao-012-K0003`

**支持知识：** `mikey-sijiao-012-K0003`、`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0005`、`mikey-sijiao-013-K0004`、`mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0003`、`mikey-sijiao-014-K0004`、`mikey-sijiao-015-K0005`、`mikey-sijiao-016-K0004`、`mikey-sijiao-016-K0005`、`mikey-sijiao-017-K0001`、`mikey-sijiao-017-K0002`、`mikey-sijiao-017-K0003`、`mikey-sijiao-019-K0002`、`mikey-sijiao-019-K0004`

**编辑说明：** 012的‘八二比例’只作为启发式，不写成机械规则。

### P15｜约会先保证体验和双向交流，再谈结果

从001、013、018等可归纳出：把当晚结果设成硬任务容易施压；约会项目要考虑体感环境、双方关系位置、交流质量和舒适度。

**条件：** 适用于首次或早期约会。；夜场时段策略是情境经验，不自动迁移到普通约会。

**相反/限制材料：** `mikey-sijiao-013-K0005`、`mikey-sijiao-003-K0008`

**支持知识：** `mikey-sijiao-001-K0002`、`mikey-sijiao-001-K0005`、`mikey-sijiao-003-K0008`、`mikey-sijiao-004-K0006`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0006`、`mikey-sijiao-018-K0004`

**编辑说明：** ‘体验为主’不等于回避表达意图，而是把结果作为反馈而不是任务。

### P16｜亲密推进必须独立于地点、酒精、过夜、停留或既往信号持续判断

材料中多处把到家、喝酒、停留、‘没有抵抗’、门禁或后续聊天与结果联系起来，但这些都不能替代当前清楚同意；地点与关系结果必须拆开记录。

**条件：** 任何拒绝、迟疑或后退都触发停止/减压。；酒精只能作为环境事实，不能用于削弱判断或提高‘成功率’。

**相反/限制材料：** `mikey-sijiao-013-K0007`、`mikey-sijiao-015-K0007`、`mikey-sijiao-016-K0007`、`mikey-sijiao-019-K0007`

**支持知识：** `mikey-sijiao-001-K0001`、`mikey-sijiao-001-K0003`、`mikey-sijiao-001-K0004`、`mikey-sijiao-001-K0005`、`mikey-sijiao-001-K0011`、`mikey-sijiao-003-K0005`、`mikey-sijiao-004-K0010`、`mikey-sijiao-005-K0008`、`mikey-sijiao-012-K0008`、`mikey-sijiao-012-K0010`、`mikey-sijiao-013-K0007`、`mikey-sijiao-013-K0008`、`mikey-sijiao-015-K0007`、`mikey-sijiao-015-K0011`、`mikey-sijiao-016-K0007`、`mikey-sijiao-016-K0008`、`mikey-sijiao-017-K0005`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0006`、`mikey-sijiao-019-K0006`、`mikey-sijiao-019-K0007`

**编辑说明：** 所有相关结果主张继续保持单方讲述/截图层级。

### P17｜修复先停止纠缠、礼物补偿和反复解释，再降低一次沟通负担

001最完整地给出修复链：先承认问题、停止证明和死缠烂打，如果对方仍愿意考虑，再提出边界清楚、时间成本低的一次沟通，并接受最终不合适。

**条件：** 只适用于对方仍有意愿考虑的情况；明确拒绝后不能无限重试。；短见面方案只是降低成本，不保证修复。

**相反/限制材料：** `mikey-sijiao-001-K0011`、`mikey-sijiao-001-K0005`

**支持知识：** `mikey-sijiao-001-K0006`、`mikey-sijiao-001-K0007`、`mikey-sijiao-001-K0008`、`mikey-sijiao-001-K0009`、`mikey-sijiao-013-K0006`、`mikey-sijiao-019-K0004`

**编辑说明：** 修复结果在案例中仍是单方材料，不把成功叙事写成因果证明。

### P18｜遇到冷淡、质疑或冲突先稳住自己，再决定解释、等待、软化或退出

多期反对因十几分钟未回、冷回复、身份质疑或朋友圈刺激而立刻追问、讨好或攻击；应先判断真实问题，再用最少必要解释、等待或与对方同步降温/软化。

**条件：** ‘少解释’不适用于应当如实披露的重大关系信息。；不能把推开、降温做成固定操控步骤。

**相反/限制材料：** `mikey-sijiao-014-K0008`、`mikey-sijiao-012-K0007`、`mikey-sijiao-014-K0006`

**支持知识：** `mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0003`、`mikey-sijiao-015-K0005`、`mikey-sijiao-015-K0009`、`mikey-sijiao-016-K0004`、`mikey-sijiao-016-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-017-K0002`、`mikey-sijiao-017-K0004`、`mikey-sijiao-019-K0002`、`mikey-sijiao-019-K0004`、`mikey-sijiao-006-K0004`

**编辑说明：** 014的沉没成本式推开、012的嫉妒策略被排除在可用方法之外。

### P19｜保留自己的标准和选择感，但不能靠隐瞒或高位表演获得控制

材料把不因外貌、欲望、单一对象或对方高条件而失去判断视为稳定心态；同时，不必对每个追问都逐项自证。这个原则的边界是重大关系信息仍需真实，且对方有自主选择。

**条件：** 适用于容易上头、讨好或过度自证的情境。；不能用‘框架’合理化隐瞒婚姻、多线关系或无视伴侣边界。

**相反/限制材料：** `mikey-sijiao-014-K0006`、`mikey-sijiao-014-K0008`、`mikey-sijiao-003-K0009`、`mikey-sijiao-004-K0014`

**支持知识：** `mikey-sijiao-001-K0009`、`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`、`mikey-sijiao-003-K0009`、`mikey-sijiao-004-K0014`、`mikey-sijiao-014-K0006`、`mikey-sijiao-016-K0001`、`mikey-sijiao-016-K0004`、`mikey-sijiao-017-K0005`、`mikey-sijiao-017-K0006`、`mikey-sijiao-017-K0008`、`mikey-sijiao-018-K0002`、`mikey-sijiao-018-K0003`、`mikey-sijiao-018-K0005`、`mikey-sijiao-019-K0008`

**编辑说明：** 把‘自己制定成功标准’与‘对方自主选择’同时保留。

### P20｜关系维护靠普通生活连接和持续互动，不是只在想要性结果时联系

维护被描述为分享生活、散步、约会、保持正常联系，并通过更多真实社交经验减少对单一对象的依赖。

**条件：** 具体关系形式与双方约定优先。；不能从一段案例宣称的长期结果反推方法必然有效。

**相反/限制材料：** `mikey-sijiao-001-K0011`、`mikey-sijiao-018-K0006`

**支持知识：** `mikey-sijiao-001-K0010`、`mikey-sijiao-017-K0006`、`mikey-sijiao-017-K0008`、`mikey-sijiao-018-K0005`

**编辑说明：** 001提供最直接的维护方法，018/017提供选择感与风险上下文。

### P21｜多线/多偶关系是高风险选择，不存在既多线又保证永不暴露

017明确承认多线关系无法同时保证永不暴露；与012/014的复杂关系、017的多次被发现一起看，隐瞒、风险管理和结果话术都不能被写成稳定通用法。

**条件：** 首先看各方关系约定、知情与自主选择。；任何‘被发现后话术’或隐藏技巧只能作为来源观点/风险材料。

**相反/限制材料：** `mikey-sijiao-017-K0007`、`mikey-sijiao-014-K0008`、`mikey-sijiao-012-K0007`

**支持知识：** `mikey-sijiao-012-K0001`、`mikey-sijiao-012-K0007`、`mikey-sijiao-012-K0008`、`mikey-sijiao-014-K0006`、`mikey-sijiao-014-K0008`、`mikey-sijiao-014-K0009`、`mikey-sijiao-017-K0006`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0008`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0007`

**编辑说明：** 此命题用于限制复杂关系案例的可迁移范围。

### P22｜分阶段学‘术’与‘道’，最终保留原则而不是复制第一次成功

从001、013、015等可归纳出同一学习顺序：新手先用足够具体的可执行方法开始行动；有经验后把注意力转到原理、条件、心态与反馈，从而面对新情境生成不同做法。

**条件：** 前期具体化不意味着机械套话；后期原则化也不意味着无结构。；任何方法都要回看其原始条件和反例。

**相反/限制材料：** `mikey-sijiao-014-K0010`、`mikey-sijiao-013-K0009`

**支持知识：** `mikey-sijiao-001-K0012`、`mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0006`、`mikey-sijiao-004-K0012`、`mikey-sijiao-006-K0007`、`mikey-sijiao-008-K0006`、`mikey-sijiao-013-K0001`、`mikey-sijiao-014-K0007`、`mikey-sijiao-014-K0010`、`mikey-sijiao-015-K0001`、`mikey-sijiao-015-K0008`、`mikey-sijiao-015-K0009`、`mikey-sijiao-015-K0010`、`mikey-sijiao-017-K0004`、`mikey-sijiao-017-K0009`

**编辑说明：** 这是回答模式的元结构：先判断阶段，再给理由、步骤、条件和反馈。

### P23｜夜场时段、高压力、同事、多人与拍摄都是情境策略，不能脱离场景迁移

夜场按时段调整目标、高压力场景练习、同事轻意图、多人互动分工、不想入镜即停止等，都说明Mikey的方法高度依赖场景结构。

**条件：** 先确认场景、关系、旁人、安全和拍摄条件。；情境经验不能升级为普遍规律或结果保证。

**相反/限制材料：** `mikey-sijiao-003-K0008`、`mikey-sijiao-011-K0003`、`mikey-sijiao-012-K0002`

**支持知识：** `mikey-sijiao-003-K0007`、`mikey-sijiao-003-K0008`、`mikey-sijiao-004-K0006`、`mikey-sijiao-011-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-013-K0005`、`mikey-sijiao-016-K0003`、`mikey-sijiao-017-K0005`、`mikey-sijiao-018-K0004`、`mikey-sijiao-019-K0001`

**编辑说明：** 用于回答用户问‘这个操作是不是任何地方都能用’时的限制。

### P24｜截图、自述、旁白、标题和证言只能证明‘被展示或被叙述过’，不能自动变成现场事实

这批输入的视觉审查反复发现：大量结果来自Mikey口述、学员汇报、选取截图、推广访谈或标题包装；它们可以证明发布者怎样叙述，但不能独立证明身份、完整时间线、同意、联系方式完成或镜头外结果。

**条件：** 跨期综合引用结果时必须保留证据层级。；视觉抽样只证明抽到的页面/人物/场景存在，不证明连续因果。

**支持知识：** `mikey-sijiao-001-K0011`、`mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0006`、`mikey-sijiao-002-K0007`、`mikey-sijiao-003-K0003`、`mikey-sijiao-003-K0010`、`mikey-sijiao-003-K0011`、`mikey-sijiao-004-K0009`、`mikey-sijiao-004-K0010`、`mikey-sijiao-004-K0011`、`mikey-sijiao-004-K0012`、`mikey-sijiao-004-K0013`、`mikey-sijiao-004-K0015`、`mikey-sijiao-005-K0004`、`mikey-sijiao-005-K0005`、`mikey-sijiao-005-K0006`、`mikey-sijiao-005-K0007`、`mikey-sijiao-005-K0008`、`mikey-sijiao-012-K0001`、`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0008`、`mikey-sijiao-012-K0009`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0008`、`mikey-sijiao-013-K0009`、`mikey-sijiao-014-K0002`、`mikey-sijiao-014-K0009`、`mikey-sijiao-014-K0010`、`mikey-sijiao-015-K0003`、`mikey-sijiao-015-K0011`、`mikey-sijiao-016-K0008`、`mikey-sijiao-017-K0003`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0006`、`mikey-sijiao-018-K0007`、`mikey-sijiao-018-K0008`、`mikey-sijiao-019-K0006`、`mikey-sijiao-019-K0007`、`mikey-sijiao-010-K0007`

**编辑说明：** 这是整个批次的证据总边界。

### P25｜快速成功、百分百拿下、课程长期有效或人生全面改善等推广主张不进入通用方法

多个来源出现课程证言、短期结果、绝对成功、听话照做、人生改变等表述，但缺少失败样本、完整原始记录和长期追踪；跨期综合只能把它们作为推广/单方结果主张。

**条件：** 可以用于理解发布者如何包装案例。；不能用于估算成功率或承诺用户结果。

**支持知识：** `mikey-sijiao-001-K0011`、`mikey-sijiao-002-K0007`、`mikey-sijiao-003-K0003`、`mikey-sijiao-003-K0010`、`mikey-sijiao-004-K0013`、`mikey-sijiao-004-K0015`、`mikey-sijiao-005-K0006`、`mikey-sijiao-009-K0005`、`mikey-sijiao-010-K0008`、`mikey-sijiao-012-K0008`、`mikey-sijiao-012-K0009`、`mikey-sijiao-013-K0008`、`mikey-sijiao-013-K0009`、`mikey-sijiao-014-K0009`、`mikey-sijiao-014-K0010`、`mikey-sijiao-015-K0003`、`mikey-sijiao-015-K0011`、`mikey-sijiao-016-K0008`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0006`、`mikey-sijiao-018-K0008`、`mikey-sijiao-019-K0007`

**编辑说明：** 所有此类知识在运行时至少降级为hold/context_only。

### P26｜制造嫉妒、沉没成本、NPC、命令服从、酒精推进和‘冒犯会被美化’等高风险做法不作为通用行动建议

这些内容确实存在于来源，但它们与批次中更稳定的反馈、减压、清楚意图和尊重边界原则冲突，且多涉及操控、知情选择或同意风险，因此只保留为冲突、反例或历史来源观点。

**条件：** 如用户直接询问，应先指出来源归属和高风险条件。；不得改写成成功率高的可执行模板。

**支持知识：** `mikey-sijiao-003-K0009`、`mikey-sijiao-004-K0010`、`mikey-sijiao-004-K0014`、`mikey-sijiao-005-K0008`、`mikey-sijiao-011-K0004`、`mikey-sijiao-012-K0007`、`mikey-sijiao-012-K0009`、`mikey-sijiao-013-K0007`、`mikey-sijiao-014-K0005`、`mikey-sijiao-014-K0006`、`mikey-sijiao-014-K0008`、`mikey-sijiao-015-K0006`、`mikey-sijiao-015-K0007`、`mikey-sijiao-016-K0007`、`mikey-sijiao-017-K0007`、`mikey-sijiao-019-K0005`

**编辑说明：** 在knowledge_index中对应条目优先使用do_not_generalize或hold。

## 6. 方法顺序与条件关系

### M01｜训练准备 → 真实开口

**关系：** 先把不可控结果降级为反馈，把可控行动设为训练入口

**为什么：** 行动焦虑阶段继续堆理论或高标准，会让人更难开始；先做可完成动作才有真实反馈。

**怎么做：**
1. 设定当前阶段目标（例如完成开口/一轮真实交流）
2. 进入真实场景
3. 记录最明显卡点而非只看结果

**条件：** 适用于尚未稳定行动的新手；不把刷次数当最终目标

**看什么反馈：** 是否能主动出手；是否能停留在互动里；最先暴露的状态问题是什么

**分支/停止：** 若明显慌到无法正常表达，转M02先处理状态；若能稳定行动，转M03/M04优化开场和互动。

**知识依据：** `mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0003`、`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`、`mikey-sijiao-005-K0005`、`mikey-sijiao-011-K0009`、`mikey-sijiao-002-K0002`、`mikey-sijiao-003-K0001`、`mikey-sijiao-003-K0002`、`mikey-sijiao-003-K0004`、`mikey-sijiao-004-K0008`

### M02｜真实开口 → 稳定状态

**关系：** 先稳语速、动作和承接能力，再加复杂技巧

**为什么：** 多期把急速输出、假笑、小动作和逃离感视为比话术不足更核心的问题。

**怎么做：**
1. 放慢语速
2. 减少多余动作和自我卸压式假笑
3. 允许停顿和被截停
4. 一次只练一个可观察点

**条件：** 状态问题明显时优先；不把所谓‘内在释放’长期效果当已证实

**看什么反馈：** 语言与身体是否一致；是否能给对方说话空间；是否仍因怕失去而抢输出

**分支/停止：** 状态稳定后进入M03；若对方已拒绝/后退，直接进入停止边界而非继续训练动作。

**知识依据：** `mikey-sijiao-002-K0002`、`mikey-sijiao-003-K0001`、`mikey-sijiao-003-K0002`、`mikey-sijiao-003-K0004`、`mikey-sijiao-004-K0008`、`mikey-sijiao-005-K0001`、`mikey-sijiao-005-K0007`、`mikey-sijiao-011-K0008`、`mikey-sijiao-011-K0010`、`mikey-sijiao-012-K0006`、`mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0005`、`mikey-sijiao-011-K0006`、`mikey-sijiao-013-K0004`、`mikey-sijiao-006-K0006`

### M03｜稳定状态 → 认识/开场

**关系：** 先取得注意力，再清楚说明真实来意

**为什么：** 对方没有注意力时完整输出容易像销售；透明来意减少猜测。

**怎么做：**
1. 确认对方看见/能听见你
2. 用自然语速开场
3. 说明真实来意
4. 对方不方便则结束

**条件：** 陌生场景适用；同事等高成本关系需要降低强度

**看什么反馈：** 对方是否真正转向并参与；是否仍把你当销售/推广；是否出现拒绝或离开

**分支/停止：** 出现拒绝/继续离开→停止；形成互动→M04。

**知识依据：** `mikey-sijiao-004-K0002`、`mikey-sijiao-004-K0007`、`mikey-sijiao-005-K0002`、`mikey-sijiao-008-K0002`、`mikey-sijiao-009-K0001`、`mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0002`、`mikey-sijiao-011-K0007`、`mikey-sijiao-001-K0009`、`mikey-sijiao-003-K0006`、`mikey-sijiao-004-K0003`、`mikey-sijiao-005-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-012-K0003`

### M04｜认识/开场 → 建立吸引与共振

**关系：** 用当下场景和真实经历形成双向内容，让对方逐步知道你是谁

**为什么：** 只问对方或只把台词说完，既缺个性也缺双向投入。

**怎么做：**
1. 从现场信息生成话题
2. 分享真实个人经历
3. 保留真实好奇
4. 句子后留空间让对方回应

**条件：** 分享不等于炫耀履历；不能把讲者心读当对方真实兴趣

**看什么反馈：** 对方是否追问/主动分享；双方是否都有投入；是否仍是一方采访另一方

**分支/停止：** 投入不足→降低强度或结束；形成基本共振→M05联系方式/线上连接或直接邀约。

**知识依据：** `mikey-sijiao-004-K0004`、`mikey-sijiao-008-K0005`、`mikey-sijiao-009-K0003`、`mikey-sijiao-009-K0004`、`mikey-sijiao-010-K0003`、`mikey-sijiao-010-K0006`、`mikey-sijiao-011-K0007`、`mikey-sijiao-006-K0006`、`mikey-sijiao-009-K0002`、`mikey-sijiao-010-K0001`、`mikey-sijiao-010-K0002`、`mikey-sijiao-010-K0004`、`mikey-sijiao-010-K0005`、`mikey-sijiao-011-K0011`、`mikey-sijiao-015-K0002`、`mikey-sijiao-018-K0001`

### M05｜建立吸引与共振 → 联系方式/线上连接

**关系：** 联系方式只作为继续连接的工具，不把手机动作当结果

**为什么：** 急于收号常是在逃离压力；无互动基础的号码可能没有后续价值。

**怎么做：**
1. 先确认有基本互动
2. 提出联系方式
3. 区分口头接受与实际操作
4. 确认是否完成添加并看后续互动

**条件：** 不要求每次互动必须收号；不能用手机号/微信推导见面或亲密同意

**看什么反馈：** 是否真正添加完成；是否有后续回复；线下互动是否给线上留下可延续内容

**分支/停止：** 未完成或拒绝→尊重；完成后进入M06网聊/邀约。

**知识依据：** `mikey-sijiao-006-K0002`、`mikey-sijiao-005-K0006`、`mikey-sijiao-009-K0005`、`mikey-sijiao-011-K0011`、`mikey-sijiao-019-K0006`

### M06｜联系方式/线上连接 → 邀约

**关系：** 按关系阶段和整体热度判断，再给清楚、真实、可拒绝的邀约

**为什么：** 慢回复、旧照片或单一分享都可能有多种解释；邀约需要现实物流和安全感，不只是话术。

**怎么做：**
1. 观察整体互动而非单一信号
2. 避免焦虑追发
3. 明确想见面的意图
4. 解决时间地点、同行、安全和临时变化

**条件：** 同事、夜场认识、路上认识安全感不同；对方拒绝或安全安排不满足时允许取消

**看什么反馈：** 是否给出明确邀约答复；是否主动补充时间/地点；是否出现称病、距离、同行者等现实问题

**分支/停止：** 现实问题→先解决/改约；明确拒绝→停止；接受并落实→M07约会。

**知识依据：** `mikey-sijiao-004-K0003`、`mikey-sijiao-004-K0005`、`mikey-sijiao-005-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-013-K0002`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0006`、`mikey-sijiao-015-K0004`、`mikey-sijiao-016-K0002`、`mikey-sijiao-016-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-017-K0005`、`mikey-sijiao-018-K0004`、`mikey-sijiao-019-K0001`、`mikey-sijiao-019-K0002`、`mikey-sijiao-019-K0006`、`mikey-sijiao-012-K0003`、`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0005`、`mikey-sijiao-013-K0004`、`mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0003`、`mikey-sijiao-014-K0004`、`mikey-sijiao-015-K0005`、`mikey-sijiao-016-K0004`、`mikey-sijiao-017-K0001`、`mikey-sijiao-017-K0002`、`mikey-sijiao-017-K0003`、`mikey-sijiao-019-K0004`

### M07｜邀约 → 约会/亲密推进

**关系：** 先保证约会体验和双向交流，亲密步骤逐级独立校准

**为什么：** 结果硬指标会增加压力；地点、酒精、停留和前一步接受都不能自动推出下一步同意。

**怎么做：**
1. 选择体感合理环境
2. 保持双向交流
3. 表达当前意图
4. 每一步看清楚持续反馈
5. 出现迟疑/后退/拒绝立即停止减压

**条件：** 酒精不能替代同意；到家/酒店/过夜不等于亲密同意

**看什么反馈：** 对方是否持续主动参与；是否出现压力、后退或事后冷却；事后沟通是否重新评估

**分支/停止：** 出现不适→停止/减压；约会后冷却或搞砸→M08修复；关系继续→M09维护。

**知识依据：** `mikey-sijiao-001-K0002`、`mikey-sijiao-001-K0005`、`mikey-sijiao-003-K0008`、`mikey-sijiao-004-K0006`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0006`、`mikey-sijiao-018-K0004`、`mikey-sijiao-001-K0001`、`mikey-sijiao-001-K0003`、`mikey-sijiao-001-K0004`、`mikey-sijiao-001-K0011`、`mikey-sijiao-003-K0005`、`mikey-sijiao-004-K0010`、`mikey-sijiao-005-K0008`、`mikey-sijiao-012-K0008`、`mikey-sijiao-012-K0010`、`mikey-sijiao-013-K0007`、`mikey-sijiao-013-K0008`、`mikey-sijiao-015-K0007`、`mikey-sijiao-015-K0011`、`mikey-sijiao-016-K0007`、`mikey-sijiao-016-K0008`、`mikey-sijiao-017-K0005`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0006`、`mikey-sijiao-019-K0006`、`mikey-sijiao-019-K0007`

### M08｜约会/线上关系失衡 → 修复或结束

**关系：** 先停止追赶和证明，识别真正问题，再给低负担、可退出的修复机会

**为什么：** 反复解释、礼物补偿和死缠烂打通常只处理自己的焦虑，不解决对方顾虑。

**怎么做：**
1. 停止连续追问/礼物/证明
2. 判断现实问题、误解、冷却还是明确拒绝
3. 只处理必要信息
4. 若对方仍愿意，提供一次边界清楚的沟通

**条件：** 明确拒绝后不无限重试；重大关系信息不能隐瞒

**看什么反馈：** 对方是否主动恢复；是否说出真实顾虑；是否再次拒绝

**分支/停止：** 再次拒绝→结束；恢复互动→回到M06/M07按新反馈重新判断。

**知识依据：** `mikey-sijiao-001-K0006`、`mikey-sijiao-001-K0007`、`mikey-sijiao-001-K0008`、`mikey-sijiao-001-K0009`、`mikey-sijiao-013-K0006`、`mikey-sijiao-019-K0004`、`mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0003`、`mikey-sijiao-015-K0005`、`mikey-sijiao-015-K0009`、`mikey-sijiao-016-K0004`、`mikey-sijiao-016-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-017-K0002`、`mikey-sijiao-017-K0004`、`mikey-sijiao-019-K0002`、`mikey-sijiao-006-K0004`

### M09｜关系继续 → 维护与长期选择

**关系：** 用普通生活连接维护，同时保持自己的标准和透明关系约定

**为什么：** 只为性结果联系难以形成稳定连接；单一对象依赖会放大恐惧，多线隐瞒又会持续制造风险。

**怎么做：**
1. 保持正常分享和见面
2. 明确关系目标和不可接受边界
3. 重要关系事实如实披露
4. 若多线，先处理各方约定与知情

**条件：** 个人标准不是普遍道德事实；不提供隐藏多线关系的优化方案

**看什么反馈：** 双方是否清楚关系约定；是否能接受对方拒绝；联系是否只有在索取结果时出现

**分支/停止：** 关系目标不一致→协商或结束；透明约定稳定→继续维护。

**知识依据：** `mikey-sijiao-001-K0009`、`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`、`mikey-sijiao-003-K0009`、`mikey-sijiao-004-K0014`、`mikey-sijiao-014-K0006`、`mikey-sijiao-016-K0001`、`mikey-sijiao-016-K0004`、`mikey-sijiao-017-K0005`、`mikey-sijiao-017-K0006`、`mikey-sijiao-017-K0008`、`mikey-sijiao-018-K0002`、`mikey-sijiao-018-K0003`、`mikey-sijiao-018-K0005`、`mikey-sijiao-019-K0008`、`mikey-sijiao-001-K0010`、`mikey-sijiao-012-K0001`、`mikey-sijiao-012-K0007`、`mikey-sijiao-012-K0008`、`mikey-sijiao-014-K0008`、`mikey-sijiao-014-K0009`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0007`

### M10｜任意阶段 → 复盘/原则迁移

**关系：** 每次结果都回到‘为什么、条件、反馈、下一步’，逐渐从术转向道

**为什么：** 固定成功套路无法覆盖不同对象与场景；原理和反馈才支持迁移。

**怎么做：**
1. 回读对应知识ID和原始条件
2. 区分Mikey判断与案例结果
3. 复盘什么有效/失败以及为什么
4. 下一次只改关键变量

**条件：** 不引入附件外常识补洞；高风险/结果条目按hold或do_not_generalize处理

**看什么反馈：** 是否能说明条件与反例；是否能在新场景调整而非照抄

**分支/停止：** 证据不足则明确待核，不把缺口合理化。

**知识依据：** `mikey-sijiao-001-K0012`、`mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0006`、`mikey-sijiao-004-K0012`、`mikey-sijiao-006-K0007`、`mikey-sijiao-008-K0006`、`mikey-sijiao-013-K0001`、`mikey-sijiao-014-K0007`、`mikey-sijiao-014-K0010`、`mikey-sijiao-015-K0001`、`mikey-sijiao-015-K0008`、`mikey-sijiao-015-K0009`、`mikey-sijiao-015-K0010`、`mikey-sijiao-017-K0004`、`mikey-sijiao-017-K0009`、`mikey-sijiao-001-K0011`、`mikey-sijiao-002-K0007`、`mikey-sijiao-003-K0003`、`mikey-sijiao-003-K0010`、`mikey-sijiao-003-K0011`、`mikey-sijiao-004-K0009`、`mikey-sijiao-004-K0010`、`mikey-sijiao-004-K0011`、`mikey-sijiao-004-K0013`、`mikey-sijiao-004-K0015`、`mikey-sijiao-005-K0004`、`mikey-sijiao-005-K0005`、`mikey-sijiao-005-K0006`、`mikey-sijiao-005-K0007`、`mikey-sijiao-005-K0008`、`mikey-sijiao-012-K0001`、`mikey-sijiao-012-K0004`

## 7. 冲突与不强行抹平的差异

### C01｜早期表达男女意图 vs 同事关系轻意图

- **一侧：** 003/004/005等强调不要拖太久，要让对方知道你是带着男女吸引或约会意图来互动。 依据：`mikey-sijiao-003-K0006`、`mikey-sijiao-004-K0003`、`mikey-sijiao-005-K0003`
- **另一侧：** 012明确说同事关系社会成本更高，强意图容易施压，应先轻松相处和轻量表达。 依据：`mikey-sijiao-012-K0002`
- **跨期处理：** 不强行统一为一句话术。上位规则是先判断关系阶段和社会成本：陌生社交场景可较早说明意图；同事等高成本关系降低强度，但仍避免长期伪装成完全无意图。
- **运行时规则：** 回答前先追问/判断双方是什么关系、认识多久、是否有工作或熟人网络成本。

### C02｜行为比言语权重高 vs 明确拒绝必须优先

- **一侧：** 012提出行为有时比口头推开更能反映兴趣。 依据：`mikey-sijiao-012-K0005`
- **另一侧：** 001/003/004/005等要求在后退、明确不见、不加或已有伴侣时先停/减压。 依据：`mikey-sijiao-001-K0001`、`mikey-sijiao-003-K0005`、`mikey-sijiao-004-K0010`、`mikey-sijiao-005-K0008`
- **跨期处理：** 只能把行为用于理解模糊信号，不能用来覆盖清楚拒绝。明确拒绝/后退是停止条件；之后若对方重新主动，再作为新一轮互动判断。
- **运行时规则：** 涉及拒绝时先执行停止逻辑，禁止用‘她其实想要’覆盖原话。

### C03｜坚定/带领/施压练习 vs 减压与不强求结果

- **一侧：** 006/011等谈坚定、关系压力、高压场景，011还出现‘看我’命令式带领。 依据：`mikey-sijiao-006-K0001`、`mikey-sijiao-006-K0003`、`mikey-sijiao-011-K0003`、`mikey-sijiao-011-K0004`
- **另一侧：** 001/003/012更稳定地强调按反馈、后退减压、松弛和不逼迫。 依据：`mikey-sijiao-001-K0002`、`mikey-sijiao-001-K0004`、`mikey-sijiao-003-K0005`、`mikey-sijiao-012-K0006`
- **跨期处理：** ‘坚定’保留为自己表达清楚、不逃离；不等于控制对方。命令式取得注意力降为do_not_generalize。关系压力只有在对方没有拒绝且持续参与时才有讨论空间。
- **运行时规则：** 把坚定解释为自我稳定，不把命令/施压包装成对方必须服从。

### C04｜早场收号/训练收号 vs 号码只是工具

- **一侧：** 003夜场经验把早场目标之一设为认识和收号；部分训练也会记录收号。 依据：`mikey-sijiao-003-K0008`、`mikey-sijiao-002-K0003`
- **另一侧：** 006/011明确说收号不是搭讪本身的目标，拿到无效号码没有意义。 依据：`mikey-sijiao-006-K0002`、`mikey-sijiao-011-K0011`
- **跨期处理：** 不矛盾：收号可作为特定阶段/场景的阶段性动作，但不能当成互动质量或关系结果。运行时同时追踪‘是否完成联系方式’与‘是否形成足够互动/后续连接’。
- **运行时规则：** 不要用收号数量评价整体成功。

### C05｜少解释/不自证 vs 重大关系信息必须真实披露

- **一侧：** 006/015/016反对因身份质疑、没听懂或连续追问而长篇自证。 依据：`mikey-sijiao-006-K0004`、`mikey-sijiao-015-K0005`、`mikey-sijiao-016-K0004`
- **另一侧：** 014存在已婚待离背景，却建议延后披露并增加沉没成本；该做法被高风险边界否定。 依据：`mikey-sijiao-014-K0006`、`mikey-sijiao-014-K0008`
- **跨期处理：** 少解释只适用于无关或重复的审视，不适用于会实质影响对方关系选择的信息。婚姻/伴侣/关系约定等重大信息应真实披露。
- **运行时规则：** 先判断信息是否会影响对方知情选择；会则不能用‘框架’回避。

### C06｜多分享自己 vs 不要连续自说自话

- **一侧：** 009/010强调让对方了解你，分享真实经历。 依据：`mikey-sijiao-009-K0003`、`mikey-sijiao-010-K0001`、`mikey-sijiao-010-K0003`、`mikey-sijiao-010-K0006`
- **另一侧：** 013/011强调别连续输出，要给对方空间。 依据：`mikey-sijiao-013-K0004`、`mikey-sijiao-011-K0005`、`mikey-sijiao-011-K0006`
- **跨期处理：** 目标是双向交流，不是从‘只问她’摆到‘只讲我’。分享应提供可回应的内容，并在句子间留空间。
- **运行时规则：** 回答‘该不该多讲自己’时同时说明比例不固定，以双方实际参与为反馈。

### C07｜设置要求/增加投资 vs 保留对方退出空间

- **一侧：** 014建议在感到兴趣后设要求、增加投资。 依据：`mikey-sijiao-014-K0005`
- **另一侧：** 多期强调不逼迫、可拒绝、按反馈校准。 依据：`mikey-sijiao-012-K0006`、`mikey-sijiao-005-K0003`、`mikey-sijiao-001-K0004`
- **跨期处理：** 014条目保持do_not_generalize。可用的上位原则不是‘让她投资’，而是观察双方是否自愿增加投入；任何要求都必须容易拒绝。
- **运行时规则：** 不输出以提高沉没成本为目的的任务式要求。

### C08｜推开/降温 vs 对方软化后同步软化

- **一侧：** 015讨论理解推开的理由；012/014还有嫉妒、降温和沉没成本式推开。 依据：`mikey-sijiao-015-K0009`、`mikey-sijiao-012-K0007`、`mikey-sijiao-014-K0008`
- **另一侧：** 019明确说对方软化后仍继续攻击会显得不近人情。 依据：`mikey-sijiao-019-K0004`
- **跨期处理：** 推开不是固定动作。可保留‘当互动失衡时降低投入’这一理由，但嫉妒/沉没成本等操控版本不发布；对方已经恢复善意时应重新校准。
- **运行时规则：** 先问当下反馈，不按预设时机执行推拉。

### C09｜多线关系的‘高风险高回报’叙事 vs 不可能保证不暴露

- **一侧：** 017把多偶描述为高风险高回报，并讨论被发现后的处理。 依据：`mikey-sijiao-017-K0006`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0009`
- **另一侧：** 017同时明确承认不可能既多线交往又保证永不暴露。 依据：`mikey-sijiao-017-K0008`
- **跨期处理：** 保留为风险框架而非成功策略。运行时先问各方关系约定与知情程度，不提供隐藏或欺骗的优化方案。
- **运行时规则：** 优先讨论透明约定、边界和承担后果。

### C10｜‘内在释放可持久化’ vs 材料没有长期跟踪

- **一侧：** 003中Mikey认为所谓释放后的状态能持久化。 依据：`mikey-sijiao-003-K0004`
- **另一侧：** 同一期编辑知识明确一次兴奋和观察不到内部状态不能证明永久改变。 依据：`mikey-sijiao-003-K0003`
- **跨期处理：** 把‘后台程序/释放’保留为Mikey的解释框架；跨期不主张心理学效果或持久因果。
- **运行时规则：** 回答时可解释他怎么想，但明确这是其框架，不把长期效果当事实。

### C11｜‘真实窗口可百分百拿下’ vs 信息不完整与结果未独立验证

- **一侧：** 012出现只要有真实窗口就可百分百拿下的绝对承诺。 依据：`mikey-sijiao-012-K0009`
- **另一侧：** 同一期又明确学员可能选择性呈现、导师会因信息不全判断错；性结果也只有单方转述。 依据：`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0008`
- **跨期处理：** 绝对承诺进入do_not_generalize；可保留的是‘信息不完整时用如果、不把窗口当事实’。
- **运行时规则：** 不提供成功率保证。

### C12｜把性结果当男性能力义务 vs 成功标准可按阶段自行定义

- **一侧：** 004出现‘每个男人都应具备与想认识女性发生性关系的能力’的规范性主张。 依据：`mikey-sijiao-004-K0014`
- **另一侧：** 002明确反对把发生性关系设成唯一成功标准，主张按当前训练阶段定义成功。 依据：`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`
- **跨期处理：** 不强行抹平为同一价值观。跨期运行时优先采用可操作的训练标准；004的男性义务表述只保留为来源价值主张，不作为普遍规范。
- **运行时规则：** 不要把性结果当人格或男性资格证明。

### C13｜技巧能帮助局部结果 vs 技巧不能替代底层吸引与真实互动

- **一侧：** 015承认具体技术在新手阶段可帮助取得局部结果。 依据：`mikey-sijiao-015-K0001`、`mikey-sijiao-015-K0002`
- **另一侧：** 001/014/015又强调只模仿操作、依赖技巧或复制第一次成功难以迁移。 依据：`mikey-sijiao-001-K0012`、`mikey-sijiao-014-K0007`、`mikey-sijiao-015-K0010`
- **跨期处理：** 保留分阶段模型：新手需要具体做法，但每次使用都要理解条件和反馈；经验增加后重心转到原则与一致性。
- **运行时规则：** 回答具体操作时必须同时给‘为什么、什么条件、看到什么反馈就改’。

## 8. 重复、重编码、同案剪辑与独立案例台账

### D01｜same_release_reencode

- 来源：`mikey-sijiao-007`
- canonical：`mikey-approach-027`；formal_weight：`0`
- 依据：输入 source_reuse_ledger 明确标注：规范化自动稿全文逐字一致。
- 处理：不产生新知识、不产生独立案例权重；如需使用，沿 canonical_source_id 回读既有来源。

### D02｜same_source_replay

- 来源：`mikey-sijiao-002`
- 依据：视觉审查确认约7:54–8:30重放此前自行车旁现场片段。
- 处理：重放不计为第二个独立成功/案例。

### D03｜same_source_replay

- 来源：`mikey-sijiao-006`
- 依据：室内电脑正在回放外景现场素材，视觉审查明确属于复盘而非新事件。
- 处理：屏幕回放与原外景按同一现场事件处理。

### D04｜same_source_replay

- 来源：`mikey-sijiao-008`
- 依据：酒店电脑播放现场录像，视觉审查明确回放与外景不能作为两次独立互动计数。
- 处理：去重后只保留现场+复盘两种证据层。

### D05｜cross_episode_preview_reuse

- 来源：`mikey-sijiao-009`、`mikey-sijiao-010`
- 依据：010视觉审查确认开头使用009末尾片段式预告。
- 处理：010开头沿用片段不作为新的案例、结果或额外权重。

### D06｜same_case_continuation_not_duplicate_source

- 来源：`mikey-sijiao-015`、`mikey-sijiao-016`
- 依据：016视觉审查明确本期与上期案例连续。
- 处理：两个来源仍各自保留知识权重，但案例层不能把上下集误算成两名独立学员/两个独立结果。

### D07｜within_source_distinct_cases

- 来源：`mikey-sijiao-014`
- 依据：视觉审查确认约06:28前后为两套不同案例材料、不同页面/对象。
- 处理：两案必须分开绑定截图和结果，禁止跨案拼接时间线。

### D08｜single_case_multiple_materials

- 来源：`mikey-sijiao-017`
- 依据：视觉审查确认是一名学员案例的剪辑式复盘，含多日期聊天、朋友圈、日记和结果图。
- 处理：多页材料不计为多个独立案例；各节点仍需按页面与日期分层。

### D09｜single_retold_student_case

- 来源：`mikey-sijiao-018`
- 依据：视觉审查确认学员‘老江’背景、前任、训练与后续均由Mikey串联为同一案例叙事。
- 处理：不同截图/网络素材不能拆算为额外独立案例。

### D10｜single_first_person_case

- 来源：`mikey-sijiao-019`
- 依据：视觉审查确认全片主要由Mikey串联9月26日至10月12日的多次邀约与局部页面。
- 处理：日期节点属于同一第一人称案例，不因页面切换拆成独立案例。

## 9. 回答模式（面向“直接问 Mikey”式运行）

统一回答顺序：**先判断 → 再讲为什么 → 给步骤 → 给条件/停止条件 → 告诉用户观察什么反馈 → 最后说明证据边界**。语气可以直接，但不声称自己就是 Mikey，不编造原话、亲历、对象身份或镜头外结果。

### AP01｜不敢行动/越学越不敢

**常见提问：** 我学了很多还是不敢上 / 我一紧张就脑子空白 / 我总想等准备好再开始

**回答顺序：**
1. 先判断当前阶段是不是‘行动焦虑’而不是知识不足。
2. 说明理由：继续堆标准会让不可控结果压过可控动作。
3. 给最小步骤：先完成一次真实开口或一轮交流。
4. 限定条件：不以收号或性结果作为这阶段唯一成功。
5. 让用户观察一个具体反馈，再进入复盘。

**需要补问：** 现在最大问题是完全不敢开始，还是开始后慌？；最近真实出手频率和最常见卡点是什么？

**语气：** 直接判断、减少抽象理论、把目标缩到可执行。

**知识依据：** `mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0003`、`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`、`mikey-sijiao-005-K0005`、`mikey-sijiao-011-K0009`、`mikey-sijiao-002-K0002`、`mikey-sijiao-003-K0001`、`mikey-sijiao-003-K0002`、`mikey-sijiao-003-K0004`、`mikey-sijiao-003-K0011`、`mikey-sijiao-004-K0001`、`mikey-sijiao-004-K0009`

### AP02｜开场像销售/话术感太重

**常见提问：** 别人总把我当销售 / 我开场背得很顺但很假 / 对方没听完就走

**回答顺序：**
1. 先判断是不是注意力都没拿到就开始完整输出。
2. 说明开场问题通常不只在词，而在可见性、语速、声音和真实来意。
3. 步骤：先被看见/听见→自然说明来意→留空间。
4. 条件：同事等高成本关系降低意图强度；拒绝就结束。
5. 观察对方有没有真正转向并开始参与。

**需要补问：** 你是在街头、夜场、同事还是熟人场景？；对方当时是在忙、走路、看手机还是已经停下来？

**语气：** 不先给万能开场句，先校准场景和浅沟通。

**知识依据：** `mikey-sijiao-004-K0002`、`mikey-sijiao-004-K0007`、`mikey-sijiao-005-K0002`、`mikey-sijiao-008-K0002`、`mikey-sijiao-009-K0001`、`mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0002`、`mikey-sijiao-011-K0007`、`mikey-sijiao-002-K0002`、`mikey-sijiao-005-K0001`、`mikey-sijiao-011-K0005`、`mikey-sijiao-011-K0006`、`mikey-sijiao-011-K0008`、`mikey-sijiao-011-K0010`、`mikey-sijiao-013-K0004`、`mikey-sijiao-006-K0006`、`mikey-sijiao-001-K0009`、`mikey-sijiao-003-K0006`、`mikey-sijiao-004-K0003`、`mikey-sijiao-005-K0003`

### AP03｜没话题/不知道怎么共振

**常见提问：** 聊两句就没话了 / 我一直问她问题 / 怎么传递个性样本

**回答顺序：**
1. 先判断是缺素材，还是只会搜索预设题目。
2. 理由：当下场景和自己的真实经历本来就有内容。
3. 步骤：从眼前信息切入→给一个自己的真实细节→让对方回应→继续双方都在意的分支。
4. 条件：分享自己不是报简历，也不是单向输出。
5. 观察是否形成追问、主动分享和双方投入。

**需要补问：** 你通常会问哪些问题？；你最近真正投入的事情、经历或现场发生了什么？

**语气：** 把‘话题’改成‘共同正在发生的内容’。

**知识依据：** `mikey-sijiao-004-K0004`、`mikey-sijiao-008-K0005`、`mikey-sijiao-009-K0003`、`mikey-sijiao-009-K0004`、`mikey-sijiao-010-K0003`、`mikey-sijiao-010-K0006`、`mikey-sijiao-011-K0007`、`mikey-sijiao-006-K0006`、`mikey-sijiao-009-K0002`、`mikey-sijiao-010-K0001`、`mikey-sijiao-010-K0002`、`mikey-sijiao-010-K0004`、`mikey-sijiao-010-K0005`、`mikey-sijiao-011-K0011`、`mikey-sijiao-015-K0002`、`mikey-sijiao-018-K0001`

### AP04｜该不该收号/拿到微信没后续

**常见提问：** 什么时候要微信 / 我收很多号为什么都不回 / 她拿手机了算同意吗

**回答顺序：**
1. 先判断当下互动有没有基本投入，不把收号当逃离按钮。
2. 说明联系方式只是后续连接工具。
3. 步骤拆开：提出→口头接受→手机操作→完成添加→后续互动。
4. 条件：任何一步失败都不能倒写成成功。
5. 观察线下是否留下可延续内容、线上是否真实回复。

**需要补问：** 你们收号前实际聊了多久、双方谁在投入？；你看到的是口头答应、扫码动作还是已完成添加？

**语气：** 先拆层级，再谈技巧。

**知识依据：** `mikey-sijiao-006-K0002`、`mikey-sijiao-005-K0006`、`mikey-sijiao-009-K0005`、`mikey-sijiao-011-K0011`、`mikey-sijiao-019-K0006`

### AP05｜网聊冷淡/慢回复/照片信号

**常见提问：** 她回复慢是不是没兴趣 / 朋友圈像别人拍的要不要质问 / 她主动发照片是不是窗口

**回答顺序：**
1. 先否定单一信号的确定解释。
2. 看关系阶段、整体热度和连续行为。
3. 不要因焦虑追发或嫉妒质问。
4. 有邀约目标就清楚提出，并看真实答复。
5. 如果明确拒绝，停止；如果只是未回复，先稳住。

**需要补问：** 你们认识方式、见过几次、最近谁更主动？；有没有明确邀约和明确答复？

**语气：** 先去脑补，再看可验证行为。

**知识依据：** `mikey-sijiao-012-K0003`、`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0005`、`mikey-sijiao-013-K0004`、`mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0003`、`mikey-sijiao-014-K0004`、`mikey-sijiao-015-K0005`、`mikey-sijiao-016-K0004`、`mikey-sijiao-016-K0005`、`mikey-sijiao-017-K0001`、`mikey-sijiao-017-K0002`、`mikey-sijiao-017-K0003`、`mikey-sijiao-019-K0002`、`mikey-sijiao-019-K0004`、`mikey-sijiao-016-K0002`、`mikey-sijiao-016-K0006`、`mikey-sijiao-017-K0005`

### AP06｜要不要推进/亲密升级

**常见提问：** 她没抵抗是不是可以继续 / 到我家/酒店是不是窗口 / 喝酒后怎么推进

**回答顺序：**
1. 先判断当前有没有清楚、持续的正向反馈；前一步接受不自动等于下一步。
2. 理由：材料本身多次承认当场接受后也可能事后重新评估。
3. 步骤：每一步独立确认；后退、迟疑、拒绝就停和减压。
4. 条件：酒精、地点、过夜、门禁、手机号都不能替代同意。
5. 观察对方是否持续主动参与，而不是只停留或配合。

**需要补问：** 她有没有明确说愿意，还是只是没有拒绝？；有没有酒精、距离后退、迟疑或事后冷却？

**语气：** 先边界后推进，不把结果当硬任务。

**知识依据：** `mikey-sijiao-001-K0001`、`mikey-sijiao-001-K0005`、`mikey-sijiao-003-K0005`、`mikey-sijiao-003-K0007`、`mikey-sijiao-004-K0010`、`mikey-sijiao-005-K0008`、`mikey-sijiao-008-K0003`、`mikey-sijiao-012-K0005`、`mikey-sijiao-012-K0010`、`mikey-sijiao-017-K0005`、`mikey-sijiao-019-K0002`、`mikey-sijiao-001-K0003`、`mikey-sijiao-001-K0004`、`mikey-sijiao-006-K0003`、`mikey-sijiao-006-K0006`、`mikey-sijiao-008-K0004`、`mikey-sijiao-011-K0002`、`mikey-sijiao-015-K0009`、`mikey-sijiao-015-K0010`、`mikey-sijiao-016-K0006`、`mikey-sijiao-019-K0004`、`mikey-sijiao-001-K0011`、`mikey-sijiao-012-K0008`、`mikey-sijiao-013-K0007`、`mikey-sijiao-013-K0008`、`mikey-sijiao-015-K0007`、`mikey-sijiao-015-K0011`、`mikey-sijiao-016-K0007`、`mikey-sijiao-016-K0008`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0006`、`mikey-sijiao-019-K0006`、`mikey-sijiao-019-K0007`

### AP07｜邀约被拒/临时变卦/安全顾虑

**常见提问：** 她说太远不来还劝吗 / 她临时说病了是不是借口 / 二约她要带闺蜜怎么办

**回答顺序：**
1. 先判断是明确拒绝、现实问题还是安全安排，不先把它解释成测试。
2. 清楚自己的邀约意图和可接受条件。
3. 现实问题能解决就解决/改约；安全安排不合适就允许取消。
4. 明确拒绝就停止，不焦虑追赶。
5. 后续若对方重新主动，再按新互动判断。

**需要补问：** 她原话是什么？；有没有替代时间、地点或安排？；你们此前见过几次、关系位置怎样？

**语气：** 把物流和边界先处理，再谈吸引。

**知识依据：** `mikey-sijiao-004-K0003`、`mikey-sijiao-004-K0005`、`mikey-sijiao-005-K0003`、`mikey-sijiao-012-K0002`、`mikey-sijiao-013-K0002`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0006`、`mikey-sijiao-015-K0004`、`mikey-sijiao-016-K0002`、`mikey-sijiao-016-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-017-K0005`、`mikey-sijiao-018-K0004`、`mikey-sijiao-019-K0001`、`mikey-sijiao-019-K0002`、`mikey-sijiao-019-K0006`、`mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0003`、`mikey-sijiao-015-K0005`、`mikey-sijiao-015-K0009`、`mikey-sijiao-016-K0004`

### AP08｜关系搞砸/怎么修复

**常见提问：** 第一次约会推进过头怎么救 / 她说不合适我该解释吗 / 送礼能不能挽回

**回答顺序：**
1. 先判断真正问题是不是施压、纠缠、误解或现实条件。
2. 停止连续解释、哄和礼物补偿。
3. 如果对方仍愿意考虑，只给一次时间成本低、边界清楚的沟通。
4. 听她真实顾虑，不急着放标准或证明价值。
5. 如果她仍明确不愿意，就结束。

**需要补问：** 她明确拒绝到什么程度？；问题发生后你发了多少解释/追问？；她有没有主动给出继续沟通空间？

**语气：** 先止损再修复，绝不把‘坚持’当成无限重试。

**知识依据：** `mikey-sijiao-001-K0006`、`mikey-sijiao-001-K0007`、`mikey-sijiao-001-K0008`、`mikey-sijiao-001-K0009`、`mikey-sijiao-013-K0006`、`mikey-sijiao-019-K0004`、`mikey-sijiao-001-K0001`、`mikey-sijiao-001-K0005`

### AP09｜容易上头/想保持框架

**常见提问：** 遇到很喜欢的女生我就失去判断 / 她条件高我就想讨好 / 怎么保持自己的标准

**回答顺序：**
1. 先判断你是不是因为外貌、稀缺感或单一对象依赖把对方设成例外。
2. 把自己的关系目标和底线说清楚。
3. 减少无关自证和服务性讨好，但重大关系事实要真实。
4. 接受对方可以拒绝你。
5. 观察自己是否仍能按同一标准判断，而不是为了拿结果修改底线。

**需要补问：** 你真正想要什么关系？；你现在为了这个人放弃了哪些原本标准？

**语气：** 强调选择感，不表演高位、不控制别人。

**知识依据：** `mikey-sijiao-001-K0009`、`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`、`mikey-sijiao-003-K0009`、`mikey-sijiao-004-K0014`、`mikey-sijiao-014-K0006`、`mikey-sijiao-016-K0001`、`mikey-sijiao-016-K0004`、`mikey-sijiao-017-K0005`、`mikey-sijiao-017-K0006`、`mikey-sijiao-017-K0008`、`mikey-sijiao-018-K0002`、`mikey-sijiao-018-K0003`、`mikey-sijiao-018-K0005`、`mikey-sijiao-019-K0008`、`mikey-sijiao-001-K0010`

### AP10｜想照抄某个Mikey操作

**常见提问：** 我能不能直接照他说的做 / 这个推拉什么时候用 / 这一句是不是万能话术

**回答顺序：**
1. 先说不能只按句子复制，先找这招在原案例解决什么问题。
2. 回到原知识ID的条件、对象、阶段和反馈。
3. 给‘为什么→最小动作→什么反馈继续/停止’。
4. 若涉及嫉妒、沉没成本、NPC、酒精推进、命令或冒犯，标为hold/do_not_generalize，不给通用模板。
5. 最后说明哪些结果只是单方材料。

**需要补问：** 你想复制的是哪一招、你现在的情境与原案例哪里相同/不同？

**语气：** 像教练复盘，不像台词库。

**知识依据：** `mikey-sijiao-001-K0012`、`mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0006`、`mikey-sijiao-004-K0012`、`mikey-sijiao-006-K0007`、`mikey-sijiao-008-K0006`、`mikey-sijiao-013-K0001`、`mikey-sijiao-014-K0007`、`mikey-sijiao-014-K0010`、`mikey-sijiao-015-K0001`、`mikey-sijiao-015-K0008`、`mikey-sijiao-015-K0009`、`mikey-sijiao-015-K0010`、`mikey-sijiao-017-K0004`、`mikey-sijiao-017-K0009`、`mikey-sijiao-003-K0009`、`mikey-sijiao-004-K0010`、`mikey-sijiao-004-K0014`、`mikey-sijiao-005-K0008`、`mikey-sijiao-011-K0004`、`mikey-sijiao-012-K0007`、`mikey-sijiao-012-K0009`、`mikey-sijiao-013-K0007`、`mikey-sijiao-014-K0005`、`mikey-sijiao-014-K0006`、`mikey-sijiao-014-K0008`、`mikey-sijiao-015-K0006`、`mikey-sijiao-015-K0007`、`mikey-sijiao-016-K0007`、`mikey-sijiao-017-K0007`、`mikey-sijiao-019-K0005`

### AP11｜问‘这个案例到底证明了什么’

**常见提问：** 这能证明她喜欢吗 / 这能证明课程有效吗 / 截图不是证据吗

**回答顺序：**
1. 先给证据层级判断。
2. 把Mikey教学判断、学员自述、现场可见、聊天截图、标题包装和结果主张分开。
3. 说明截图/静帧实际能证明到哪一步。
4. 指出硬切、回放、角色或完整性缺口。
5. 只在支持范围内给结论，不用常识补洞。

**语气：** 编辑审计口吻，短而明确。

**知识依据：** `mikey-sijiao-001-K0011`、`mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0006`、`mikey-sijiao-002-K0007`、`mikey-sijiao-003-K0003`、`mikey-sijiao-003-K0010`、`mikey-sijiao-003-K0011`、`mikey-sijiao-004-K0009`、`mikey-sijiao-004-K0010`、`mikey-sijiao-004-K0011`、`mikey-sijiao-004-K0012`、`mikey-sijiao-004-K0013`、`mikey-sijiao-004-K0015`、`mikey-sijiao-005-K0004`、`mikey-sijiao-005-K0005`、`mikey-sijiao-005-K0006`、`mikey-sijiao-005-K0007`、`mikey-sijiao-005-K0008`、`mikey-sijiao-012-K0001`、`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0008`、`mikey-sijiao-012-K0009`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0008`、`mikey-sijiao-013-K0009`、`mikey-sijiao-014-K0002`、`mikey-sijiao-014-K0009`、`mikey-sijiao-014-K0010`、`mikey-sijiao-015-K0003`、`mikey-sijiao-015-K0011`、`mikey-sijiao-016-K0008`、`mikey-sijiao-017-K0003`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0010`、`mikey-sijiao-018-K0006`、`mikey-sijiao-018-K0007`、`mikey-sijiao-018-K0008`、`mikey-sijiao-019-K0006`、`mikey-sijiao-019-K0007`、`mikey-sijiao-010-K0007`、`mikey-sijiao-009-K0005`、`mikey-sijiao-010-K0008`

## 10. 视觉校准台账

### mikey-sijiao-001｜sparse_survey_complete_selected_source_frames_checked_continuous_av_pending

- 主体是聊天截图、女性照片、Mikey画中画讲解与编辑字幕，不是现场约会连续录像。
- 11:40静帧可见对方明确表达‘不见面’，后续短时咖啡邀约不能倒写成当时已接受。
- 17:16与19:19等结果只证明学员/群聊式汇报文字被展示。
- **跨期修正：** 成功挽回、反应很好、发生关系、长期关系等继续标为学员/发布者主张；截图不证明现场动作、同意或身份。
- **影响知识：** `mikey-sijiao-001-K0001`、`mikey-sijiao-001-K0002`、`mikey-sijiao-001-K0003`、`mikey-sijiao-001-K0004`、`mikey-sijiao-001-K0005`、`mikey-sijiao-001-K0006`、`mikey-sijiao-001-K0007`、`mikey-sijiao-001-K0008`、`mikey-sijiao-001-K0009`、`mikey-sijiao-001-K0010`、`mikey-sijiao-001-K0011`、`mikey-sijiao-001-K0012`

### mikey-sijiao-002｜sparse_survey_complete_selected_source_frames_checked_continuous_av_pending

- 现场、采访和重放交错；7:54–8:30重放不能计第二次案例。
- 手机被拿出/操作只证明出现过手机动作，不能确认添加完成。
- 3:06–7:46主要是推广/复盘采访语境。
- **跨期修正：** 课程效果与三天变化保留学员推广证言层级；现场收号与拒绝需连续音画。
- **影响知识：** `mikey-sijiao-002-K0001`、`mikey-sijiao-002-K0002`、`mikey-sijiao-002-K0003`、`mikey-sijiao-002-K0004`、`mikey-sijiao-002-K0005`、`mikey-sijiao-002-K0006`、`mikey-sijiao-002-K0007`

### mikey-sijiao-003｜sparse_survey_complete_selected_source_frames_checked_continuous_av_pending

- 机场、课堂、自拍、街头、室内复盘和证言存在多次硬切，不能拼成连续因果链。
- 13:09–18:57现场段可见人物和手机，但说话人、后退、收号与拍摄同意仍待连续核验。
- 18:57后是课程证言。
- **跨期修正：** 冥想/释放持续效果、收号、课程效果与结果都不能由抽样画面独立证明。
- **影响知识：** `mikey-sijiao-003-K0001`、`mikey-sijiao-003-K0002`、`mikey-sijiao-003-K0003`、`mikey-sijiao-003-K0004`、`mikey-sijiao-003-K0005`、`mikey-sijiao-003-K0006`、`mikey-sijiao-003-K0007`、`mikey-sijiao-003-K0008`、`mikey-sijiao-003-K0009`、`mikey-sijiao-003-K0010`、`mikey-sijiao-003-K0011`

### mikey-sijiao-004｜sparse_survey_complete_selected_source_frames_checked_continuous_av_pending

- 前33分钟多组现场与室内复盘交错；33:15后为长谈，43:26后为访谈/证言。
- 多人互动与手机操作无法靠单帧确定角色或完成结果。
- 25–30分钟出现伴侣/不加等边界，需要连续人物顺序。
- **跨期修正：** 现场行为、事后解释、个人履历和推广证言分层；收号、拒绝、成功率与心理判断不由静帧升级。
- **影响知识：** `mikey-sijiao-004-K0001`、`mikey-sijiao-004-K0002`、`mikey-sijiao-004-K0003`、`mikey-sijiao-004-K0004`、`mikey-sijiao-004-K0005`、`mikey-sijiao-004-K0006`、`mikey-sijiao-004-K0007`、`mikey-sijiao-004-K0008`、`mikey-sijiao-004-K0009`、`mikey-sijiao-004-K0010`、`mikey-sijiao-004-K0011`、`mikey-sijiao-004-K0012`、`mikey-sijiao-004-K0013`、`mikey-sijiao-004-K0014`、`mikey-sijiao-004-K0015`

### mikey-sijiao-005｜sparse_survey_complete_continuous_av_pending

- 白天/夜间多轮街头互动频繁切换，不能把不同女性合成一案。
- 镜头透视无法独立确认标题‘一米六’或精确身高差。
- 两个顺序窗口均未显示足以确认联系方式添加完成的画面。
- **跨期修正：** 14个微信、七八次拒绝、身高影响和课程变化继续保留学员自述/编辑统计层级。
- **影响知识：** `mikey-sijiao-005-K0001`、`mikey-sijiao-005-K0002`、`mikey-sijiao-005-K0003`、`mikey-sijiao-005-K0004`、`mikey-sijiao-005-K0005`、`mikey-sijiao-005-K0006`、`mikey-sijiao-005-K0007`、`mikey-sijiao-005-K0008`

### mikey-sijiao-006｜sparse_survey_complete_selected_source_frames_checked_continuous_av_pending

- 多个现场与酒店电脑复盘交错；室内电脑是回放，不是新案例。
- 室内机位可确认Mikey与学员位置，但不能自动套到全部外景声音。
- 手机出现不能确认添加成功。
- **跨期修正：** 坚定、注意力、浅沟通等属于复盘判断；不同对象按不同案例处理，回放去重。
- **影响知识：** `mikey-sijiao-006-K0001`、`mikey-sijiao-006-K0002`、`mikey-sijiao-006-K0003`、`mikey-sijiao-006-K0004`、`mikey-sijiao-006-K0005`、`mikey-sijiao-006-K0006`、`mikey-sijiao-006-K0007`

### mikey-sijiao-008｜sparse_survey_complete_selected_source_frames_checked_continuous_av_pending

- 商场现场与酒店复盘频繁切换；电脑回放与外景原片不得重复计数。
- 室内可确认Mikey右侧、学员打码，但外景逐句归属未完全核。
- 一致性是Mikey复盘解释，不是对象内心事实。
- **跨期修正：** 现场行为、Mikey复盘、学员回应三层分开；成功结果保持未确认。
- **影响知识：** `mikey-sijiao-008-K0001`、`mikey-sijiao-008-K0002`、`mikey-sijiao-008-K0003`、`mikey-sijiao-008-K0004`、`mikey-sijiao-008-K0005`、`mikey-sijiao-008-K0006`

### mikey-sijiao-009｜sparse_survey_complete_selected_source_frames_checked_continuous_av_pending

- 正片为多位女性、多地点的夜间现场，不是一条连续互动。
- 暗光窗口无法稳定识别人脸、动作、拒绝、接触或收号。
- 片尾预告与课程广告不是本期结果证据。
- **跨期修正：** 纯享片段只支持互动结构，不支持训练效果或后续结果证明。
- **影响知识：** `mikey-sijiao-009-K0001`、`mikey-sijiao-009-K0002`、`mikey-sijiao-009-K0003`、`mikey-sijiao-009-K0004`、`mikey-sijiao-009-K0005`

### mikey-sijiao-010｜sparse_survey_complete_selected_source_frames_checked_continuous_av_pending

- 开头复用009末尾预告；大部分是一段夜间约会/餐桌谈话，Mikey红框画中画持续讲解。
- 现场对话、Mikey后期讲解和编辑字幕是三个证据层。
- 35分钟后街头画面与餐桌场景有断点，不能自动视为同一因果链。
- **跨期修正：** 个性样本等可作为Mikey复盘观点；对象心理与片尾结果仍是讲者解释/回述。
- **影响知识：** `mikey-sijiao-010-K0001`、`mikey-sijiao-010-K0002`、`mikey-sijiao-010-K0003`、`mikey-sijiao-010-K0004`、`mikey-sijiao-010-K0005`、`mikey-sijiao-010-K0006`、`mikey-sijiao-010-K0007`、`mikey-sijiao-010-K0008`

### mikey-sijiao-011｜sampled_visual_review_complete

- 室内黑色ESSENTIALS者为Mikey、灰衣背对镜头者为学员；街头与室内复盘多次硬切。
- 380–388秒女性低头看手机，随后硬切复盘；‘我命令他’只证明Mikey复盘中说过。
- 多个街搭窗口彼此独立。
- **跨期修正：** ‘加微信后放松’和‘看我’不能当现场已执行/已接受的事实；低头、停留、微笑不证明兴趣。
- **影响知识：** `mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0002`、`mikey-sijiao-011-K0003`、`mikey-sijiao-011-K0004`、`mikey-sijiao-011-K0005`、`mikey-sijiao-011-K0006`、`mikey-sijiao-011-K0007`、`mikey-sijiao-011-K0008`、`mikey-sijiao-011-K0009`、`mikey-sijiao-011-K0010`、`mikey-sijiao-011-K0011`

### mikey-sijiao-012｜sampled_visual_review_complete_continuous_av_pending

- 主体是Mikey口播加教练聊天、长文、PDF和语音缩略图，没有女同事线下连续录像。
- 大量屏幕材料是学员与Mikey的教练聊天，不是目标女性的第一手完整对话。
- 学员长段复盘属于单方汇报。
- **跨期修正：** 四人关系、示好、私密空间、性结果和持续关系不因出现截图而升级；绝对成功承诺仍是营销式主张。
- **影响知识：** `mikey-sijiao-012-K0001`、`mikey-sijiao-012-K0002`、`mikey-sijiao-012-K0003`、`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0005`、`mikey-sijiao-012-K0006`、`mikey-sijiao-012-K0007`、`mikey-sijiao-012-K0008`、`mikey-sijiao-012-K0009`、`mikey-sijiao-012-K0010`

### mikey-sijiao-013｜sampled_visual_review_complete_continuous_av_pending

- 主体是Mikey口播，插入教练聊天和局部目标聊天，没有三次约会现场录像。
- 页面为编辑式插入，不能自动拼成连续聊天。
- 32度公园、餐厅、家中第三约与8月24日结果主要由讲解串联。
- **跨期修正：** 三次约会、家中邀约、饮酒和性结果保持单方叙述；‘听话照做所以成功’不作为因果。
- **影响知识：** `mikey-sijiao-013-K0001`、`mikey-sijiao-013-K0002`、`mikey-sijiao-013-K0003`、`mikey-sijiao-013-K0004`、`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0006`、`mikey-sijiao-013-K0007`、`mikey-sijiao-013-K0008`、`mikey-sijiao-013-K0009`

### mikey-sijiao-014｜sampled_visual_review_complete_continuous_av_pending

- 确有两套案例材料，约06:28前后必须分案。
- 没有机场收号或约会连续录像；不同聊天界面和头像不能合并。
- 学员长段汇报与‘最近不缺她了’等是服务聊天/评价。
- **跨期修正：** 家庭披露、对象投资、沉没成本与所谓结果必须分案并保留单方材料；高影响策略不得由静帧升级。
- **影响知识：** `mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0002`、`mikey-sijiao-014-K0003`、`mikey-sijiao-014-K0004`、`mikey-sijiao-014-K0005`、`mikey-sijiao-014-K0006`、`mikey-sijiao-014-K0007`、`mikey-sijiao-014-K0008`、`mikey-sijiao-014-K0009`、`mikey-sijiao-014-K0010`

### mikey-sijiao-015｜sampled_visual_review_complete_continuous_av_pending

- 主体是Mikey口播，穿插影视/网络素材、教练聊天和少量目标聊天，没有酒吧/邀约/约会连续现场。
- 至少包含教练聊天、当前对象和另一更喜欢对象三种材料层。
- 影视/课程素材不是本案证据。
- **跨期修正：** 需求加后缀等可作为建议记录；实际发送、喝酒、约出和最终结果继续待核。
- **影响知识：** `mikey-sijiao-015-K0001`、`mikey-sijiao-015-K0002`、`mikey-sijiao-015-K0003`、`mikey-sijiao-015-K0004`、`mikey-sijiao-015-K0005`、`mikey-sijiao-015-K0006`、`mikey-sijiao-015-K0007`、`mikey-sijiao-015-K0008`、`mikey-sijiao-015-K0009`、`mikey-sijiao-015-K0010`、`mikey-sijiao-015-K0011`

### mikey-sijiao-016｜sampled_visual_review_complete

- 与015同一案例连续，但视频仍是Mikey对聊天与学员经历的讲解，不是约会现场。
- 聊天页能定位邀约、等待、称病、改约等节点，不能自动证明气泡角色和完整上下文。
- 影视素材只是概念说明。
- **跨期修正：** 称病、门禁、到达和完成约会等结果继续为讲者叙述/局部截图；地点不等于进一步同意。
- **影响知识：** `mikey-sijiao-016-K0001`、`mikey-sijiao-016-K0002`、`mikey-sijiao-016-K0003`、`mikey-sijiao-016-K0004`、`mikey-sijiao-016-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-016-K0007`、`mikey-sijiao-016-K0008`

### mikey-sijiao-017｜sampled_visual_review_complete

- 一名学员的剪辑式复盘，穿插教练聊天、对象聊天、朋友圈、照片、日记与推广。
- 不同气泡既可能是学员向Mikey汇报，也可能是对象聊天。
- 三次约会、多线关系、被发现和见家长主要由Mikey串联。
- **跨期修正：** 旧照邀约暗示是Mikey解读；抱团邀约需保留安全顾虑；多线和长期结果均非独立验证。
- **影响知识：** `mikey-sijiao-017-K0001`、`mikey-sijiao-017-K0002`、`mikey-sijiao-017-K0003`、`mikey-sijiao-017-K0004`、`mikey-sijiao-017-K0005`、`mikey-sijiao-017-K0006`、`mikey-sijiao-017-K0007`、`mikey-sijiao-017-K0008`、`mikey-sijiao-017-K0009`、`mikey-sijiao-017-K0010`

### mikey-sijiao-018｜sampled_visual_review_complete

- ‘老江’背景、前任、冲突、训练和后续变化由Mikey讲述，没有连续当事人记录。
- 社交资料、局部结果截图与影视/网络说明素材并存，不能混成同一证据链。
- 后半段人生、工作、商业改变是论证与推广包装。
- **跨期修正：** 前任多人关系、肢体冲突、酒店转场、后二约和人生全面改变均保持单方/推广层级。
- **影响知识：** `mikey-sijiao-018-K0001`、`mikey-sijiao-018-K0002`、`mikey-sijiao-018-K0003`、`mikey-sijiao-018-K0004`、`mikey-sijiao-018-K0005`、`mikey-sijiao-018-K0006`、`mikey-sijiao-018-K0007`、`mikey-sijiao-018-K0008`

### mikey-sijiao-019｜sampled_visual_review_complete

- 215–300秒顺序帧确认先播放约20秒语音，随后Mikey解释，再出现聊天截图；三者不是同镜头即时对话。
- 多日期聊天为局部页面，没有未删节导出。
- 位置、叫车、手机号、到楼下、过夜和后续主动分属不同证据节点。
- **跨期修正：** 手机号/位置不等同于见面同意；到家、过夜和后续主动继续是Mikey第一人称结果主张；语音逐字内容待原音听校。
- **影响知识：** `mikey-sijiao-019-K0001`、`mikey-sijiao-019-K0002`、`mikey-sijiao-019-K0003`、`mikey-sijiao-019-K0004`、`mikey-sijiao-019-K0005`、`mikey-sijiao-019-K0006`、`mikey-sijiao-019-K0007`、`mikey-sijiao-019-K0008`

## 11. 可追溯性问题

### TR01｜ASR_and_audio｜blocking_or_major_by_source

- 来源：`mikey-sijiao-001`、`mikey-sijiao-002`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-005`、`mikey-sijiao-006`、`mikey-sijiao-008`、`mikey-sijiao-009`、`mikey-sijiao-010`、`mikey-sijiao-011`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-014`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-019`
- 问题：自动稿整体未逐句听校；部分来源有长压缩、错词、否定词或语音附件，019约20秒语音还未逐字核验。
- 处理：跨期只引用知识对象已给出的含义与SID；涉及拒绝、数字、人物、结果和高影响建议时保持原有hold/边界，不自行修词补义。

### TR02｜speaker_attribution｜blocking

- 来源：`mikey-sijiao-002`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-005`、`mikey-sijiao-006`、`mikey-sijiao-008`、`mikey-sijiao-009`、`mikey-sijiao-010`、`mikey-sijiao-011`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-014`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`
- 问题：Mikey、学员、对象、旁白、摄影者以及教练聊天/对象聊天的逐句归属并非全部完成。
- 处理：knowledge_index中candidate_only与未分离说话人的条目不升为direct；视觉能确认的室内身份只在对应机位使用。

### TR03｜chat_screen_order_and_roles｜blocking

- 来源：`mikey-sijiao-001`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-014`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-019`
- 问题：截图常为编辑式插入，绿/白气泡、头像、日期、教练聊天与目标对象聊天不能仅凭颜色或展示顺序自动映射。
- 处理：只把画面当作‘视频展示过该页/文字’证据；不补齐漏页，不把教练建议误写成对象回复。

### TR04｜refusal_stop_and_consent｜blocking

- 来源：`mikey-sijiao-001`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-005`、`mikey-sijiao-008`、`mikey-sijiao-011`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-019`
- 问题：明确拒绝后的停止、身体后退、伴侣边界、拍摄意愿、酒精与亲密行为均有高影响边界。
- 处理：运行时优先采用P10/P16：明确拒绝和后退触发停止；后续继续聊天不追溯改写为之前的同意。

### TR05｜contact_exchange｜blocking

- 来源：`mikey-sijiao-002`、`mikey-sijiao-004`、`mikey-sijiao-005`、`mikey-sijiao-006`、`mikey-sijiao-008`、`mikey-sijiao-009`、`mikey-sijiao-011`、`mikey-sijiao-019`
- 问题：静帧/字幕经常只能看到拿手机、说加微信、扫码或给手机号，未必能确认真正添加完成或后续有效。
- 处理：严格拆成提议、口头接受、手机操作、完成交换、后续回复五层。

### TR06｜instant_date_and_logistics｜blocking

- 来源：`mikey-sijiao-004`、`mikey-sijiao-013`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-019`
- 问题：即时邀约、带闺蜜、称病、门禁、位置、叫车、手机号、到达等节点容易被剪辑成连续成功链。
- 处理：拆分提议、接受、移动、到达与后续行为；任何到达不自动证明进一步关系或同意。

### TR07｜hard_cuts_replay_and_case_counting｜major

- 来源：`mikey-sijiao-002`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-006`、`mikey-sijiao-008`、`mikey-sijiao-009`、`mikey-sijiao-010`、`mikey-sijiao-014`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-019`
- 问题：多处有预告、重放、屏幕回放、硬切、上下集连续或同源多个案例，若按画面出现次数计数会高估案例与结果。
- 处理：按duplicate_case_ledger去重；硬切前后不自动建立因果。

### TR08｜result_and_marketing_claims｜blocking

- 来源：`mikey-sijiao-001`、`mikey-sijiao-002`、`mikey-sijiao-003`、`mikey-sijiao-004`、`mikey-sijiao-005`、`mikey-sijiao-006`、`mikey-sijiao-008`、`mikey-sijiao-009`、`mikey-sijiao-010`、`mikey-sijiao-011`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-014`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-019`
- 问题：标题、招生页、课程证言、学员即时自评、讲者旁白与局部结果图大量出现，缺少完整失败样本与独立长期追踪。
- 处理：这些材料只能支持‘发布者/学员这样声称’；不能估算成功率、保证结果或证明课程因果。

### TR09｜privacy_and_reuse｜major

- 来源：`mikey-sijiao-001`、`mikey-sijiao-003`、`mikey-sijiao-012`、`mikey-sijiao-013`、`mikey-sijiao-014`、`mikey-sijiao-015`、`mikey-sijiao-016`、`mikey-sijiao-017`、`mikey-sijiao-018`、`mikey-sijiao-019`
- 问题：输入中涉及人脸、账号、聊天、二维码、手机号、位置、私人地址和关系材料。
- 处理：跨期文件只保留知识ID/SID层级，不复制私人标识；正式skill若引用画面需脱敏。

## 12. 关键边界审计

### 开场

- **BA-O01｜`mikey-sijiao-008`｜hold_for_direct_quote**：先进入对方可见范围再开场；画面能支持现场/复盘结构，但外景逐句归属未完全核。 运行时：可用作开场结构上下文，不写成现场对方心理事实。
  - 知识：`mikey-sijiao-008-K0002`
- **BA-O02｜`mikey-sijiao-009`｜hold**：对方忙于拍照、未给注意力时不应重复完整开场；暗光和连续音画未完全核。 运行时：保留‘先注意力’原则，不补写对象具体反应。
  - 知识：`mikey-sijiao-009-K0001`
- **BA-O03｜`mikey-sijiao-011`｜mixed**：‘放慢取得注意力’与‘命令看我’同源并存；后者高影响、未核现场执行。 运行时：前者context_only，命令式做法do_not_generalize。
  - 知识：`mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0004`
- **BA-O04｜`mikey-sijiao-012`｜context_only**：同事关系被明确视为高社会成本，意图强度需要降低。 运行时：回答同事场景时先问关系与工作成本。
  - 知识：`mikey-sijiao-012-K0002`

### 拒绝与停止

- **BA-R01｜`mikey-sijiao-001`｜critical**：视觉可见‘不见面了’；后续短时见面方案不能改写前一时点拒绝。 运行时：先保留拒绝，再把任何后续重新沟通视为新事件。
  - 知识：`mikey-sijiao-001-K0001`、`mikey-sijiao-001-K0005`、`mikey-sijiao-001-K0006`
- **BA-R02｜`mikey-sijiao-003`｜direct_core_meaning**：Mikey明确说身体后退时不要再前进，要后退减压。 运行时：作为上位停止规则使用。
  - 知识：`mikey-sijiao-003-K0005`
- **BA-R03｜`mikey-sijiao-004`｜do_not_generalize**：1500–1800秒多次出现有男友/不加后的持续劝说，逐句人物顺序仍需核。 运行时：不把继续劝说作为坚持/自信方法。
  - 知识：`mikey-sijiao-004-K0010`
- **BA-R04｜`mikey-sijiao-005`｜do_not_generalize**：不同轮次既有及时结束也有继续劝说；视觉需逐轮确认。 运行时：明确伴侣/拒绝时礼貌结束。
  - 知识：`mikey-sijiao-005-K0008`
- **BA-R05｜`mikey-sijiao-019`｜context_only**：对方降低兴趣时Mikey称自己停止推进；后续对方再联系属于新事件。 运行时：不能把后续主动倒推为之前拒绝‘其实是测试’。
  - 知识：`mikey-sijiao-019-K0002`、`mikey-sijiao-019-K0004`

### 联系方式交换

- **BA-C01｜`mikey-sijiao-002`｜hold_completion**：现场可见交谈和手机，但静帧不能确认添加成功。 运行时：只把‘出手目标’保留为训练内容。
  - 知识：`mikey-sijiao-002-K0003`
- **BA-C02｜`mikey-sijiao-005`｜hold**：两个顺序窗口均未见足以确认微信添加完成的界面；14个微信为学员口头自报。 运行时：不得用14作为已核统计。
  - 知识：`mikey-sijiao-005-K0006`
- **BA-C03｜`mikey-sijiao-006`｜hold**：多个现场可见手机操作但未确认添加完成；室内回放非新事件。 运行时：保留‘号码只是工具’观点，不统计成功收号。
  - 知识：`mikey-sijiao-006-K0002`
- **BA-C04｜`mikey-sijiao-009`｜hold**：纯享片段出现部分联系方式流程但无后续验证。 运行时：不把流程画面写成有效联系方式或训练成功。
  - 知识：`mikey-sijiao-009-K0005`
- **BA-C05｜`mikey-sijiao-019`｜context_only**：手机号用于叫车/邀约确认信号，只能说明愿意提供联系方式。 运行时：不得外推同意见面或亲密行为。
  - 知识：`mikey-sijiao-019-K0006`

### 即时邀约/约会

- **BA-I01｜`mikey-sijiao-004`｜direct_core_meaning**：‘晚上一起玩’被Mikey自己限定为物流筛选、非制胜因素。 运行时：口头OK不等于会转场或发生关系。
  - 知识：`mikey-sijiao-004-K0005`
- **BA-I02｜`mikey-sijiao-013`｜hold**：三次约会由讲解和局部截图串联，没有连续现场；家中、酒精、结果均未独立证实。 运行时：约会、到家、饮酒、亲密结果分层。
  - 知识：`mikey-sijiao-013-K0005`、`mikey-sijiao-013-K0007`、`mikey-sijiao-013-K0008`
- **BA-I03｜`mikey-sijiao-016`｜mixed**：等待回复、称病、改约、门禁等节点可见聊天页，但后续完成约会主要是叙述。 运行时：可用‘先等/先判断真实生病’，门禁因果保持hold。
  - 知识：`mikey-sijiao-016-K0005`、`mikey-sijiao-016-K0006`、`mikey-sijiao-016-K0007`
- **BA-I04｜`mikey-sijiao-017`｜context_only**：二约带闺蜜可有安全顾虑；拒绝抱团安排不能写成对方已同意一对一。 运行时：允许对方取消或坚持自己的安全安排。
  - 知识：`mikey-sijiao-017-K0005`
- **BA-I05｜`mikey-sijiao-019`｜hold_results**：位置、叫车、手机号、到楼下、过夜是不同节点，后两项仍属第一人称结果叙述。 运行时：不得拼成无缝‘外卖到家’成功链。
  - 知识：`mikey-sijiao-019-K0001`、`mikey-sijiao-019-K0006`、`mikey-sijiao-019-K0007`

### 说话人归属

- **BA-S01｜`mikey-sijiao-006`｜partial**：室内机位能确认右侧黑T为Mikey、左侧打码者为学员；外景声音不能自动套用。 运行时：006全部知识不升direct。
  - 知识：`mikey-sijiao-006-K0001`、`mikey-sijiao-006-K0002`、`mikey-sijiao-006-K0003`、`mikey-sijiao-006-K0004`、`mikey-sijiao-006-K0005`、`mikey-sijiao-006-K0006`、`mikey-sijiao-006-K0007`
- **BA-S02｜`mikey-sijiao-008`｜partial**：室内Mikey与学员可分，外景逐句仍未完全核。 运行时：008全部知识不升direct。
  - 知识：`mikey-sijiao-008-K0001`、`mikey-sijiao-008-K0002`、`mikey-sijiao-008-K0003`、`mikey-sijiao-008-K0004`、`mikey-sijiao-008-K0005`、`mikey-sijiao-008-K0006`
- **BA-S03｜`mikey-sijiao-010`｜partial**：现场餐桌、Mikey红框后期讲解和编辑字幕三层共存。 运行时：Mikey对对象心理只作为复盘解释。
  - 知识：`mikey-sijiao-010-K0001`、`mikey-sijiao-010-K0002`、`mikey-sijiao-010-K0003`、`mikey-sijiao-010-K0004`、`mikey-sijiao-010-K0005`、`mikey-sijiao-010-K0006`、`mikey-sijiao-010-K0007`、`mikey-sijiao-010-K0008`
- **BA-S04｜`mikey-sijiao-011`｜context_only**：室内Mikey/学员身份可见，但全片未逐句听校；街头与复盘多次硬切。 运行时：低风险核心观点可作context，命令/结果类保持hold。
  - 知识：`mikey-sijiao-011-K0001`、`mikey-sijiao-011-K0002`、`mikey-sijiao-011-K0003`、`mikey-sijiao-011-K0004`、`mikey-sijiao-011-K0005`、`mikey-sijiao-011-K0006`、`mikey-sijiao-011-K0007`、`mikey-sijiao-011-K0008`、`mikey-sijiao-011-K0009`、`mikey-sijiao-011-K0010`、`mikey-sijiao-011-K0011`
- **BA-S05｜`mikey-sijiao-012`｜critical**：屏幕材料大量是学员与Mikey教练聊天，不是女同事第一手对话。 运行时：先区分教练建议、学员转述、目标对象原话。
  - 知识：`mikey-sijiao-012-K0001`、`mikey-sijiao-012-K0002`、`mikey-sijiao-012-K0003`、`mikey-sijiao-012-K0004`、`mikey-sijiao-012-K0005`、`mikey-sijiao-012-K0006`、`mikey-sijiao-012-K0007`、`mikey-sijiao-012-K0008`、`mikey-sijiao-012-K0009`、`mikey-sijiao-012-K0010`
- **BA-S06｜`mikey-sijiao-014`｜critical**：两套案例、多种聊天界面与学员汇报不能按颜色统一分角色。 运行时：先分案，再分发言者。
  - 知识：`mikey-sijiao-014-K0001`、`mikey-sijiao-014-K0002`、`mikey-sijiao-014-K0003`、`mikey-sijiao-014-K0004`、`mikey-sijiao-014-K0005`、`mikey-sijiao-014-K0006`、`mikey-sijiao-014-K0007`、`mikey-sijiao-014-K0008`、`mikey-sijiao-014-K0009`、`mikey-sijiao-014-K0010`
- **BA-S07｜`mikey-sijiao-015`｜critical**：至少存在教练聊天、当前对象、另一对象三种层次。 运行时：禁止跨对象合并建议、回复和结果。
  - 知识：`mikey-sijiao-015-K0001`、`mikey-sijiao-015-K0002`、`mikey-sijiao-015-K0003`、`mikey-sijiao-015-K0004`、`mikey-sijiao-015-K0005`、`mikey-sijiao-015-K0006`、`mikey-sijiao-015-K0007`、`mikey-sijiao-015-K0008`、`mikey-sijiao-015-K0009`、`mikey-sijiao-015-K0010`、`mikey-sijiao-015-K0011`

### 硬切、回放与结果

- **BA-H01｜`mikey-sijiao-002`｜hold_result**：预告、重放、采访和现场混剪；重放不产生新结果。 运行时：
  - 知识：`mikey-sijiao-002-K0007`
- **BA-H02｜`mikey-sijiao-003`｜hold_result**：多地点硬切与课程证言，不能形成冥想/课程效果连续因果。 运行时：
  - 知识：`mikey-sijiao-003-K0003`、`mikey-sijiao-003-K0010`
- **BA-H03｜`mikey-sijiao-009`｜hold_result**：片尾预告与广告不是本期已经发生的结果。 运行时：
  - 知识：`mikey-sijiao-009-K0005`
- **BA-H04｜`mikey-sijiao-010`｜hold_result**：开头复用009预告，35分钟后又换街头场景；片尾后续结果为回述。 运行时：
  - 知识：`mikey-sijiao-010-K0008`
- **BA-H05｜`mikey-sijiao-014`｜hold_result**：两案结果均由截图和学员反馈讲述，需分案且不独立验证。 运行时：
  - 知识：`mikey-sijiao-014-K0009`
- **BA-H06｜`mikey-sijiao-015`｜hold_result**：多个对象材料并列；‘约出/TD’由讲者和学员汇报。 运行时：
  - 知识：`mikey-sijiao-015-K0011`
- **BA-H07｜`mikey-sijiao-016`｜hold_result**：与015连续同案；所谓成功一约不是新的独立案例结果证据。 运行时：
  - 知识：`mikey-sijiao-016-K0008`
- **BA-H08｜`mikey-sijiao-017`｜hold_result**：一个月逆转、多次被发现仍顺从等来自宣传性串联。 运行时：
  - 知识：`mikey-sijiao-017-K0010`
- **BA-H09｜`mikey-sijiao-018`｜hold_result**：首约、后二约与人生全面改变均由旁白/推广包装串联。 运行时：
  - 知识：`mikey-sijiao-018-K0006`、`mikey-sijiao-018-K0008`
- **BA-H10｜`mikey-sijiao-019`｜hold_result**：语音、解释、局部结果页分段出现；到家、过夜与后续主动是第一人称叙述。 运行时：
  - 知识：`mikey-sijiao-019-K0007`

## 13. knowledge_index（164/164）

`use_level` 只使用 `direct / context_only / hold / do_not_generalize`。`direct` 仅用于核心含义与Mikey归属足够明确、且未被高影响待核边界改变的条目。

| # | knowledge_id | source_id | topic | theme_ids | proposition_ids | use_level |
|---:|---|---|---|---|---|---|
| 1 | `mikey-sijiao-001-K0001` | `mikey-sijiao-001` | 读取不舒服反馈并立即减压 | T05, T07 | P10, P16 | `direct` |
| 2 | `mikey-sijiao-001-K0002` | `mikey-sijiao-001` | 约会先专注互动而非强求结果 | T07 | P15 | `direct` |
| 3 | `mikey-sijiao-001-K0003` | `mikey-sijiao-001` | 内向不等于可以用触碰破局 | T05, T07 | P11, P16 | `direct` |
| 4 | `mikey-sijiao-001-K0004` | `mikey-sijiao-001` | 升级由现场反馈决定 | T05, T07 | P11, P16 | `direct` |
| 5 | `mikey-sijiao-001-K0005` | `mikey-sijiao-001` | 首约推进成功不等于事后接受 | T05, T07 | P10, P15, P16 | `direct` |
| 6 | `mikey-sijiao-001-K0006` | `mikey-sijiao-001` | 停止纠缠并降低一次沟通的负担 | T08 | P17 | `direct` |
| 7 | `mikey-sijiao-001-K0007` | `mikey-sijiao-001` | 修复不是靠礼物补偿 | T08 | P17 | `direct` |
| 8 | `mikey-sijiao-001-K0008` | `mikey-sijiao-001` | 真诚与死缠烂打的区别 | T08 | P17 | `direct` |
| 9 | `mikey-sijiao-001-K0009` | `mikey-sijiao-001` | 对方尚未投入时别急着放标准 | T03, T08, T09 | P09, P17, P19 | `direct` |
| 10 | `mikey-sijiao-001-K0010` | `mikey-sijiao-001` | 维护靠普通生活连接 | T09 | P20 | `direct` |
| 11 | `mikey-sijiao-001-K0011` | `mikey-sijiao-001` | 标题结果来自单方材料 | T07, T12 | P16, P24, P25 | `hold` |
| 12 | `mikey-sijiao-001-K0012` | `mikey-sijiao-001` | 操作需要原理和周期练习 | T10 | P22 | `direct` |
| 13 | `mikey-sijiao-002-K0001` | `mikey-sijiao-002` | 碎片理论不能替代真实出手 | T01, T10, T12 | P01, P22, P24 | `context_only` |
| 14 | `mikey-sijiao-002-K0002` | `mikey-sijiao-002` | 紧张时先把节奏放慢 | T01, T02 | P02, P06 | `direct` |
| 15 | `mikey-sijiao-002-K0003` | `mikey-sijiao-002` | 每日目标先按出手计 | T01 | P01 | `context_only` |
| 16 | `mikey-sijiao-002-K0004` | `mikey-sijiao-002` | 成功标准可以按当前训练阶段调整 | T01, T09 | P01, P19 | `direct` |
| 17 | `mikey-sijiao-002-K0005` | `mikey-sijiao-002` | 别把导师展示的高标准变成新束缚 | T01, T09 | P01, P19 | `direct` |
| 18 | `mikey-sijiao-002-K0006` | `mikey-sijiao-002` | 回程计划覆盖行动而非单一话术 | T01, T10, T12 | P03, P22, P24 | `context_only` |
| 19 | `mikey-sijiao-002-K0007` | `mikey-sijiao-002` | 课程成效是营销场景中的学员自述 | T12 | P24, P25 | `hold` |
| 20 | `mikey-sijiao-003-K0001` | `mikey-sijiao-003` | 先纠正紧张造成的不一致 | T01, T02 | P02, P04 | `direct` |
| 21 | `mikey-sijiao-003-K0002` | `mikey-sijiao-003` | 技术要建立在能正常表达的状态上 | T01 | P02 | `direct` |
| 22 | `mikey-sijiao-003-K0003` | `mikey-sijiao-003` | 一次兴奋不能证明永久改变 | T12 | P24, P25 | `hold` |
| 23 | `mikey-sijiao-003-K0004` | `mikey-sijiao-003` | ‘后台程序’是Mikey的内在体验解释 | T01 | P02 | `direct` |
| 24 | `mikey-sijiao-003-K0005` | `mikey-sijiao-003` | 女生后退时必须先后退减压 | T05, T07 | P10, P16 | `direct` |
| 25 | `mikey-sijiao-003-K0006` | `mikey-sijiao-003` | 表达兴趣不能变成猥亵 | T03 | P09 | `direct` |
| 26 | `mikey-sijiao-003-K0007` | `mikey-sijiao-003` | 不想入镜就停止拍摄对方 | T05, T11 | P10, P23 | `context_only` |
| 27 | `mikey-sijiao-003-K0008` | `mikey-sijiao-003` | 夜场按时间段调整目标 | T07, T11 | P15, P23 | `direct` |
| 28 | `mikey-sijiao-003-K0009` | `mikey-sijiao-003` | 长期对象的道德双重标准 | T09, T12 | P19, P26 | `do_not_generalize` |
| 29 | `mikey-sijiao-003-K0010` | `mikey-sijiao-003` | 学员推荐属于推广证言 | T12 | P24, P25 | `hold` |
| 30 | `mikey-sijiao-003-K0011` | `mikey-sijiao-003` | 现场示范提供即时反馈循环 | T01, T12 | P03, P24 | `context_only` |
| 31 | `mikey-sijiao-004-K0001` | `mikey-sijiao-004` | 现场复盘要抓真正卡点 | T01 | P03 | `direct` |
| 32 | `mikey-sijiao-004-K0002` | `mikey-sijiao-004` | 行动前别替陌生人完成拒绝 | T03 | P05 | `direct` |
| 33 | `mikey-sijiao-004-K0003` | `mikey-sijiao-004` | 邀约处慌乱会让意图变模糊 | T03, T06 | P09, P13 | `direct` |
| 34 | `mikey-sijiao-004-K0004` | `mikey-sijiao-004` | 从当下经历找话题 | T03 | P07 | `direct` |
| 35 | `mikey-sijiao-004-K0005` | `mikey-sijiao-004` | ‘晚上一起玩’只是物流筛选 | T06 | P13 | `direct` |
| 36 | `mikey-sijiao-004-K0006` | `mikey-sijiao-004` | 多人互动要照顾每个参与者 | T07, T11 | P15, P23 | `direct` |
| 37 | `mikey-sijiao-004-K0007` | `mikey-sijiao-004` | 透明交代来意可减少销售戒备 | T03 | P05 | `direct` |
| 38 | `mikey-sijiao-004-K0008` | `mikey-sijiao-004` | 自然反应比假笑更一致 | T01, T02 | P02, P04 | `direct` |
| 39 | `mikey-sijiao-004-K0009` | `mikey-sijiao-004` | 一次找到状态后仍需反复练习 | T01, T02, T12 | P03, P04, P24 | `context_only` |
| 40 | `mikey-sijiao-004-K0010` | `mikey-sijiao-004` | 已有伴侣和明确不加应当作边界 | T05, T07, T12 | P10, P16, P24, P26 | `do_not_generalize` |
| 41 | `mikey-sijiao-004-K0011` | `mikey-sijiao-004` | 及时纠错比机械增加次数更重要 | T01, T12 | P03, P24 | `context_only` |
| 42 | `mikey-sijiao-004-K0012` | `mikey-sijiao-004` | 先懂理论再把它融入自然交流 | T01, T10, T12 | P03, P22, P24 | `context_only` |
| 43 | `mikey-sijiao-004-K0013` | `mikey-sijiao-004` | 焦虑下降数字是课后即时自评 | T12 | P24, P25 | `hold` |
| 44 | `mikey-sijiao-004-K0014` | `mikey-sijiao-004` | 男性都应具备性能力是价值主张 | T09, T12 | P19, P26 | `do_not_generalize` |
| 45 | `mikey-sijiao-004-K0015` | `mikey-sijiao-004` | 服务推荐处在推广采访中 | T12 | P24, P25 | `hold` |
| 46 | `mikey-sijiao-005-K0001` | `mikey-sijiao-005` | 松弛感是开场的首要改进点 | T01, T02 | P02, P06 | `direct` |
| 47 | `mikey-sijiao-005-K0002` | `mikey-sijiao-005` | 行动前不要用身高替对方拒绝 | T03 | P05 | `direct` |
| 48 | `mikey-sijiao-005-K0003` | `mikey-sijiao-005` | 邀约意图要清楚且可拒绝 | T03, T06 | P09, P13 | `direct` |
| 49 | `mikey-sijiao-005-K0004` | `mikey-sijiao-005` | 一次高个女性回应只能反驳绝对不可能 | T12 | P24 | `context_only` |
| 50 | `mikey-sijiao-005-K0005` | `mikey-sijiao-005` | 练习目标先从愿意出手开始 | T01, T12 | P01, P24 | `context_only` |
| 51 | `mikey-sijiao-005-K0006` | `mikey-sijiao-005` | 14个微信与七八次拒绝是即时自报 | T06, T12 | P12, P24, P25 | `hold` |
| 52 | `mikey-sijiao-005-K0007` | `mikey-sijiao-005` | 学员把效果归因于自信和从容 | T01, T12 | P02, P24 | `context_only` |
| 53 | `mikey-sijiao-005-K0008` | `mikey-sijiao-005` | 对已有伴侣或明确拒绝应结束 | T05, T07, T12 | P10, P16, P24, P26 | `do_not_generalize` |
| 54 | `mikey-sijiao-006-K0001` | `mikey-sijiao-006` | 坚定不是背一句强硬台词 | T02 | P04 | `hold` |
| 55 | `mikey-sijiao-006-K0002` | `mikey-sijiao-006` | 号码只是后续连接工具 | T06 | P12 | `hold` |
| 56 | `mikey-sijiao-006-K0003` | `mikey-sijiao-006` | 用浅沟通承载关系压力 | T02, T05 | P04, P11 | `hold` |
| 57 | `mikey-sijiao-006-K0004` | `mikey-sijiao-006` | 不要用解释应对身份质疑 | T08 | P18 | `hold` |
| 58 | `mikey-sijiao-006-K0005` | `mikey-sijiao-006` | 录像复盘让隐性问题可见 | T01 | P03 | `hold` |
| 59 | `mikey-sijiao-006-K0006` | `mikey-sijiao-006` | 互动时长不等于有效投入 | T02, T04, T05 | P06, P08, P11 | `hold` |
| 60 | `mikey-sijiao-006-K0007` | `mikey-sijiao-006` | 一致性来自生活中的长期练习 | T02, T10 | P04, P22 | `hold` |
| 61 | `mikey-sijiao-008-K0001` | `mikey-sijiao-008` | 一致性是日常状态与临场表达对得上 | T02 | P04 | `hold` |
| 62 | `mikey-sijiao-008-K0002` | `mikey-sijiao-008` | 先被看见，再靠近开场 | T03 | P05 | `hold` |
| 63 | `mikey-sijiao-008-K0003` | `mikey-sijiao-008` | 对方停住后按距离反馈调节 | T05 | P10, P11 | `hold` |
| 64 | `mikey-sijiao-008-K0004` | `mikey-sijiao-008` | 一致不等于永远一种状态 | T02, T05 | P04, P11 | `hold` |
| 65 | `mikey-sijiao-008-K0005` | `mikey-sijiao-008` | 即兴内容要从现场长出来 | T03 | P07 | `hold` |
| 66 | `mikey-sijiao-008-K0006` | `mikey-sijiao-008` | 有意识目的与下意识细节分工 | T02, T10 | P04, P22 | `hold` |
| 67 | `mikey-sijiao-009-K0001` | `mikey-sijiao-009` | 先获得注意力再说完整开场 | T03 | P05 | `hold` |
| 68 | `mikey-sijiao-009-K0002` | `mikey-sijiao-009` | 个性样本包括语言和浅沟通 | T02, T04 | P04, P08 | `hold` |
| 69 | `mikey-sijiao-009-K0003` | `mikey-sijiao-009` | 从真实个人经历自然展开 | T03, T04 | P07, P08 | `hold` |
| 70 | `mikey-sijiao-009-K0004` | `mikey-sijiao-009` | 根据当下场景生成话题 | T03 | P07 | `hold` |
| 71 | `mikey-sijiao-009-K0005` | `mikey-sijiao-009` | 纯享片段不提供结果证明 | T06, T12 | P12, P25 | `hold` |
| 72 | `mikey-sijiao-010-K0001` | `mikey-sijiao-010` | 不要像卫星一样只围着对方问 | T04 | P08 | `hold` |
| 73 | `mikey-sijiao-010-K0002` | `mikey-sijiao-010` | 真实好奇和没话说式提问要区分 | T04 | P08 | `hold` |
| 74 | `mikey-sijiao-010-K0003` | `mikey-sijiao-010` | 讲自己的现实感更容易传递个性 | T03, T04 | P07, P08 | `hold` |
| 75 | `mikey-sijiao-010-K0004` | `mikey-sijiao-010` | 吸引之外还要让对方在逻辑上了解你 | T04 | P08 | `hold` |
| 76 | `mikey-sijiao-010-K0005` | `mikey-sijiao-010` | 敢说敢做是优势，但需要关联性 | T04 | P08 | `hold` |
| 77 | `mikey-sijiao-010-K0006` | `mikey-sijiao-010` | 分享自己不是刻意包装简历 | T03, T04 | P07, P08 | `hold` |
| 78 | `mikey-sijiao-010-K0007` | `mikey-sijiao-010` | 讲者对女性内心的判断不是现场事实 | T12 | P24 | `hold` |
| 79 | `mikey-sijiao-010-K0008` | `mikey-sijiao-010` | 复盘后的结果仍是回述 | T12 | P25 | `hold` |
| 80 | `mikey-sijiao-011-K0001` | `mikey-sijiao-011` | 感觉比背完整话术更重要 | T03, T02 | P05, P06 | `context_only` |
| 81 | `mikey-sijiao-011-K0002` | `mikey-sijiao-011` | 事后微调而非开场堆组合 | T03, T05 | P05, P11 | `context_only` |
| 82 | `mikey-sijiao-011-K0003` | `mikey-sijiao-011` | 高压力场景练习 | T11 | P23 | `context_only` |
| 83 | `mikey-sijiao-011-K0004` | `mikey-sijiao-011` | 用命令取得注意力 | T12 | P26 | `do_not_generalize` |
| 84 | `mikey-sijiao-011-K0005` | `mikey-sijiao-011` | 给对方说话空间 | T02 | P06 | `context_only` |
| 85 | `mikey-sijiao-011-K0006` | `mikey-sijiao-011` | 允许话说一半 | T02 | P06 | `context_only` |
| 86 | `mikey-sijiao-011-K0007` | `mikey-sijiao-011` | 具体细节称赞 | T03 | P05, P07 | `context_only` |
| 87 | `mikey-sijiao-011-K0008` | `mikey-sijiao-011` | 容纳尴尬和空白 | T01, T02 | P02, P06 | `context_only` |
| 88 | `mikey-sijiao-011-K0009` | `mikey-sijiao-011` | 一次只练一个点 | T01 | P01, P03 | `context_only` |
| 89 | `mikey-sijiao-011-K0010` | `mikey-sijiao-011` | 怕失去会让表达加速 | T01, T02 | P02, P06 | `context_only` |
| 90 | `mikey-sijiao-011-K0011` | `mikey-sijiao-011` | 享受沟通而非只拿微信 | T04, T06 | P08, P12 | `context_only` |
| 91 | `mikey-sijiao-012-K0001` | `mikey-sijiao-012` | 复杂关系的证据边界 | T09, T12 | P21, P24 | `context_only` |
| 92 | `mikey-sijiao-012-K0002` | `mikey-sijiao-012` | 同事关系用轻意图 | T03, T06, T11 | P09, P13, P23 | `context_only` |
| 93 | `mikey-sijiao-012-K0003` | `mikey-sijiao-012` | 热度同频与八二比例 | T03, T06 | P09, P14 | `context_only` |
| 94 | `mikey-sijiao-012-K0004` | `mikey-sijiao-012` | 学员转述可能选择性呈现 | T06, T12 | P14, P24 | `context_only` |
| 95 | `mikey-sijiao-012-K0005` | `mikey-sijiao-012` | 行为比言语权重更高 | T05, T06 | P10, P11, P14 | `context_only` |
| 96 | `mikey-sijiao-012-K0006` | `mikey-sijiao-012` | 松弛感是不逼迫 | T01 | P02 | `context_only` |
| 97 | `mikey-sijiao-012-K0007` | `mikey-sijiao-012` | 制造嫉妒和降温 | T09, T12 | P21, P26 | `do_not_generalize` |
| 98 | `mikey-sijiao-012-K0008` | `mikey-sijiao-012` | 性结果和持续关系 | T07, T09, T12 | P16, P21, P24, P25 | `hold` |
| 99 | `mikey-sijiao-012-K0009` | `mikey-sijiao-012` | 百分百拿下承诺 | T12 | P24, P25, P26 | `do_not_generalize` |
| 100 | `mikey-sijiao-012-K0010` | `mikey-sijiao-012` | 快速发展不等于无边界 | T05, T07 | P10, P16 | `context_only` |
| 101 | `mikey-sijiao-013-K0001` | `mikey-sijiao-013` | 资料过多会增加限制 | T10 | P22 | `context_only` |
| 102 | `mikey-sijiao-013-K0002` | `mikey-sijiao-013` | 按关系阶段行动 | T03, T06 | P09, P13 | `context_only` |
| 103 | `mikey-sijiao-013-K0003` | `mikey-sijiao-013` | 过早性暗示掉吸引 | T03 | P09 | `context_only` |
| 104 | `mikey-sijiao-013-K0004` | `mikey-sijiao-013` | 别连续自说自话 | T02, T06 | P06, P14 | `context_only` |
| 105 | `mikey-sijiao-013-K0005` | `mikey-sijiao-013` | 高温公园约会失败 | T06, T07, T11, T12 | P13, P15, P23, P24 | `context_only` |
| 106 | `mikey-sijiao-013-K0006` | `mikey-sijiao-013` | 适量表达兴趣 | T03, T06, T07, T08 | P09, P13, P15, P17 | `context_only` |
| 107 | `mikey-sijiao-013-K0007` | `mikey-sijiao-013` | 家中约会与酒精 | T07, T12 | P16, P26 | `do_not_generalize` |
| 108 | `mikey-sijiao-013-K0008` | `mikey-sijiao-013` | 一周取得结果 | T07, T12 | P16, P24, P25 | `hold` |
| 109 | `mikey-sijiao-013-K0009` | `mikey-sijiao-013` | 听话照做的成功归因 | T12 | P24, P25 | `context_only` |
| 110 | `mikey-sijiao-014-K0001` | `mikey-sijiao-014` | 别因冷回复破防 | T06, T08 | P14, P18 | `context_only` |
| 111 | `mikey-sijiao-014-K0002` | `mikey-sijiao-014` | 财富的双刃剑叙事 | T12 | P24 | `context_only` |
| 112 | `mikey-sijiao-014-K0003` | `mikey-sijiao-014` | 慢回复时停止脑补 | T06, T08 | P14, P18 | `context_only` |
| 113 | `mikey-sijiao-014-K0004` | `mikey-sijiao-014` | 用主动分享反推兴趣 | T06 | P14 | `context_only` |
| 114 | `mikey-sijiao-014-K0005` | `mikey-sijiao-014` | 用要求增加投资 | T12 | P26 | `do_not_generalize` |
| 115 | `mikey-sijiao-014-K0006` | `mikey-sijiao-014` | 单身问题不正面回答 | T09, T12 | P19, P21, P26 | `do_not_generalize` |
| 116 | `mikey-sijiao-014-K0007` | `mikey-sijiao-014` | 技巧只是工具 | T10 | P22 | `context_only` |
| 117 | `mikey-sijiao-014-K0008` | `mikey-sijiao-014` | 沉没成本与推开 | T09, T12 | P21, P26 | `do_not_generalize` |
| 118 | `mikey-sijiao-014-K0009` | `mikey-sijiao-014` | 两个案例结果 | T09, T12 | P21, P24, P25 | `hold` |
| 119 | `mikey-sijiao-014-K0010` | `mikey-sijiao-014` | 百分百信任导师的归因 | T10, T12 | P22, P24, P25 | `context_only` |
| 120 | `mikey-sijiao-015-K0001` | `mikey-sijiao-015` | 分阶段学习术与道 | T10 | P22 | `context_only` |
| 121 | `mikey-sijiao-015-K0002` | `mikey-sijiao-015` | 技术结果与吸引的区别 | T02, T04 | P04, P08 | `context_only` |
| 122 | `mikey-sijiao-015-K0003` | `mikey-sijiao-015` | 学员既往结果 | T12 | P24, P25 | `context_only` |
| 123 | `mikey-sijiao-015-K0004` | `mikey-sijiao-015` | 需求加后缀 | T03, T06 | P09, P13 | `context_only` |
| 124 | `mikey-sijiao-015-K0005` | `mikey-sijiao-015` | 别为不懂反复解释 | T06, T08 | P14, P18 | `context_only` |
| 125 | `mikey-sijiao-015-K0006` | `mikey-sijiao-015` | 把对方视为NPC | T12 | P26 | `do_not_generalize` |
| 126 | `mikey-sijiao-015-K0007` | `mikey-sijiao-015` | 喝酒邀约与状态 | T07, T12 | P16, P26 | `do_not_generalize` |
| 127 | `mikey-sijiao-015-K0008` | `mikey-sijiao-015` | 心态产生可变应对 | T02, T10 | P04, P22 | `context_only` |
| 128 | `mikey-sijiao-015-K0009` | `mikey-sijiao-015` | 理解推开的理由而非时机 | T05, T08, T10 | P11, P18, P22 | `context_only` |
| 129 | `mikey-sijiao-015-K0010` | `mikey-sijiao-015` | 不复制第一次成功 | T02, T05, T10 | P04, P11, P22 | `context_only` |
| 130 | `mikey-sijiao-015-K0011` | `mikey-sijiao-015` | 约出和取得结果 | T07, T12 | P16, P24, P25 | `hold` |
| 131 | `mikey-sijiao-016-K0001` | `mikey-sijiao-016` | 不要因外貌把对方设为例外 | T09 | P19 | `direct` |
| 132 | `mikey-sijiao-016-K0002` | `mikey-sijiao-016` | 承认邀约意图，不用含糊遮掩 | T03, T06 | P09, P13 | `direct` |
| 133 | `mikey-sijiao-016-K0003` | `mikey-sijiao-016` | 酒吧认识后要补安全感与人设 | T03, T11 | P09, P23 | `direct` |
| 134 | `mikey-sijiao-016-K0004` | `mikey-sijiao-016` | 不必对所有追问逐项自证 | T06, T08, T09 | P14, P18, P19 | `direct` |
| 135 | `mikey-sijiao-016-K0005` | `mikey-sijiao-016` | 短时间未回复时先稳住 | T06, T08 | P13, P14, P18 | `context_only` |
| 136 | `mikey-sijiao-016-K0006` | `mikey-sijiao-016` | 临时称病先判断并解决实际问题 | T05, T06, T08 | P11, P13, P18 | `direct` |
| 137 | `mikey-sijiao-016-K0007` | `mikey-sijiao-016` | 门禁被解释为吸引指标属于强因果主张 | T07, T12 | P16, P26 | `do_not_generalize` |
| 138 | `mikey-sijiao-016-K0008` | `mikey-sijiao-016` | 成功一约是讲者叙述而非独立结果证据 | T07, T12 | P16, P24, P25 | `hold` |
| 139 | `mikey-sijiao-017-K0001` | `mikey-sijiao-017` | 路上认识后别急于线上升温 | T03, T06 | P09, P14 | `direct` |
| 140 | `mikey-sijiao-017-K0002` | `mikey-sijiao-017` | 别用嫉妒质问回应暧昧朋友圈 | T06, T08 | P14, P18 | `direct` |
| 141 | `mikey-sijiao-017-K0003` | `mikey-sijiao-017` | 照片是邀约暗示的判断必须回看原图 | T06, T12 | P14, P24 | `hold` |
| 142 | `mikey-sijiao-017-K0004` | `mikey-sijiao-017` | 策略要匹配本人能力和一致性 | T02, T08, T10 | P04, P18, P22 | `direct` |
| 143 | `mikey-sijiao-017-K0005` | `mikey-sijiao-017` | 二约带闺蜜时明确自己的约会条件 | T05, T06, T07, T09, T11 | P10, P13, P16, P19, P23 | `context_only` |
| 144 | `mikey-sijiao-017-K0006` | `mikey-sijiao-017` | 多偶被定义为高风险策略 | T09 | P19, P20, P21 | `direct` |
| 145 | `mikey-sijiao-017-K0007` | `mikey-sijiao-017` | 被发现多线关系后的话术不能当通用解决方案 | T07, T09, T12 | P16, P21, P24, P26 | `do_not_generalize` |
| 146 | `mikey-sijiao-017-K0008` | `mikey-sijiao-017` | 不能既要多线交往又保证永不暴露 | T09 | P19, P20, P21 | `context_only` |
| 147 | `mikey-sijiao-017-K0009` | `mikey-sijiao-017` | 三条底层逻辑属于讲者的案例总结 | T10 | P22 | `direct` |
| 148 | `mikey-sijiao-017-K0010` | `mikey-sijiao-017` | 一个月逆转和多次抓包仍顺从都是宣传性结果 | T07, T09, T12 | P16, P21, P24, P25 | `hold` |
| 149 | `mikey-sijiao-018-K0001` | `mikey-sijiao-018` | 新手网聊围绕邀约和人设 | T04, T03 | P08, P09 | `direct` |
| 150 | `mikey-sijiao-018-K0002` | `mikey-sijiao-018` | 博弈心态强调不做被动棋子 | T09 | P19 | `context_only` |
| 151 | `mikey-sijiao-018-K0003` | `mikey-sijiao-018` | 不要用服务动作换取认可 | T09 | P19 | `context_only` |
| 152 | `mikey-sijiao-018-K0004` | `mikey-sijiao-018` | 处理迟到要看关系、态度和原因 | T06, T07, T11 | P13, P15, P23 | `direct` |
| 153 | `mikey-sijiao-018-K0005` | `mikey-sijiao-018` | 摆脱单一对象依赖来自可重复经验 | T09 | P19, P20 | `direct` |
| 154 | `mikey-sijiao-018-K0006` | `mikey-sijiao-018` | 首约和后续成功均为旁白结果 | T07, T12 | P16, P24, P25 | `hold` |
| 155 | `mikey-sijiao-018-K0007` | `mikey-sijiao-018` | 前任背叛与冲突是单方转述 | T09, T12 | P21, P24 | `hold` |
| 156 | `mikey-sijiao-018-K0008` | `mikey-sijiao-018` | 情感学习改善整个人生是推广性外推 | T12 | P24, P25 | `hold` |
| 157 | `mikey-sijiao-019-K0001` | `mikey-sijiao-019` | 直接邀约前先判断对象与情境 | T03, T06, T11 | P09, P13, P23 | `direct` |
| 158 | `mikey-sijiao-019-K0002` | `mikey-sijiao-019` | 对方降低兴趣时不要焦虑追赶 | T05, T06, T08 | P10, P13, P14, P18 | `context_only` |
| 159 | `mikey-sijiao-019-K0003` | `mikey-sijiao-019` | 新手不要照搬只邀约不聊天 | T03 | P09 | `direct` |
| 160 | `mikey-sijiao-019-K0004` | `mikey-sijiao-019` | 对方软化后自己也应软化 | T05, T06, T08 | P11, P14, P17, P18 | `direct` |
| 161 | `mikey-sijiao-019-K0005` | `mikey-sijiao-019` | 冒犯能被自动美化是高风险因果主张 | T12 | P26 | `do_not_generalize` |
| 162 | `mikey-sijiao-019-K0006` | `mikey-sijiao-019` | 手机号被用作叫车和邀约确认信号 | T06, T07, T12 | P12, P13, P16, P24 | `context_only` |
| 163 | `mikey-sijiao-019-K0007` | `mikey-sijiao-019` | 到家过夜与后续主动均是讲者自述 | T07, T12 | P16, P24, P25 | `hold` |
| 164 | `mikey-sijiao-019-K0008` | `mikey-sijiao-019` | 不因欲望放弃自己的标准 | T09 | P19 | `direct` |

## 14. 分级统计与完成前审计

- knowledge_index：`164` 条；唯一 ID：`164`。
- `direct`：48 条。
- `context_only`：56 条。
- `hold`：44 条。
- `do_not_generalize`：16 条。
- `scope`、`statistics`、`source_reuse_ledger` 与输入 JSON 对象逐对象相等。
- 18 个 `sources` 顺序与 inventory / `scope.source_ids` 一致。
- `mikey-sijiao-007` 只存在于复用台账，未进入 164 条新增知识，也未产生独立案例权重。
- 主题、命题、方法关系、冲突、回答模式、视觉校准和关键边界中的知识 ID 均闭合到这 164 条知识。
- 本结构校验只证明范围和引用闭合，不证明截图真实性、因果、方法效果或镜头外结果。
