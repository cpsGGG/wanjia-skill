# YouTube公开直播第三批跨期综合

**交付性质：跨期综合候选。** 本文与同名JSON来自同一数据对象，不修改逐期材料，不接入正式skill，也不表示任何人物化回答已经运行。

这十期材料形成的主要判断顺序是：先区分事实与自己的解释，再看问题发生在首次互动、后续呈现、聊天投入还是具体安排；不要用一句话术解释整个结果，也不要用一次拒绝解释自己的全部价值。人物材料反复强调真实状态、主心骨和实践反馈，但与支配、羞辱、绕过拒绝及群体概括存在明确冲突。下面保留它如何判断、为什么、方法之间怎样连接，同时把不能进入行动答案的部分单独受控。

完整读取的是四个上传文本文件及其中的结构化记录：10期、153条知识、136个事件、63项待核、10份说话人登记和直播70的16段归属跨度。16132是登记SID总数，并不表示紧凑包附有16132条逐字稿；963是原引文/引用记录总数，本包实际附288条代表引文记录。去重后共959个证据定位，其中671个没有代表正文，对应675个未附正文的引用位置。本次没有听辨原音、查看图片或观看连续视频。

综合索引：**direct 8、context_only 1、hold 122、do_not_generalize 22，合计153条。** 原逐期发布状态与归属没有改动，保存在JSON原样档案和本文逐条索引中。direct只允许其收窄范围内的间接观点转述，不等于原话听校、事实验证或人物化授权。

## 1. 来源范围与使用规则

| 来源ID | 直播 | 发布日期（原登记） | SID | 事件 | 知识 | 待核 |
|---|---:|---|---:|---:|---:|---:|
| `mikey-youtube-live-021` | 68 | 2025-08-17 | 1217 | 12 | 19 | 9 |
| `mikey-youtube-live-022` | 70 | 2025-08-28 | 2014 | 16 | 18 | 5 |
| `mikey-youtube-live-023` | 72 | 2025-09-15 | 1958 | 14 | 25 | 12 |
| `mikey-youtube-live-024` | 75 | 2025-10-19 | 2113 | 13 | 16 | 10 |
| `mikey-youtube-live-025` | 77 | 2025-11-10 | 1346 | 12 | 16 | 8 |
| `mikey-youtube-live-026` | 79 | 2025-11-20 | 1287 | 12 | 9 | 4 |
| `mikey-youtube-live-027` | 80 | 2025-11-22 | 1270 | 14 | 12 | 3 |
| `mikey-youtube-live-028` | 81 | 2025-11-23 | 1581 | 15 | 12 | 4 |
| `mikey-youtube-live-029` | 82 | 2025-11-24 | 2017 | 15 | 12 | 4 |
| `mikey-youtube-live-030` | 83 | 2025-12-04 | 1329 | 13 | 14 | 4 |

原来源标题、video_id、URL和知识ID列表均在JSON的`sources`中原样保留；原`scope`、`statistics`、`sources`三个字段对象逐项一致。输入中的本地inventory或历史运行路径只是原记录，不表示本次另行打开那些文件。

**原记录与人物归属：**knowledge.claim是逐期编辑概括，可能混入编辑者的安全收窄；原attribution_status不等于概括中每个规范句都曾由Mikey说出。

**限制传播：**先保持原限制，再传播开放blocking/major；同时使用声明event_ids与evidence_id所属真实事件，不能靠错误时间窗绕过；代表片段不足则追加hold。

**review字段的含义：**列出在本综合中实际阻断该条使用的现有review ID，可能含原severity=major；原严重度未被改写，见review_dependency_map。

**引文规则：**原文只在as_supplied档案转存；叙述直接引用时必须用“自动稿记录为”，不修正错词后冒充原话。

**先前视觉声明：**所有as_supplied字段是上传资料原样转存，其中先前审核者写的“实际查看”等描述不是本次助手的工作声明。

## 2. 按主题恢复判断链

### T01 · 吸引的连续性：短时表现与日常状态要接得上

**判断：**附件反复把“短时间表现不错、后来失去吸引”解释为不同场景里的行为线索不一致，而非缺少一句更强的话术。这是人物解释框架，不是已经验证的心理定律。

**理由与跨期联系：**直播68把压力和意外作为表演容易露出原反应的地方；直播72强调初步吸引后不要持续加码表现；直播75及80/81把聊天、朋友圈与真实生活接在一起。共同点不是永远保持兴奋，而是避免只在追求时扮演一个人。后几期相似概括仅增加主题线索，不能补足尚缺的原文或归属。

**候选顺序：**先区分首次印象没有形成，还是形成后出现了明显落差。；回看对方最初接触到的行为、表达和生活信息，与后来相处是否一致。；候选学习方向是通过实践把可持续的行为变成习惯，而不是不断追加表演；具体训练量不从本包推导。

**适用条件：**只讨论双方自愿的日常互动。；不能先假定对方态度变化必由当事人的人格造成；安排、偏好和其他因素仍未确定。

**观察什么反馈：**观察同一个人在陌生、熟悉、受挫等情境下是否出现明显不同的表达方式。；对方的后续回应只能说明这次互动，不能验证整套人格理论。

**边界：**一致性不是服从、控制或持续高能量。；多个支撑条目关联待核，整条主题不能直接作为运行时建议。

**可有限转述的direct子集：**`mikey-youtube-live-023-K005`

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-021-K006` → `mikey-youtube-live-021-E0004-R039` / `S00323`；`mikey-youtube-live-021-K011` → `mikey-youtube-live-021-E0006-R057` / `S00554`；`mikey-youtube-live-023-K001` → `mikey-youtube-live-023-E0001-R045` / `S00045`；`mikey-youtube-live-023-K005` → `mikey-youtube-live-023-E0002-R005` / `S00192`；`mikey-youtube-live-024-K003` → `mikey-youtube-live-024-E0002-R104` / `S00249`；`mikey-youtube-live-024-K008` → `mikey-youtube-live-024-E0004-R154` / `S00860`；`mikey-youtube-live-024-K010` → `mikey-youtube-live-024-E0007-R009` / `S01235`；`mikey-youtube-live-025-K009` → `mikey-youtube-live-025-E0005-R005` / `S00609`；`mikey-youtube-live-027-K006` → `mikey-youtube-live-027-E0005-R028` / `S00448`；`mikey-youtube-live-027-K010` → `mikey-youtube-live-027-E0012-R043` / `S01173`；`mikey-youtube-live-028-K004` → `mikey-youtube-live-028-E0006-R016` / `S00576`；`mikey-youtube-live-030-K007` → `mikey-youtube-live-030-E0003-R089` / `S00355`。

</details>
### T02 · 自我价值与主体性：不把每一次互动当成人格审判

**判断：**这一组材料把紧张和过度讨好联系到“把对方当成决定自己价值的裁判”。其较稳定的意思是保有自己的判断，而不是让别人失去判断权。

**理由与跨期联系：**直播77区分资源条件与价值感；直播83再次谈事实、解释和自我评价。直播72的旁观者/NPC比喻与直播75的双方独立并不天然一致：减轻对外界评价的依赖，可以作为候选心理解释；否认他人主体则必须另列冲突。

**候选顺序：**先写清发生的事情：一次拒绝、一次冷淡、一次表现不佳，还是已有的长期问题。；区分事情本身与“我整个人没有价值”的解释。；保留自己的真实意图和退出选择，同时保留对方相同的选择权。

**适用条件：**不是临床诊断或焦虑治疗。；不能把自己感觉稳定当作对方必然被吸引的证据。

**观察什么反馈：**能否承认这次互动没有成立，同时不靠贬低对方修复自尊。；能否根据具体反馈改行为，而不是靠别人持续认可维持状态。

**边界：**主心骨不等于支配。；NPC、宠物或性价值比喻不能当作普遍看待人的方式。；部分完整解释仅有半句代表引文，已在索引中hold。

**可有限转述的direct子集：**`mikey-youtube-live-024-K004`、`mikey-youtube-live-025-K012`

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K002` → `mikey-youtube-live-023-E0001-R068` / `S00068`；`mikey-youtube-live-023-K003` → `mikey-youtube-live-023-E0001-R134` / `S00134`；`mikey-youtube-live-023-K008` → `mikey-youtube-live-023-E0003-R060` / `S00388`；`mikey-youtube-live-023-K013` → `mikey-youtube-live-023-E0005-R175` / `S00814`；`mikey-youtube-live-023-K020` → `mikey-youtube-live-023-E0010-R020` / `S01408`；`mikey-youtube-live-024-K004` → `mikey-youtube-live-024-E0002-R139` / `S00284`；`mikey-youtube-live-025-K004` → `mikey-youtube-live-025-E0002-R059` / `S00227`；`mikey-youtube-live-025-K011` → `mikey-youtube-live-025-E0007-R031` / `S00844`；`mikey-youtube-live-025-K012` → `mikey-youtube-live-025-E0007-R073` / `S00886`；`mikey-youtube-live-026-K004` → `mikey-youtube-live-026-E0012-R044` / `S01224`；`mikey-youtube-live-028-K007` → `mikey-youtube-live-028-E0010-R128` / `S01128`；`mikey-youtube-live-029-K001` → `mikey-youtube-live-029-E0001-R130` / `S00130`；`mikey-youtube-live-029-K003` → `mikey-youtube-live-029-E0002-R014` / `S00173`；`mikey-youtube-live-030-K002` → `mikey-youtube-live-030-E0001-R152` / `S00152`；`mikey-youtube-live-030-K003` → `mikey-youtube-live-030-E0002-R022` / `S00177`；`mikey-youtube-live-030-K004` → `mikey-youtube-live-030-E0002-R051` / `S00206`；`mikey-youtube-live-030-K005` → `mikey-youtube-live-030-E0002-R059` / `S00214`；`mikey-youtube-live-030-K006` → `mikey-youtube-live-030-E0003-R007` / `S00273`。

</details>
### T03 · 学习路径：从收藏技巧转到带着问题实践和复盘

**判断：**跨期候选链是：少量理解帮助开始，真实互动产生反馈，再回头调整判断。材料并非简单主张“理论无用”，而是反对用积累术语和句子替代实际能力。

**理由与跨期联系：**直播72谈话术的临时支撑与成为能自然表达的人；直播77批评理论过载；直播79/80又谈具体问题、框架和主动整理，说明理论在材料中更像行动的辅助而不是通用按钮。直播82的渐进案例是观众经历，直播83的成长回顾是人物自述，二者都不能当作效果实验。

**候选顺序：**明确卡点是开始行动、表达、邀约还是复盘，不先购买更多理论来替代诊断。；挑出与卡点有关的最少概念，再在自愿、可退出的现实互动中尝试。；记录实际发生的回应与自己的解释；录音拍摄不属于自动获得的权限。；比较预期和实际，调整下一次的条件或行为，不把一次结果写成成功法则。

**适用条件：**本包不能给出统一练习次数、每周约会量或成功率标准。；需要录音或使用私人聊天作材料时，另行处理授权与隐私。

**观察什么反馈：**看是否形成可解释的判断，而不只看收藏了多少话术。；进步可描述为能完成原先做不到的步骤，但不能把别人的接受或亲密行为当作必须取得的训练指标。

**边界：**直播79每周3—4次等数字是课程语境，不是普适剂量。；直播80信念—行动循环与直播79长期目标的代表引文错配，不能用于闭环证明。

**可有限转述的direct子集：**`mikey-youtube-live-023-K009`

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K010` → `mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-023-K004` → `mikey-youtube-live-023-E0001-R162` / `S00162`；`mikey-youtube-live-023-K009` → `mikey-youtube-live-023-E0004-R005` / `S00473`；`mikey-youtube-live-023-K017` → `mikey-youtube-live-023-E0009-R023` / `S01287`；`mikey-youtube-live-023-K018` → `mikey-youtube-live-023-E0009-R110` / `S01374`；`mikey-youtube-live-023-K021` → `mikey-youtube-live-023-E0011-R030` / `S01529`；`mikey-youtube-live-023-K023` → `mikey-youtube-live-023-E0012-R036` / `S01643`；`mikey-youtube-live-025-K010` → `mikey-youtube-live-025-E0005-R037` / `S00641`；`mikey-youtube-live-026-K001` → `mikey-youtube-live-026-E0004-R045` / `S00375`；`mikey-youtube-live-026-K002` → `mikey-youtube-live-026-E0004-R082` / `S00412`；`mikey-youtube-live-026-K003` → `mikey-youtube-live-026-E0007-R093` / `S00723`；`mikey-youtube-live-026-K009` → `mikey-youtube-live-026-E0011-R101` / `S01161`；`mikey-youtube-live-027-K001` → `mikey-youtube-live-027-E0001-R016` / `S00016`；`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-027-K003` → `mikey-youtube-live-027-E0002-R049` / `S00154`；`mikey-youtube-live-027-K009` → `mikey-youtube-live-027-E0009-R043` / `S00883`；`mikey-youtube-live-027-K011` → `mikey-youtube-live-027-E0013-R011` / `S01211`；`mikey-youtube-live-028-K002` → `mikey-youtube-live-028-E0005-R071` / `S00521`；`mikey-youtube-live-028-K003` → `mikey-youtube-live-028-E0005-R049` / `S00499`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-030-K008` → `mikey-youtube-live-030-E0004-R020` / `S00394`；`mikey-youtube-live-030-K011` → `mikey-youtube-live-030-E0007-R052` / `S00727`；`mikey-youtube-live-030-K012` → `mikey-youtube-live-030-E0013-R024` / `S01318`。

</details>
### T04 · 呈现与表达：状态、风格和真实生活信息，而非统一模板

**判断：**材料中的表达建议同时关注外形、语气、眼神、能量和生活内容，但没有支持一套人人相同的表演模板。

**理由与跨期联系：**直播68讨论销售式表达与外形特征平衡；直播72区分开场方式的适用状态并强调白话；直播80讨论翻译工具，说明使用工具不自动等于弱势。学历、领域能力和朋友圈又被当作信息是否被对方感知的问题，而不是资历本身保证吸引。

**候选顺序：**先辨认互动中给人的整体印象，避免只修改孤立措辞。；根据真实气质和能理解的语言表达，不把安静伪装成淡定，也不强迫自己持续高能量。；让外在呈现与真实生活能够对应；不补造履历、照片内容或兴趣经历。

**适用条件：**外形维护不扩展为医美、药物、训练频率或年龄效果承诺。；语言工具只解决理解问题，不能替代对方是否愿意交流。

**观察什么反馈：**关注表达是否清楚、对方是否理解以及能否自然继续，而非是否完整复制某个句式。；穿搭、语气等只能作为候选因素，不能从一次结果认定因果。

**边界：**高低能量与强弱行为线索的对应关系未做实证检验。；人物案例和风格平衡不能升级为性别或外貌等级表。

**可有限转述的direct子集：**无

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K007` → `mikey-youtube-live-021-E0005-R003` / `S00384`；`mikey-youtube-live-021-K008` → `mikey-youtube-live-021-E0005-R012` / `S00393`；`mikey-youtube-live-021-K018` → `mikey-youtube-live-021-E0011-R040` / `S01122`；`mikey-youtube-live-021-K019` → `mikey-youtube-live-021-E0012-R016` / `S01180`；`mikey-youtube-live-023-K010` → `mikey-youtube-live-023-E0007-R048` / `S01062`；`mikey-youtube-live-023-K014` → `mikey-youtube-live-023-E0006-R085` / `S00933`；`mikey-youtube-live-025-K002` → `mikey-youtube-live-025-E0001-R094` / `S00094`；`mikey-youtube-live-025-K006` → `mikey-youtube-live-025-E0003-R019` / `S00377`；`mikey-youtube-live-025-K007` → `mikey-youtube-live-025-E0004-R015` / `S00490`；`mikey-youtube-live-025-K009` → `mikey-youtube-live-025-E0005-R005` / `S00609`；`mikey-youtube-live-027-K004` → `mikey-youtube-live-027-E0003-R002` / `S00197`；`mikey-youtube-live-029-K008` → `mikey-youtube-live-029-E0005-R122` / `S00722`；`mikey-youtube-live-030-K007` → `mikey-youtube-live-030-E0003-R089` / `S00355`。

</details>
### T05 · 不回复与态度变化：把诊断放回完整互动，而非神奇话术

**判断：**较清楚的跨期判断是：拿到联系方式只是一个环节；不回复、聊不动或突然热络，不能只归因于最后一句话。

**理由与跨期联系：**直播68与72把现场状态、后续呈现和聊天连起来；直播75用“新身份信息被看见”的假设说明错误归因；直播77的提前离开和主动性讨论提醒，行为可以有多种解释。这里保留的是诊断方向，不是代替对方宣布内心原因。

**候选顺序：**把联系前、交换联系方式、后续聊天和邀约分成不同环节。；检查出现变化前是否有新信息、情境改变或互动落差。；优先描述可观察行为，再提出有限解释；不能因为某次用了话术就认定话术有效。

**适用条件：**没有私人完整记录时，不给唯一原因。；不能把拿号、回复、见面、到场与亲密结果串成自动成立的因果链。

**观察什么反馈：**区分是否回复、是否主动延展以及是否给出具体安排。；相似主题多次出现，只说明同类解释被反复提起，不是独立验证。

**边界：**直播72拿号条目的代表片段只有观众提问；直播81收号条目引文偏离主题，均暂缓。；直播75的名人身份例子是说明归因的假设，不是本次核实的真实约会。

**可有限转述的direct子集：**`mikey-youtube-live-021-K005`、`mikey-youtube-live-024-K007`

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K005` → `mikey-youtube-live-021-E0004-R008` / `S00292`；`mikey-youtube-live-021-K006` → `mikey-youtube-live-021-E0004-R039` / `S00323`；`mikey-youtube-live-023-K006` → `mikey-youtube-live-023-E0002-R091` / `S00278`；`mikey-youtube-live-024-K001` → `mikey-youtube-live-024-E0001-R037` / `S00037`；`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-025-K003` → `mikey-youtube-live-025-E0002-R031` / `S00199`；`mikey-youtube-live-025-K008` → `mikey-youtube-live-025-E0004-R046` / `S00521`；`mikey-youtube-live-027-K005` → `mikey-youtube-live-027-E0004-R028` / `S00338`；`mikey-youtube-live-028-K006` → `mikey-youtube-live-028-E0009-R051` / `S00941`；`mikey-youtube-live-029-K004` → `mikey-youtube-live-029-E0002-R068` / `S00227`。

</details>
### T06 · 聊天与邀约：看实际投入和可行安排，不无限猜测

**判断：**这组材料通常先问“对方有没有继续交流或见面的行动”，而不是把问题永远留在聊天热不热。

**理由与跨期联系：**直播75把单向输出与对方可能不想聊天分开；直播72在“忙”的情境里转向愿意见面与具体可行时间。其他几期讨论基本熟悉、线上与现实的落差、异地安排和时间边界。它们能形成有条件的候选路径，但不能推成越早越好或见面一定安全。

**候选顺序：**先看是否有基本身份与交流意愿，不把回复本身理解为下一步许可。；对于模糊的忙或没空，用一次清楚的澄清了解是否愿意见面以及是否有可行时间。；没有明确安排或对方拒绝时停止反复追问；不要用时间边界包装惩罚和施压。

**适用条件：**无固定聊天天数或通用邀约次数。；异地、预算、交通和独立离开能力会改变实际可行性。；涉及酒精、夜间私人地点或电话压力的条目不进入这条方法链。

**观察什么反馈：**观察对方是否主动提问、延展话题或提出替代安排。；不给具体时间可作为停止投入的行动依据，不能证明对方恶意或某类人格。

**边界：**接受一次见面仅限该次安排。；直播79主动邀约、直播80地点建议和直播81线上邀约的代表引文不足，不能借本主题获得放行。

**可有限转述的direct子集：**`mikey-youtube-live-023-K007`、`mikey-youtube-live-024-K006`

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K002` → `mikey-youtube-live-021-E0002-R080` / `S00128`；`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-021-K017` → `mikey-youtube-live-021-E0011-R022` / `S01104`；`mikey-youtube-live-023-K007` → `mikey-youtube-live-023-E0003-R006` / `S00334`；`mikey-youtube-live-023-K016` → `mikey-youtube-live-023-E0008-R024` / `S01189`；`mikey-youtube-live-024-K002` → `mikey-youtube-live-024-E0001-R061` / `S00061`；`mikey-youtube-live-024-K006` → `mikey-youtube-live-024-E0004-R027` / `S00733`；`mikey-youtube-live-024-K009` → `mikey-youtube-live-024-E0005-R193` / `S01084`；`mikey-youtube-live-024-K010` → `mikey-youtube-live-024-E0007-R009` / `S01235`；`mikey-youtube-live-026-K005` → `mikey-youtube-live-026-E0008-R033` / `S00763`；`mikey-youtube-live-027-K008` → `mikey-youtube-live-027-E0008-R071` / `S00811`；`mikey-youtube-live-028-K001` → `mikey-youtube-live-028-E0001-R061` / `S00061`；`mikey-youtube-live-029-K002` → `mikey-youtube-live-029-E0001-R045` / `S00045`。

</details>
### T07 · 面对拒绝与退出：不自我否定，也不绕开对方边界

**判断：**候选主线是把拒绝从整个人的价值中分离，并愿意退出不成立的互动；与“换号绕过拉黑”“骂回去”必须保持显式冲突。

**理由与跨期联系：**直播72、75、80、83反复讨论拒绝和紧张；直播68的放鸽子边界、直播81的离开与压抑涉及不同场景。复盘自己和控制自己是否继续投入，是一类行为；迫使对方继续、报复或把他人的拒绝当作训练障碍，是另一类行为。

**候选顺序：**先确认反馈是拒绝、暂时不能安排，还是尚不明确，不能把明确拒绝重新解释成等待说服。；明确拒绝或拉黑后结束该次推进。；在不继续打扰原对象的前提下复盘可改因素；未来练习属于新的自愿互动。

**适用条件：**已有伴侣、师生、未成年或其他权力差异要先处理适用边界。；不把不反抗、留下、接受前一步或继续聊天当成下一步同意。

**观察什么反馈：**能否结束而不辱骂、不换渠道追踪、不把拒绝归为整个人失败。；所谓真的不在意不能靠让对方屈服来证明。

**边界：**安全退出和拒绝边界是本输出的编辑规则，不冒充所有原讲者均贯彻过。；冲突未因后一期相似观点而被撤回或修正。

**可有限转述的direct子集：**无

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K009` → `mikey-youtube-live-021-E0005-R075` / `S00456`；`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-023-K011` → `mikey-youtube-live-023-E0002-R133` / `S00320`；`mikey-youtube-live-023-K012` → `mikey-youtube-live-023-E0005-R113` / `S00752`；`mikey-youtube-live-023-K019` → `mikey-youtube-live-023-E0010-R001` / `S01389`；`mikey-youtube-live-023-K024` → `mikey-youtube-live-023-E0014-R013` / `S01857`；`mikey-youtube-live-024-K015` → `mikey-youtube-live-024-E0011-R040` / `S01830`；`mikey-youtube-live-024-K016` → `mikey-youtube-live-024-E0010-R029` / `S01694`；`mikey-youtube-live-027-K007` → `mikey-youtube-live-027-E0008-R012` / `S00752`；`mikey-youtube-live-028-K005` → `mikey-youtube-live-028-E0008-R061` / `S00841`；`mikey-youtube-live-028-K011` → `mikey-youtube-live-028-E0014-R019` / `S01483`；`mikey-youtube-live-030-K002` → `mikey-youtube-live-030-E0001-R152` / `S00152`；`mikey-youtube-live-030-K009` → `mikey-youtube-live-030-E0005-R078` / `S00523`。

</details>
### T08 · 真实意图、承诺与互惠：独立选择不等于单方制定规则

**判断：**材料中“不要隐性索取、不要空头承诺、保留自己的标准”与“支配、单方面双重标准、羞辱”并存，不能写成一条无矛盾的关系哲学。

**理由与跨期联系：**直播82/83讨论讨好背后的期待和真实表达；直播77谈承诺与行动；直播72/75谈金钱互惠。另一方面，多期出现服从、不可离开、欺骗或对另一方的限制。前者至多是有条件的候选观点，后者保留在不可泛化与冲突账本，不用“主体性”重新命名。

**候选顺序：**把自己想要的关系与愿意承担的承诺说清楚，不把含糊当成免于说明的办法。；检查双方是否理解并自愿接受，而非只有一方定义关系。；金钱、礼物、陪伴与性同意分别判断；关系不符合约定时退出，不以羞辱和强制服从维持。

**适用条件：**自愿、清楚、可撤回是编辑使用边界。；任何一方都可以拒绝关系、拒绝具体行为或改变主意。

**观察什么反馈：**比较实际行动与明确约定，而非根据一句“我不主动”或“我专一”完成判断。；没有同意闭环的结果叙述不能验证方法正当或有效。

**边界：**这不是对原稿矛盾进行道德美化；相反立场逐条并列。；相关金钱、性行为、支配、电话和偷拍/录音条目多数受开放待核限制。

**可有限转述的direct子集：**无

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K015` → `mikey-youtube-live-023-E0006-R107` / `S00955`；`mikey-youtube-live-024-K013` → `mikey-youtube-live-024-E0008-R067` / `S01423`；`mikey-youtube-live-025-K014` → `mikey-youtube-live-025-E0011-R007` / `S01205`；`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-027-K012` → `mikey-youtube-live-027-E0007-R021` / `S00651`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-029-K006` → `mikey-youtube-live-029-E0003-R064` / `S00386`；`mikey-youtube-live-029-K007` → `mikey-youtube-live-029-E0004-R142` / `S00562`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-030-K001` → `mikey-youtube-live-030-E0001-R060` / `S00060`；`mikey-youtube-live-030-K009` → `mikey-youtube-live-030-E0005-R078` / `S00523`；`mikey-youtube-live-030-K010` → `mikey-youtube-live-030-E0001-R107` / `S00107`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### T09 · 把两性问题放回自己的生活：资源、重心与选择成本

**判断：**材料不只谈互动技巧，也谈工作、教育、时间、住处、课程消费和长期投入；它们不能被压缩成“为了吸引而改造一切”。

**理由与跨期联系：**直播72把人生重心和具体问题拆解联系起来；直播68有拒绝贷款报课的片段及投入经历自述；直播77讨论大学去留与能力如何呈现。这些内容可帮助理解人物的取舍顺序，但求职、收益和成长叙述不是可复制回报承诺。

**候选顺序：**先识别现实约束是钱、时间、工作、学习还是居住安排。；把一次关系问题与长期生活决定分开，列出替代路径及能够承担的成本。；在自己愿意持续做的事情上投入；课程、消费或关系选择不以保证获得他人作为回报。

**适用条件：**不提供包中没有的退学、就业、负债或投资方案。；不得把某次工作offer、收入或自述成功当作普适因果。

**观察什么反馈：**看现实问题是否被具体处理，而不是仅获得短时情绪激励。；教育或工作调整需要独立信息，本包只能保留讨论框架。

**边界：**直播79长期目标条目代表引文明显偏向关系规则，不能补写成创业或事业理论。；人生重心也不能被误解为忽视对方承诺和边界。

**可有限转述的direct子集：**无

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K010` → `mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-021-K013` → `mikey-youtube-live-021-E0007-R037` / `S00659`；`mikey-youtube-live-023-K003` → `mikey-youtube-live-023-E0001-R134` / `S00134`；`mikey-youtube-live-023-K017` → `mikey-youtube-live-023-E0009-R023` / `S01287`；`mikey-youtube-live-023-K023` → `mikey-youtube-live-023-E0012-R036` / `S01643`；`mikey-youtube-live-025-K001` → `mikey-youtube-live-025-E0001-R081` / `S00081`；`mikey-youtube-live-025-K002` → `mikey-youtube-live-025-E0001-R094` / `S00094`；`mikey-youtube-live-025-K004` → `mikey-youtube-live-025-E0002-R059` / `S00227`；`mikey-youtube-live-025-K005` → `mikey-youtube-live-025-E0002-R108` / `S00276`；`mikey-youtube-live-025-K013` → `mikey-youtube-live-025-E0009-R076` / `S01107`；`mikey-youtube-live-026-K009` → `mikey-youtube-live-026-E0011-R101` / `S01161`；`mikey-youtube-live-029-K002` → `mikey-youtube-live-029-E0001-R045` / `S00045`；`mikey-youtube-live-029-K008` → `mikey-youtube-live-029-E0005-R122` / `S00722`；`mikey-youtube-live-030-K010` → `mikey-youtube-live-030-E0001-R107` / `S00107`。

</details>
### T10 · 直播70：动漫角色讨论只能保留为多人材料，不能借角色替Mikey发言

**判断：**本期18条知识的归属全部为mixed_speakers，2014个SID全部落在uncertain_overlap。可以分析它讨论了哪些评价维度，但不能确定这些话由Mikey独立提出。

**理由与跨期联系：**标题与事件目录具体描述火影等动漫角色排名、角色立绘和剧情复述；任务同时要求按游戏五类控制。二者可兼容为播放材料/角色讨论的归属管理，不能据此新增实际游戏操作或角色经历。稳定、真实性、领导力、缺爱和降低摩擦等概括只能作候选主题，精神控制、酒精金钱压力和权力操纵仍不可方法化。

**候选顺序：**先对照五类归属，不以频道、标题、主持在场或声音相似代替逐句映射。；剧情、观众文字、朗读与个人评论分开。；只有今后被实际核为mikey_commentary且其他限制已解除的片段，才可能支持人物观点；本次没有这样的SID。

**适用条件：**不把戴面具者、其他嘉宾和未知声音直接合并为Mikey。；角色说过/做过与现实可用原则之间不得自动迁移。

**观察什么反馈：**本次反馈仅是归属表覆盖与限制是否保留，不能评价游戏或关系方法是否有效。

**边界：**10条candidate_only映射hold，原4条hold保持hold，4条do_not_generalize保持原限制。；所有动漫主题与其他期的相似仅作并列，不算Mikey观点的额外佐证。

**可有限转述的direct子集：**无

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### T11 · 直播82：电话演示按通话事件与说话人分别封存

**判断：**电话接通、继续说话、参与者自述、拒绝、邀请和最终结果必须逐层分开。当前没有足以把整段电话变成Mikey示范话术的句级归属。

**理由与跨期联系：**事件目录含多轮拨打、长通话及回拨话题，但caller-01是集合占位。E0007至E0012与E0014不能被自动串成同一女性、同一关系或同一次结果；事件层spoken_by_id仍写主持，也不能覆盖更细的call_participants_not_sentence_level_diarized限制。

**候选顺序：**逐事件登记时间、可能参与者和未知项，不推断电话另一端姓名或身份。；先核查谁说、是否知道直播、是否授权公开，再区分邀请和具体拒绝。；出现拒绝或想睡觉的语句时，不产生继续推进、辱骂或施压的回答模板。

**适用条件：**该期全期visual_not_available阻断仍开放。；电话音轨或聊天界面不证明到场、亲密、身份一致或持续同意。

**观察什么反馈：**只能检查本包有没有提供明确归属与授权；没有就保持未知。

**边界：**不是重新听辨结果，也没有连续观看电话画面。；9条非DNG知识均hold，3条DNG保留；当中的原direct与context_only没有被删改。

**可有限转述的direct子集：**无

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`。

</details>
### T12 · 身体、医疗与心理解释：保留语境，不变成诊断或安全保证

**判断：**皮肤、性传播感染、非安全性行为、原生家庭、缺爱与上头等话题不能因为出现在同一人物体系里就获得医学或心理学效力。

**理由与跨期联系：**材料中有去正规医疗机构的收窄，也有药物、疾病风险、避孕及创伤解释的高风险概括。原知识中“不能……”常是逐期编辑者补充的限制，不可倒写成Mikey始终表达过的医学立场。

**候选顺序：**区分当事人主诉、人物观点、编辑纠正与需要专业核验的问题。；保留普通生活讨论的语境，但不推出疗程、药物效果、遗传决定或疾病概率。；涉及人身安全、治疗或性健康的片段暂不用于行动建议。

**适用条件：**本次未做医疗文献检索、诊断或治疗指导。；年龄、外貌或关系经验不能代替个体健康事实。

**观察什么反馈：**只检查证据是否足以支持原范围，不用个人经历替代可靠医疗判断。

**边界：**阴性词、数字或否定词变化可能完全改变风险含义；原音待核不解除。；对安全规则的编辑表述不等于已核实的原话。

**可有限转述的direct子集：**无

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K012` → `mikey-youtube-live-021-E0006-R083` / `S00580`；`mikey-youtube-live-021-K019` → `mikey-youtube-live-021-E0012-R016` / `S01180`；`mikey-youtube-live-024-K005` → `mikey-youtube-live-024-E0003-R152` / `S00563`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-026-K006` → `mikey-youtube-live-026-E0007-R084` / `S00714`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`；`mikey-youtube-live-028-K009` → `mikey-youtube-live-028-E0013-R031` / `S01413`；`mikey-youtube-live-028-K010` → `mikey-youtube-live-028-E0013-R045` / `S01427`。

</details>
### T13 · 群体、标签与评价：人物立场不等于社会事实

**判断：**避免被一个标签支配与对性别、族群、职业、地域或体型的贬损同时存在；必须保存这种张力，而不是挑出正面部分替人物统一立场。

**理由与跨期联系：**直播68讨论网络样本与标签，直播72/75讨论外界评价，后几期却出现NPC、职业、性别、族群和体型概括。平台动机、个人心理和群体行为均无独立验证；批评者是否出于嫉妒也不是本包能确认的事实。

**候选顺序：**先确定是谁提出评价，是观众、人物、角色还是编辑概括。；把可定位的言论作为立场证据保存，不推出该群体真实如此。；涉及未成年人、职业权力和隐私时，先执行适用边界，不用个体“主体性”覆盖它。

**适用条件：**不输出群体贬损、体型羞辱或追求弱势人群的策略。；不把公共舆论热度当作现实比例。

**观察什么反馈：**观察答案是否从具体人和实际行为滑向群体本质；出现该变化就停止泛化。

**边界：**争议材料仍保留，不删除、不美化，也不作为行动建议。；跨期重复偏见不增加其真实性。

**可有限转述的direct子集：**无

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K014` → `mikey-youtube-live-021-E0009-R064` / `S00945`；`mikey-youtube-live-021-K016` → `mikey-youtube-live-021-E0010-R071` / `S01031`；`mikey-youtube-live-023-K020` → `mikey-youtube-live-023-E0010-R020` / `S01408`；`mikey-youtube-live-023-K022` → `mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-023-K025` → `mikey-youtube-live-023-E0006-R006` / `S00854`；`mikey-youtube-live-024-K014` → `mikey-youtube-live-024-E0008-R089` / `S01445`；`mikey-youtube-live-025-K016` → `mikey-youtube-live-025-E0003-R005` / `S00363`；`mikey-youtube-live-027-K012` → `mikey-youtube-live-027-E0007-R021` / `S00651`；`mikey-youtube-live-028-K007` → `mikey-youtube-live-028-E0010-R128` / `S01128`；`mikey-youtube-live-028-K008` → `mikey-youtube-live-028-E0011-R075` / `S01203`；`mikey-youtube-live-029-K012` → `mikey-youtube-live-029-E0001-R030` / `S00030`；`mikey-youtube-live-030-K005` → `mikey-youtube-live-030-E0002-R059` / `S00214`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### T14 · 同意、法律与隐私：独立于吸引解释的使用闸门

**判断：**吸引、接受邀约、进入某处、没有反抗、付出金钱或关系身份，都不能在本综合中替代对具体行为的清楚同意。此处是编辑边界，不是假称人物一贯立场。

**理由与跨期联系：**直播68的酒精和转场、直播72/75的拉黑、未成年与性压力、直播79的非安全性行为、直播81的欺骗上楼、直播82的电话拒绝、直播83的脱衣与不反抗，属于不同事件。它们需要各自证据，不能用别的案例或后续结果补写前一时点的授权。

**候选顺序：**先分辨行为对象、具体行为、当时意愿和是否存在能力/权力问题。；拒绝、撤回、犹疑和边界表达分别标记；不得由前一步同意跳到下一步。；涉及私密材料、录音拍摄或公开电话，单独核查是否有相应授权；未核材料不进入示范。

**适用条件：**不提供绕过拉黑、削弱判断、灌酒、羞辱或强行推进的做法。；本次也不把人物区分搭讪与暴力的说法当作法律结论。

**观察什么反馈：**看到同意链或授权链缺项就保持hold/DNG，不拿标题或当事人口述结果补齐。

**边界：**危害边界优先于动作序列和人物化表达。；对方留下、不反抗或接电话不构成下一步授权。

**可有限转述的direct子集：**无

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K003` → `mikey-youtube-live-021-E0002-R099` / `S00147`；`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-023-K015` → `mikey-youtube-live-023-E0006-R107` / `S00955`；`mikey-youtube-live-023-K019` → `mikey-youtube-live-023-E0010-R001` / `S01389`；`mikey-youtube-live-023-K022` → `mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-023-K024` → `mikey-youtube-live-023-E0014-R013` / `S01857`；`mikey-youtube-live-023-K025` → `mikey-youtube-live-023-E0006-R006` / `S00854`；`mikey-youtube-live-024-K011` → `mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-024-K016` → `mikey-youtube-live-024-E0010-R029` / `S01694`；`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-026-K006` → `mikey-youtube-live-026-E0007-R084` / `S00714`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-027-K012` → `mikey-youtube-live-027-E0007-R021` / `S00651`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-030-K009` → `mikey-youtube-live-030-E0005-R078` / `S00523`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### T15 · 案例、数字与效果：区分讲述、教学例子和可验证结果

**判断：**多个故事和多次相似判断只能表明材料中重复出现某种解释，不能证明成功率、回报或方法因果。

**理由与跨期联系：**高成功率、短期求职、固定周练习量、三秒及百分比、观众两次到五次的尝试、个人成长回顾都处于不同证据层。假设例子尤其不能与真实案例合并。整期来源unique也不说明每个故事都是新的独立样本。

**候选顺序：**先标明数字来自人物自述、观众转述、课程要求还是假设例子。；确认是否有分母、统计口径、时间范围与独立结果证据。；缺项时保留原表述的定位，不计算新成功率或累计案例样本量。

**适用条件：**不把号码、见面和亲密结果换算成同一个指标。；没有完整逐字稿和连续音画时，不对重播或硬切前后建立结果闭环。

**观察什么反馈：**检查结论是否仍明确“谁声称了什么”，而不是变成“已经发生/已经证明”。

**边界：**本次未运行回答质量测试、成功率评测或正式接入。；963原引文计数不能伪装成本次看过963条引文。

**可有限转述的direct子集：**`mikey-youtube-live-024-K007`

其余支撑只作候选、背景或争议定位；主题本身不是可执行回答。

<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-021-K010` → `mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-023-K001` → `mikey-youtube-live-023-E0001-R045` / `S00045`；`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-025-K003` → `mikey-youtube-live-025-E0002-R031` / `S00199`；`mikey-youtube-live-025-K005` → `mikey-youtube-live-025-E0002-R108` / `S00276`；`mikey-youtube-live-026-K002` → `mikey-youtube-live-026-E0004-R082` / `S00412`；`mikey-youtube-live-027-K009` → `mikey-youtube-live-027-E0009-R043` / `S00883`；`mikey-youtube-live-028-K003` → `mikey-youtube-live-028-E0005-R049` / `S00499`；`mikey-youtube-live-028-K006` → `mikey-youtube-live-028-E0009-R051` / `S00941`；`mikey-youtube-live-029-K004` → `mikey-youtube-live-029-E0002-R068` / `S00227`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-030-K012` → `mikey-youtube-live-030-E0013-R024` / `S01318`。

</details>
## 3. 命题：支持、反例与不能跨越的范围

### P01 · 在这套候选解释中，维持吸引更依赖真实状态的一致，而非持续加码表演。

**理由：**压力会暴露短时表演与日常反应的差距；线上信息、现场表现和后续生活被放在同一条解释链。

**条件：**不推定某人的冷淡必由不一致造成；不提供表演维持技巧。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K001`、`mikey-youtube-live-023-K005`、`mikey-youtube-live-024-K008`、`mikey-youtube-live-027-K006`、`mikey-youtube-live-027-K010`、`mikey-youtube-live-028-K004`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-023-K005` → `mikey-youtube-live-023-E0002-R005` / `S00192`；`mikey-youtube-live-024-K008` → `mikey-youtube-live-024-E0004-R154` / `S00860`；`mikey-youtube-live-027-K006` → `mikey-youtube-live-027-E0005-R028` / `S00448`；`mikey-youtube-live-027-K010` → `mikey-youtube-live-027-E0012-R043` / `S01173`；`mikey-youtube-live-028-K004` → `mikey-youtube-live-028-E0006-R016` / `S00576`。

</details>
### P02 · “稳定”与话多、话少或高能量不是同一个维度。

**理由：**材料区分可持续的自我状态与外在活跃程度，不要求统一的外向模板。

**条件：**直播68/75/83相关支撑受待核或代表片段不足限制。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K011`、`mikey-youtube-live-024-K003`、`mikey-youtube-live-030-K007`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K011` → `mikey-youtube-live-021-E0006-R057` / `S00554`；`mikey-youtube-live-024-K003` → `mikey-youtube-live-024-E0002-R104` / `S00249`；`mikey-youtube-live-030-K007` → `mikey-youtube-live-030-E0003-R089` / `S00355`。

</details>
### P03 · 初始印象被解释为一组线索，而非一个孤立动作。

**理由：**现场线索提供最初画像，后续个性和生活信息再补充；属于人物模型而非实证机制。

**条件：**不把角色排名、照片或一次回复当作模型验证。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K006`、`mikey-youtube-live-023-K001`、`mikey-youtube-live-025-K007`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K006` → `mikey-youtube-live-021-E0004-R039` / `S00323`；`mikey-youtube-live-023-K001` → `mikey-youtube-live-023-E0001-R045` / `S00045`；`mikey-youtube-live-025-K007` → `mikey-youtube-live-025-E0004-R015` / `S00490`。

</details>
### P04 · 一次拒绝或一次表现不佳，不足以判定一个人的全部价值。

**理由：**候选解释把过度紧张联系到把对方当裁判；不能借该解释贬低对方。

**条件：**不当作焦虑症诊断或治疗。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-023-K002`、`mikey-youtube-live-023-K008`、`mikey-youtube-live-023-K020`、`mikey-youtube-live-025-K011`、`mikey-youtube-live-030-K002`、`mikey-youtube-live-030-K004`

**限制或相反知识：**`mikey-youtube-live-028-K008`、`mikey-youtube-live-030-K005`

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K002` → `mikey-youtube-live-023-E0001-R068` / `S00068`；`mikey-youtube-live-023-K008` → `mikey-youtube-live-023-E0003-R060` / `S00388`；`mikey-youtube-live-023-K020` → `mikey-youtube-live-023-E0010-R020` / `S01408`；`mikey-youtube-live-025-K011` → `mikey-youtube-live-025-E0007-R031` / `S00844`；`mikey-youtube-live-030-K002` → `mikey-youtube-live-030-E0001-R152` / `S00152`；`mikey-youtube-live-030-K004` → `mikey-youtube-live-030-E0002-R051` / `S00206`；`mikey-youtube-live-028-K008` → `mikey-youtube-live-028-E0011-R075` / `S01203`；`mikey-youtube-live-030-K005` → `mikey-youtube-live-030-E0002-R059` / `S00214`。

</details>
### P05 · 资源条件与自我价值感在材料中被分开讨论。

**理由：**金钱、学历、地位和自我认可不是同一概念；仅能有限转述主心骨观点，不能设定通用魅力公式。

**条件：**不得保证拥有或放弃某种资源会带来特定关系结果。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-025-K004`、`mikey-youtube-live-025-K012`、`mikey-youtube-live-030-K006`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K004` → `mikey-youtube-live-025-E0002-R059` / `S00227`；`mikey-youtube-live-025-K012` → `mikey-youtube-live-025-E0007-R073` / `S00886`；`mikey-youtube-live-030-K006` → `mikey-youtube-live-030-E0003-R007` / `S00273`。

</details>
### P06 · 保有独立判断不等于有权控制另一方。

**理由：**直播75的自我与退出和其他期的主心骨可并列；支配、服从和单方规则构成必须保留的冲突。

**条件：**自主同样属于对方；两者不能通过改名合并。

**归属层：**cross_episode_view_comparison_with_editorial_boundary

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-024-K004`、`mikey-youtube-live-023-K013`、`mikey-youtube-live-026-K004`、`mikey-youtube-live-028-K007`、`mikey-youtube-live-029-K001`

**限制或相反知识：**`mikey-youtube-live-025-K015`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-030-K013`

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K004` → `mikey-youtube-live-024-E0002-R139` / `S00284`；`mikey-youtube-live-023-K013` → `mikey-youtube-live-023-E0005-R175` / `S00814`；`mikey-youtube-live-026-K004` → `mikey-youtube-live-026-E0012-R044` / `S01224`；`mikey-youtube-live-028-K007` → `mikey-youtube-live-028-E0010-R128` / `S01128`；`mikey-youtube-live-029-K001` → `mikey-youtube-live-029-E0001-R130` / `S00130`；`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### P07 · 理论和话术的候选作用是帮助行动，不是代替能力。

**理由：**批评理论过载与强调框架可按阶段区分：初学支撑、实践暴露问题、整理提升判断。

**条件：**不推导购买课程必要性或统一练习量。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-023-K004`、`mikey-youtube-live-023-K009`、`mikey-youtube-live-025-K010`、`mikey-youtube-live-026-K001`、`mikey-youtube-live-026-K003`、`mikey-youtube-live-027-K001`、`mikey-youtube-live-027-K003`、`mikey-youtube-live-030-K011`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K004` → `mikey-youtube-live-023-E0001-R162` / `S00162`；`mikey-youtube-live-023-K009` → `mikey-youtube-live-023-E0004-R005` / `S00473`；`mikey-youtube-live-025-K010` → `mikey-youtube-live-025-E0005-R037` / `S00641`；`mikey-youtube-live-026-K001` → `mikey-youtube-live-026-E0004-R045` / `S00375`；`mikey-youtube-live-026-K003` → `mikey-youtube-live-026-E0007-R093` / `S00723`；`mikey-youtube-live-027-K001` → `mikey-youtube-live-027-E0001-R016` / `S00016`；`mikey-youtube-live-027-K003` → `mikey-youtube-live-027-E0002-R049` / `S00154`；`mikey-youtube-live-030-K011` → `mikey-youtube-live-030-E0007-R052` / `S00727`。

</details>
### P08 · 练习应连接反馈与复盘，不能仅以重复数量计算成长。

**理由：**渐进、经历和思考在多期出现，但观众经历、课程要求与人物自述须分层。

**条件：**隐私授权另审；不把他人的接受作为训练任务。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K001`、`mikey-youtube-live-023-K018`、`mikey-youtube-live-023-K021`、`mikey-youtube-live-027-K002`、`mikey-youtube-live-027-K009`、`mikey-youtube-live-027-K011`、`mikey-youtube-live-028-K002`、`mikey-youtube-live-029-K005`、`mikey-youtube-live-030-K008`、`mikey-youtube-live-030-K012`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-023-K018` → `mikey-youtube-live-023-E0009-R110` / `S01374`；`mikey-youtube-live-023-K021` → `mikey-youtube-live-023-E0011-R030` / `S01529`；`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-027-K009` → `mikey-youtube-live-027-E0009-R043` / `S00883`；`mikey-youtube-live-027-K011` → `mikey-youtube-live-027-E0013-R011` / `S01211`；`mikey-youtube-live-028-K002` → `mikey-youtube-live-028-E0005-R071` / `S00521`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-030-K008` → `mikey-youtube-live-030-E0004-R020` / `S00394`；`mikey-youtube-live-030-K012` → `mikey-youtube-live-030-E0013-R024` / `S01318`。

</details>
### P09 · 生活约束和长期取舍要先具体化，不能全部折算为追求结果。

**理由：**工作、时间、居住、学习和课程成本被放在实际问题层；投入故事不是回报承诺。

**条件：**不提供本包没有的退学、求职或负债方案。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K010`、`mikey-youtube-live-021-K013`、`mikey-youtube-live-023-K003`、`mikey-youtube-live-023-K017`、`mikey-youtube-live-023-K023`、`mikey-youtube-live-025-K001`、`mikey-youtube-live-025-K013`、`mikey-youtube-live-026-K009`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K010` → `mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-021-K013` → `mikey-youtube-live-021-E0007-R037` / `S00659`；`mikey-youtube-live-023-K003` → `mikey-youtube-live-023-E0001-R134` / `S00134`；`mikey-youtube-live-023-K017` → `mikey-youtube-live-023-E0009-R023` / `S01287`；`mikey-youtube-live-023-K023` → `mikey-youtube-live-023-E0012-R036` / `S01643`；`mikey-youtube-live-025-K001` → `mikey-youtube-live-025-E0001-R081` / `S00081`；`mikey-youtube-live-025-K013` → `mikey-youtube-live-025-E0009-R076` / `S01107`；`mikey-youtube-live-026-K009` → `mikey-youtube-live-026-E0011-R101` / `S01161`。

</details>
### P10 · 自然表达关注真实状态和理解，而不是标准化的凶、温柔或高能量姿态。

**理由：**销售式表达、白话、开场条件、外形平衡和翻译工具是不同维度；不能合并为一套强制表演。

**条件：**不能新增外貌等级、医美或训练处方。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K007`、`mikey-youtube-live-021-K008`、`mikey-youtube-live-021-K018`、`mikey-youtube-live-021-K019`、`mikey-youtube-live-023-K010`、`mikey-youtube-live-023-K014`、`mikey-youtube-live-025-K006`、`mikey-youtube-live-025-K009`、`mikey-youtube-live-027-K004`、`mikey-youtube-live-030-K007`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K007` → `mikey-youtube-live-021-E0005-R003` / `S00384`；`mikey-youtube-live-021-K008` → `mikey-youtube-live-021-E0005-R012` / `S00393`；`mikey-youtube-live-021-K018` → `mikey-youtube-live-021-E0011-R040` / `S01122`；`mikey-youtube-live-021-K019` → `mikey-youtube-live-021-E0012-R016` / `S01180`；`mikey-youtube-live-023-K010` → `mikey-youtube-live-023-E0007-R048` / `S01062`；`mikey-youtube-live-023-K014` → `mikey-youtube-live-023-E0006-R085` / `S00933`；`mikey-youtube-live-025-K006` → `mikey-youtube-live-025-E0003-R019` / `S00377`；`mikey-youtube-live-025-K009` → `mikey-youtube-live-025-E0005-R005` / `S00609`；`mikey-youtube-live-027-K004` → `mikey-youtube-live-027-E0003-R002` / `S00197`；`mikey-youtube-live-030-K007` → `mikey-youtube-live-030-E0003-R089` / `S00355`。

</details>
### P11 · 专业能力或稀有身份不自动等于一段互动中的吸引。

**理由：**材料关心信息是否被看到以及双方如何相处；“稀有即有魅力”的推论被用荒谬例子质疑。

**条件：**不拿假设例子评价真实名人的私人关系。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-025-K002`、`mikey-youtube-live-025-K004`、`mikey-youtube-live-025-K006`、`mikey-youtube-live-029-K004`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K002` → `mikey-youtube-live-025-E0001-R094` / `S00094`；`mikey-youtube-live-025-K004` → `mikey-youtube-live-025-E0002-R059` / `S00227`；`mikey-youtube-live-025-K006` → `mikey-youtube-live-025-E0003-R019` / `S00377`；`mikey-youtube-live-029-K004` → `mikey-youtube-live-029-E0002-R068` / `S00227`。

</details>
### P12 · 拿到联系方式后不回复，需要回看整个链路，而非只修补最后一句话。

**理由：**现场呈现、个性信息和后续互动是候选因素；没有完整案例不能宣布唯一原因。

**条件：**直播72/81相关代表引文不足，不能作为独立加强证据。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K005`、`mikey-youtube-live-023-K006`、`mikey-youtube-live-024-K001`、`mikey-youtube-live-025-K007`、`mikey-youtube-live-027-K005`、`mikey-youtube-live-028-K006`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K005` → `mikey-youtube-live-021-E0004-R008` / `S00292`；`mikey-youtube-live-023-K006` → `mikey-youtube-live-023-E0002-R091` / `S00278`；`mikey-youtube-live-024-K001` → `mikey-youtube-live-024-E0001-R037` / `S00037`；`mikey-youtube-live-025-K007` → `mikey-youtube-live-025-E0004-R015` / `S00490`；`mikey-youtube-live-027-K005` → `mikey-youtube-live-027-E0004-R028` / `S00338`；`mikey-youtube-live-028-K006` → `mikey-youtube-live-028-E0009-R051` / `S00941`。

</details>
### P13 · 态度改变前出现的新信息，是检验话术归因的重要替代解释。

**理由：**直播75的身份假设例子明确指向误归因；具体问题具体分析而不是万能按钮。

**条件：**只保留逻辑演示，不宣称真实案例或因果实验。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-024-K007`、`mikey-youtube-live-026-K001`、`mikey-youtube-live-026-K003`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-026-K001` → `mikey-youtube-live-026-E0004-R045` / `S00375`；`mikey-youtube-live-026-K003` → `mikey-youtube-live-026-E0007-R093` / `S00723`。

</details>
### P14 · 聊不动可能意味着对方不想继续，而不只是自己不够会说。

**理由：**看对方是否提问和延展，比无限单向输出更能定位问题，但短回复并不自动证明动机。

**条件：**不把观察指标变成识别谎言或惩罚对方的技术。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-024-K006`、`mikey-youtube-live-023-K016`、`mikey-youtube-live-025-K008`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K006` → `mikey-youtube-live-024-E0004-R027` / `S00733`；`mikey-youtube-live-023-K016` → `mikey-youtube-live-023-E0008-R024` / `S01189`；`mikey-youtube-live-025-K008` → `mikey-youtube-live-025-E0004-R046` / `S00521`。

</details>
### P15 · 模糊的“忙”可以转为对见面意愿和可行时间的澄清。

**理由：**从猜测转到具体安排；持续不给安排可用于停止无限追问，而非证明对方是什么人。

**条件：**不含酒精、私人转场压力；基本意愿不等于具体身体行为同意。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K002`、`mikey-youtube-live-021-K015`、`mikey-youtube-live-021-K017`、`mikey-youtube-live-023-K007`、`mikey-youtube-live-024-K002`、`mikey-youtube-live-024-K009`、`mikey-youtube-live-024-K010`、`mikey-youtube-live-026-K005`、`mikey-youtube-live-027-K008`、`mikey-youtube-live-028-K001`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K002` → `mikey-youtube-live-021-E0002-R080` / `S00128`；`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-021-K017` → `mikey-youtube-live-021-E0011-R022` / `S01104`；`mikey-youtube-live-023-K007` → `mikey-youtube-live-023-E0003-R006` / `S00334`；`mikey-youtube-live-024-K002` → `mikey-youtube-live-024-E0001-R061` / `S00061`；`mikey-youtube-live-024-K009` → `mikey-youtube-live-024-E0005-R193` / `S01084`；`mikey-youtube-live-024-K010` → `mikey-youtube-live-024-E0007-R009` / `S01235`；`mikey-youtube-live-026-K005` → `mikey-youtube-live-026-E0008-R033` / `S00763`；`mikey-youtube-live-027-K008` → `mikey-youtube-live-027-E0008-R071` / `S00811`；`mikey-youtube-live-028-K001` → `mikey-youtube-live-028-E0001-R061` / `S00061`。

</details>
### P16 · 约会提前结束或约不出来，存在多个解释，不能自动写成吸引失败。

**理由：**材料虽倾向从互动表现分析，但行程、偏好和其他未知因素不能被排除。

**条件：**限背景解释，不补写对方心理。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-025-K003`、`mikey-youtube-live-024-K001`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K003` → `mikey-youtube-live-025-E0002-R031` / `S00199`；`mikey-youtube-live-024-K001` → `mikey-youtube-live-024-E0001-R037` / `S00037`。

</details>
### P17 · 面对拒绝可以保留自我评价，但必须结束对方已经拒绝的推进。

**理由：**自我复盘与继续纠缠是不同动作；后续练习是新的自愿互动。

**条件：**停止规则属于编辑使用边界；不隐去原稿的相反做法。

**归属层：**mikey_view_as_summarized_plus_separate_editorial_stop_rule

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-023-K011`、`mikey-youtube-live-024-K015`、`mikey-youtube-live-027-K007`、`mikey-youtube-live-030-K002`

**限制或相反知识：**`mikey-youtube-live-023-K024`、`mikey-youtube-live-024-K016`

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K011` → `mikey-youtube-live-023-E0002-R133` / `S00320`；`mikey-youtube-live-024-K015` → `mikey-youtube-live-024-E0011-R040` / `S01830`；`mikey-youtube-live-027-K007` → `mikey-youtube-live-027-E0008-R012` / `S00752`；`mikey-youtube-live-030-K002` → `mikey-youtube-live-030-E0001-R152` / `S00152`；`mikey-youtube-live-023-K024` → `mikey-youtube-live-023-E0014-R013` / `S01857`；`mikey-youtube-live-024-K016` → `mikey-youtube-live-024-E0010-R029` / `S01694`。

</details>
### P18 · 设边界的可保留部分是自己的选择和退出，不是辱骂、惩罚或控制。

**理由：**被放鸽子、冒犯、已有伴侣和离开后反刍是不同场景，不能套用同一句强硬话术。

**条件：**明确拒绝、已有关系和权力问题先单独判断。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K009`、`mikey-youtube-live-023-K012`、`mikey-youtube-live-023-K019`、`mikey-youtube-live-028-K005`、`mikey-youtube-live-028-K011`、`mikey-youtube-live-030-K009`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K009` → `mikey-youtube-live-021-E0005-R075` / `S00456`；`mikey-youtube-live-023-K012` → `mikey-youtube-live-023-E0005-R113` / `S00752`；`mikey-youtube-live-023-K019` → `mikey-youtube-live-023-E0010-R001` / `S01389`；`mikey-youtube-live-028-K005` → `mikey-youtube-live-028-E0008-R061` / `S00841`；`mikey-youtube-live-028-K011` → `mikey-youtube-live-028-E0014-R019` / `S01483`；`mikey-youtube-live-030-K009` → `mikey-youtube-live-030-E0005-R078` / `S00523`。

</details>
### P19 · 自愿消费与互惠不能作为换取亲密的债权。

**理由：**金钱互惠、不必机械AA和昂贵安排涉及不同预算与关系情境，不能导出谁花钱谁有权推进。

**条件：**安全限制为编辑规则；不生成性交易交换脚本。

**归属层：**contextual_view_with_editorial_non_exchange_rule

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-023-K015`、`mikey-youtube-live-024-K013`、`mikey-youtube-live-029-K002`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K015` → `mikey-youtube-live-023-E0006-R107` / `S00955`；`mikey-youtube-live-024-K013` → `mikey-youtube-live-024-E0008-R067` / `S01423`；`mikey-youtube-live-029-K002` → `mikey-youtube-live-029-E0001-R045` / `S00045`。

</details>
### P20 · 真实意图与行动承诺应分开核对，含糊不等于获得默认许可。

**理由：**讨好背后的隐性期待、空头承诺和关系定义构成同一组候选问题，但一方不能替另一方约定规则。

**条件：**不替任何一方猜测未表达的接受。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-025-K014`、`mikey-youtube-live-029-K006`、`mikey-youtube-live-029-K007`、`mikey-youtube-live-030-K001`、`mikey-youtube-live-030-K010`

**限制或相反知识：**`mikey-youtube-live-026-K008`、`mikey-youtube-live-028-K012`

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K014` → `mikey-youtube-live-025-E0011-R007` / `S01205`；`mikey-youtube-live-029-K006` → `mikey-youtube-live-029-E0003-R064` / `S00386`；`mikey-youtube-live-029-K007` → `mikey-youtube-live-029-E0004-R142` / `S00562`；`mikey-youtube-live-030-K001` → `mikey-youtube-live-030-E0001-R060` / `S00060`；`mikey-youtube-live-030-K010` → `mikey-youtube-live-030-E0001-R107` / `S00107`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`。

</details>
### P21 · 真实兴趣和生活信息可以成为交流材料，但不能被编成身份包装。

**理由：**朋友圈、个性样本和兴趣活动的共同点在于能与日常生活对应，而非伪造展示面。

**条件：**共同兴趣或到家活动不代表其他许可。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-029-K008`、`mikey-youtube-live-025-K007`、`mikey-youtube-live-027-K006`、`mikey-youtube-live-027-K010`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K008` → `mikey-youtube-live-029-E0005-R122` / `S00722`；`mikey-youtube-live-025-K007` → `mikey-youtube-live-025-E0004-R015` / `S00490`；`mikey-youtube-live-027-K006` → `mikey-youtube-live-027-E0005-R028` / `S00448`；`mikey-youtube-live-027-K010` → `mikey-youtube-live-027-E0012-R043` / `S01173`。

</details>
### P22 · 网络样本、批评者动机和群体标签不能被当作已核社会事实。

**理由：**避免整体否定与贬损概括并存；应当保留立场冲突，而非选一边替人物补成统一理论。

**条件：**不输出群体本质论。

**归属层：**editorial_limit_on_reported_views

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K014`、`mikey-youtube-live-021-K016`、`mikey-youtube-live-023-K020`、`mikey-youtube-live-024-K014`

**限制或相反知识：**`mikey-youtube-live-025-K016`、`mikey-youtube-live-029-K012`、`mikey-youtube-live-030-K014`

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K014` → `mikey-youtube-live-021-E0009-R064` / `S00945`；`mikey-youtube-live-021-K016` → `mikey-youtube-live-021-E0010-R071` / `S01031`；`mikey-youtube-live-023-K020` → `mikey-youtube-live-023-E0010-R020` / `S01408`；`mikey-youtube-live-024-K014` → `mikey-youtube-live-024-E0008-R089` / `S01445`；`mikey-youtube-live-025-K016` → `mikey-youtube-live-025-E0003-R005` / `S00363`；`mikey-youtube-live-029-K012` → `mikey-youtube-live-029-E0001-R030` / `S00030`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### P23 · 直播70只能支持“本期多人材料讨论了这些维度”，不能支持Mikey独立主张。

**理由：**2014 SID全部uncertain_overlap；角色、嘉宾、观众和主持朗读没有句级分离。

**条件：**其他四类计数为0；不是已有可用mikey_commentary而遗漏提取。

**归属层：**editorial_attribution_audit

**支持依赖闸门：**do_not_generalize

**支持知识：**`mikey-youtube-live-022-K001`、`mikey-youtube-live-022-K002`、`mikey-youtube-live-022-K003`、`mikey-youtube-live-022-K004`、`mikey-youtube-live-022-K005`、`mikey-youtube-live-022-K006`、`mikey-youtube-live-022-K007`、`mikey-youtube-live-022-K008`、`mikey-youtube-live-022-K009`、`mikey-youtube-live-022-K010`、`mikey-youtube-live-022-K011`、`mikey-youtube-live-022-K012`、`mikey-youtube-live-022-K013`、`mikey-youtube-live-022-K014`、`mikey-youtube-live-022-K015`、`mikey-youtube-live-022-K016`、`mikey-youtube-live-022-K017`、`mikey-youtube-live-022-K018`

**限制或相反知识：**无

**编辑说明：**此命题是归属审计结论；所列知识是被审对象，不是对其内容的赞同。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### P24 · 直播82电话材料的说话人、公开授权和结果必须逐事件独立核对。

**理由：**接通、继续交谈、拒绝和事后结果不是同一证据层；集合caller占位不证明同人。

**条件：**全部非DNG条目受全期视觉阻断，不作示范话术。

**归属层：**editorial_attribution_and_privacy_audit

**支持依赖闸门：**do_not_generalize

**支持知识：**`mikey-youtube-live-029-K009`、`mikey-youtube-live-029-K010`、`mikey-youtube-live-029-K011`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`。

</details>
### P25 · 拒绝、未反抗、醉酒和前一步接受不能被改写成下一步同意。

**理由：**相应高风险事件跨期出现，但不可作为方法序列；编辑明确阻止同意层级跳跃。

**条件：**这是编辑规则，不冒充人物始终表达或遵守的立场。

**归属层：**editorial_safety_rule_not_mikey_quote

**支持依赖闸门：**do_not_generalize

**支持知识：**`mikey-youtube-live-021-K015`、`mikey-youtube-live-023-K025`、`mikey-youtube-live-024-K011`、`mikey-youtube-live-025-K015`、`mikey-youtube-live-026-K007`、`mikey-youtube-live-028-K012`、`mikey-youtube-live-029-K010`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-030-K009`、`mikey-youtube-live-030-K013`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-023-K025` → `mikey-youtube-live-023-E0006-R006` / `S00854`；`mikey-youtube-live-024-K011` → `mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-030-K009` → `mikey-youtube-live-030-E0005-R078` / `S00523`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### P26 · 被拉黑后的换渠道联系、私密材料展示和录音拍摄都不能被默认为已获授权。

**理由：**联系许可、录制许可与公开许可必须分开；此包没有替代缺失授权的材料。

**条件：**不提供规避拉黑或秘密记录的方法。

**归属层：**editorial_privacy_rule_not_legal_opinion

**支持依赖闸门：**do_not_generalize

**支持知识：**`mikey-youtube-live-023-K024`、`mikey-youtube-live-024-K016`、`mikey-youtube-live-027-K002`、`mikey-youtube-live-029-K009`、`mikey-youtube-live-028-K012`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K024` → `mikey-youtube-live-023-E0014-R013` / `S01857`；`mikey-youtube-live-024-K016` → `mikey-youtube-live-024-E0010-R029` / `S01694`；`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`。

</details>
### P27 · 未成年人、师生与已有关系的边界不能被普通邀约方法覆盖。

**理由：**校园或外校不是解除年龄与权力问题的理由；逐期收窄不等于人物原句就已充分。

**条件：**不从标题、角色外形或校园场景推定成年。

**归属层：**editorial_applicability_boundary

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-023-K019`、`mikey-youtube-live-023-K022`、`mikey-youtube-live-025-K001`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K019` → `mikey-youtube-live-023-E0010-R001` / `S01389`；`mikey-youtube-live-023-K022` → `mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-025-K001` → `mikey-youtube-live-025-E0001-R081` / `S00081`。

</details>
### P28 · 健康与创伤相关片段只能保存观点和风险定位，不能生成诊断或安全保证。

**理由：**原稿、逐期编辑纠正和专业事实尚未闭环；没有独立核验药物、疾病、遗传或治疗效果。

**条件：**不提供医疗概率、疗程、药物或替代治疗建议。

**归属层：**editorial_medical_and_mental_health_boundary

**支持依赖闸门：**do_not_generalize

**支持知识：**`mikey-youtube-live-021-K012`、`mikey-youtube-live-021-K019`、`mikey-youtube-live-024-K005`、`mikey-youtube-live-024-K012`、`mikey-youtube-live-026-K006`、`mikey-youtube-live-026-K007`、`mikey-youtube-live-028-K009`、`mikey-youtube-live-028-K010`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K012` → `mikey-youtube-live-021-E0006-R083` / `S00580`；`mikey-youtube-live-021-K019` → `mikey-youtube-live-021-E0012-R016` / `S01180`；`mikey-youtube-live-024-K005` → `mikey-youtube-live-024-E0003-R152` / `S00563`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-026-K006` → `mikey-youtube-live-026-E0007-R084` / `S00714`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`；`mikey-youtube-live-028-K009` → `mikey-youtube-live-028-E0013-R031` / `S01413`；`mikey-youtube-live-028-K010` → `mikey-youtube-live-028-E0013-R045` / `S01427`。

</details>
### P29 · 成功率、次数、收入与成长结果必须保留统计口径和讲述者限制。

**理由：**没有分母、比较条件和独立结果，不能把自述、课程要求或观众故事转成普遍预测。

**条件：**不将整期unique折算为独立成功样本。

**归属层：**editorial_evidence_quality_boundary

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K004`、`mikey-youtube-live-021-K010`、`mikey-youtube-live-025-K005`、`mikey-youtube-live-026-K002`、`mikey-youtube-live-028-K003`、`mikey-youtube-live-029-K005`、`mikey-youtube-live-030-K012`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-021-K010` → `mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-025-K005` → `mikey-youtube-live-025-E0002-R108` / `S00276`；`mikey-youtube-live-026-K002` → `mikey-youtube-live-026-E0004-R082` / `S00412`；`mikey-youtube-live-028-K003` → `mikey-youtube-live-028-E0005-R049` / `S00499`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-030-K012` → `mikey-youtube-live-030-E0013-R024` / `S01318`。

</details>
### P30 · NPC隐喻最多只能被研究为减轻评价压力的表达，不能用来否认他人主体。

**理由：**同一隐喻在不同事件中可能从心理距离转为去人化；必须保留差异。

**条件：**限制性改写是编辑行为，不是替原话追认善意。

**归属层：**editorial_interpretation_boundary

**支持依赖闸门：**do_not_generalize

**支持知识：**`mikey-youtube-live-023-K008`、`mikey-youtube-live-028-K007`、`mikey-youtube-live-028-K008`、`mikey-youtube-live-030-K005`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K008` → `mikey-youtube-live-023-E0003-R060` / `S00388`；`mikey-youtube-live-028-K007` → `mikey-youtube-live-028-E0010-R128` / `S01128`；`mikey-youtube-live-028-K008` → `mikey-youtube-live-028-E0011-R075` / `S01203`；`mikey-youtube-live-030-K005` → `mikey-youtube-live-030-E0002-R059` / `S00214`。

</details>
### P31 · 支配、羞辱、剥削与单方关系规则不能被吸收到主体性方法中。

**理由：**两组材料在权利归属上存在真实冲突，而非强度不同的同一技巧。

**条件：**保留争议证据，不生成相关行动路线。

**归属层：**editorial_conflict_boundary

**支持依赖闸门：**do_not_generalize

**支持知识：**`mikey-youtube-live-025-K015`、`mikey-youtube-live-026-K008`、`mikey-youtube-live-027-K012`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-030-K013`

**限制或相反知识：**`mikey-youtube-live-024-K004`

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-027-K012` → `mikey-youtube-live-027-E0007-R021` / `S00651`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`；`mikey-youtube-live-024-K004` → `mikey-youtube-live-024-E0002-R139` / `S00284`。

</details>
### P32 · 先分事实、解释和希望结果，能避免把教学例子写成已证实规律。

**理由：**直播75归因例子与直播83实事求是条目构成候选判断顺序，但后者仍受全期阻断。

**条件：**不声称这是一套经过测试的统计方法。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-024-K007`、`mikey-youtube-live-029-K004`、`mikey-youtube-live-030-K003`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-029-K004` → `mikey-youtube-live-029-E0002-R068` / `S00227`；`mikey-youtube-live-030-K003` → `mikey-youtube-live-030-E0002-R022` / `S00177`。

</details>
### P33 · 区分普通社交与暴力行为的说法不能当作对具体接触方式的法律背书。

**理由：**直播68该条已有major法律边界待核；人物观点不能替代实际行为、同意和当地法律判断。

**条件：**本次不作法律意见，不据此解除任何风险限制。

**归属层：**editorial_legal_applicability_boundary

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-021-K003`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K003` → `mikey-youtube-live-021-E0002-R099` / `S00147`。

</details>
### P34 · 前任比较在材料中被作为是否陷入竞争式自我证明的问题，而不是需要战胜第三人。

**理由：**直播82给出回到当前互动的候选方向，但该期整体仍hold，不能据零散片段形成针对具体人的心理判断。

**条件：**不贬损前任或猜测对方操纵动机。

**归属层：**mikey_view_as_summarized_in_input

**支持依赖闸门：**hold

**支持知识：**`mikey-youtube-live-029-K003`

**限制或相反知识：**无

**编辑说明：**这是按逐期概括建立的候选命题，不是新发现的逐字话语；受限支持不因重复而升级。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K003` → `mikey-youtube-live-029-E0002-R014` / `S00173`。

</details>
## 4. 方法之间的连接与停止条件

下列关系是编辑从材料中恢复的候选结构，不是新验证的操作流程。依赖hold或DNG的连接不运行。

### M01 · 描述实际发生的互动 → 区分事实与解释

**关系类型与闸门：**prerequisite / hold

**何时连接：**先确定发生的是拒绝、未回复还是无法安排。

**为什么：**不同反馈不能共享一个预设原因；事实层先于人物动机推断。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-030-K003` → `mikey-youtube-live-030-E0002-R022` / `S00177`。

</details>
### M02 · 确认拿号或回复这一环节 → 回看现场、呈现和后续互动

**关系类型与闸门：**diagnostic_expansion / hold

**何时连接：**有联系方式但后续停滞，且没有完整原因。

**为什么：**只改最后一句话可能忽略早先印象或新信息。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K005` → `mikey-youtube-live-021-E0004-R008` / `S00292`；`mikey-youtube-live-023-K006` → `mikey-youtube-live-023-E0002-R091` / `S00278`；`mikey-youtube-live-024-K001` → `mikey-youtube-live-024-E0001-R037` / `S00037`；`mikey-youtube-live-028-K006` → `mikey-youtube-live-028-E0009-R051` / `S00941`。

</details>
### M03 · 观察单向输出 → 检验是否有继续交流意愿

**关系类型与闸门：**conditional_branch / hold

**何时连接：**对方很少延展，不能直接认定是自己话术差。

**为什么：**不想继续是替代解释；短回复本身仍不足以确定。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K006` → `mikey-youtube-live-024-E0004-R027` / `S00733`；`mikey-youtube-live-023-K016` → `mikey-youtube-live-023-E0008-R024` / `S01189`；`mikey-youtube-live-025-K008` → `mikey-youtube-live-025-E0004-R046` / `S00521`。

</details>
### M04 · 出现模糊的忙或没空 → 澄清愿意见面及可行时间

**关系类型与闸门：**conditional_branch / hold

**何时连接：**对方尚未明确拒绝。

**为什么：**把猜测转为可观察安排，不无限加大聊天和追问。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K007` → `mikey-youtube-live-023-E0003-R006` / `S00334`；`mikey-youtube-live-021-K002` → `mikey-youtube-live-021-E0002-R080` / `S00128`；`mikey-youtube-live-024-K002` → `mikey-youtube-live-024-E0001-R061` / `S00061`。

</details>
### M05 · 没有明确安排或收到拒绝 → 结束该次推进

**关系类型与闸门：**stop_rule / do_not_generalize

**何时连接：**不可把不给安排转成辱骂或更大压力。

**为什么：**停止自己的投入与判断对方人格是两件事；拒绝不因自信训练而失效。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K007` → `mikey-youtube-live-023-E0003-R006` / `S00334`；`mikey-youtube-live-023-K011` → `mikey-youtube-live-023-E0002-R133` / `S00320`；`mikey-youtube-live-024-K016` → `mikey-youtube-live-024-E0010-R029` / `S01694`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`。

</details>
### M06 · 形成初步吸引的候选解释 → 检查后续是否出现表演落差

**关系类型与闸门：**maintenance_not_escalation / hold

**何时连接：**只讨论真实、自愿互动中的一致性。

**为什么：**后续保持生活与表达一致，不是不断升级表演。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-021-K006` → `mikey-youtube-live-021-E0004-R039` / `S00323`；`mikey-youtube-live-023-K005` → `mikey-youtube-live-023-E0002-R005` / `S00192`；`mikey-youtube-live-024-K008` → `mikey-youtube-live-024-E0004-R154` / `S00860`。

</details>
### M07 · 学习少量框架或话术 → 进入具体实践

**关系类型与闸门：**learning_stage / hold

**何时连接：**把工具作为临时支撑，不把收藏数量当能力。

**为什么：**理论只有与具体问题结合才可能产生反馈。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K004` → `mikey-youtube-live-023-E0001-R162` / `S00162`；`mikey-youtube-live-023-K009` → `mikey-youtube-live-023-E0004-R005` / `S00473`；`mikey-youtube-live-026-K001` → `mikey-youtube-live-026-E0004-R045` / `S00375`；`mikey-youtube-live-027-K003` → `mikey-youtube-live-027-E0002-R049` / `S00154`。

</details>
### M08 · 完成一次自愿互动 → 复盘观察与预期差异

**关系类型与闸门：**feedback_loop / hold

**何时连接：**不要求秘密录音，不把别人是否接受当成绩。

**为什么：**复盘对象是判断和自身行为，不是制造成功故事。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-027-K009` → `mikey-youtube-live-027-E0009-R043` / `S00883`；`mikey-youtube-live-030-K011` → `mikey-youtube-live-030-E0007-R052` / `S00727`；`mikey-youtube-live-030-K012` → `mikey-youtube-live-030-E0013-R024` / `S01318`。

</details>
### M09 · 发现能力或情境不足 → 调整下一步难度

**关系类型与闸门：**gradual_adjustment / hold

**何时连接：**不能从课程指标推出人人相同的次数。

**为什么：**渐进路径与固定配额、三秒百分比不是同一主张。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K018` → `mikey-youtube-live-023-E0009-R110` / `S01374`；`mikey-youtube-live-026-K002` → `mikey-youtube-live-026-E0004-R082` / `S00412`；`mikey-youtube-live-027-K011` → `mikey-youtube-live-027-E0013-R011` / `S01211`；`mikey-youtube-live-028-K002` → `mikey-youtube-live-028-E0005-R071` / `S00521`；`mikey-youtube-live-028-K003` → `mikey-youtube-live-028-E0005-R049` / `S00499`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`。

</details>
### M10 · 不把对方当价值裁判 → 保留真实意图与退出选择

**关系类型与闸门：**supporting_condition / hold

**何时连接：**同样承认对方是独立的人。

**为什么：**自我价值可减少讨好，但不能成为控制他人的理由。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K011` → `mikey-youtube-live-025-E0007-R031` / `S00844`；`mikey-youtube-live-025-K012` → `mikey-youtube-live-025-E0007-R073` / `S00886`；`mikey-youtube-live-024-K004` → `mikey-youtube-live-024-E0002-R139` / `S00284`；`mikey-youtube-live-030-K001` → `mikey-youtube-live-030-E0001-R060` / `S00060`；`mikey-youtube-live-030-K006` → `mikey-youtube-live-030-E0003-R007` / `S00273`。

</details>
### M11 · 自我稳定 → 选择合适的表达方式

**关系类型与闸门：**dimension_separation / hold

**何时连接：**说话量、高低能量和内在稳定不能互相替代。

**为什么：**直接开场、间接表达与个人气质需要分条件，而非统一模板。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K007` → `mikey-youtube-live-021-E0005-R003` / `S00384`；`mikey-youtube-live-021-K011` → `mikey-youtube-live-021-E0006-R057` / `S00554`；`mikey-youtube-live-023-K010` → `mikey-youtube-live-023-E0007-R048` / `S01062`；`mikey-youtube-live-024-K003` → `mikey-youtube-live-024-E0002-R104` / `S00249`；`mikey-youtube-live-030-K007` → `mikey-youtube-live-030-E0003-R089` / `S00355`。

</details>
### M12 · 看到态度变化 → 检查新身份或生活信息

**关系类型与闸门：**alternative_explanation / hold

**何时连接：**变化恰与某句话同时发生，也不证明是那句话造成。

**为什么：**直播75假设例子解释了相关先后与因果归因的区别。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-025-K006` → `mikey-youtube-live-025-E0003-R019` / `S00377`；`mikey-youtube-live-029-K004` → `mikey-youtube-live-029-E0002-R068` / `S00227`。

</details>
### M13 · 表达关系意图 → 核对双方约定与实际行动

**关系类型与闸门：**mutual_agreement / do_not_generalize

**何时连接：**一方的规则不是双方同意。

**为什么：**隐性索取、空头承诺和双重标准不能被包装成主体性。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K014` → `mikey-youtube-live-025-E0011-R007` / `S01205`；`mikey-youtube-live-029-K006` → `mikey-youtube-live-029-E0003-R064` / `S00386`；`mikey-youtube-live-029-K007` → `mikey-youtube-live-029-E0004-R142` / `S00562`；`mikey-youtube-live-030-K001` → `mikey-youtube-live-030-E0001-R060` / `S00060`；`mikey-youtube-live-030-K010` → `mikey-youtube-live-030-E0001-R107` / `S00107`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`。

</details>
### M14 · 接受聊天或见面 → 判断下一项具体行为是否获同意

**关系类型与闸门：**non_inference_boundary / do_not_generalize

**何时连接：**前一步接受不能自动传递。

**为什么：**电话、共同兴趣、到家或未反抗都不补齐具体行为许可。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K008` → `mikey-youtube-live-029-E0005-R122` / `S00722`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-024-K011` → `mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### M15 · 获得私人聊天或通话材料 → 核对记录和公开授权

**关系类型与闸门：**privacy_prerequisite / do_not_generalize

**何时连接：**联系、记录与公开是不同权限。

**为什么：**演示价值不能覆盖参与者授权和身份未知。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`。

</details>
### M16 · 看到动漫角色或多人讨论 → 完成五类归属与句级说话人核验

**关系类型与闸门：**attribution_prerequisite / do_not_generalize

**何时连接：**uncertain_overlap不进入Mikey观点支持。

**为什么：**角色设定与主持发声都不能替代原创主张归属。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### M17 · 收到拒绝或拉黑 → 停止而不是更换接触渠道

**关系类型与闸门：**prohibition_boundary / do_not_generalize

**何时连接：**不为满足训练、报复或证明价值继续接触。

**为什么：**后续不同场景的练习不能指向同一被拒绝对象。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K024` → `mikey-youtube-live-023-E0014-R013` / `S01857`；`mikey-youtube-live-024-K016` → `mikey-youtube-live-024-E0010-R029` / `S01694`；`mikey-youtube-live-027-K007` → `mikey-youtube-live-027-E0008-R012` / `S00752`。

</details>
### M18 · 听到疾病或心理原因解释 → 转入待核与专业边界

**关系类型与闸门：**evidence_gate / do_not_generalize

**何时连接：**不从人物自述推出病因、概率、疗效或安全性。

**为什么：**自动稿错词与未核数字可能根本改变含义。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K012` → `mikey-youtube-live-021-E0006-R083` / `S00580`；`mikey-youtube-live-024-K005` → `mikey-youtube-live-024-E0003-R152` / `S00563`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-026-K006` → `mikey-youtube-live-026-E0007-R084` / `S00714`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`；`mikey-youtube-live-028-K009` → `mikey-youtube-live-028-E0013-R031` / `S01413`；`mikey-youtube-live-028-K010` → `mikey-youtube-live-028-E0013-R045` / `S01427`。

</details>
### M19 · 听到成功率或结果故事 → 区分讲述者、分母和独立结果

**关系类型与闸门：**evidence_gate / hold

**何时连接：**同类故事出现次数不等于独立样本数。

**为什么：**自述、观众、课程要求、假设例子分别登记。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-021-K010` → `mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-026-K002` → `mikey-youtube-live-026-E0004-R082` / `S00412`；`mikey-youtube-live-028-K003` → `mikey-youtube-live-028-E0005-R049` / `S00499`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-030-K012` → `mikey-youtube-live-030-E0013-R024` / `S01318`。

</details>
### M20 · 想用关系技巧解决所有问题 → 识别生活约束和选择成本

**关系类型与闸门：**scope_correction / hold

**何时连接：**教育、工作、预算与关系承诺不能被统一的吸引解释覆盖。

**为什么：**现实问题需要分解，而不是继续增加话术或课程消费。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K013` → `mikey-youtube-live-021-E0007-R037` / `S00659`；`mikey-youtube-live-023-K003` → `mikey-youtube-live-023-E0001-R134` / `S00134`；`mikey-youtube-live-023-K017` → `mikey-youtube-live-023-E0009-R023` / `S01287`；`mikey-youtube-live-023-K023` → `mikey-youtube-live-023-E0012-R036` / `S01643`；`mikey-youtube-live-025-K013` → `mikey-youtube-live-025-E0009-R076` / `S01107`；`mikey-youtube-live-026-K009` → `mikey-youtube-live-026-E0011-R101` / `S01161`。

</details>
## 5. 冲突：保留分歧，不强行统一

### C01 · 主体性与支配不是同义词

**一侧：**独立自我、真实意图与可以退出。 依据：`mikey-youtube-live-024-K004`、`mikey-youtube-live-026-K004`

**另一侧：**要求服从、不可离开、羞辱或把人作为可控制对象。 依据：`mikey-youtube-live-025-K015`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-030-K013`

**日期与语境：**直播75（2025-10-19）的独立自我，与直播77/82/83相关支配内容处于不同讨论场景；晚一期不等于已撤回前期。

**如何处理：**保持实质冲突。仅“自己不失去判断”可以作为受控候选；剥夺对方判断权不得改名放行。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K004` → `mikey-youtube-live-024-E0002-R139` / `S00284`；`mikey-youtube-live-026-K004` → `mikey-youtube-live-026-E0012-R044` / `S01224`；`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### C02 · 接受拒绝与绕过拉黑

**一侧：**拒绝不否定全部人格，可以结束后复盘。 依据：`mikey-youtube-live-023-K011`、`mikey-youtube-live-024-K015`、`mikey-youtube-live-027-K007`、`mikey-youtube-live-030-K002`

**另一侧：**换号码、渠道或其他方式在被拉黑后继续联系。 依据：`mikey-youtube-live-023-K024`、`mikey-youtube-live-024-K016`

**日期与语境：**直播72内部及直播75内部均出现不同方向，不需要以日期演进解释。

**如何处理：**保留同一期内的冲突；停止规则优先，不把绕过拉黑并入克服焦虑练习。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K011` → `mikey-youtube-live-023-E0002-R133` / `S00320`；`mikey-youtube-live-024-K015` → `mikey-youtube-live-024-E0011-R040` / `S01830`；`mikey-youtube-live-027-K007` → `mikey-youtube-live-027-E0008-R012` / `S00752`；`mikey-youtube-live-030-K002` → `mikey-youtube-live-030-E0001-R152` / `S00152`；`mikey-youtube-live-023-K024` → `mikey-youtube-live-023-E0014-R013` / `S01857`；`mikey-youtube-live-024-K016` → `mikey-youtube-live-024-E0010-R029` / `S01694`。

</details>
### C03 · 真实一致性与欺骗、隐性索取

**一侧：**日常生活、表达和承诺应能相互对应。 依据：`mikey-youtube-live-021-K001`、`mikey-youtube-live-024-K008`、`mikey-youtube-live-029-K007`、`mikey-youtube-live-030-K001`

**另一侧：**欺骗上楼、含糊承诺、以讨好交换隐性回报或单方规则。 依据：`mikey-youtube-live-026-K008`、`mikey-youtube-live-028-K012`、`mikey-youtube-live-025-K014`

**日期与语境：**直播68/75的一致性框架与直播79/81的关系、转场争议，不能靠“目的相同”合并。

**如何处理：**不能从真实性主题中删除相反材料，也不能把欺骗合理化为降低摩擦。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-024-K008` → `mikey-youtube-live-024-E0004-R154` / `S00860`；`mikey-youtube-live-029-K007` → `mikey-youtube-live-029-E0004-R142` / `S00562`；`mikey-youtube-live-030-K001` → `mikey-youtube-live-030-E0001-R060` / `S00060`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-025-K014` → `mikey-youtube-live-025-E0011-R007` / `S01205`。

</details>
### C04 · 少理论与建立框架

**一侧：**反对收藏句子、术语和理论过载。 依据：`mikey-youtube-live-023-K004`、`mikey-youtube-live-023-K009`、`mikey-youtube-live-025-K010`

**另一侧：**强调主动整理、理解框架和复盘。 依据：`mikey-youtube-live-026-K001`、`mikey-youtube-live-026-K003`、`mikey-youtube-live-027-K001`、`mikey-youtube-live-027-K003`、`mikey-youtube-live-030-K011`

**日期与语境：**直播72/77与直播79/80/83对应初学支撑、实践和反思的不同阶段。

**如何处理：**可作阶段性兼容：理论帮助开始，反馈修正理解；不得推成不必学习或只要买课。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K004` → `mikey-youtube-live-023-E0001-R162` / `S00162`；`mikey-youtube-live-023-K009` → `mikey-youtube-live-023-E0004-R005` / `S00473`；`mikey-youtube-live-025-K010` → `mikey-youtube-live-025-E0005-R037` / `S00641`；`mikey-youtube-live-026-K001` → `mikey-youtube-live-026-E0004-R045` / `S00375`；`mikey-youtube-live-026-K003` → `mikey-youtube-live-026-E0007-R093` / `S00723`；`mikey-youtube-live-027-K001` → `mikey-youtube-live-027-E0001-R016` / `S00016`；`mikey-youtube-live-027-K003` → `mikey-youtube-live-027-E0002-R049` / `S00154`；`mikey-youtube-live-030-K011` → `mikey-youtube-live-030-E0007-R052` / `S00727`。

</details>
### C05 · 稳定不等于高能量与开场方式看状态

**一侧：**稳定不等于话少、话多或一直兴奋。 依据：`mikey-youtube-live-021-K011`、`mikey-youtube-live-024-K003`

**另一侧：**不同开场可能依赖当时状态和表达方式。 依据：`mikey-youtube-live-023-K010`、`mikey-youtube-live-021-K007`

**日期与语境：**直播68、72、75分别谈内在状态和外在动作；不是同一个判断变量。

**如何处理：**保留维度差异，不得把能量当道德或吸引等级，也不凭两种说法判为反悔。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K011` → `mikey-youtube-live-021-E0006-R057` / `S00554`；`mikey-youtube-live-024-K003` → `mikey-youtube-live-024-E0002-R104` / `S00249`；`mikey-youtube-live-023-K010` → `mikey-youtube-live-023-E0007-R048` / `S01062`；`mikey-youtube-live-021-K007` → `mikey-youtube-live-021-E0005-R003` / `S00384`。

</details>
### C06 · 资源价值与自我价值感

**一侧：**主心骨、自我认可不完全依靠钱、学历和反馈。 依据：`mikey-youtube-live-025-K012`、`mikey-youtube-live-030-K006`

**另一侧：**领域能力、身份信息与呈现会改变互动感知。 依据：`mikey-youtube-live-024-K007`、`mikey-youtube-live-025-K002`、`mikey-youtube-live-025-K004`、`mikey-youtube-live-025-K006`

**日期与语境：**直播75身份假设与直播77/83价值感讨论回答的问题不同。

**如何处理：**可以区分外部信息与内部自评，但不得进一步宣称资源无用或资源决定关系。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K012` → `mikey-youtube-live-025-E0007-R073` / `S00886`；`mikey-youtube-live-030-K006` → `mikey-youtube-live-030-E0003-R007` / `S00273`；`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-025-K002` → `mikey-youtube-live-025-E0001-R094` / `S00094`；`mikey-youtube-live-025-K004` → `mikey-youtube-live-025-E0002-R059` / `S00227`；`mikey-youtube-live-025-K006` → `mikey-youtube-live-025-E0003-R019` / `S00377`。

</details>
### C07 · 基本熟悉后邀约与用吸引绕过安全或同意

**一侧：**从基本信息、意愿和可行时间判断是否见面。 依据：`mikey-youtube-live-023-K007`、`mikey-youtube-live-024-K002`、`mikey-youtube-live-024-K009`

**另一侧：**对拒绝后说服、酒精、私人转场或未反抗的有害解释。 依据：`mikey-youtube-live-021-K015`、`mikey-youtube-live-024-K011`、`mikey-youtube-live-028-K012`、`mikey-youtube-live-029-K010`、`mikey-youtube-live-030-K013`

**日期与语境：**直播68、75、81、82、83分别涉及不同事件；一次接受不能跨事件迁移。

**如何处理：**安全、隐私和具体同意独立受控；不将高风险材料解释成邀约的进阶步骤。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K007` → `mikey-youtube-live-023-E0003-R006` / `S00334`；`mikey-youtube-live-024-K002` → `mikey-youtube-live-024-E0001-R061` / `S00061`；`mikey-youtube-live-024-K009` → `mikey-youtube-live-024-E0005-R193` / `S01084`；`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-024-K011` → `mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### C08 · 自愿互惠与交换式期待

**一侧：**消费可结合预算和自愿安排，不必机械套用同一分摊规则。 依据：`mikey-youtube-live-023-K015`、`mikey-youtube-live-024-K013`、`mikey-youtube-live-029-K002`

**另一侧：**把金钱、礼物或付出当作亲密回报的隐性债权。 依据：`mikey-youtube-live-030-K001`、`mikey-youtube-live-025-K015`

**日期与语境：**直播72/75消费讨论与直播82/83讨好和昂贵约会的语境不同。

**如何处理：**互惠只描述各方愿意承担什么，不能产生性许可；不从摘要中的安全收窄推断人物始终一致。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K015` → `mikey-youtube-live-023-E0006-R107` / `S00955`；`mikey-youtube-live-024-K013` → `mikey-youtube-live-024-E0008-R067` / `S01423`；`mikey-youtube-live-029-K002` → `mikey-youtube-live-029-E0001-R045` / `S00045`；`mikey-youtube-live-030-K001` → `mikey-youtube-live-030-E0001-R060` / `S00060`；`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`。

</details>
### C09 · 不因标签否定整个人与群体贬损

**一侧：**网络样本可能失真，标签不能代替对具体人的判断。 依据：`mikey-youtube-live-021-K014`、`mikey-youtube-live-021-K016`、`mikey-youtube-live-023-K020`

**另一侧：**性别、族群、地域、职业、体型和NPC去人化概括。 依据：`mikey-youtube-live-025-K016`、`mikey-youtube-live-028-K008`、`mikey-youtube-live-029-K012`、`mikey-youtube-live-030-K014`

**日期与语境：**直播68与直播77/81/82/83均有不同内容；并非只有早期或只有后期。

**如何处理：**立场证据与社会事实分开；保留矛盾，不选取正面片段进行人物净化。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K014` → `mikey-youtube-live-021-E0009-R064` / `S00945`；`mikey-youtube-live-021-K016` → `mikey-youtube-live-021-E0010-R071` / `S01031`；`mikey-youtube-live-023-K020` → `mikey-youtube-live-023-E0010-R020` / `S01408`；`mikey-youtube-live-025-K016` → `mikey-youtube-live-025-E0003-R005` / `S00363`；`mikey-youtube-live-028-K008` → `mikey-youtube-live-028-E0011-R075` / `S01203`；`mikey-youtube-live-029-K012` → `mikey-youtube-live-029-E0001-R030` / `S00030`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### C10 · 愿意退出与辱骂或报复

**一侧：**不通过乞求维持关系，能够结束投入。 依据：`mikey-youtube-live-028-K011`、`mikey-youtube-live-024-K004`、`mikey-youtube-live-030-K009`

**另一侧：**将冒犯、放鸽子或性挫败转成羞辱、惩罚和报复。 依据：`mikey-youtube-live-021-K009`、`mikey-youtube-live-023-K012`、`mikey-youtube-live-023-K025`、`mikey-youtube-live-029-K011`

**日期与语境：**直播68放鸽子、直播72冒犯与报复、直播82电话羞辱不是同一事件。

**如何处理：**把自己的退出与攻击他人分开；后者不得以强边界的名义执行。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-028-K011` → `mikey-youtube-live-028-E0014-R019` / `S01483`；`mikey-youtube-live-024-K004` → `mikey-youtube-live-024-E0002-R139` / `S00284`；`mikey-youtube-live-030-K009` → `mikey-youtube-live-030-E0005-R078` / `S00523`；`mikey-youtube-live-021-K009` → `mikey-youtube-live-021-E0005-R075` / `S00456`；`mikey-youtube-live-023-K012` → `mikey-youtube-live-023-E0005-R113` / `S00752`；`mikey-youtube-live-023-K025` → `mikey-youtube-live-023-E0006-R006` / `S00854`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`。

</details>
### C11 · 生活经历的解释与医疗、心理因果

**一侧：**人物把成长、抗压或家庭影响放在经历中讲述。 依据：`mikey-youtube-live-028-K009`、`mikey-youtube-live-028-K010`、`mikey-youtube-live-030-K008`、`mikey-youtube-live-030-K012`

**另一侧：**疾病风险、非安全性行为、遗传或创伤的无依据确定性解释。 依据：`mikey-youtube-live-021-K012`、`mikey-youtube-live-024-K005`、`mikey-youtube-live-024-K012`、`mikey-youtube-live-026-K006`、`mikey-youtube-live-026-K007`

**日期与语境：**直播68、75、79、81、83横跨生活经验与医疗心理语境，不可跨领域搬用。

**如何处理：**经历叙述不提供诊断或安全保证；原编辑纠正也不冒充专业验证。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-028-K009` → `mikey-youtube-live-028-E0013-R031` / `S01413`；`mikey-youtube-live-028-K010` → `mikey-youtube-live-028-E0013-R045` / `S01427`；`mikey-youtube-live-030-K008` → `mikey-youtube-live-030-E0004-R020` / `S00394`；`mikey-youtube-live-030-K012` → `mikey-youtube-live-030-E0013-R024` / `S01318`；`mikey-youtube-live-021-K012` → `mikey-youtube-live-021-E0006-R083` / `S00580`；`mikey-youtube-live-024-K005` → `mikey-youtube-live-024-E0003-R152` / `S00563`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-026-K006` → `mikey-youtube-live-026-E0007-R084` / `S00714`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`。

</details>
### C12 · 渐进实践与固定数量、成功率

**一侧：**将行动分小、逐步积累经验并复盘。 依据：`mikey-youtube-live-023-K018`、`mikey-youtube-live-028-K002`、`mikey-youtube-live-029-K005`

**另一侧：**三秒、百分比、每周固定次数和高成功率可能被误当统一标准。 依据：`mikey-youtube-live-021-K004`、`mikey-youtube-live-026-K002`、`mikey-youtube-live-028-K003`

**日期与语境：**直播72渐进任务、直播79课程语境、直播81数字断言和直播82观众故事不同。

**如何处理：**次数只能按各自来源语境保留；不合成训练配额，也不根据成功故事预期结果。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K018` → `mikey-youtube-live-023-E0009-R110` / `S01374`；`mikey-youtube-live-028-K002` → `mikey-youtube-live-028-E0005-R071` / `S00521`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-026-K002` → `mikey-youtube-live-026-E0004-R082` / `S00412`；`mikey-youtube-live-028-K003` → `mikey-youtube-live-028-E0005-R049` / `S00499`。

</details>
### C13 · 动漫相似主题与人物归属

**一侧：**其他期逐期摘要把稳定、主心骨和真实性归给Mikey。 依据：`mikey-youtube-live-021-K001`、`mikey-youtube-live-024-K004`、`mikey-youtube-live-027-K006`

**另一侧：**直播70类似词语来自未分离多人和剧情材料。 依据：`mikey-youtube-live-022-K003`、`mikey-youtube-live-022-K008`、`mikey-youtube-live-022-K010`、`mikey-youtube-live-022-K015`、`mikey-youtube-live-022-K016`

**日期与语境：**2025-08-28动漫讨论与后续直播主题重合，不代表同一讲话人。

**如何处理：**不计算为人物观点的重复支持；只有真实句级核验能改变归属，不以相似措辞补证。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-024-K004` → `mikey-youtube-live-024-E0002-R139` / `S00284`；`mikey-youtube-live-027-K006` → `mikey-youtube-live-027-E0005-R028` / `S00448`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`。

</details>
## 6. 来源复用、同案复述与重播账本

上传复用账本的最终结果是**10 unique、0 reuse、0 suspected**。本次只转存并限定该结果，没有重新执行音频或视频指纹；也没有把不同来源合并或改变正式权重。

| 来源 | 原账本状态 | 原建议权重 | 本次是否实际接入 |
|---|---|---:|---|
| `mikey-youtube-live-021` | unique | 1 | 否 |
| `mikey-youtube-live-022` | unique | 1 | 否 |
| `mikey-youtube-live-023` | unique | 1 | 否 |
| `mikey-youtube-live-024` | unique | 1 | 否 |
| `mikey-youtube-live-025` | unique | 1 | 否 |
| `mikey-youtube-live-026` | unique | 1 | 否 |
| `mikey-youtube-live-027` | unique | 1 | 否 |
| `mikey-youtube-live-028` | unique | 1 | 否 |
| `mikey-youtube-live-029` | unique | 1 | 否 |
| `mikey-youtube-live-030` | unique | 1 | 否 |

账本部分早期content_precheck仍写pending，与最终unique是不同阶段信息。本文不重判那些旧候选，也不据最终unique声称所有短片段和局部故事都独立。

### DUP-LOCAL-01 · 同一现实案例的跨期复述

**状态：**unknown

**处理：**没有稳定当事人标识、完整聊天/通话序列或同案指纹；不因话题、邀约框架或结果措辞相似而合并。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-023-K001` → `mikey-youtube-live-023-E0001-R045` / `S00045`；`mikey-youtube-live-024-K001` → `mikey-youtube-live-024-E0001-R037` / `S00037`；`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-025-K003` → `mikey-youtube-live-025-E0002-R031` / `S00199`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`。

</details>
### DUP-LOCAL-02 · 动漫剧情或角色观点重复

**状态：**unknown

**处理：**角色名称和类似性格维度不构成同一现实案例；未比对逐帧剧情或台词指纹，局部重复未知。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### DUP-LOCAL-03 · 单期内部回放、硬切或重新播放

**状态：**unknown

**处理：**事件按story_order登记不等于连续观看；无切点与连续音画证据，不能确认或排除局部重播。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K001` → `mikey-youtube-live-023-E0001-R045` / `S00045`；`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-030-K011` → `mikey-youtube-live-030-E0007-R052` / `S00727`。

</details>
### DUP-LOCAL-04 · 仅主题重合

**状态：**theme_overlap_only

**处理：**一致性、主心骨、理论实践和邀约反复出现，只作主题联系；不是重复来源判据，也不是独立实证样本。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-021-K005` → `mikey-youtube-live-021-E0004-R008` / `S00292`；`mikey-youtube-live-023-K005` → `mikey-youtube-live-023-E0002-R005` / `S00192`；`mikey-youtube-live-023-K006` → `mikey-youtube-live-023-E0002-R091` / `S00278`；`mikey-youtube-live-023-K009` → `mikey-youtube-live-023-E0004-R005` / `S00473`；`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-024-K008` → `mikey-youtube-live-024-E0004-R154` / `S00860`；`mikey-youtube-live-025-K010` → `mikey-youtube-live-025-E0005-R037` / `S00641`；`mikey-youtube-live-027-K006` → `mikey-youtube-live-027-E0005-R028` / `S00448`；`mikey-youtube-live-028-K004` → `mikey-youtube-live-028-E0006-R016` / `S00576`。

</details>
## 7. 说话人、五类归属与电话边界

| 直播70归属类别 | 登记SID数 |
|---|---:|
| `mikey_commentary` | 0 |
| `game_dialogue_or_narration` | 0 |
| `viewer_chat_text` | 0 |
| `mikey_quote_or_reading` | 0 |
| `uncertain_overlap` | 2014 |

其他四类为0，不是漏掉了可用评论；本次没有任何可据该表作为Mikey本人观点的SID。

### ATTR-GAME-mikey_commentary

**运行时规则：**只有真实句级映射到Mikey本人评论的材料才可能支持其观点；还须通过release、待核和语义审查，不自动direct。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### ATTR-GAME-game_dialogue_or_narration

**运行时规则：**只作播放材料或剧情内容；不得转写成Mikey经历、建议或赞同。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### ATTR-GAME-viewer_chat_text

**运行时规则：**单独记录问题或观点；主持读出不等于背书。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### ATTR-GAME-mikey_quote_or_reading

**运行时规则：**引用/朗读只证明其读出某内容，不能自动支持本人立场。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### ATTR-GAME-uncertain_overlap

**运行时规则：**保持hold；原do_not_generalize继续DNG。多人、角色和未知声音不得静默归并。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### ATTR-RELAY

**运行时规则：**viewer-question-01是多名观众集合。spoken_by_id=mikey只说明事件级发声标记，不能把被朗读的问题、身份或经历写成Mikey本人。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K006` → `mikey-youtube-live-023-E0002-R091` / `S00278`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-030-K007` → `mikey-youtube-live-030-E0003-R089` / `S00355`。

</details>
### ATTR-PHONE

**运行时规则：**caller-01也是集合占位，unknown-voice-01未解；电话事件的call_participants_not_sentence_level_diarized优先于粗粒度spoken_by_id。逐句未知、直播告知和公开授权未核均保持hold/DNG。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`。

</details>
### ATTR-SCREEN

**运行时规则：**截图/屏幕能证明的最多是输入登记曾展示某界面；作者、真实性、顺序、身份与结果分别待核，不能从聊天文字推定现实到场或亲密。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K007` → `mikey-youtube-live-025-E0004-R015` / `S00490`；`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`。

</details>
### ATTR-UNKNOWN

**运行时规则：**面具、座位、频道主持和代称不构成声音映射。未知人物不补姓名；跨期相同占位ID不表示同一真实人。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`。

</details>
### ATTR-PLOT

**运行时规则：**目录是动漫角色排名/剧情讨论；保留任务的五类控制，不据此宣称有实际游戏操作或把超能力迁移成现实操作。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### ATTR-EDITOR

**运行时规则：**逐期claim含“不能”等编辑收窄时，保留原文和原attribution_status，但不得声称每句规范性结论都是Mikey原话或其一贯立场。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K022` → `mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-024-K011` → `mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### ATTR-REGISTRY

**运行时规则：**speaker confirmed/partially_confirmed是上传登记状态，不等于本次声纹或嘴型验证；登记URL不一致项另列追溯问题，不能据其补认证。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-023-K005` → `mikey-youtube-live-023-E0002-R005` / `S00192`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`。

</details>
### 直播70原归属跨度

| 事件ID | 起始SID | 结束SID | 数量 | 类别 |
|---|---|---|---:|---|
| `mikey-youtube-live-022-E0001` | `S00001` | `S00100` | 100 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0002` | `S00101` | `S00200` | 100 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0003` | `S00201` | `S00350` | 150 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0004` | `S00351` | `S00460` | 110 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0005` | `S00461` | `S00570` | 110 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0006` | `S00571` | `S00700` | 130 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0007` | `S00701` | `S00850` | 150 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0008` | `S00851` | `S01020` | 170 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0009` | `S01021` | `S01150` | 130 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0010` | `S01151` | `S01300` | 150 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0011` | `S01301` | `S01440` | 140 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0012` | `S01441` | `S01600` | 160 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0013` | `S01601` | `S01760` | 160 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0014` | `S01761` | `S01880` | 120 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0015` | `S01881` | `S01980` | 100 | `uncertain_overlap` |
| `mikey-youtube-live-022-E0016` | `S01981` | `S02014` | 34 | `uncertain_overlap` |

### 直播82电话事件原始定位

以下时间是原事件目录，不是本次连续听看后的切分。caller-01为集合占位，跨事件同一人未知；不得由粗spoken_by_id=mikey把全部台词归给主持。

| 事件ID | 起止秒（原值） | 原事件标题 |
|---|---|---|
| `mikey-youtube-live-029-E0007` | 4223.18–4498.77 | 首次电话连线与性话题 |
| `mikey-youtube-live-029-E0008` | 4504.02–5100.69 | 连续拨打、第二次电话与隐私性话题 |
| `mikey-youtube-live-029-E0009` | 5100.69–5714.56 | 第三次电话、直播知情、邀约与评价排序 |
| `mikey-youtube-live-029-E0010` | 5714.56–6299.48 | 继续拨号、交友软件现场操作与来电 |
| `mikey-youtube-live-029-E0011` | 6300.56–6900.68 | 长电话：室友、性经历、支配回忆与反复邀约 |
| `mikey-youtube-live-029-E0012` | 6902.22–7505.62 | 长电话续：反复性邀约、约会安排与支配回忆 |
| `mikey-youtube-live-029-E0014` | 8437.82–8994.67 | 政治观点、电话回拨与关系猜测 |

**电话限制：**事件起止只作定位。粗spoken_by_id不能压过未分离通话类别；不得推定跨拨号或回拨为同一人。

## 8. 回答模式：只交付结构，不冒充已经运行的答案

共14条回答结构，其中4条只可作有限研究提纲，10条因所需知识受限而禁用。**所有人物化路线均为NOT_AUTHORIZED；没有运行答案生成。** 研究提纲也不是Mikey逐字回答。

### A01 · 聊天总是单向

**适用问题：**为什么总要我找话题？

**状态：**RESEARCH_OUTLINE_ONLY；依赖 direct

**先给判断：**先保留“对方可能不想继续”这一分支，不急着判为不会聊天。

**解释理由：**逐期摘要将对方提问和扩展话题作为投入观察；仅一个短回复不能判断动机。

**说明条件：**缺少完整聊天时不下唯一结论。

**下一步：**询问最近互动中对方是否愿意延展；无意继续时停止强行填充。

**观察反馈：**看是否形成双向交流，而不是自己新增了多少句子。

**必需依赖：**`mikey-youtube-live-024-K006`

**不得拿来补强的hold比较项：**`mikey-youtube-live-023-K016`、`mikey-youtube-live-025-K008`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K006` → `mikey-youtube-live-024-E0004-R027` / `S00733`；`mikey-youtube-live-023-K016` → `mikey-youtube-live-023-E0008-R024` / `S01189`；`mikey-youtube-live-025-K008` → `mikey-youtube-live-025-E0004-R046` / `S00521`。

</details>
### A02 · 拿号后没有下文

**适用问题：**为什么拿到联系方式仍不回复？

**状态：**RESEARCH_OUTLINE_ONLY；依赖 direct

**先给判断：**先回看完整互动，不认定最后一句就是原因。

**解释理由：**现场状态、呈现和后续信息都可能影响印象；时间相邻不等于因果。

**说明条件：**不推测具体人的心理或人格。

**下一步：**按联系前、拿号时、后续信息三个环节描述观察，再保留多个解释。

**观察反馈：**看新信息能否排除某些解释；没有证据就保留不确定。

**必需依赖：**`mikey-youtube-live-021-K005`、`mikey-youtube-live-024-K007`

**不得拿来补强的hold比较项：**`mikey-youtube-live-023-K006`、`mikey-youtube-live-028-K006`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**`mikey-youtube-live-024-K001`

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K005` → `mikey-youtube-live-021-E0004-R008` / `S00292`；`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-023-K006` → `mikey-youtube-live-023-E0002-R091` / `S00278`；`mikey-youtube-live-028-K006` → `mikey-youtube-live-028-E0009-R051` / `S00941`；`mikey-youtube-live-024-K001` → `mikey-youtube-live-024-E0001-R037` / `S00037`。

</details>
### A03 · 对方总说忙

**适用问题：**怎么判断还要不要继续约？

**状态：**RESEARCH_OUTLINE_ONLY；依赖 direct

**先给判断：**从猜测动机转为澄清愿意见面与可行安排。

**解释理由：**愿意给出具体时间与持续模糊是不同反馈，但不给时间不等于恶意。

**说明条件：**明确拒绝时不再追问。；不涉及酒精、私密转场或施压。

**下一步：**用一次不带指控的澄清了解是否有双方都能接受的时间；没有就停止无限追问。

**观察反馈：**只观察是否出现可行安排，不用结果证明对方是哪类人。

**必需依赖：**`mikey-youtube-live-023-K007`

**不得拿来补强的hold比较项：**`mikey-youtube-live-021-K002`、`mikey-youtube-live-021-K015`、`mikey-youtube-live-021-K017`、`mikey-youtube-live-024-K002`、`mikey-youtube-live-024-K009`、`mikey-youtube-live-026-K005`、`mikey-youtube-live-028-K001`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K007` → `mikey-youtube-live-023-E0003-R006` / `S00334`；`mikey-youtube-live-021-K002` → `mikey-youtube-live-021-E0002-R080` / `S00128`；`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-021-K017` → `mikey-youtube-live-021-E0011-R022` / `S01104`；`mikey-youtube-live-024-K002` → `mikey-youtube-live-024-E0001-R061` / `S00061`；`mikey-youtube-live-024-K009` → `mikey-youtube-live-024-E0005-R193` / `S01084`；`mikey-youtube-live-026-K005` → `mikey-youtube-live-026-E0008-R033` / `S00763`；`mikey-youtube-live-028-K001` → `mikey-youtube-live-028-E0001-R061` / `S00061`。

</details>
### A04 · 学了话术仍不会表达

**适用问题：**还要继续背句子吗？

**状态：**RESEARCH_OUTLINE_ONLY；依赖 direct

**先给判断：**话术可临时支撑，但不等于表达能力。

**解释理由：**材料区分借助句子与形成真实理解；此处不引入未经核定的训练配额。

**说明条件：**不推荐本包未提供的课程、频率或效果承诺。

**下一步：**先说明卡在理解、表达还是实际互动，再把句子当工具而非最终目标。

**观察反馈：**看能否解释表达的理由和条件，不以收藏数量判断成长。

**必需依赖：**`mikey-youtube-live-023-K009`

**不得拿来补强的hold比较项：**`mikey-youtube-live-023-K004`、`mikey-youtube-live-025-K010`、`mikey-youtube-live-027-K001`、`mikey-youtube-live-027-K003`、`mikey-youtube-live-030-K011`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K009` → `mikey-youtube-live-023-E0004-R005` / `S00473`；`mikey-youtube-live-023-K004` → `mikey-youtube-live-023-E0001-R162` / `S00162`；`mikey-youtube-live-025-K010` → `mikey-youtube-live-025-E0005-R037` / `S00641`；`mikey-youtube-live-027-K001` → `mikey-youtube-live-027-E0001-R016` / `S00016`；`mikey-youtube-live-027-K003` → `mikey-youtube-live-027-E0002-R049` / `S00154`；`mikey-youtube-live-030-K011` → `mikey-youtube-live-030-E0007-R052` / `S00727`。

</details>
### A05 · 短期不错，熟悉后失去吸引

**适用问题：**为什么开始能吸引，后来不行？

**状态：**DISABLED_PENDING_REVIEW；依赖 hold

**先给判断：**候选方向是检查表演和真实生活的落差。

**解释理由：**多期摘要强调一致性，但完整机制和部分归属仍有待核。

**说明条件：**仅候选结构，当前不运行。

**下一步：**未来核清后才能比较最初线索、后续生活与受压反应；不凭目前片段开出训练方案。

**观察反馈：**是否存在具体落差，而非把任何冷淡都归因于人格。

**必需依赖：**`mikey-youtube-live-021-K001`、`mikey-youtube-live-024-K008`

**不得拿来补强的hold比较项：**`mikey-youtube-live-027-K006`、`mikey-youtube-live-027-K010`、`mikey-youtube-live-028-K004`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**`mikey-youtube-live-023-K005`

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-024-K008` → `mikey-youtube-live-024-E0004-R154` / `S00860`；`mikey-youtube-live-023-K005` → `mikey-youtube-live-023-E0002-R005` / `S00192`；`mikey-youtube-live-027-K006` → `mikey-youtube-live-027-E0005-R028` / `S00448`；`mikey-youtube-live-027-K010` → `mikey-youtube-live-027-E0012-R043` / `S01173`；`mikey-youtube-live-028-K004` → `mikey-youtube-live-028-E0006-R016` / `S00576`。

</details>
### A06 · 拒绝后强烈自我否定

**适用问题：**是不是我整个人没有价值？

**状态：**DISABLED_PENDING_REVIEW；依赖 hold

**先给判断：**候选区分是这次互动没有成立与整体人格不同。

**解释理由：**裁判心态和自我价值是材料解释，不是临床诊断。

**说明条件：**当前完整支撑仍hold。

**下一步：**核清后可据具体反馈复盘；任何时候都不绕过拒绝或拉黑。

**观察反馈：**是否能接受结束，而不是靠纠缠或贬低别人恢复自尊。

**必需依赖：**`mikey-youtube-live-025-K011`、`mikey-youtube-live-030-K002`

**不得拿来补强的hold比较项：**`mikey-youtube-live-023-K002`、`mikey-youtube-live-023-K011`、`mikey-youtube-live-024-K015`、`mikey-youtube-live-027-K007`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K011` → `mikey-youtube-live-025-E0007-R031` / `S00844`；`mikey-youtube-live-030-K002` → `mikey-youtube-live-030-E0001-R152` / `S00152`；`mikey-youtube-live-023-K002` → `mikey-youtube-live-023-E0001-R068` / `S00068`；`mikey-youtube-live-023-K011` → `mikey-youtube-live-023-E0002-R133` / `S00320`；`mikey-youtube-live-024-K015` → `mikey-youtube-live-024-E0011-R040` / `S01830`；`mikey-youtube-live-027-K007` → `mikey-youtube-live-027-E0008-R012` / `S00752`。

</details>
### A07 · 安静是否等于没魅力

**适用问题：**必须外向或高能量吗？

**状态：**DISABLED_PENDING_REVIEW；依赖 hold

**先给判断：**候选回答区分能量、说话量与稳定状态。

**解释理由：**不同表达方式不应被压缩为统一姿态；代表片段尚不足以放行完整模型。

**说明条件：**当前不运行，不增加风格或外貌标准。

**下一步：**核验后再把表达选择与真实气质、具体情境对应。

**观察反馈：**对方是否理解以及互动是否自愿，而不是看表演强度。

**必需依赖：**`mikey-youtube-live-021-K011`、`mikey-youtube-live-024-K003`

**不得拿来补强的hold比较项：**`mikey-youtube-live-021-K007`、`mikey-youtube-live-021-K008`、`mikey-youtube-live-023-K010`、`mikey-youtube-live-030-K007`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K011` → `mikey-youtube-live-021-E0006-R057` / `S00554`；`mikey-youtube-live-024-K003` → `mikey-youtube-live-024-E0002-R104` / `S00249`；`mikey-youtube-live-021-K007` → `mikey-youtube-live-021-E0005-R003` / `S00384`；`mikey-youtube-live-021-K008` → `mikey-youtube-live-021-E0005-R012` / `S00393`；`mikey-youtube-live-023-K010` → `mikey-youtube-live-023-E0007-R048` / `S01062`；`mikey-youtube-live-030-K007` → `mikey-youtube-live-030-E0003-R089` / `S00355`。

</details>
### A08 · 已有关系或边界冲突

**适用问题：**对方有伴侣、越界或反复失约怎么办？

**状态：**DISABLED_PENDING_REVIEW；依赖 hold

**先给判断：**先分清关系事实、具体越界与自己的退出选择。

**解释理由：**这些场景不能共享辱骂、支配或惩罚话术。

**说明条件：**相关条目待核，不能直接套用。

**下一步：**核清事实后只讨论自己的选择；不把改变对方行为作为默认权利。

**观察反馈：**是否尊重对方拒绝，同时不放弃自己的明确边界。

**必需依赖：**`mikey-youtube-live-023-K019`、`mikey-youtube-live-028-K005`

**不得拿来补强的hold比较项：**`mikey-youtube-live-021-K009`、`mikey-youtube-live-023-K012`、`mikey-youtube-live-028-K011`、`mikey-youtube-live-030-K009`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K019` → `mikey-youtube-live-023-E0010-R001` / `S01389`；`mikey-youtube-live-028-K005` → `mikey-youtube-live-028-E0008-R061` / `S00841`；`mikey-youtube-live-021-K009` → `mikey-youtube-live-021-E0005-R075` / `S00456`；`mikey-youtube-live-023-K012` → `mikey-youtube-live-023-E0005-R113` / `S00752`；`mikey-youtube-live-028-K011` → `mikey-youtube-live-028-E0014-R019` / `S01483`；`mikey-youtube-live-030-K009` → `mikey-youtube-live-030-E0005-R078` / `S00523`。

</details>
### A09 · 第一次安排很贵

**适用问题：**怎样理解昂贵约会要求？

**状态：**DISABLED_PENDING_REVIEW；依赖 hold

**先给判断：**预算与安排先于给对方贴动机标签。

**解释理由：**昂贵选择不能单独证明逐利；付费也不能换取关系或亲密权利。

**说明条件：**直播82全期阻断未解除。

**下一步：**当前仅保存问题结构，核清后可讨论是否有双方自愿的替代安排。

**观察反馈：**是否能形成可接受安排，而不是如何逼对方证明诚意。

**必需依赖：**`mikey-youtube-live-029-K002`

**不得拿来补强的hold比较项：**`mikey-youtube-live-023-K015`、`mikey-youtube-live-024-K013`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K002` → `mikey-youtube-live-029-E0001-R045` / `S00045`；`mikey-youtube-live-023-K015` → `mikey-youtube-live-023-E0006-R107` / `S00955`；`mikey-youtube-live-024-K013` → `mikey-youtube-live-024-E0008-R067` / `S01423`。

</details>
### A10 · 学习、工作和课程取舍

**适用问题：**是不是应该为提升吸引改变学业或花更多钱？

**状态：**DISABLED_PENDING_REVIEW；依赖 hold

**先给判断：**先拆现实问题与可承担的成本。

**解释理由：**生活选择不能用人物求职或成长自述保证回报。

**说明条件：**教育、财务情境需要独立事实；相关知识仍受待核限制。

**下一步：**当前不输出退学、负债或购买路线；仅登记需要比较的约束与替代路径。

**观察反馈：**现实问题是否具体化，而非情绪激励是否足够强。

**必需依赖：**`mikey-youtube-live-021-K013`、`mikey-youtube-live-025-K013`

**不得拿来补强的hold比较项：**`mikey-youtube-live-021-K010`、`mikey-youtube-live-023-K003`、`mikey-youtube-live-023-K017`、`mikey-youtube-live-023-K023`、`mikey-youtube-live-026-K009`

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K013` → `mikey-youtube-live-021-E0007-R037` / `S00659`；`mikey-youtube-live-025-K013` → `mikey-youtube-live-025-E0009-R076` / `S01107`；`mikey-youtube-live-021-K010` → `mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-023-K003` → `mikey-youtube-live-023-E0001-R134` / `S00134`；`mikey-youtube-live-023-K017` → `mikey-youtube-live-023-E0009-R023` / `S01287`；`mikey-youtube-live-023-K023` → `mikey-youtube-live-023-E0012-R036` / `S01643`；`mikey-youtube-live-026-K009` → `mikey-youtube-live-026-E0011-R101` / `S01161`。

</details>
### A11 · 从动漫角色学方法

**适用问题：**直播70的角色排名能否说明Mikey的方法？

**状态：**DISABLED_PENDING_REVIEW；依赖 do_not_generalize

**先给判断：**不能把未分离多人和剧情内容作为他的独立建议。

**解释理由：**2014 SID全部uncertain_overlap，没有可用mikey_commentary。

**说明条件：**不运行人物化回答。

**下一步：**只呈现归属缺口与候选讨论维度；等待逐句核验，不照搬控制或超能力剧情。

**观察反馈：**核验能否实际改变分类，不能以其他期同主题补证。

**必需依赖：**`mikey-youtube-live-022-K001`、`mikey-youtube-live-022-K002`、`mikey-youtube-live-022-K003`、`mikey-youtube-live-022-K004`、`mikey-youtube-live-022-K005`、`mikey-youtube-live-022-K006`、`mikey-youtube-live-022-K007`、`mikey-youtube-live-022-K008`、`mikey-youtube-live-022-K009`、`mikey-youtube-live-022-K010`、`mikey-youtube-live-022-K011`、`mikey-youtube-live-022-K012`、`mikey-youtube-live-022-K013`、`mikey-youtube-live-022-K014`、`mikey-youtube-live-022-K015`、`mikey-youtube-live-022-K016`、`mikey-youtube-live-022-K017`、`mikey-youtube-live-022-K018`

**不得拿来补强的hold比较项：**无

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**仅归属与安全解释；不提供操纵或羞辱方法。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### A12 · 模仿直播电话演示

**适用问题：**能否照着直播82的电话推进？

**状态：**DISABLED_PENDING_REVIEW；依赖 do_not_generalize

**先给判断：**当前不能作为示范路线。

**解释理由：**说话人、授权、拒绝和结果链没有核清，且全期视觉阻断开放。

**说明条件：**不生成施压、羞辱或绕过拒绝的台词。

**下一步：**保留逐事件待核清单；拒绝和想休息不被改写为待突破的障碍。

**观察反馈：**只看缺失的归属和授权是否补齐，不拿持续通话当同意。

**必需依赖：**`mikey-youtube-live-029-K009`、`mikey-youtube-live-029-K010`、`mikey-youtube-live-029-K011`

**不得拿来补强的hold比较项：**无

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`。

</details>
### A13 · 健康与原生家庭解释

**适用问题：**这些观点能指导皮肤、性健康或心理问题吗？

**状态：**DISABLED_PENDING_REVIEW；依赖 do_not_generalize

**先给判断：**本包只能保留人物观点与待核，不能给诊断或安全保证。

**解释理由：**自动稿、编辑收窄和专业结论不是同一层。

**说明条件：**不运行医疗或心理治疗型答案。

**下一步：**把相应问题转到证据和专业核验，不增加药物、概率或治疗步骤。

**观察反馈：**所需专业事实是否得到核实；个人经历不替代证据。

**必需依赖：**`mikey-youtube-live-021-K012`、`mikey-youtube-live-024-K005`、`mikey-youtube-live-024-K012`、`mikey-youtube-live-026-K006`、`mikey-youtube-live-026-K007`、`mikey-youtube-live-028-K009`、`mikey-youtube-live-028-K010`

**不得拿来补强的hold比较项：**无

**仅作冲突定位的DNG比较项：**无

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K012` → `mikey-youtube-live-021-E0006-R083` / `S00580`；`mikey-youtube-live-024-K005` → `mikey-youtube-live-024-E0003-R152` / `S00563`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-026-K006` → `mikey-youtube-live-026-E0007-R084` / `S00714`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`；`mikey-youtube-live-028-K009` → `mikey-youtube-live-028-E0013-R031` / `S01413`；`mikey-youtube-live-028-K010` → `mikey-youtube-live-028-E0013-R045` / `S01427`。

</details>
### A14 · 礼貌、讨好与承诺

**适用问题：**真实表达与隐性索取怎么区分？

**状态：**DISABLED_PENDING_REVIEW；依赖 hold

**先给判断：**候选关注表面顺从背后的期待及行动是否符合承诺。

**解释理由：**不能把不承诺、含糊或单方规则解释为真实。

**说明条件：**直播82/83相关条目均未放行。

**下一步：**只保存判断问题：自己明确说了什么、对方实际接受什么、行为是否一致。

**观察反馈：**双方是否仍能自由拒绝，不用对方服从来证明真实性。

**必需依赖：**`mikey-youtube-live-029-K007`、`mikey-youtube-live-030-K001`

**不得拿来补强的hold比较项：**`mikey-youtube-live-025-K014`、`mikey-youtube-live-029-K006`、`mikey-youtube-live-030-K010`

**仅作冲突定位的DNG比较项：**`mikey-youtube-live-026-K008`

**额外direct比较项（不解除本模式的其他阻断）：**无

**仅背景项：**无

**边界：**不复制粗口，不编造经历，不把编辑安全收窄冒充人物原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K007` → `mikey-youtube-live-029-E0004-R142` / `S00562`；`mikey-youtube-live-030-K001` → `mikey-youtube-live-030-E0001-R060` / `S00060`；`mikey-youtube-live-025-K014` → `mikey-youtube-live-025-E0011-R007` / `S01205`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-029-K006` → `mikey-youtube-live-029-E0003-R064` / `S00386`；`mikey-youtube-live-030-K010` → `mikey-youtube-live-030-E0001-R107` / `S00107`。

</details>
## 9. 不可泛化账本

以下是20类编辑使用边界，不代表所有涉及知识都被新增标为DNG；原22条DNG原样保留，其余按各自hold/context/direct范围受控。对有害观点的限制不能反过来冒充Mikey说过的纠正。

### DG01 · 性别概括

**规则：**不能把女性、男性或某类关系对象描述成固定本质；记录为人物立场或争议，不作为事实和选人规则。

**原DNG知识：**`mikey-youtube-live-023-K025`、`mikey-youtube-live-025-K016`、`mikey-youtube-live-029-K012`、`mikey-youtube-live-030-K014`

**关联待核：**`mikey-youtube-live-021-R008`、`mikey-youtube-live-023-R003`、`mikey-youtube-live-023-R004`、`mikey-youtube-live-023-R005`、`mikey-youtube-live-023-R006`、`mikey-youtube-live-023-R007`、`mikey-youtube-live-023-R008`、`mikey-youtube-live-025-R003`、`mikey-youtube-live-025-R008`、`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K016` → `mikey-youtube-live-021-E0010-R071` / `S01031`；`mikey-youtube-live-023-K025` → `mikey-youtube-live-023-E0006-R006` / `S00854`；`mikey-youtube-live-025-K016` → `mikey-youtube-live-025-E0003-R005` / `S00363`；`mikey-youtube-live-029-K012` → `mikey-youtube-live-029-E0001-R030` / `S00030`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### DG02 · 地域与职业标签

**规则：**地域、职业、平台样本和个体故事不能推出群体行为；材料不足时不得补造具体群体属性。

**原DNG知识：**`mikey-youtube-live-022-K014`、`mikey-youtube-live-025-K016`、`mikey-youtube-live-030-K014`

**关联待核：**`mikey-youtube-live-021-R007`、`mikey-youtube-live-021-R008`、`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`、`mikey-youtube-live-025-R003`、`mikey-youtube-live-025-R008`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K014` → `mikey-youtube-live-021-E0009-R064` / `S00945`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-025-K016` → `mikey-youtube-live-025-E0003-R005` / `S00363`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### DG03 · 族群概括

**规则：**族群与关系成功或吸引优势的泛化不作真实规律；保留原来源风险及语境，不复制羞辱性表述。

**原DNG知识：**`mikey-youtube-live-030-K014`

**关联待核：**`mikey-youtube-live-021-R007`、`mikey-youtube-live-021-R008`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K014` → `mikey-youtube-live-021-E0009-R064` / `S00945`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### DG04 · 外貌与体型

**规则：**风格讨论不扩展为体型羞辱、固定吸引等级或对外貌的群体推断。

**原DNG知识：**`mikey-youtube-live-029-K012`、`mikey-youtube-live-030-K014`

**关联待核：**`mikey-youtube-live-021-R004`、`mikey-youtube-live-021-R009`、`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K008` → `mikey-youtube-live-021-E0005-R012` / `S00393`；`mikey-youtube-live-021-K019` → `mikey-youtube-live-021-E0012-R016` / `S01180`；`mikey-youtube-live-029-K012` → `mikey-youtube-live-029-E0001-R030` / `S00030`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### DG05 · 年龄与外形成熟

**规则：**年龄、外形与场景不证明成年或健康状态；不编造年龄阈值、衰退曲线或成长效果。

**原DNG知识：**无

**关联待核：**`mikey-youtube-live-021-R009`、`mikey-youtube-live-023-R010`、`mikey-youtube-live-023-R011`、`mikey-youtube-live-025-R001`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K019` → `mikey-youtube-live-021-E0012-R016` / `S01180`；`mikey-youtube-live-023-K022` → `mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-025-K001` → `mikey-youtube-live-025-E0001-R081` / `S00081`。

</details>
### DG06 · 未成年人、校园与职业权力

**规则：**外校、不是自己学生或校园场景都不能解除未成年及权力边界；普通搭讪方法不得向未成年人或受权力影响者迁移。

**原DNG知识：**无

**关联待核：**`mikey-youtube-live-023-R008`、`mikey-youtube-live-023-R009`、`mikey-youtube-live-023-R010`、`mikey-youtube-live-023-R011`、`mikey-youtube-live-025-R001`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K019` → `mikey-youtube-live-023-E0010-R001` / `S01389`；`mikey-youtube-live-023-K022` → `mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-025-K001` → `mikey-youtube-live-025-E0001-R081` / `S00081`。

</details>
### DG07 · 拒绝、撤回与持续同意

**规则：**不能把未反抗、醉酒、继续交谈、同意见面或留下解释成下一项行为同意；停止和撤回单独生效。

**原DNG知识：**`mikey-youtube-live-023-K025`、`mikey-youtube-live-024-K011`、`mikey-youtube-live-025-K015`、`mikey-youtube-live-026-K007`、`mikey-youtube-live-028-K012`、`mikey-youtube-live-029-K010`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-030-K013`

**关联待核：**`mikey-youtube-live-021-R008`、`mikey-youtube-live-023-R003`、`mikey-youtube-live-023-R004`、`mikey-youtube-live-023-R005`、`mikey-youtube-live-023-R006`、`mikey-youtube-live-023-R007`、`mikey-youtube-live-023-R008`、`mikey-youtube-live-024-R002`、`mikey-youtube-live-024-R003`、`mikey-youtube-live-025-R003`、`mikey-youtube-live-025-R005`、`mikey-youtube-live-025-R006`、`mikey-youtube-live-025-R008`、`mikey-youtube-live-026-R002`、`mikey-youtube-live-026-R004`、`mikey-youtube-live-028-R002`、`mikey-youtube-live-028-R004`、`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R002`、`mikey-youtube-live-030-R003`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-023-K025` → `mikey-youtube-live-023-E0006-R006` / `S00854`；`mikey-youtube-live-024-K011` → `mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-030-K009` → `mikey-youtube-live-030-E0005-R078` / `S00523`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### DG08 · 私密聊天与电话隐私

**规则：**能看到或听到不代表同意记录、公开或用于教学；身份、真实性、公开授权和说话人各自待核。

**原DNG知识：**`mikey-youtube-live-029-K010`

**关联待核：**`mikey-youtube-live-025-R004`、`mikey-youtube-live-027-R002`、`mikey-youtube-live-027-R003`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K007` → `mikey-youtube-live-025-E0004-R015` / `S00490`；`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`。

</details>
### DG09 · 偷拍、录音与公开演示

**规则：**不提供秘密记录、规避授权或公开私密材料的方法；练习复盘并不自动授权录音拍摄。

**原DNG知识：**`mikey-youtube-live-028-K012`

**关联待核：**`mikey-youtube-live-027-R002`、`mikey-youtube-live-027-R003`、`mikey-youtube-live-028-R002`、`mikey-youtube-live-028-R004`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`。

</details>
### DG10 · 医疗与性健康

**规则：**疾病风险、药物效果、避孕和非安全性行为片段不得作为健康建议；没有专业核验就不提供概率、保证或疗程。

**原DNG知识：**`mikey-youtube-live-024-K012`、`mikey-youtube-live-026-K006`、`mikey-youtube-live-026-K007`

**关联待核：**`mikey-youtube-live-021-R005`、`mikey-youtube-live-024-R002`、`mikey-youtube-live-024-R003`、`mikey-youtube-live-024-R008`、`mikey-youtube-live-026-R002`、`mikey-youtube-live-026-R003`、`mikey-youtube-live-026-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K012` → `mikey-youtube-live-021-E0006-R083` / `S00580`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-026-K006` → `mikey-youtube-live-026-E0007-R084` / `S00714`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`。

</details>
### DG11 · 心理健康与原生家庭

**规则：**缺爱、创伤、遗传、上头、催眠或内在小孩类解释不构成诊断或治疗；个人经历不证明因果。

**原DNG知识：**无

**关联待核：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`、`mikey-youtube-live-024-R001`、`mikey-youtube-live-028-R004`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-024-K005` → `mikey-youtube-live-024-E0003-R152` / `S00563`；`mikey-youtube-live-028-K009` → `mikey-youtube-live-028-E0013-R031` / `S01413`；`mikey-youtube-live-028-K010` → `mikey-youtube-live-028-E0013-R045` / `S01427`；`mikey-youtube-live-030-K008` → `mikey-youtube-live-030-E0004-R020` / `S00394`。

</details>
### DG12 · 成功率与固定数字

**规则：**没有分母、统计口径和独立比较时，不把百分比、三秒或每周次数变为效果承诺。

**原DNG知识：**无

**关联待核：**`mikey-youtube-live-021-R002`、`mikey-youtube-live-021-R003`、`mikey-youtube-live-026-R004`、`mikey-youtube-live-028-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-026-K002` → `mikey-youtube-live-026-E0004-R082` / `S00412`；`mikey-youtube-live-028-K003` → `mikey-youtube-live-028-E0005-R049` / `S00499`。

</details>
### DG13 · 收入、工作结果与消费

**规则：**自述offer、收入或课程收益不能推出可复制回报；不建议为关系结果负债，也不补造财务方案。

**原DNG知识：**无

**关联待核：**`mikey-youtube-live-021-R005`、`mikey-youtube-live-021-R006`、`mikey-youtube-live-025-R007`、`mikey-youtube-live-026-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K010` → `mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-021-K013` → `mikey-youtube-live-021-E0007-R037` / `S00659`；`mikey-youtube-live-025-K013` → `mikey-youtube-live-025-E0009-R076` / `S01107`；`mikey-youtube-live-026-K009` → `mikey-youtube-live-026-E0011-R101` / `S01161`。

</details>
### DG14 · 结果与案例真实性

**规则：**口述、标题、号码、通话或截图不能证明到场、亲密或长期效果；观众经历与人物经历分开。

**原DNG知识：**无

**关联待核：**`mikey-youtube-live-021-R002`、`mikey-youtube-live-021-R003`、`mikey-youtube-live-021-R008`、`mikey-youtube-live-025-R002`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-025-K003` → `mikey-youtube-live-025-E0002-R031` / `S00199`；`mikey-youtube-live-025-K005` → `mikey-youtube-live-025-E0002-R108` / `S00276`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-030-K012` → `mikey-youtube-live-030-E0013-R024` / `S01318`。

</details>
### DG15 · 羞辱、复仇与攻击

**规则：**不把羞辱、辱骂、报复或剥夺尊严当作高价值表达、边界训练或关系维护。

**原DNG知识：**`mikey-youtube-live-023-K025`、`mikey-youtube-live-025-K015`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-029-K012`、`mikey-youtube-live-030-K013`、`mikey-youtube-live-030-K014`

**关联待核：**`mikey-youtube-live-021-R004`、`mikey-youtube-live-023-R003`、`mikey-youtube-live-023-R004`、`mikey-youtube-live-023-R005`、`mikey-youtube-live-023-R006`、`mikey-youtube-live-023-R007`、`mikey-youtube-live-023-R008`、`mikey-youtube-live-025-R003`、`mikey-youtube-live-025-R005`、`mikey-youtube-live-025-R006`、`mikey-youtube-live-025-R008`、`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R002`、`mikey-youtube-live-030-R003`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K009` → `mikey-youtube-live-021-E0005-R075` / `S00456`；`mikey-youtube-live-023-K012` → `mikey-youtube-live-023-E0005-R113` / `S00752`；`mikey-youtube-live-023-K025` → `mikey-youtube-live-023-E0006-R006` / `S00854`；`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-029-K012` → `mikey-youtube-live-029-E0001-R030` / `S00030`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### DG16 · 操纵、支配与单方规则

**规则：**剧情控制、服从、酒精金钱压力、剥削与双重标准仅保留争议定位，不进入现实行动链。

**原DNG知识：**`mikey-youtube-live-022-K006`、`mikey-youtube-live-022-K011`、`mikey-youtube-live-022-K014`、`mikey-youtube-live-022-K018`、`mikey-youtube-live-025-K015`、`mikey-youtube-live-026-K008`、`mikey-youtube-live-027-K012`、`mikey-youtube-live-028-K012`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-030-K013`

**关联待核：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`、`mikey-youtube-live-025-R003`、`mikey-youtube-live-025-R005`、`mikey-youtube-live-025-R006`、`mikey-youtube-live-025-R008`、`mikey-youtube-live-026-R004`、`mikey-youtube-live-027-R001`、`mikey-youtube-live-027-R003`、`mikey-youtube-live-028-R002`、`mikey-youtube-live-028-R004`、`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R002`、`mikey-youtube-live-030-R003`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`；`mikey-youtube-live-025-K015` → `mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-027-K012` → `mikey-youtube-live-027-E0007-R021` / `S00651`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### DG17 · NPC及其他去人化比喻

**规则：**减轻评价压力与否认他人主体不同；限制性解释属于编辑界定，不替人物原话补善意。

**原DNG知识：**`mikey-youtube-live-028-K008`

**关联待核：**`mikey-youtube-live-023-R004`、`mikey-youtube-live-023-R011`、`mikey-youtube-live-028-R003`、`mikey-youtube-live-028-R004`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K008` → `mikey-youtube-live-023-E0003-R060` / `S00388`；`mikey-youtube-live-028-K007` → `mikey-youtube-live-028-E0010-R128` / `S01128`；`mikey-youtube-live-028-K008` → `mikey-youtube-live-028-E0011-R075` / `S01203`；`mikey-youtube-live-030-K005` → `mikey-youtube-live-030-E0002-R059` / `S00214`。

</details>
### DG18 · 被拉黑后继续联系

**规则：**不提供换号、借号或跨渠道规避拒绝；后续新练习不指向同一个已拒绝的人。

**原DNG知识：**`mikey-youtube-live-023-K024`、`mikey-youtube-live-024-K016`

**关联待核：**`mikey-youtube-live-023-R012`、`mikey-youtube-live-024-R007`、`mikey-youtube-live-024-R008`、`mikey-youtube-live-024-R010`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K024` → `mikey-youtube-live-023-E0014-R013` / `S01857`；`mikey-youtube-live-024-K016` → `mikey-youtube-live-024-E0010-R029` / `S01694`。

</details>
### DG19 · 露骨性内容、婚外情与剥削

**规则：**不把性报复、利用关系脆弱性或不对等规则作为可复制策略；只记录证据归属和冲突。

**原DNG知识：**`mikey-youtube-live-023-K025`、`mikey-youtube-live-026-K008`、`mikey-youtube-live-027-K012`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-030-K013`

**关联待核：**`mikey-youtube-live-023-R003`、`mikey-youtube-live-023-R004`、`mikey-youtube-live-023-R005`、`mikey-youtube-live-023-R006`、`mikey-youtube-live-023-R007`、`mikey-youtube-live-023-R008`、`mikey-youtube-live-026-R004`、`mikey-youtube-live-027-R001`、`mikey-youtube-live-027-R003`、`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R002`、`mikey-youtube-live-030-R003`、`mikey-youtube-live-030-R004`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K025` → `mikey-youtube-live-023-E0006-R006` / `S00854`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-027-K012` → `mikey-youtube-live-027-E0007-R021` / `S00651`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
### DG20 · 动漫能力和权力的现实迁移

**规则：**角色剧情、超能力和等级排名不是现实授权或效果证据；本期又未完成说话人归属，不能借题发挥为Mikey建议。

**原DNG知识：**`mikey-youtube-live-022-K006`、`mikey-youtube-live-022-K011`、`mikey-youtube-live-022-K014`、`mikey-youtube-live-022-K018`

**关联待核：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
## 10. 视觉校准账本

### VIS-021 · mikey-youtube-live-021

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：标题标明Mikey直播；实际查看7/7张全片联系表，00:00–01:01持续为同一男性主持固定机位，右侧为直播评论区。静帧不能逐句证明嘴型。；自动稿以主持代读观众问题并连续回答为主；手机画面和评论文本未逐条OCR。；viewer-question-01：7张联系表均显示直播评论区，自动稿反复出现主持代读问题。；多名观众集合占位；问题内容不是Mikey自己的主张。

**开放视觉待核：**无

**待核原问题：**无

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`。

</details>
### VIS-022 · mikey-youtube-live-022

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：频道直播主持身份可确认，但当前未完成逐句声音映射。；只有明确映射到Mikey的评价才能作为其观点。；guest-masked-01：画面左侧戴橙色头套/面具。；不能仅凭位置确认姓名或声音。；guest-unknown-02：题目和语境称与两名门徒讨论，但抽样画面不能完成个人映射。；保持未知。；unknown-live-speaker-01：自动稿没有说话人分离，多人交替和重叠无法可靠分开。；逐句人物核验前不得升级。；viewer-chat-01：画面持续显示实时评论栏。；代表多个观众，不是同一人。；media-character-or-plot：等级表、角色立绘和剧情复述是讨论材料。；不是Mikey亲历。

**开放视觉待核：**`mikey-youtube-live-022-R005`

**待核原问题：**未人工查看的联系表及稀疏间隙是否有手机聊天截图、动漫正片或其他承载教学信息的画面？

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`。

</details>
### VIS-023 · mikey-youtube-live-023

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：频道直播由Mikey主持；本期自动稿表现为单一主持人朗读观众问题并连续回答。最终人物确认仍等待本期视觉联系表复核。；观众问题通常由Mikey朗读，不能因出现在音轨里就把问题内容当成Mikey自己的经历。；viewer-question-01：直播答疑中反复出现称呼Mikey、陈述个人处境并等待回答的段落。；这是多个观众的集合占位符，不代表同一个人，也不是Mikey本人经历。

**开放视觉待核：**无

**待核原问题：**无

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K001` → `mikey-youtube-live-023-E0001-R045` / `S00045`。

</details>
### VIS-024 · mikey-youtube-live-024

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：搭讪玩家TV直播75由Mikey主持，完整稿为主持人连续答疑；开场明确说明相机失焦。；观众问题由主持人朗读，问题经历不归给Mikey。；viewer-question-01：多名直播观众问题由主持人转述。；集合占位符。

**开放视觉待核：**无

**待核原问题：**无

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K001` → `mikey-youtube-live-024-E0001-R037` / `S00037`。

</details>
### VIS-025 · mikey-youtube-live-025

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：搭讪玩家TV直播77由Mikey主持；完整稿为主持人连续答疑，视觉联系表另行记录画面结构。；观众问题由主持人口头转述，问题中的经历不归给Mikey。；viewer-question-01：多名观众的文字问题由主持人朗读。；集合占位符，不代表同一人物。

**开放视觉待核：**无

**待核原问题：**无

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K001` → `mikey-youtube-live-025-E0001-R081` / `S00081`。

</details>
### VIS-026 · mikey-youtube-live-026

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：搭讪玩家TV直播79由Mikey主持；自动稿按连续主持框架整理，具体画面及切换仍依视觉审查。；观众问题由主持人口头转述，问题中的经历不归给Mikey。；viewer-question-01：多名观众的文字问题由主持人朗读。；集合占位符，不代表同一人物。

**开放视觉待核：**`mikey-youtube-live-026-R004`

**待核原问题：**低清候选虽已生成，直播中是否存在屏幕、截图、播放材料或人物切换尚未语义审查？

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-026-K001` → `mikey-youtube-live-026-E0004-R045` / `S00375`。

</details>
### VIS-027 · mikey-youtube-live-027

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：搭讪玩家TV直播80由Mikey主持；自动稿按连续主持框架整理，具体画面及切换仍依视觉审查。；观众问题由主持人口头转述，问题中的经历不归给Mikey。；viewer-question-01：多名观众的文字问题由主持人朗读。；集合占位符，不代表同一人物。

**开放视觉待核：**`mikey-youtube-live-027-R003`

**待核原问题：**低清候选和联系表尚未人工语义审查，是否有截图、演示或人物切换？

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K001` → `mikey-youtube-live-027-E0001-R016` / `S00016`。

</details>
### VIS-028 · mikey-youtube-live-028

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：搭讪玩家TV直播81由Mikey主持；自动稿按连续主持框架整理，具体画面及切换仍依视觉审查。；观众问题由主持人口头转述，问题中的经历不归给Mikey。；viewer-question-01：多名观众的文字问题由主持人朗读。；集合占位符，不代表同一人物。

**开放视觉待核：**`mikey-youtube-live-028-R004`

**待核原问题：**431个低清候选尚未语义审查，是否出现屏幕、聊天截图、播放材料或人物切换？

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-028-K001` → `mikey-youtube-live-028-E0001-R061` / `S00061`。

</details>
### VIS-029 · mikey-youtube-live-029

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：搭讪玩家TV直播82由Mikey主持；自动稿按连续主持框架整理，具体画面及切换仍依视觉审查。；观众问题由主持人口头转述，问题中的经历不归给Mikey。；viewer-question-01：多名观众的文字问题由主持人朗读。；集合占位符，不代表同一人物。；caller-01：直播后段出现多次电话连线；未完成逐句说话人分离和身份核验。；集合占位符，不代表同一人物；来电者的话不得归给Mikey。；unknown-voice-01：电话段自动稿混合主持人和多名来电者，尚未逐句分离。；只用于覆盖混合语音事件。

**开放视觉待核：**`mikey-youtube-live-029-R004`

**待核原问题：**尚无正式视觉manifest，屏幕、交友软件、电话状态、聊天和人物切换均未核。

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K001` → `mikey-youtube-live-029-E0001-R130` / `S00130`。

</details>
### VIS-030 · mikey-youtube-live-030

**本次材料：**逐期摘要；代表引文；事件目录；说话人登记；待核目录

**本次视听工作：**没有图片或连续视频文件；未执行视觉检查。

**输入登记的先前核验声明（不是本次行为）：**mikey：搭讪玩家TV直播83由Mikey主持；自动稿按连续主持框架整理，具体画面及切换仍依视觉审查。；观众问题由主持人口头转述，问题中的经历不归给Mikey。；viewer-question-01：多名观众的文字问题由主持人朗读。；集合占位符，不代表同一人物。

**开放视觉待核：**`mikey-youtube-live-030-R004`

**待核原问题：**尚无正式视觉manifest，屏幕、课程宣传、人物与展示内容均未核。

**不能证明：**句级嘴型与说话人；截图文字作者和真实性；切点前后连续顺序；同一身份跨通话/跨场景成立；到场、进房和亲密结果；持续同意；动作与结果的因果

**事件状态：**该源事件observations为空且review_status仍为pending；本次不能据事件标题补可观察事实。

**对使用的影响：**直播79/80/81的全期major视觉待核在本综合中保守阻断；直播82/83的全期blocking继续阻断。其他源按具体关联待核控制，不因此宣称其余已连续核验。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-030-K001` → `mikey-youtube-live-030-E0001-R060` / `S00060`。

</details>
## 11. 追溯问题与输入不一致

共62项。这里的TI编号是本次新增的追溯问题编号，不冒充输入review ID。所有原值保留；时间窗、URL或代表引文存在问题，不意味着未提供的完整材料必然没有正确答案。

### TI001 · compact_package_scope

**发现：**完整的是目录与结构，不是逐句原稿或视听证据。

**知识：**无

**事件：**无

**原待核：**无

**核对细节：**{"registered_sid_count": 16132, "provided_representative_quote_records": 288, "original_quote_count_as_supplied": 963, "archive_file_count": 4}

**处理：**所有跨期命题限制在上传概括和实际代表片段；675个引用位置未附正文，去重后涉及671个证据定位；不补写、不声称已读。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI002 · speaker_registry_url_mismatch

**发现：**说话人登记的证据URL指向与本期sources不同的视频ID，不能作为本期人物确认的独立依据。

**知识：**无

**事件：**无

**原待核：**无

**核对细节：**{"mismatched_entries": [{"speaker_id": "mikey", "url_as_supplied": "https://www.youtube.com/watch?v=JXUQx19xDuw", "video_id_in_url": "JXUQx19xDuw", "expected_video_id_from_sources": "dZgV_s1FVv8"}]}

**处理：**登记原样保留，不猜测替换URL；direct仅是来源摘要的有限间接转述，不得据此声称身份或句级归属已核。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI003 · speaker_registry_url_mismatch

**发现：**说话人登记的证据URL指向与本期sources不同的视频ID，不能作为本期人物确认的独立依据。

**知识：**无

**事件：**无

**原待核：**无

**核对细节：**{"mismatched_entries": [{"speaker_id": "mikey", "url_as_supplied": "https://www.youtube.com/watch?v=LDHv4sFeQ8Q&t=28s", "video_id_in_url": "LDHv4sFeQ8Q", "expected_video_id_from_sources": "wjizzSk9eAI"}, {"speaker_id": "viewer-question-01", "url_as_supplied": "https://www.youtube.com/watch?v=LDHv4sFeQ8Q&t=217s", "video_id_in_url": "LDHv4sFeQ8Q", "expected_video_id_from_sources": "wjizzSk9eAI"}]}

**处理：**登记原样保留，不猜测替换URL；direct仅是来源摘要的有限间接转述，不得据此声称身份或句级归属已核。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI004 · knowledge_event_membership_mismatch

**发现：**知识声明的event_ids未覆盖它所引用证据实际所属的事件。

**知识：**`mikey-youtube-live-022-K009`

**事件：**`mikey-youtube-live-022-E0007`、`mikey-youtube-live-022-E0008`

**原待核：**无

**核对细节：**{"event_ids_as_supplied": ["mikey-youtube-live-022-E0007"], "additional_events_implied_by_existing_evidence_ids": ["mikey-youtube-live-022-E0008"]}

**处理：**不改逐期event_ids；跨期待核传播同时考虑声明事件和证据所属事件，防止漏传阻断。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`。

</details>
### TI005 · knowledge_event_membership_mismatch

**发现：**知识声明的event_ids未覆盖它所引用证据实际所属的事件。

**知识：**`mikey-youtube-live-023-K002`

**事件：**`mikey-youtube-live-023-E0001`、`mikey-youtube-live-023-E0002`、`mikey-youtube-live-023-E0003`

**原待核：**无

**核对细节：**{"event_ids_as_supplied": ["mikey-youtube-live-023-E0001", "mikey-youtube-live-023-E0002"], "additional_events_implied_by_existing_evidence_ids": ["mikey-youtube-live-023-E0003"]}

**处理：**不改逐期event_ids；跨期待核传播同时考虑声明事件和证据所属事件，防止漏传阻断。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K002` → `mikey-youtube-live-023-E0001-R068` / `S00068`。

</details>
### TI006 · knowledge_event_membership_mismatch

**发现：**知识声明的event_ids未覆盖它所引用证据实际所属的事件。

**知识：**`mikey-youtube-live-023-K019`

**事件：**`mikey-youtube-live-023-E0009`、`mikey-youtube-live-023-E0010`

**原待核：**无

**核对细节：**{"event_ids_as_supplied": ["mikey-youtube-live-023-E0010"], "additional_events_implied_by_existing_evidence_ids": ["mikey-youtube-live-023-E0009"]}

**处理：**不改逐期event_ids；跨期待核传播同时考虑声明事件和证据所属事件，防止漏传阻断。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K019` → `mikey-youtube-live-023-E0010-R001` / `S01389`。

</details>
### TI007 · knowledge_event_membership_mismatch

**发现：**知识声明的event_ids未覆盖它所引用证据实际所属的事件。

**知识：**`mikey-youtube-live-023-K025`

**事件：**`mikey-youtube-live-023-E0005`、`mikey-youtube-live-023-E0006`、`mikey-youtube-live-023-E0007`、`mikey-youtube-live-023-E0008`

**原待核：**无

**核对细节：**{"event_ids_as_supplied": ["mikey-youtube-live-023-E0005", "mikey-youtube-live-023-E0007", "mikey-youtube-live-023-E0008"], "additional_events_implied_by_existing_evidence_ids": ["mikey-youtube-live-023-E0006"]}

**处理：**不改逐期event_ids；跨期待核传播同时考虑声明事件和证据所属事件，防止漏传阻断。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K025` → `mikey-youtube-live-023-E0006-R006` / `S00854`。

</details>
### TI008 · knowledge_event_membership_mismatch

**发现：**知识声明的event_ids未覆盖它所引用证据实际所属的事件。

**知识：**`mikey-youtube-live-026-K004`

**事件：**`mikey-youtube-live-026-E0011`、`mikey-youtube-live-026-E0012`

**原待核：**无

**核对细节：**{"event_ids_as_supplied": ["mikey-youtube-live-026-E0011"], "additional_events_implied_by_existing_evidence_ids": ["mikey-youtube-live-026-E0012"]}

**处理：**不改逐期event_ids；跨期待核传播同时考虑声明事件和证据所属事件，防止漏传阻断。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-026-K004` → `mikey-youtube-live-026-E0012-R044` / `S01224`。

</details>
### TI009 · knowledge_event_membership_mismatch

**发现：**知识声明的event_ids未覆盖它所引用证据实际所属的事件。

**知识：**`mikey-youtube-live-027-K002`

**事件：**`mikey-youtube-live-027-E0001`、`mikey-youtube-live-027-E0002`、`mikey-youtube-live-027-E0004`

**原待核：**无

**核对细节：**{"event_ids_as_supplied": ["mikey-youtube-live-027-E0001", "mikey-youtube-live-027-E0004"], "additional_events_implied_by_existing_evidence_ids": ["mikey-youtube-live-027-E0002"]}

**处理：**不改逐期event_ids；跨期待核传播同时考虑声明事件和证据所属事件，防止漏传阻断。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`。

</details>
### TI010 · knowledge_event_membership_mismatch

**发现：**知识声明的event_ids未覆盖它所引用证据实际所属的事件。

**知识：**`mikey-youtube-live-028-K012`

**事件：**`mikey-youtube-live-028-E0003`、`mikey-youtube-live-028-E0007`、`mikey-youtube-live-028-E0008`

**原待核：**无

**核对细节：**{"event_ids_as_supplied": ["mikey-youtube-live-028-E0003", "mikey-youtube-live-028-E0007"], "additional_events_implied_by_existing_evidence_ids": ["mikey-youtube-live-028-E0008"]}

**处理：**不改逐期event_ids；跨期待核传播同时考虑声明事件和证据所属事件，防止漏传阻断。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`。

</details>
### TI011 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-021-E0007`、`mikey-youtube-live-021-E0008`

**原待核：**`mikey-youtube-live-021-R006`

**核对细节：**{"start_as_supplied": 2030, "end_as_supplied": 2410, "duration_seconds_as_supplied": 3665.060862, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-021-E0007-R070", "youtube_url": "https://www.youtube.com/watch?v=gkADT8_5s14&t=2026s", "url_second_as_supplied": 2026.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI012 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-023-E0005`

**原待核：**`mikey-youtube-live-023-R004`

**核对细节：**{"start_as_supplied": 1800, "end_as_supplied": 2050, "duration_seconds_as_supplied": 5779.609252, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-023-E0005-R070", "youtube_url": "https://www.youtube.com/watch?v=wjizzSk9eAI&t=1783s", "url_second_as_supplied": 1783.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI013 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-023-E0011`、`mikey-youtube-live-023-E0012`

**原待核：**`mikey-youtube-live-023-R011`

**核对细节：**{"start_as_supplied": 4120, "end_as_supplied": 4300, "duration_seconds_as_supplied": 5779.609252, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-023-E0011-R076", "youtube_url": "https://www.youtube.com/watch?v=wjizzSk9eAI&t=4108s", "url_second_as_supplied": 4108.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI014 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-024-E0008`

**原待核：**`mikey-youtube-live-024-R004`

**核对细节：**{"start_as_supplied": 3900, "end_as_supplied": 4140, "duration_seconds_as_supplied": 5785.274921, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-024-E0008-R051", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3867s", "url_second_as_supplied": 3867.0}, {"evidence_id": "mikey-youtube-live-024-E0008-R053", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3875s", "url_second_as_supplied": 3875.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI015 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-024-E0009`

**原待核：**`mikey-youtube-live-024-R006`

**核对细节：**{"start_as_supplied": 4550, "end_as_supplied": 4800, "duration_seconds_as_supplied": 5785.274921, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-024-E0009-R021", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4239s", "url_second_as_supplied": 4239.0}, {"evidence_id": "mikey-youtube-live-024-E0009-R023", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4241s", "url_second_as_supplied": 4241.0}, {"evidence_id": "mikey-youtube-live-024-E0009-R034", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4267s", "url_second_as_supplied": 4267.0}, {"evidence_id": "mikey-youtube-live-024-E0009-R040", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4276s", "url_second_as_supplied": 4276.0}, {"evidence_id": "mikey-youtube-live-024-E0009-R046", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4284s", "url_second_as_supplied": 4284.0}, {"evidence_id": "mikey-youtube-live-024-E0009-R065", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4307s", "url_second_as_supplied": 4307.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI016 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-024-E0010`

**原待核：**`mikey-youtube-live-024-R007`

**核对细节：**{"start_as_supplied": 5080, "end_as_supplied": 5160, "duration_seconds_as_supplied": 5785.274921, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-024-E0010-R024", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4562s", "url_second_as_supplied": 4562.0}, {"evidence_id": "mikey-youtube-live-024-E0010-R029", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4570s", "url_second_as_supplied": 4570.0}, {"evidence_id": "mikey-youtube-live-024-E0010-R030", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4572s", "url_second_as_supplied": 4572.0}, {"evidence_id": "mikey-youtube-live-024-E0010-R032", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4576s", "url_second_as_supplied": 4576.0}, {"evidence_id": "mikey-youtube-live-024-E0010-R033", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4578s", "url_second_as_supplied": 4578.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI017 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-024-E0010`

**原待核：**`mikey-youtube-live-024-R008`

**核对细节：**{"start_as_supplied": 5580, "end_as_supplied": 5670, "duration_seconds_as_supplied": 5785.274921, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-024-E0010-R075", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4683s", "url_second_as_supplied": 4683.0}, {"evidence_id": "mikey-youtube-live-024-E0010-R076", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4689s", "url_second_as_supplied": 4689.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI018 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-024-E0011`、`mikey-youtube-live-024-E0012`

**原待核：**`mikey-youtube-live-024-R009`

**核对细节：**{"start_as_supplied": 6010, "end_as_supplied": 6080, "duration_seconds_as_supplied": 5785.274921, "end_exceeds_duration_by_more_than_1s": true, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-024-E0011-R111", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5079s", "url_second_as_supplied": 5079.0}, {"evidence_id": "mikey-youtube-live-024-E0011-R112", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5081s", "url_second_as_supplied": 5081.0}, {"evidence_id": "mikey-youtube-live-024-E0011-R116", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5090s", "url_second_as_supplied": 5090.0}, {"evidence_id": "mikey-youtube-live-024-E0012-R003", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5103s", "url_second_as_supplied": 5103.0}, {"evidence_id": "mikey-youtube-live-024-E0012-R010", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5114s", "url_second_as_supplied": 5114.0}, {"evidence_id": "mikey-youtube-live-024-E0012-R011", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5116s", "url_second_as_supplied": 5116.0}, {"evidence_id": "mikey-youtube-live-024-E0012-R014", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5125s", "url_second_as_supplied": 5125.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI019 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-024-E0013`

**原待核：**`mikey-youtube-live-024-R010`

**核对细节：**{"start_as_supplied": 6740, "end_as_supplied": 6810, "duration_seconds_as_supplied": 5785.274921, "end_exceeds_duration_by_more_than_1s": true, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-024-E0013-R040", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5631s", "url_second_as_supplied": 5631.0}, {"evidence_id": "mikey-youtube-live-024-E0013-R048", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5645s", "url_second_as_supplied": 5645.0}, {"evidence_id": "mikey-youtube-live-024-E0013-R055", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5655s", "url_second_as_supplied": 5655.0}, {"evidence_id": "mikey-youtube-live-024-E0013-R061", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5663s", "url_second_as_supplied": 5663.0}, {"evidence_id": "mikey-youtube-live-024-E0013-R063", "youtube_url": "https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5666s", "url_second_as_supplied": 5666.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI020 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-025-E0005`、`mikey-youtube-live-025-E0006`

**原待核：**`mikey-youtube-live-025-R005`

**核对细节：**{"start_as_supplied": 1600, "end_as_supplied": 1960, "duration_seconds_as_supplied": 3995.062857, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-025-E0006-R065", "youtube_url": "https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2018s", "url_second_as_supplied": 2018.0}, {"evidence_id": "mikey-youtube-live-025-E0006-R068", "youtube_url": "https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2025s", "url_second_as_supplied": 2025.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI021 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-025-E0009`

**原待核：**`mikey-youtube-live-025-R007`

**核对细节：**{"start_as_supplied": 2620, "end_as_supplied": 2830, "duration_seconds_as_supplied": 3995.062857, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-025-E0009-R074", "youtube_url": "https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2899s", "url_second_as_supplied": 2899.0}, {"evidence_id": "mikey-youtube-live-025-E0009-R083", "youtube_url": "https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2920s", "url_second_as_supplied": 2920.0}, {"evidence_id": "mikey-youtube-live-025-E0009-R086", "youtube_url": "https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2928s", "url_second_as_supplied": 2928.0}, {"evidence_id": "mikey-youtube-live-025-E0009-R104", "youtube_url": "https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2962s", "url_second_as_supplied": 2962.0}, {"evidence_id": "mikey-youtube-live-025-E0009-R108", "youtube_url": "https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2967s", "url_second_as_supplied": 2967.0}, {"evidence_id": "mikey-youtube-live-025-E0009-R110", "youtube_url": "https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2969s", "url_second_as_supplied": 2969.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI022 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-026-E0002`

**原待核：**`mikey-youtube-live-026-R001`

**核对细节：**{"start_as_supplied": 500, "end_as_supplied": 900, "duration_seconds_as_supplied": 3970.078186, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-026-E0002-R020", "youtube_url": "https://www.youtube.com/watch?v=PQbkX-IUGcs&t=345s", "url_second_as_supplied": 345.0}, {"evidence_id": "mikey-youtube-live-026-E0002-R082", "youtube_url": "https://www.youtube.com/watch?v=PQbkX-IUGcs&t=468s", "url_second_as_supplied": 468.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI023 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-026-E0003`

**原待核：**`mikey-youtube-live-026-R002`

**核对细节：**{"start_as_supplied": 900, "end_as_supplied": 1450, "duration_seconds_as_supplied": 3970.078186, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-026-E0003-R026", "youtube_url": "https://www.youtube.com/watch?v=PQbkX-IUGcs&t=627s", "url_second_as_supplied": 627.0}, {"evidence_id": "mikey-youtube-live-026-E0003-R027", "youtube_url": "https://www.youtube.com/watch?v=PQbkX-IUGcs&t=629s", "url_second_as_supplied": 629.0}, {"evidence_id": "mikey-youtube-live-026-E0003-R028", "youtube_url": "https://www.youtube.com/watch?v=PQbkX-IUGcs&t=630s", "url_second_as_supplied": 630.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI024 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-027-E0007`

**原待核：**`mikey-youtube-live-027-R001`

**核对细节：**{"start_as_supplied": 2100, "end_as_supplied": 2300, "duration_seconds_as_supplied": 4460.065669, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-027-E0007-R020", "youtube_url": "https://www.youtube.com/watch?v=8jCwDoBjWT0&t=2306s", "url_second_as_supplied": 2306.0}, {"evidence_id": "mikey-youtube-live-027-E0007-R021", "youtube_url": "https://www.youtube.com/watch?v=8jCwDoBjWT0&t=2318s", "url_second_as_supplied": 2318.0}, {"evidence_id": "mikey-youtube-live-027-E0007-R022", "youtube_url": "https://www.youtube.com/watch?v=8jCwDoBjWT0&t=2319s", "url_second_as_supplied": 2319.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI025 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-028-E0007`、`mikey-youtube-live-028-E0008`

**原待核：**`mikey-youtube-live-028-R002`

**核对细节：**{"start_as_supplied": 1500, "end_as_supplied": 2900, "duration_seconds_as_supplied": 5465.048526, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-028-E0008-R041", "youtube_url": "https://www.youtube.com/watch?v=vBoAYfRFhh0&t=2912s", "url_second_as_supplied": 2912.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI026 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-029-E0011`、`mikey-youtube-live-029-E0012`

**原待核：**`mikey-youtube-live-029-R003`

**核对细节：**{"start_as_supplied": 7500, "end_as_supplied": 10200, "duration_seconds_as_supplied": 9355.064308, "end_exceeds_duration_by_more_than_1s": true, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-029-E0011-R163", "youtube_url": "https://www.youtube.com/watch?v=knZc0MMOnbw&t=6894s", "url_second_as_supplied": 6894.0}, {"evidence_id": "mikey-youtube-live-029-E0011-R164", "youtube_url": "https://www.youtube.com/watch?v=knZc0MMOnbw&t=6897s", "url_second_as_supplied": 6897.0}, {"evidence_id": "mikey-youtube-live-029-E0012-R001", "youtube_url": "https://www.youtube.com/watch?v=knZc0MMOnbw&t=6902s", "url_second_as_supplied": 6902.0}, {"evidence_id": "mikey-youtube-live-029-E0012-R074", "youtube_url": "https://www.youtube.com/watch?v=knZc0MMOnbw&t=7147s", "url_second_as_supplied": 7147.0}, {"evidence_id": "mikey-youtube-live-029-E0012-R082", "youtube_url": "https://www.youtube.com/watch?v=knZc0MMOnbw&t=7171s", "url_second_as_supplied": 7171.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI027 · review_window_inconsistent

**发现：**待核时间窗与其证据URL秒数不一致，或超过来源账本时长；这不是解除待核的依据。

**知识：**无

**事件：**`mikey-youtube-live-030-E0001`

**原待核：**`mikey-youtube-live-030-R001`

**核对细节：**{"start_as_supplied": 700, "end_as_supplied": 1000, "duration_seconds_as_supplied": 4085.063401, "end_exceeds_duration_by_more_than_1s": false, "evidence_outside_window_with_1s_tolerance": [{"evidence_id": "mikey-youtube-live-030-E0001-R134", "youtube_url": "https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=533s", "url_second_as_supplied": 533.0}, {"evidence_id": "mikey-youtube-live-030-E0001-R137", "youtube_url": "https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=538s", "url_second_as_supplied": 538.0}, {"evidence_id": "mikey-youtube-live-030-E0001-R138", "youtube_url": "https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=540s", "url_second_as_supplied": 540.0}, {"evidence_id": "mikey-youtube-live-030-E0001-R139", "youtube_url": "https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=540s", "url_second_as_supplied": 540.0}]}

**处理：**原窗和证据地址原样保留；本地逐证据定位修复。当前按ID/事件/证据关联传播限制，不用错误时间窗裁掉拒绝或风险片段。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI028 · representative_excerpt_insufficient_or_off_topic

**发现：**代表片段仅到“留下…行为”的半句，尚不能独立支撑模糊画像、好奇与后续累积的完整机制。

**知识：**`mikey-youtube-live-021-K006`

**事件：**`mikey-youtube-live-021-E0004`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-021-E0004-R038` / `S00322`（999.47–1001.13秒），自动稿记录为："初始吸引就是留下"。

`mikey-youtube-live-021-E0004-R039` / `S00323`（1001.13–1003.39秒），自动稿记录为："留下一定量的行为"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K006` → `mikey-youtube-live-021-E0004-R039` / `S00323`。

</details>
### TI029 · representative_excerpt_insufficient_or_off_topic

**发现：**两条代表片段均为观众陈述拿号后不回复，未附对应回答原文；不能把提问直接用作Mikey的因果判断。

**知识：**`mikey-youtube-live-023-K006`

**事件：**`mikey-youtube-live-023-E0002`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-023-E0002-R088` / `S00275`（730.69–734.07秒），自动稿记录为："Mikey我这段时间出去搭讪"。

`mikey-youtube-live-023-E0002-R091` / `S00278`（737.03–739.27秒），自动稿记录为："但回来发信息都不回"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K006` → `mikey-youtube-live-023-E0002-R091` / `S00278`。

</details>
### TI030 · representative_excerpt_insufficient_or_off_topic

**发现：**代表片段仅出现淡定与“你这个人淡定”，未展示话多/话少对照；完整区分暂保留为逐期编辑概括。

**知识：**`mikey-youtube-live-024-K003`

**事件：**`mikey-youtube-live-024-E0002`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-024-E0002-R101` / `S00246`（829.46–840.61秒），自动稿记录为："要淡定"。

`mikey-youtube-live-024-E0002-R104` / `S00249`（845.07–846.59秒），自动稿记录为："你这个人淡定"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-024-K003` → `mikey-youtube-live-024-E0002-R104` / `S00249`。

</details>
### TI031 · representative_excerpt_insufficient_or_off_topic

**发现：**代表片段止于紧张原因的提问和“因为在潜意识里”，尚未展示裁判、自我价值与失败归因的完整回答。

**知识：**`mikey-youtube-live-025-K011`

**事件：**`mikey-youtube-live-025-E0007`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-025-E0007-R025` / `S00838`（2172.56–2175.0秒），自动稿记录为："你跟女生讲话会紧张的原因"。

`mikey-youtube-live-025-E0007-R031` / `S00844`（2182.1–2184.02秒），自动稿记录为："是因为你在潜意识里"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-025-K011` → `mikey-youtube-live-025-E0007-R031` / `S00844`。

</details>
### TI032 · representative_excerpt_insufficient_or_off_topic

**发现：**主动邀约条目的代表片段是多偶男性魅力评价，不能支持邀约步骤。

**知识：**`mikey-youtube-live-026-K005`

**事件：**`mikey-youtube-live-026-E0008`

**原待核：**无

**核对细节：**{"original_release_status": "context_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-026-E0008-R032` / `S00762`（2055.69–2057.33秒），自动稿记录为："多偶的男人是最有魅力的"。

`mikey-youtube-live-026-E0008-R033` / `S00763`（2057.33–2059.81秒），自动稿记录为："就是多偶的男人是最有魅力的"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-026-K005` → `mikey-youtube-live-026-E0008-R033` / `S00763`。

</details>
### TI033 · representative_excerpt_insufficient_or_off_topic

**发现：**非安全性行为条目的代表片段偏向ATM、金钱和出轨，不能充当健康或避孕结论的逐字依据。

**知识：**`mikey-youtube-live-026-K007`

**事件：**`mikey-youtube-live-026-E0003`

**原待核：**无

**核对细节：**{"original_release_status": "do_not_generalize", "runtime_use_level": "do_not_generalize"}

**代表自动稿原样定位：**

`mikey-youtube-live-026-E0003-R026` / `S00256`（627.81–629.03秒），自动稿记录为："她只会把你当ATMG"。

`mikey-youtube-live-026-E0003-R027` / `S00257`（629.03–630.67秒），自动稿记录为："然后拿你的钱去跟黄毛上床"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`。

</details>
### TI034 · representative_excerpt_insufficient_or_off_topic

**发现：**关系规则条目的代表片段偏向金钱或随时可得，不足以独立还原完整双重标准。

**知识：**`mikey-youtube-live-026-K008`

**事件：**`mikey-youtube-live-026-E0010`

**原待核：**无

**核对细节：**{"original_release_status": "do_not_generalize", "runtime_use_level": "do_not_generalize"}

**代表自动稿原样定位：**

`mikey-youtube-live-026-E0010-R052` / `S01002`（3035.54–3037.34秒），自动稿记录为："你他妈的天天随叫随到"。

`mikey-youtube-live-026-E0010-R053` / `S01003`（3037.34–3039.44秒），自动稿记录为："女人要多少钱你给他多少钱"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`。

</details>
### TI035 · representative_excerpt_insufficient_or_off_topic

**发现：**长期目标条目的代表片段谈婚后出轨及对方不可以，不能证明长期目标和创造的主张。

**知识：**`mikey-youtube-live-026-K009`

**事件：**`mikey-youtube-live-026-E0011`、`mikey-youtube-live-026-E0012`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-026-E0011-R100` / `S01160`（3548.52–3550.1秒），自动稿记录为："就是你结婚你是可以出轨的"。

`mikey-youtube-live-026-E0011-R101` / `S01161`（3550.1–3550.6秒），自动稿记录为："他不可以"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-026-K009` → `mikey-youtube-live-026-E0011-R101` / `S01161`。

</details>
### TI036 · representative_excerpt_insufficient_or_off_topic

**发现：**第一次约会地点条目的代表片段未给出安静、友好或便于退出的地点判断。

**知识：**`mikey-youtube-live-027-K008`

**事件：**`mikey-youtube-live-027-E0008`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-027-E0008-R070` / `S00810`（3052.78–3053.66秒），自动稿记录为："但是不会掉吸引"。

`mikey-youtube-live-027-E0008-R071` / `S00811`（3053.66–3069.8秒），自动稿记录为："可以多举一些增加吸引和掉吸引的行为吗"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K008` → `mikey-youtube-live-027-E0008-R071` / `S00811`。

</details>
### TI037 · representative_excerpt_insufficient_or_off_topic

**发现：**信念—行动循环条目的代表片段是是否继续直播的问答，不能证明该循环。

**知识：**`mikey-youtube-live-027-K009`

**事件：**`mikey-youtube-live-027-E0009`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-027-E0009-R042` / `S00882`（3208.42–3209.8秒），自动稿记录为："还会给兄弟们播吗"。

`mikey-youtube-live-027-E0009-R043` / `S00883`（3209.8–3211.2秒），自动稿记录为："会啊"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K009` → `mikey-youtube-live-027-E0009-R043` / `S00883`。

</details>
### TI038 · representative_excerpt_insufficient_or_off_topic

**发现：**生活状态一致性条目的代表片段是零散“掉心瞬间/过渡期”表述，不足以独立展开机制。

**知识：**`mikey-youtube-live-027-K010`

**事件：**`mikey-youtube-live-027-E0012`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-027-E0012-R042` / `S01172`（4073.46–4074.72秒），自动稿记录为："掉心是一瞬间的事"。

`mikey-youtube-live-027-E0012-R043` / `S01173`（4074.72–4076.36秒），自动稿记录为："我感觉这种事情是一个过渡期"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K010` → `mikey-youtube-live-027-E0012-R043` / `S01173`。

</details>
### TI039 · representative_excerpt_insufficient_or_off_topic

**发现：**渐进练习条目的代表片段侧重坐着聊天的行为线索，不能据此还原完整练习方案。

**知识：**`mikey-youtube-live-027-K011`

**事件：**`mikey-youtube-live-027-E0013`

**原待核：**无

**核对细节：**{"original_release_status": "context_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-027-E0013-R010` / `S01210`（4198.7–4263.03秒），自动稿记录为："强行无线索从言谈举止就完全够了"。

`mikey-youtube-live-027-E0013-R011` / `S01211`（4263.03–4264.51秒），自动稿记录为："就你跟他坐着聊天的"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K011` → `mikey-youtube-live-027-E0013-R011` / `S01211`。

</details>
### TI040 · representative_excerpt_insufficient_or_off_topic

**发现：**婚外情与剥削条目的代表片段不足以独立支持概括；原do_not_generalize仍保留，不能因引文不足反向洗白。

**知识：**`mikey-youtube-live-027-K012`

**事件：**`mikey-youtube-live-027-E0007`

**原待核：**无

**核对细节：**{"original_release_status": "do_not_generalize", "runtime_use_level": "do_not_generalize"}

**代表自动稿原样定位：**

`mikey-youtube-live-027-E0007-R020` / `S00650`（2306.3–2318.03秒），自动稿记录为："它是大于长相的"。

`mikey-youtube-live-027-E0007-R021` / `S00651`（2318.03–2319.93秒），自动稿记录为："麦哥很多女的一直跟我说"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K012` → `mikey-youtube-live-027-E0007-R021` / `S00651`。

</details>
### TI041 · representative_excerpt_insufficient_or_off_topic

**发现：**线上邀约条目的代表片段转入新观众提示，不能证明身份确认、意愿或具体邀约流程。

**知识：**`mikey-youtube-live-028-K001`

**事件：**`mikey-youtube-live-028-E0001`

**原待核：**无

**核对细节：**{"original_release_status": "context_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-028-E0001-R060` / `S00060`（823.14–824.42秒），自动稿记录为："很简单"。

`mikey-youtube-live-028-E0001-R061` / `S00061`（824.42–832.02秒），自动稿记录为："新来的兄弟们都点这里"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-028-K001` → `mikey-youtube-live-028-E0001-R061` / `S00061`。

</details>
### TI042 · representative_excerpt_insufficient_or_off_topic

**发现：**关系边界条目的代表片段是声音状态及零散伴侣话题，不能证明完整处理方法。

**知识：**`mikey-youtube-live-028-K005`

**事件：**`mikey-youtube-live-028-E0008`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-028-E0008-R060` / `S00840`（2962.84–2963.94秒），自动稿记录为："那个话就会非常的糊"。

`mikey-youtube-live-028-E0008-R061` / `S00841`（2963.94–2979.6秒），自动稿记录为："我今天搭上了很多女生都说自己有对象"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-028-K005` → `mikey-youtube-live-028-E0008-R061` / `S00841`。

</details>
### TI043 · representative_excerpt_insufficient_or_off_topic

**发现：**收号跟进条目的代表片段谈租住与带回家，不能独立支持全链路诊断。

**知识：**`mikey-youtube-live-028-K006`

**事件：**`mikey-youtube-live-028-E0009`

**原待核：**无

**核对细节：**{"original_release_status": "direct", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-028-E0009-R050` / `S00940`（3262.32–3268.75秒），自动稿记录为："租的房子很一般"。

`mikey-youtube-live-028-E0009-R051` / `S00941`（3268.75–3269.69秒），自动稿记录为："怎么带到家里"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-028-K006` → `mikey-youtube-live-028-E0009-R051` / `S00941`。

</details>
### TI044 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K001`

**事件：**`mikey-youtube-live-022-E0001`

**原待核：**无

**核对细节：**{"original_release_status": "candidate_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0001-R051` / `S00051`（154.91–156.17秒），自动稿记录为："最后就拉"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`。

</details>
### TI045 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K002`

**事件：**`mikey-youtube-live-022-E0003`

**原待核：**无

**核对细节：**{"original_release_status": "candidate_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0003-R001` / `S00201`（672.88–675.88秒），自动稿记录为："那你觉得卡尔西应该评什么集"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`。

</details>
### TI046 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K005`

**事件：**`mikey-youtube-live-022-E0005`

**原待核：**无

**核对细节：**{"original_release_status": "hold", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0005-R041` / `S00501`（1454.41–1456.95秒），自动稿记录为："她就是为了那个撑你的任务"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`。

</details>
### TI047 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K007`

**事件：**`mikey-youtube-live-022-E0006`

**原待核：**无

**核对细节：**{"original_release_status": "candidate_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0006-R031` / `S00601`（1721.79–1723.59秒），自动稿记录为："然后我现在的徒弟在牛逼"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`。

</details>
### TI048 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K008`

**事件：**`mikey-youtube-live-022-E0007`

**原待核：**无

**核对细节：**{"original_release_status": "candidate_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0007-R051` / `S00751`（2201.63–2213.21秒），自动稿记录为："钥匙都上人了 佐柱我觉得不配影集"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`。

</details>
### TI049 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K009`

**事件：**`mikey-youtube-live-022-E0007`、`mikey-youtube-live-022-E0008`

**原待核：**无

**核对细节：**{"original_release_status": "hold", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0008-R001` / `S00851`（2509.02–2509.72秒），自动稿记录为："然后做不到"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`。

</details>
### TI050 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K010`

**事件：**`mikey-youtube-live-022-E0008`

**原待核：**无

**核对细节：**{"original_release_status": "candidate_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0008-R101` / `S00951`（2748.44–2749.24秒），自动稿记录为："卧槽"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`。

</details>
### TI051 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K012`

**事件：**`mikey-youtube-live-022-E0010`

**原待核：**无

**核对细节：**{"original_release_status": "candidate_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0010-R001` / `S01151`（3288.02–3291.02秒），自动稿记录为："结果的妈的女人都已经受尾了"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`。

</details>
### TI052 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K013`

**事件：**`mikey-youtube-live-022-E0010`

**原待核：**无

**核对细节：**{"original_release_status": "candidate_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0010-R101` / `S01251`（3558.69–3560.69秒），自动稿记录为："他们的某些特质是有点too much"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`。

</details>
### TI053 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K015`

**事件：**`mikey-youtube-live-022-E0013`

**原待核：**无

**核对细节：**{"original_release_status": "candidate_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0013-R051` / `S01651`（4808.98–4810.02秒），自动稿记录为："我觉得他不容易"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`。

</details>
### TI054 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K016`

**事件：**`mikey-youtube-live-022-E0014`

**原待核：**无

**核对细节：**{"original_release_status": "candidate_only", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0014-R041` / `S01801`（5224.31–5226.31秒），自动稿记录为："他其实还行"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`。

</details>
### TI055 · representative_excerpt_insufficient_or_off_topic

**发现：**动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**知识：**`mikey-youtube-live-022-K017`

**事件：**`mikey-youtube-live-022-E0015`

**原待核：**无

**核对细节：**{"original_release_status": "hold", "runtime_use_level": "hold"}

**代表自动稿原样定位：**

`mikey-youtube-live-022-E0015-R071` / `S01951`（5746.88–5747.88秒），自动稿记录为："其实我觉得"。

**处理：**本次只作代表片段审计，不断言未提供的其余引文不存在或原观点必错；非DNG设hold，DNG不变，不能向其他期借证补完整原话。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`。

</details>
### TI056 · phone_coarse_speaker_conflict

**发现：**电话事件粗粒度spoken_by_id记为mikey，同时细粒度归属为未完成通话说话人分离；后者必须限制前者。

**知识：**`mikey-youtube-live-029-K009`、`mikey-youtube-live-029-K010`、`mikey-youtube-live-029-K011`

**事件：**`mikey-youtube-live-029-E0007`、`mikey-youtube-live-029-E0008`、`mikey-youtube-live-029-E0009`、`mikey-youtube-live-029-E0010`、`mikey-youtube-live-029-E0011`、`mikey-youtube-live-029-E0012`、`mikey-youtube-live-029-E0014`

**原待核：**`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`

**核对细节：**{"caller_01_is_collective": true, "same_caller_across_events": "unknown"}

**处理：**不把每句话归给主持；不从caller集合占位推定同一来电者。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`。

</details>
### TI057 · task_gameplay_label_vs_anime_event_catalog

**发现：**任务采用游戏五类归属控制，而本期目录具体是动漫角色排名/剧情复述；不能从上层标签推造实际游戏操作。

**知识：**`mikey-youtube-live-022-K001`、`mikey-youtube-live-022-K002`、`mikey-youtube-live-022-K003`、`mikey-youtube-live-022-K004`、`mikey-youtube-live-022-K005`、`mikey-youtube-live-022-K006`、`mikey-youtube-live-022-K007`、`mikey-youtube-live-022-K008`、`mikey-youtube-live-022-K009`、`mikey-youtube-live-022-K010`、`mikey-youtube-live-022-K011`、`mikey-youtube-live-022-K012`、`mikey-youtube-live-022-K013`、`mikey-youtube-live-022-K014`、`mikey-youtube-live-022-K015`、`mikey-youtube-live-022-K016`、`mikey-youtube-live-022-K017`、`mikey-youtube-live-022-K018`

**事件：**无

**原待核：**无

**处理：**保留五类与uncertain_overlap全部计数；叙述称动漫/播放材料与多人讨论，不新增未观察动作。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### TI058 · edited_claim_is_not_verbatim_attribution

**发现：**原claim混合了人物观点、观众案例及逐期编辑的安全收窄。仅保留attribution_status不能证明整段claim逐句均为人物原话。

**知识：**`mikey-youtube-live-023-K022`、`mikey-youtube-live-024-K011`、`mikey-youtube-live-024-K012`、`mikey-youtube-live-029-K005`、`mikey-youtube-live-030-K013`、`mikey-youtube-live-030-K014`

**事件：**无

**原待核：**无

**处理：**原claim与原状态完整转存；综合中分别标明人物概括、观众经历、编辑边界，不第一人称化。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K022` → `mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-024-K011` → `mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### TI059 · unobserved_event_continuity

**发现：**136个事件的顺序和起止来自上传结构，observations均为空，review_status全部pending。

**知识：**无

**事件：**无

**原待核：**无

**核对细节：**{"events": 136, "empty_observations": 136}

**处理：**不把事件标题、story_order或静帧描述升级为连续行为、因果、身份或结果。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI060 · reuse_ledger_stage_difference

**发现：**复用账本最终10 unique，但部分content_precheck仍保留早期待核或剩余工作字样。

**知识：**无

**事件：**无

**原待核：**无

**核对细节：**{"final_result_counts_as_supplied": {"unique": 10, "reuse": 0, "suspected": 0}}

**处理：**保留最终账本结论及其边界，不推翻为重复，也不声称本次重跑排除所有局部复述。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI061 · sid_is_source_local

**发现：**同样的SID字符串可出现在不同来源；SID不能离开source_id独立匹配。

**知识：**无

**事件：**无

**原待核：**无

**处理：**所有新证据引用同时绑定source_id、knowledge_id、event_id、evidence_id和SID；禁止跨源SID碰撞。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
### TI062 · input_validator_scope

**发现：**附件validation passed只说明其报告范围内的结构和计数，不意味着以上语义、归属、时间窗与风险已解除。

**知识：**无

**事件：**无

**原待核：**无

**核对细节：**{"input_validation_report": {"status": "passed", "input": "D:\\startup\\玩家.skill\\research\\youtube-live-batch3\\youtube-live-batch3-cross-input.json", "source_count": 10, "segments": 16132, "events": 136, "knowledge": 153, "knowledge_quotes": 963, "review_needed": 63, "blocking_review_needed": 47, "major_review_needed": 16, "release_counts": {"direct": 85, "context_only": 28, "hold": 8, "candidate_only": 10, "do_not_generalize": 22}, "attribution_counts": {"explicit_mikey": 132, "mixed_speakers": 21}, "gameplay_counts": {"uncertain_overlap": 2014}}}

**处理：**本次分别报告机械引用检查PASS与内容待核OPEN，不把两者合并。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

无新增证据；依据相应原目录/元数据。。

</details>
## 12. 九类关键边界审计

### viewer_question_relay

**CB-viewer_question_relay-01 · 观众问题不是主持人经历。** 发声者、问题作者和案例当事人三者分开；事件级spoken_by不覆盖句级不明。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K006` → `mikey-youtube-live-023-E0002-R091` / `S00278`；`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-030-K007` → `mikey-youtube-live-030-E0003-R089` / `S00355`。

</details>
**CB-viewer_question_relay-02 · 提问片段不能作为回答的逐字支持。** 直播72拿号不回复条目的两段代表片段仍在观众提问层，完整判断暂hold。 结果：边界已保留，内容待核未解除。关联原review：无。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K006` → `mikey-youtube-live-023-E0002-R091` / `S00278`。

</details>
### gameplay_five_class_attribution

**CB-gameplay_five_class_attribution-01 · mikey_commentary。** 只有真实句级映射到Mikey本人评论的材料才可能支持其观点；还须通过release、待核和语义审查，不自动direct。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`。

**细节：**{"class_count": 0, "source_id": "mikey-youtube-live-022"}


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
**CB-gameplay_five_class_attribution-02 · game_dialogue_or_narration。** 只作播放材料或剧情内容；不得转写成Mikey经历、建议或赞同。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`。

**细节：**{"class_count": 0, "source_id": "mikey-youtube-live-022"}


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
**CB-gameplay_five_class_attribution-03 · viewer_chat_text。** 单独记录问题或观点；主持读出不等于背书。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`。

**细节：**{"class_count": 0, "source_id": "mikey-youtube-live-022"}


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
**CB-gameplay_five_class_attribution-04 · mikey_quote_or_reading。** 引用/朗读只证明其读出某内容，不能自动支持本人立场。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`。

**细节：**{"class_count": 0, "source_id": "mikey-youtube-live-022"}


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
**CB-gameplay_five_class_attribution-05 · uncertain_overlap。** 保持hold；原do_not_generalize继续DNG。多人、角色和未知声音不得静默归并。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`。

**细节：**{"class_count": 2014, "source_id": "mikey-youtube-live-022"}


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
### speaker_attribution

**CB-speaker_attribution-01 · 多人及未知嘉宾。** 面具、座位、频道和角色不能确定发声者；所有uncertain_overlap保持hold/DNG。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`。

</details>
**CB-speaker_attribution-02 · 电话集合占位。** caller-01不表示单一已知女性，跨次通话的身份连续性未知；句级说话人未分离。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`。

**细节：**{"phone_event_ids": ["mikey-youtube-live-029-E0007", "mikey-youtube-live-029-E0008", "mikey-youtube-live-029-E0009", "mikey-youtube-live-029-E0010", "mikey-youtube-live-029-E0011", "mikey-youtube-live-029-E0012", "mikey-youtube-live-029-E0014"]}


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`。

</details>
**CB-speaker_attribution-03 · 编辑安全句不冒充原话。** 保留原attribution_status与claim，但不能把其中的编辑“不能”写成人物一贯主张。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-023-R010`、`mikey-youtube-live-023-R011`、`mikey-youtube-live-024-R002`、`mikey-youtube-live-024-R003`、`mikey-youtube-live-024-R008`、`mikey-youtube-live-030-R002`、`mikey-youtube-live-030-R003`、`mikey-youtube-live-030-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K022` → `mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-024-K011` → `mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### refusals_stops_and_consent

**CB-refusals_stops_and_consent-01 · 邀请和持续同意分层。** 酒精、同意见面、到场、留下或不反抗不等于下一项行为同意。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-021-R008`、`mikey-youtube-live-024-R002`、`mikey-youtube-live-024-R003`、`mikey-youtube-live-028-R002`、`mikey-youtube-live-028-R004`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R002`、`mikey-youtube-live-030-R003`、`mikey-youtube-live-030-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K015` → `mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-024-K011` → `mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
**CB-refusals_stops_and_consent-02 · 电话中的拒绝与休息表达。** 直播82时间窗即使错位，拒绝证据仍须随事件和证据ID进入阻断，不写成推进方法。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`。

**细节：**{"existing_review_window_is_not_authority_to_exclude_refusal": true}


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-K011` → `mikey-youtube-live-029-E0006-R122` / `S00881`。

</details>
**CB-refusals_stops_and_consent-03 · 拉黑和退出。** 拉黑后换号不作为克服拒绝的练习；自我复盘与继续接触原对象分开。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-023-R012`、`mikey-youtube-live-024-R007`、`mikey-youtube-live-024-R008`、`mikey-youtube-live-024-R010`、`mikey-youtube-live-027-R003`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K024` → `mikey-youtube-live-023-E0014-R013` / `S01857`；`mikey-youtube-live-024-K016` → `mikey-youtube-live-024-E0010-R029` / `S01694`；`mikey-youtube-live-027-K007` → `mikey-youtube-live-027-E0008-R012` / `S00752`。

</details>
### age_power_and_relationship_status

**CB-age_power_and_relationship_status-01 · 未成年及职业权力。** 外校/非自己学生不能解除年龄和师生边界；不得默认校园对象成年。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-023-R010`、`mikey-youtube-live-023-R011`、`mikey-youtube-live-025-R001`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K022` → `mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-025-K001` → `mikey-youtube-live-025-E0001-R081` / `S00081`。

</details>
**CB-age_power_and_relationship_status-02 · 已有伴侣和单方约定。** 关系事实需明确；不生成剥削婚外关系或要求只有另一方守约的策略。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-023-R008`、`mikey-youtube-live-023-R009`、`mikey-youtube-live-026-R004`、`mikey-youtube-live-027-R001`、`mikey-youtube-live-027-R003`、`mikey-youtube-live-030-R001`、`mikey-youtube-live-030-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K019` → `mikey-youtube-live-023-E0010-R001` / `S01389`；`mikey-youtube-live-026-K008` → `mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-027-K012` → `mikey-youtube-live-027-E0007-R021` / `S00651`；`mikey-youtube-live-030-K010` → `mikey-youtube-live-030-E0001-R107` / `S00107`。

</details>
### law_privacy_and_filming

**CB-law_privacy_and_filming-01 · 人物法律判断不替代法律意见。** 普通搭讪与暴力的区分不对未核具体行为背书。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-021-R001`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K003` → `mikey-youtube-live-021-E0002-R099` / `S00147`。

</details>
**CB-law_privacy_and_filming-02 · 录音拍摄与公开分开授权。** 复盘练习、电话演示和聊天展示不自动获得记录或公开许可。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-025-R004`、`mikey-youtube-live-027-R002`、`mikey-youtube-live-027-R003`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-025-K007` → `mikey-youtube-live-025-E0004-R015` / `S00490`。

</details>
**CB-law_privacy_and_filming-03 · 欺骗转场与秘密用途。** 不能以降低摩擦、上传文件或示范教学的名义补写缺失授权。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-028-R002`、`mikey-youtube-live-028-R004`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-028-K012` → `mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`。

</details>
### medical_body_and_mental_health

**CB-medical_body_and_mental_health-01 · 医疗与非安全性行为。** 不将疾病、药物、避孕和风险断言转成执行建议；原音与专业证据均未补齐。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-021-R005`、`mikey-youtube-live-024-R002`、`mikey-youtube-live-024-R003`、`mikey-youtube-live-024-R008`、`mikey-youtube-live-026-R002`、`mikey-youtube-live-026-R003`、`mikey-youtube-live-026-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K012` → `mikey-youtube-live-021-E0006-R083` / `S00580`；`mikey-youtube-live-024-K012` → `mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-026-K006` → `mikey-youtube-live-026-E0007-R084` / `S00714`；`mikey-youtube-live-026-K007` → `mikey-youtube-live-026-E0003-R027` / `S00257`。

</details>
**CB-medical_body_and_mental_health-02 · 家庭、缺爱与心理原因。** 人物解释、观众主诉和编辑限制分层；不作创伤、遗传或人格诊断。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`、`mikey-youtube-live-024-R001`、`mikey-youtube-live-028-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-024-K005` → `mikey-youtube-live-024-E0003-R152` / `S00563`；`mikey-youtube-live-028-K009` → `mikey-youtube-live-028-E0013-R031` / `S01413`；`mikey-youtube-live-028-K010` → `mikey-youtube-live-028-E0013-R045` / `S01427`。

</details>
**CB-medical_body_and_mental_health-03 · 身体与年龄羞辱。** 不从外貌、体型或年龄推出人格、关系价值或医学结论。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-021-R009`、`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K019` → `mikey-youtube-live-021-E0012-R016` / `S01180`；`mikey-youtube-live-029-K012` → `mikey-youtube-live-029-E0001-R030` / `S00030`；`mikey-youtube-live-030-K014` → `mikey-youtube-live-030-E0009-R030` / `S00940`。

</details>
### numbers_success_rates_and_outcomes

**CB-numbers_success_rates_and_outcomes-01 · 成功率和课程配额。** 高百分比、三秒、固定周次数不共享分母和适用人群；不能合成统一练习标准。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-021-R002`、`mikey-youtube-live-021-R003`、`mikey-youtube-live-026-R004`、`mikey-youtube-live-028-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-026-K002` → `mikey-youtube-live-026-E0004-R082` / `S00412`；`mikey-youtube-live-028-K003` → `mikey-youtube-live-028-E0005-R049` / `S00499`。

</details>
**CB-numbers_success_rates_and_outcomes-02 · 收入和成长自述。** offer、经历和成长回顾只能按讲述层级保留，不是收益证明。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-021-R005`、`mikey-youtube-live-025-R002`、`mikey-youtube-live-030-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K010` → `mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-025-K005` → `mikey-youtube-live-025-E0002-R108` / `S00276`；`mikey-youtube-live-030-K012` → `mikey-youtube-live-030-E0013-R024` / `S01318`。

</details>
**CB-numbers_success_rates_and_outcomes-03 · 观众故事和结果。** 观众尝试数量不变成人物亲历，电话或号码不变成到场/亲密闭环。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-021-R002`、`mikey-youtube-live-021-R003`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-029-K005` → `mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-021-K004` → `mikey-youtube-live-021-E0003-R056` / `S00240`。

</details>
### screen_material_hard_cuts_and_replays

**CB-screen_material_hard_cuts_and_replays-01 · 事件目录不等于连续观看。** 136个事件保留原始起止和story_order；不建立未核硬切、重播前后或画外结果链。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-023-R001`、`mikey-youtube-live-023-R002`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-023-K001` → `mikey-youtube-live-023-E0001-R045` / `S00045`；`mikey-youtube-live-024-K007` → `mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-030-K011` → `mikey-youtube-live-030-E0007-R052` / `S00727`。

</details>
**CB-screen_material_hard_cuts_and_replays-02 · 动漫、电话和截图各自分层。** 角色立绘不是实际行为；通话界面不是身份或同意；截图文字不是现实结果。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`、`mikey-youtube-live-025-R004`、`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-022-K001` → `mikey-youtube-live-022-E0001-R051` / `S00051`；`mikey-youtube-live-022-K002` → `mikey-youtube-live-022-E0003-R001` / `S00201`；`mikey-youtube-live-022-K003` → `mikey-youtube-live-022-E0003-R101` / `S00301`；`mikey-youtube-live-022-K004` → `mikey-youtube-live-022-E0004-R101` / `S00451`；`mikey-youtube-live-022-K005` → `mikey-youtube-live-022-E0005-R041` / `S00501`；`mikey-youtube-live-022-K006` → `mikey-youtube-live-022-E0005-R091` / `S00551`；`mikey-youtube-live-022-K007` → `mikey-youtube-live-022-E0006-R031` / `S00601`；`mikey-youtube-live-022-K008` → `mikey-youtube-live-022-E0007-R051` / `S00751`；`mikey-youtube-live-022-K009` → `mikey-youtube-live-022-E0008-R001` / `S00851`；`mikey-youtube-live-022-K010` → `mikey-youtube-live-022-E0008-R101` / `S00951`；`mikey-youtube-live-022-K011` → `mikey-youtube-live-022-E0009-R081` / `S01101`；`mikey-youtube-live-022-K012` → `mikey-youtube-live-022-E0010-R001` / `S01151`；`mikey-youtube-live-022-K013` → `mikey-youtube-live-022-E0010-R101` / `S01251`；`mikey-youtube-live-022-K014` → `mikey-youtube-live-022-E0012-R011` / `S01451`；`mikey-youtube-live-022-K015` → `mikey-youtube-live-022-E0013-R051` / `S01651`；`mikey-youtube-live-022-K016` → `mikey-youtube-live-022-E0014-R041` / `S01801`；`mikey-youtube-live-022-K017` → `mikey-youtube-live-022-E0015-R071` / `S01951`；`mikey-youtube-live-022-K018` → `mikey-youtube-live-022-E0016-R021` / `S02001`；`mikey-youtube-live-025-K007` → `mikey-youtube-live-025-E0004-R015` / `S00490`；`mikey-youtube-live-029-K009` → `mikey-youtube-live-029-E0008-R008` / `S01014`。

</details>
**CB-screen_material_hard_cuts_and_replays-03 · 静帧不能证明嘴型、因果和持续同意。** 输入里先前的联系表描述只作原审核声明转存，本次没有图片文件或连续视频可查看。 结果：边界已保留，内容待核未解除。关联原review：`mikey-youtube-live-021-R001`、`mikey-youtube-live-027-R002`、`mikey-youtube-live-027-R003`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`、`mikey-youtube-live-030-R002`、`mikey-youtube-live-030-R003`、`mikey-youtube-live-030-R004`。


<details><summary>知识与精确证据定位（只作定位，不自动解除限制）</summary>

`mikey-youtube-live-021-K001` → `mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-027-K002` → `mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-029-K010` → `mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-030-K013` → `mikey-youtube-live-030-E0005-R020` / `S00465`。

</details>
## 13. 全量知识索引：153条，按原来源顺序各一项

每一项对应JSON中knowledge_index的一行；其他章节反复出现的ID只是交叉引用，不另计知识。下面同时呈现原状态、原概括、综合状态、限制原因和证据定位。原概括不等同逐句原话。

### 来源 `mikey-youtube-live-021` · 直播68

#### mikey-youtube-live-021-K001 · 长期吸引的一致性

**原问题与概括：**为什么短期能吸引、长期却维持不住？ 他把问题归因于人格和行为线索不一致：短时间可以表演有魅力，但压力或意外会暴露原有反应；训练路径不是永远表演，而是反复实践、失败、延长稳定时间，最终把强行为线索变成习惯。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T01` / `P01`、`P08`

**阻断review：**`mikey-youtube-live-021-R001`

**原未知项：**‘强/弱行为线索’是其理论术语

**原声明事件：**`mikey-youtube-live-021-E0001`、`mikey-youtube-live-021-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0001-R047` / `S00047`；`mikey-youtube-live-021-E0002-R001` / `S00049`；`mikey-youtube-live-021-E0002-R026` / `S00074`；`mikey-youtube-live-021-E0002-R047` / `S00095`；`mikey-youtube-live-021-E0002-R051` / `S00099`；`mikey-youtube-live-021-E0002-R061` / `S00109`；`mikey-youtube-live-021-E0002-R066` / `S00114`；`mikey-youtube-live-021-E0002-R070` / `S00118`；`mikey-youtube-live-021-E0002-R074` / `S00122`。

`mikey-youtube-live-021-E0001-R047` / `S00047`（293.31–295.31秒），自动稿记录为："你真是没有一致性,然后呢"。

`mikey-youtube-live-021-E0002-R001` / `S00049`（300.31–306.81秒），自动稿记录为："他在他在装有魅力,那么他肯定会露线"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K002 · 异地对象的投入判断

**原问题与概括：**网上认识的人在另一座城市，要不要直接放弃？ 他的判断不是见到异地就放弃，而是先看对方是否值得投入；若确实优秀，可以维持聊天并等双方旅行或工作产生真实见面机会。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T06` / `P15`

**阻断review：**`mikey-youtube-live-021-R001`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-021-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0002-R079` / `S00127`；`mikey-youtube-live-021-E0002-R080` / `S00128`；`mikey-youtube-live-021-E0002-R084` / `S00132`；`mikey-youtube-live-021-E0002-R087` / `S00135`；`mikey-youtube-live-021-E0002-R088` / `S00136`；`mikey-youtube-live-021-E0002-R091` / `S00139`。

`mikey-youtube-live-021-E0002-R079` / `S00127`（482.14–483.58秒），自动稿记录为："得看她有多优秀"。

`mikey-youtube-live-021-E0002-R080` / `S00128`（483.58–484.78秒），自动稿记录为："她如果真的很优秀的话"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K003 · 搭讪与暴力犯罪边界

**原问题与概括：**暴力事件会不会证明搭讪本身就是犯罪？ 他明确区分正常接触与暴力、胁迫：因被拒绝而伤害他人的行为在他看来是犯罪，不应与搭讪划等号；否则会让实践者把每次正常开口都误解成犯罪。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T14` / `P33`

**阻断review：**`mikey-youtube-live-021-R001`

**原未知项：**不构成法律意见

**原声明事件：**`mikey-youtube-live-021-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0002-R098` / `S00146`；`mikey-youtube-live-021-E0002-R099` / `S00147`；`mikey-youtube-live-021-E0002-R118` / `S00166`；`mikey-youtube-live-021-E0002-R119` / `S00167`；`mikey-youtube-live-021-E0002-R122` / `S00170`；`mikey-youtube-live-021-E0002-R125` / `S00173`；`mikey-youtube-live-021-E0002-R127` / `S00175`。

`mikey-youtube-live-021-E0002-R098` / `S00146`（518.84–520.8秒），自动稿记录为："他那个不叫搭讪者"。

`mikey-youtube-live-021-E0002-R099` / `S00147`（520.8–522.46秒），自动稿记录为："他呢就是一个强盗"。

原始引文计数为7；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K004 · 成功率优先于收号量

**原问题与概括：**衡量搭讪水平应该看收号数还是后续转化？ 他反对用大量收号作为主要成绩，更看重号码能否推进到见面和关系结果；但直播中的80%至100%数字及性结果均是本人自述，不能当作可复制基准。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T14`、`T15` / `P29`

**阻断review：**`mikey-youtube-live-021-R002`、`mikey-youtube-live-021-R003`

**原未知项：**成功率和样本均未独立核验

**原声明事件：**`mikey-youtube-live-021-E0003`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0003-R055` / `S00239`；`mikey-youtube-live-021-E0003-R056` / `S00240`；`mikey-youtube-live-021-E0003-R057` / `S00241`；`mikey-youtube-live-021-E0003-R059` / `S00243`；`mikey-youtube-live-021-E0003-R060` / `S00244`；`mikey-youtube-live-021-E0003-R070` / `S00254`；`mikey-youtube-live-021-E0003-R071` / `S00255`；`mikey-youtube-live-021-E0003-R072` / `S00256`。

`mikey-youtube-live-021-E0003-R055` / `S00239`（802.18–805.16秒），自动稿记录为："因为我在我的眼里"。

`mikey-youtube-live-021-E0003-R056` / `S00240`（805.16–807.24秒），自动稿记录为："我认为成功率是大于一切的"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K005 · 废号的全链路诊断

**原问题与概括：**为什么搭讪拿到号码后聊不起来甚至被删？ 他认为不能只怪聊天一句话，而要回看现场状态、穿搭形象、朋友圈和后续聊天整个链路；现场若显得像求对方加号的销售，会先形成负面画像。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `direct`。

**使用理由：**仅按逐期摘要转述：拿号后不回复时，应回看现场状态、穿搭呈现与后续链路；不能确定某位女性的真实动机或断言必是吸引不足。 仅有限间接观点转述，不是逐字引语、事实验证或正式skill接入。

**仅限direct范围：**仅按逐期摘要转述：拿号后不回复时，应回看现场状态、穿搭呈现与后续链路；不能确定某位女性的真实动机或断言必是吸引不足。

**主题 / 命题：**`T05` / `P12`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-021-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0004-R004` / `S00288`；`mikey-youtube-live-021-E0004-R008` / `S00292`；`mikey-youtube-live-021-E0004-R009` / `S00293`；`mikey-youtube-live-021-E0004-R010` / `S00294`；`mikey-youtube-live-021-E0004-R011` / `S00295`；`mikey-youtube-live-021-E0004-R012` / `S00296`；`mikey-youtube-live-021-E0004-R016` / `S00300`；`mikey-youtube-live-021-E0004-R035` / `S00319`；`mikey-youtube-live-021-E0004-R036` / `S00320`。

`mikey-youtube-live-021-E0004-R004` / `S00288`（909.4–911.2秒），自动稿记录为："你搭讪的时候你的状态肯定有问题"。

`mikey-youtube-live-021-E0004-R008` / `S00292`（916.56–919.16秒），自动稿记录为："你可能你的那个穿戴也有问题"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K006 · 初始吸引的形成

**原问题与概括：**初始吸引是怎么建立的？ 他把初始吸引解释为：对方先从一组强行为线索形成模糊画像和好奇，后续接触不断补充线索，画像才逐渐具体。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**代表片段仅到“留下…行为”的半句，尚不能独立支撑模糊画像、好奇与后续累积的完整机制。

**主题 / 命题：**`T01`、`T05` / `P03`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-021-E0004`

**本次追溯问题：**`TI028`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0004-R038` / `S00322`；`mikey-youtube-live-021-E0004-R039` / `S00323`；`mikey-youtube-live-021-E0004-R040` / `S00324`；`mikey-youtube-live-021-E0004-R041` / `S00325`；`mikey-youtube-live-021-E0004-R043` / `S00327`；`mikey-youtube-live-021-E0004-R045` / `S00329`；`mikey-youtube-live-021-E0004-R049` / `S00333`；`mikey-youtube-live-021-E0004-R052` / `S00336`。

`mikey-youtube-live-021-E0004-R038` / `S00322`（999.47–1001.13秒），自动稿记录为："初始吸引就是留下"。

`mikey-youtube-live-021-E0004-R039` / `S00323`（1001.13–1003.39秒），自动稿记录为："留下一定量的行为"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K007 · 去除销售式表达

**原问题与概括：**搭讪时怎样减少销售感？ 他的具体要求是抬头、放松、敢于眼神接触，并把语速明显放慢；工作是销售不代表下班约会还要保留销售角色，可以通过洗澡、更衣和状态切换把工作感放下。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04` / `P10`

**阻断review：**`mikey-youtube-live-021-R004`、`mikey-youtube-live-021-R005`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-021-E0005`、`mikey-youtube-live-021-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0005-R001` / `S00382`；`mikey-youtube-live-021-E0005-R003` / `S00384`；`mikey-youtube-live-021-E0005-R005` / `S00386`；`mikey-youtube-live-021-E0005-R007` / `S00388`；`mikey-youtube-live-021-E0005-R008` / `S00389`；`mikey-youtube-live-021-E0006-R001` / `S00498`；`mikey-youtube-live-021-E0006-R003` / `S00500`；`mikey-youtube-live-021-E0006-R006` / `S00503`；`mikey-youtube-live-021-E0006-R008` / `S00505`；`mikey-youtube-live-021-E0006-R010` / `S00507`。

`mikey-youtube-live-021-E0005-R001` / `S00382`（1203.14–1204.6秒），自动稿记录为："你说话的状态的时候"。

`mikey-youtube-live-021-E0005-R003` / `S00384`（1205.62–1208.22秒），自动稿记录为："然后不要害怕"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K008 · 外形特征的平衡

**原问题与概括：**长相太凶或太乖时怎么调整？ 他建议用造型做平衡：脸显凶可用长发、眼镜或减少全黑穿搭柔化；长相偏乖则可用配饰增加个性。核心不是套统一模板，而是补足自身视觉信号的另一面。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04` / `P10`

**阻断review：**`mikey-youtube-live-021-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-021-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0005-R011` / `S00392`；`mikey-youtube-live-021-E0005-R012` / `S00393`；`mikey-youtube-live-021-E0005-R013` / `S00394`；`mikey-youtube-live-021-E0005-R014` / `S00395`；`mikey-youtube-live-021-E0005-R015` / `S00396`；`mikey-youtube-live-021-E0005-R016` / `S00397`；`mikey-youtube-live-021-E0005-R017` / `S00398`；`mikey-youtube-live-021-E0005-R018` / `S00399`。

`mikey-youtube-live-021-E0005-R011` / `S00392`（1236.25–1240.25秒），自动稿记录为："想办法你把你的那个 你长相凶的话 你可以留长发"。

`mikey-youtube-live-021-E0005-R012` / `S00393`（1240.25–1245.25秒），自动稿记录为："然后呢 你把自己的就是外形进行一个融合一点吧"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K009 · 被放鸽子时设边界

**原问题与概括：**对方约好后临时去上网，应该怎么办？ 他主张当场指出对方违约，不能装作无所谓，让对方知道这种行为会有后果；原话使用‘骂她’，实际应用必须改成清楚、克制地表达不接受，不升级辱骂或威胁。

**原发布状态：** `hold`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**原hold未获解除。 关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07` / `P18`

**阻断review：**`mikey-youtube-live-021-R004`

**原未知项：**原表达有冲突升级风险

**原声明事件：**`mikey-youtube-live-021-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0005-R074` / `S00455`；`mikey-youtube-live-021-E0005-R075` / `S00456`；`mikey-youtube-live-021-E0005-R076` / `S00457`；`mikey-youtube-live-021-E0005-R077` / `S00458`；`mikey-youtube-live-021-E0005-R079` / `S00460`；`mikey-youtube-live-021-E0005-R082` / `S00463`；`mikey-youtube-live-021-E0005-R086` / `S00467`；`mikey-youtube-live-021-E0005-R088` / `S00469`；`mikey-youtube-live-021-E0005-R089` / `S00470`。

`mikey-youtube-live-021-E0005-R074` / `S00455`（1397.0–1397.68秒），自动稿记录为："直接放弃吗"。

`mikey-youtube-live-021-E0005-R075` / `S00456`（1397.68–1398.48秒），自动稿记录为："你直接骂他"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K010 · 投入做到极致

**原问题与概括：**为什么他认为自己换行业也可能成功？ 他把自己的优势描述为选择少数事情后高强度投入，并以画画和游戏建筑经历举例；可借鉴的是专注与持续练习，三个月拿职业offer等结果仅是本人自述。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03`、`T09`、`T15` / `P09`、`P29`

**阻断review：**`mikey-youtube-live-021-R005`

**原未知项：**经历和时间未独立核验

**原声明事件：**`mikey-youtube-live-021-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0006-R018` / `S00515`；`mikey-youtube-live-021-E0006-R019` / `S00516`；`mikey-youtube-live-021-E0006-R020` / `S00517`；`mikey-youtube-live-021-E0006-R021` / `S00518`；`mikey-youtube-live-021-E0006-R023` / `S00520`；`mikey-youtube-live-021-E0006-R025` / `S00522`；`mikey-youtube-live-021-E0006-R030` / `S00527`；`mikey-youtube-live-021-E0006-R031` / `S00528`；`mikey-youtube-live-021-E0006-R032` / `S00529`；`mikey-youtube-live-021-E0006-R033` / `S00530`。

`mikey-youtube-live-021-E0006-R018` / `S00515`（1533.02–1534.6秒），自动稿记录为："就是我要么不做一件事情"。

`mikey-youtube-live-021-E0006-R019` / `S00516`（1534.6–1535.58秒），自动稿记录为："我如果做这件事情"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K011 · 强行为线索不等于高能量

**原问题与概括：**约会一定要高能量才有吸引吗？ 他认为高能量和低能量都只是表面，关键是行为传递出的主体性；高昂但讨好的状态仍然是弱线索。所谓效率，就是更快、更清楚地传递强行为线索。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T01` / `P02`

**阻断review：**`mikey-youtube-live-021-R005`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-021-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0006-R055` / `S00552`；`mikey-youtube-live-021-E0006-R057` / `S00554`；`mikey-youtube-live-021-E0006-R058` / `S00555`；`mikey-youtube-live-021-E0006-R059` / `S00556`；`mikey-youtube-live-021-E0006-R060` / `S00557`；`mikey-youtube-live-021-E0006-R061` / `S00558`；`mikey-youtube-live-021-E0006-R066` / `S00563`；`mikey-youtube-live-021-E0006-R078` / `S00575`；`mikey-youtube-live-021-E0006-R079` / `S00576`。

`mikey-youtube-live-021-E0006-R055` / `S00552`（1644.82–1645.96秒），自动稿记录为："是强行为线索"。

`mikey-youtube-live-021-E0006-R057` / `S00554`（1647.42–1648.78秒），自动稿记录为："不管你高能量还是低能量"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K012 · 皮肤问题先就医

**原问题与概括：**痘痘很久不好应该先买产品还是看医生？ 他的实际建议是停止乱试宣传产品，先去正规医院处理；但‘三天就好’和所有外用产品含激素等绝对判断没有医学核验，不能照搬。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T12` / `P28`

**阻断review：**`mikey-youtube-live-021-R005`

**原未知项：**涉及医疗，具体诊疗听从合格医生

**原声明事件：**`mikey-youtube-live-021-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0006-R082` / `S00579`；`mikey-youtube-live-021-E0006-R083` / `S00580`；`mikey-youtube-live-021-E0006-R086` / `S00583`；`mikey-youtube-live-021-E0006-R087` / `S00584`；`mikey-youtube-live-021-E0006-R095` / `S00592`；`mikey-youtube-live-021-E0006-R099` / `S00596`；`mikey-youtube-live-021-E0006-R100` / `S00597`；`mikey-youtube-live-021-E0006-R101` / `S00598`。

`mikey-youtube-live-021-E0006-R082` / `S00579`（1713.76–1714.54秒），自动稿记录为："你去医院就行了"。

`mikey-youtube-live-021-E0006-R083` / `S00580`（1714.54–1716.42秒），自动稿记录为："我这边教你没有用"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K013 · 课程消费边界

**原问题与概括：**可以贷款报名他的线下课吗？ 他明确劝阻贷款报名，要求先解决经济问题、好好赚钱。这是少数清楚的消费边界表达。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T09` / `P09`

**阻断review：**`mikey-youtube-live-021-R006`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-021-E0007`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0007-R036` / `S00658`；`mikey-youtube-live-021-E0007-R037` / `S00659`；`mikey-youtube-live-021-E0007-R038` / `S00660`；`mikey-youtube-live-021-E0007-R039` / `S00661`。

`mikey-youtube-live-021-E0007-R036` / `S00658`（1886.75–1899.66秒），自动稿记录为："麦哥我准备贷款报你线下课"。

`mikey-youtube-live-021-E0007-R037` / `S00659`（1899.66–1901.02秒），自动稿记录为："你贷款的话就不要报了"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K014 · 网络舆论与现实样本

**原问题与概括：**网上看见大量性别对立内容，是否代表现实中的人都这样？ 他提醒不要把平台推送当成现实比例：线上极端内容会被集中呈现，现实接触中的样本可能完全不同；被舆论制造的焦虑带进约会，会直接增加压力。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T13` / `P22`

**阻断review：**`mikey-youtube-live-021-R007`、`mikey-youtube-live-021-R008`

**原未知项：**平台推送动机为其推测

**原声明事件：**`mikey-youtube-live-021-E0009`、`mikey-youtube-live-021-E0010`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0009-R060` / `S00941`；`mikey-youtube-live-021-E0009-R064` / `S00945`；`mikey-youtube-live-021-E0009-R069` / `S00950`；`mikey-youtube-live-021-E0009-R070` / `S00951`；`mikey-youtube-live-021-E0010-R001` / `S00961`；`mikey-youtube-live-021-E0010-R003` / `S00963`；`mikey-youtube-live-021-E0010-R006` / `S00966`；`mikey-youtube-live-021-E0010-R015` / `S00975`；`mikey-youtube-live-021-E0010-R018` / `S00978`；`mikey-youtube-live-021-E0010-R021` / `S00981`；`mikey-youtube-live-021-E0010-R023` / `S00983`。

`mikey-youtube-live-021-E0009-R060` / `S00941`（2640.51–2644.23秒），自动稿记录为："我的账号每天都有很多兄弟在私信说"。

`mikey-youtube-live-021-E0009-R064` / `S00945`（2649.05–2653.88秒），自动稿记录为："因为因为那个我每天都看小红书"。

原始引文计数为11；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K015 · 给模糊邀约设置时间边界

**原问题与概括：**对方说喝完酒再来但不给时间，怎么处理？ 他的做法是给出自己的可用时间并说明过晚就休息，不无限等待；保留自己的作息比追问和催促更有主体性。涉及饮酒和私密空间时仍必须重新确认清醒、持续同意。

**原发布状态：** `hold`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**原hold未获解除。 关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T06`、`T07`、`T14` / `P15`、`P25`

**阻断review：**`mikey-youtube-live-021-R008`

**原未知项：**饮酒后同意能力和来访安全未在直播中展开

**原声明事件：**`mikey-youtube-live-021-E0010`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0010-R039` / `S00999`；`mikey-youtube-live-021-E0010-R041` / `S01001`；`mikey-youtube-live-021-E0010-R042` / `S01002`；`mikey-youtube-live-021-E0010-R044` / `S01004`；`mikey-youtube-live-021-E0010-R046` / `S01006`；`mikey-youtube-live-021-E0010-R047` / `S01007`；`mikey-youtube-live-021-E0010-R048` / `S01008`；`mikey-youtube-live-021-E0010-R056` / `S01016`。

`mikey-youtube-live-021-E0010-R039` / `S00999`（2840.0–2841.74秒），自动稿记录为："她说她喝完酒了来找我"。

`mikey-youtube-live-021-E0010-R041` / `S01001`（2844.5–2845.98秒），自动稿记录为："然后我问她几点来"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K016 · 避免因一个标签否定整个人

**原问题与概括：**发现女生有一点女权倾向，就该直接淘汰吗？ 尽管他对极端女权有强烈批评，但此处又明确区分一时情绪、隐藏倾向与公开极端立场，反对因为一个倾向就把人一杆子打死。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T13` / `P22`

**阻断review：**`mikey-youtube-live-021-R008`

**原未知项：**仍包含对群体和动机的未经核验推断

**原声明事件：**`mikey-youtube-live-021-E0010`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0010-R069` / `S01029`；`mikey-youtube-live-021-E0010-R071` / `S01031`；`mikey-youtube-live-021-E0010-R074` / `S01034`；`mikey-youtube-live-021-E0010-R077` / `S01037`；`mikey-youtube-live-021-E0010-R080` / `S01040`；`mikey-youtube-live-021-E0010-R086` / `S01046`；`mikey-youtube-live-021-E0010-R088` / `S01048`；`mikey-youtube-live-021-E0010-R091` / `S01051`；`mikey-youtube-live-021-E0010-R093` / `S01053`；`mikey-youtube-live-021-E0010-R105` / `S01065`；`mikey-youtube-live-021-E0010-R107` / `S01067`。

`mikey-youtube-live-021-E0010-R069` / `S01029`（2904.05–2905.71秒），自动稿记录为："那人呢"。

`mikey-youtube-live-021-E0010-R071` / `S01031`（2906.91–2907.97秒），自动稿记录为："都是带有点恶的"。

原始引文计数为11；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K017 · 从聊天转到见面

**原问题与概括：**线上聊到什么程度才适合邀约？ 他不设固定聊多久的门槛；双方已经知道彼此是谁、基本做什么，并且当下都有空，就可以提出见面，核心是完成最低限度熟悉而非把所有话题在线上聊完。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T06` / `P15`

**阻断review：**`mikey-youtube-live-021-R009`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-021-E0011`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0011-R021` / `S01103`；`mikey-youtube-live-021-E0011-R022` / `S01104`；`mikey-youtube-live-021-E0011-R023` / `S01105`；`mikey-youtube-live-021-E0011-R024` / `S01106`；`mikey-youtube-live-021-E0011-R025` / `S01107`；`mikey-youtube-live-021-E0011-R026` / `S01108`；`mikey-youtube-live-021-E0011-R027` / `S01109`；`mikey-youtube-live-021-E0011-R028` / `S01110`；`mikey-youtube-live-021-E0011-R032` / `S01114`。

`mikey-youtube-live-021-E0011-R021` / `S01103`（3066.86–3068.36秒），自动稿记录为："应该保持怎样的状态"。

`mikey-youtube-live-021-E0011-R022` / `S01104`（3068.36–3071.06秒），自动稿记录为："再和女生聊到什么程度"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K018 · 面试与约会的评价机制

**原问题与概括：**面试和约会的本质一样吗？ 他反对简单类比：面试主要看可验证的业务能力和数据，约会更多依赖互动中的感觉与状态。两者都可能涉及表现，但评价依据不同。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04` / `P10`

**阻断review：**`mikey-youtube-live-021-R009`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-021-E0011`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0011-R038` / `S01120`；`mikey-youtube-live-021-E0011-R040` / `S01122`；`mikey-youtube-live-021-E0011-R041` / `S01123`；`mikey-youtube-live-021-E0011-R042` / `S01124`；`mikey-youtube-live-021-E0011-R045` / `S01127`；`mikey-youtube-live-021-E0011-R046` / `S01128`；`mikey-youtube-live-021-E0011-R047` / `S01129`；`mikey-youtube-live-021-E0011-R048` / `S01130`；`mikey-youtube-live-021-E0011-R049` / `S01131`；`mikey-youtube-live-021-E0011-R051` / `S01133`。

`mikey-youtube-live-021-E0011-R038` / `S01120`（3093.01–3108.18秒），自动稿记录为："麦哥面试的本质和约会类似吗"。

`mikey-youtube-live-021-E0011-R040` / `S01122`（3109.72–3112.74秒），自动稿记录为："面试的本质和约会的本质是不一样的"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-021-K019 · 男性外形成熟后的维护

**原问题与概括：**男生颜值能维持到多少岁？ 他不给固定年龄，认为精神压力、身体状态、运动、发型等都影响外观；可操作部分是减少长期焦虑、保持运动并找到适合自己的发型。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04`、`T12` / `P10`、`P28`

**阻断review：**`mikey-youtube-live-021-R009`

**原未知项：**‘长期焦虑会变丑’为经验性表达

**原声明事件：**`mikey-youtube-live-021-E0012`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-021-E0012-R015` / `S01179`；`mikey-youtube-live-021-E0012-R016` / `S01180`；`mikey-youtube-live-021-E0012-R017` / `S01181`；`mikey-youtube-live-021-E0012-R018` / `S01182`；`mikey-youtube-live-021-E0012-R020` / `S01184`；`mikey-youtube-live-021-E0012-R021` / `S01185`；`mikey-youtube-live-021-E0012-R023` / `S01187`；`mikey-youtube-live-021-E0012-R040` / `S01204`；`mikey-youtube-live-021-E0012-R041` / `S01205`。

`mikey-youtube-live-021-E0012-R015` / `S01179`（3369.9–3383.27秒），自动稿记录为："男生的颜值是能维持到多少岁"。

`mikey-youtube-live-021-E0012-R016` / `S01180`（3383.27–3384.59秒），自动稿记录为："看你的状态的"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

### 来源 `mikey-youtube-live-022` · 直播70

#### mikey-youtube-live-022-K001 · 评价框架

**原问题与概括：**能力强就一定有异性吸引力吗？ 本期讨论先把战斗力和异性吸引力分开：能力、外形、身份、情绪状态和相处体验需要分别判断。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0001`

**本次追溯问题：**`TI044`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0001-R051` / `S00051`。

`mikey-youtube-live-022-E0001-R051` / `S00051`（154.91–156.17秒），自动稿记录为："最后就拉"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K002 · 神秘感

**原问题与概括：**为什么神秘感有时会产生吸引？ 讨论以卡卡西的面罩为例，把对方仍想继续了解的未知感视为吸引的一部分；这只是角色类比，不能证明刻意隐瞒必然有效。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0003`

**本次追溯问题：**`TI045`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0003-R001` / `S00201`。

`mikey-youtube-live-022-E0003-R001` / `S00201`（672.88–675.88秒），自动稿记录为："那你觉得卡尔西应该评什么集"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K003 · 稳定感

**原问题与概括：**稳定和可靠为什么会影响吸引？ 讨论把‘有他兜底就不慌’当作稳定感的例子，说明吸引不仅是刺激，也包括对方是否让人感到局面可控。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0003`

**本次追溯问题：**`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0003-R101` / `S00301`。

`mikey-youtube-live-022-E0003-R101` / `S00301`（908.0–910.32秒），自动稿记录为："你感觉有他兜底你是不慌的"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K004 · 领导力

**原问题与概括：**领袖魅力靠什么形成？ 讨论把表达、经历和被群体认可放在领袖魅力中，但也用了邪教类比；群体追随本身不能证明一个人健康或值得模仿。

**原发布状态：** `hold`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原hold未获解除。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0004`

**本次追溯问题：**`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0004-R101` / `S00451`。

`mikey-youtube-live-022-E0004-R101` / `S00451`（1284.34–1286.18秒），自动稿记录为："而且佩恩有领袖魅力"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K005 · 不吃反应

**原问题与概括：**不被负反馈带着走是什么意思？ 讨论把不因对方一时反应就失去自身方向视为一种稳定；具体说法混合动漫评价，仍需确认说话人和现实适用边界。

**原发布状态：** `hold`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原hold未获解除。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0005`

**本次追溯问题：**`TI046`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0005-R041` / `S00501`。

`mikey-youtube-live-022-E0005-R041` / `S00501`（1454.41–1456.95秒），自动稿记录为："她就是为了那个撑你的任务"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K006 · 操纵边界

**原问题与概括：**能不能靠改变意识或精神控制推进性关系？ 本期出现用能力迫使女性自我说服并接受性交的玩笑式讨论。这不是可采用的方法，不能转成Mikey第一人称建议。

**原发布状态：** `do_not_generalize`；**原归属：** `mixed_speakers`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R002`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0005`

**本次追溯问题：**`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0005-R091` / `S00551`。

`mikey-youtube-live-022-E0005-R091` / `S00551`（1583.17–1585.61秒），自动稿记录为："他直接来个别天神 那女的在那边反思了"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K007 · 缺爱

**原问题与概括：**缺爱会怎样影响一个人的关系表现？ 讨论把强烈缺爱与难以自然建立关系联系起来，但这是对动漫角色的概括，不能直接诊断现实中的人。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0006`

**本次追溯问题：**`TI047`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0006-R031` / `S00601`。

`mikey-youtube-live-022-E0006-R031` / `S00601`（1721.79–1723.59秒），自动稿记录为："然后我现在的徒弟在牛逼"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K008 · 主体性

**原问题与概括：**为什么过度被别人反应牵动会削弱吸引？ 讨论批评角色不断被他人刺激、缺少自我方向，提示主体性来自自己的目标与选择，而不是只对外界做反应。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0007`

**本次追溯问题：**`TI048`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0007-R051` / `S00751`。

`mikey-youtube-live-022-E0007-R051` / `S00751`（2201.63–2213.21秒），自动稿记录为："钥匙都上人了 佐柱我觉得不配影集"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K009 · 关系边界

**原问题与概括：**明确不给承诺是否等于高吸引？ 讨论把提前说明不谈关系与边界清晰联系起来，但不承诺不自动等于吸引，也不能替代诚实、同意和尊重。

**原发布状态：** `hold`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原hold未获解除。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0007`

**本次追溯问题：**`TI004`、`TI049`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0008-R001` / `S00851`。

`mikey-youtube-live-022-E0008-R001` / `S00851`（2509.02–2509.72秒），自动稿记录为："然后做不到"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K010 · 一致性

**原问题与概括：**目标感为什么比表演出来的强势更重要？ 讨论赞赏鸣人真正相信自己的价值体系且长期一致，认为稳定的信念和目标感比临时摆姿态更有力量。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0008`

**本次追溯问题：**`TI050`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0008-R101` / `S00951`。

`mikey-youtube-live-022-E0008-R101` / `S00951`（2748.44–2749.24秒），自动稿记录为："卧槽"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K011 · 精神控制

**原问题与概括：**通过洗脑和精神控制获得关系可行吗？ 本期将某角色描述为通过洗脑和精神控制影响他人。这是危险类比，不得当成两性方法。

**原发布状态：** `do_not_generalize`；**原归属：** `mixed_speakers`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R003`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0009`

**本次追溯问题：**`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0009-R081` / `S01101`。

`mikey-youtube-live-022-E0009-R081` / `S01101`（3161.76–3163.76秒），自动稿记录为："他簡直就是邪教領袖那種"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K012 · 降低摩擦

**原问题与概括：**安排更便利会不会提高邀约成功率？ 讨论以瞬间移动夸张说明：减少交通和次日安排的摩擦，可能让共同计划更容易执行；前提仍是对方自愿，而不是把便利当成同意。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0010`

**本次追溯问题：**`TI051`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0010-R001` / `S01151`。

`mikey-youtube-live-022-E0010-R001` / `S01151`（3288.02–3291.02秒），自动稿记录为："结果的妈的女人都已经受尾了"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K013 · 综合能力

**原问题与概括：**单项突出和整体吸引有什么区别？ 讨论把斑称为‘六边形战士’，强调外形、身份、能力和性格等多个维度共同作用；这是角色评价框架，不是现实评分公式。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0010`

**本次追溯问题：**`TI052`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0010-R101` / `S01251`。

`mikey-youtube-live-022-E0010-R101` / `S01251`（3558.69–3560.69秒），自动稿记录为："他们的某些特质是有点too much"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K014 · 金钱与酒精

**原问题与概括：**能不能靠喝酒和给钱推进关系？ 本期出现包KTV、喝酒后询问缺钱并给钱的情节设想。酒精、金钱和性推进混合会损害自由同意，不得作为方法。

**原发布状态：** `do_not_generalize`；**原归属：** `mixed_speakers`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R004`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0012`

**本次追溯问题：**`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0012-R011` / `S01451`。

`mikey-youtube-live-022-E0012-R011` / `S01451`（4185.6–4187.0秒），自动稿记录为："尤其在成都"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K015 · 真实性

**原问题与概括：**没有需求感和真实自我是什么关系？ 讨论借路飞说明：一个人不为了从异性获得回馈而扭曲自己时，更容易显得自然；这不等于对他人需求毫不关心。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0013`

**本次追溯问题：**`TI053`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0013-R051` / `S01651`。

`mikey-youtube-live-022-E0013-R051` / `S01651`（4808.98–4810.02秒），自动稿记录为："我觉得他不容易"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K016 · 模仿边界

**原问题与概括：**模仿有魅力的人能不能变得有魅力？ 讨论认为擅长表演的人可以复制外在样子，但模仿能力不等于形成真实、自洽且长期稳定的个人状态。

**原发布状态：** `candidate_only`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原candidate_only不升级；跨期索引无candidate_only枚举，运行时映射为hold。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0014`

**本次追溯问题：**`TI054`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0014-R041` / `S01801`。

`mikey-youtube-live-022-E0014-R041` / `S01801`（5224.31–5226.31秒），自动稿记录为："他其实还行"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K017 · 人格魅力

**原问题与概括：**所谓阳性能量在本期指什么？ 讨论用柱间和斑的阴阳对照描述人格魅力，侧重热情、带动感与坚定；这是动漫隐喻，含义需要结合其他真实材料确认。

**原发布状态：** `hold`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原hold未获解除。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 动漫排名或零散半句不足以独立支持完整心理、关系或方法解释；同时全部SID均为uncertain_overlap。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0015`

**本次追溯问题：**`TI055`、`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0015-R071` / `S01951`。

`mikey-youtube-live-022-E0015-R071` / `S01951`（5746.88–5747.88秒），自动稿记录为："其实我觉得"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-022-K018 · 权力操纵

**原问题与概括：**阴暗和强控制能不能形成健康吸引？ 结尾用团藏类比强权和阴暗控制。权力造成的服从不能等同于健康吸引，也不能用于现实操纵。

**原发布状态：** `do_not_generalize`；**原归属：** `mixed_speakers`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T10` / `P23`

**阻断review：**`mikey-youtube-live-022-R001`、`mikey-youtube-live-022-R005`

**原未知项：**多人讨论中无法仅凭自动稿确认这句话是否由Mikey提出；只可作为本期讨论线索

**原声明事件：**`mikey-youtube-live-022-E0016`

**本次追溯问题：**`TI057`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-022-E0016-R021` / `S02001`。

`mikey-youtube-live-022-E0016-R021` / `S02001`（5948.51–5957.02秒），自动稿记录为："我们得假设我们不知道他那些东西的情况下"。

原始引文计数为1；本条只附1条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

### 来源 `mikey-youtube-live-023` · 直播72

#### mikey-youtube-live-023-K001 · 案例与底层

**原问题与概括：**为什么不同案例看起来不一样？ Mikey说案例表面策略会随对象变化，但反复出现的底层仍是他所谓的‘强行为线索’；不必把每个案例当成一套全新理论。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T01`、`T15` / `P03`

**阻断review：**`mikey-youtube-live-023-R001`、`mikey-youtube-live-023-R002`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0001`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0001-R028` / `S00028`；`mikey-youtube-live-023-E0001-R045` / `S00045`；`mikey-youtube-live-023-E0001-R047` / `S00047`；`mikey-youtube-live-023-E0001-R048` / `S00048`。

`mikey-youtube-live-023-E0001-R028` / `S00028`（155.09–166.5秒），自动稿记录为："不是每一个案例"。

`mikey-youtube-live-023-E0001-R045` / `S00045`（190.32–192.52秒），自动稿记录为："你会发现其实讲完讲去就那么点东西"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K002 · 搭讪焦虑

**原问题与概括：**被拒绝为什么会让人瘫住？ 他把焦虑的一部分归因于低自我价值和把一次拒绝理解为整个人格被否定；陌生人并不了解你的经历，一次拒绝最多反映当下呈现、误解或不匹配。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02` / `P04`

**阻断review：**`mikey-youtube-live-023-R001`、`mikey-youtube-live-023-R002`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0001`、`mikey-youtube-live-023-E0002`

**本次追溯问题：**`TI005`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0001-R066` / `S00066`；`mikey-youtube-live-023-E0001-R068` / `S00068`；`mikey-youtube-live-023-E0001-R092` / `S00092`；`mikey-youtube-live-023-E0001-R101` / `S00101`；`mikey-youtube-live-023-E0001-R113` / `S00113`；`mikey-youtube-live-023-E0001-R114` / `S00114`；`mikey-youtube-live-023-E0002-R140` / `S00327`；`mikey-youtube-live-023-E0003-R001` / `S00329`；`mikey-youtube-live-023-E0003-R002` / `S00330`。

`mikey-youtube-live-023-E0001-R066` / `S00066`（245.26–248.82秒），自动稿记录为："因为那个时候我认为搭讪是在骚扰别人"。

`mikey-youtube-live-023-E0001-R068` / `S00068`（251.2–253.48秒），自动稿记录为："因为我那个时候我觉得我自己没有价值"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K003 · 人生重心

**原问题与概括：**为什么不能把所有提升都围绕女性认可？ 如果买车、赚钱、运动都只为了被女性喜欢，人生会空虚，得到的也可能只是条件吸引；先确认这些选择是否也是自己真正想要的。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02`、`T09` / `P09`

**阻断review：**`mikey-youtube-live-023-R001`、`mikey-youtube-live-023-R002`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0001`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0001-R127` / `S00127`；`mikey-youtube-live-023-E0001-R134` / `S00134`；`mikey-youtube-live-023-E0001-R137` / `S00137`；`mikey-youtube-live-023-E0001-R138` / `S00138`；`mikey-youtube-live-023-E0001-R142` / `S00142`；`mikey-youtube-live-023-E0001-R146` / `S00146`；`mikey-youtube-live-023-E0001-R150` / `S00150`；`mikey-youtube-live-023-E0001-R152` / `S00152`。

`mikey-youtube-live-023-E0001-R127` / `S00127`（369.34–371.46秒），自动稿记录为："你做什么事情都是为了女人而做的"。

`mikey-youtube-live-023-E0001-R134` / `S00134`（382.36–384.38秒），自动稿记录为："你买车不是因为你喜欢车"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K004 · 理论与实践

**原问题与概括：**为什么听得越多反而越不会？ 不同体系都能自洽，全部混在一起会让判断互相打架；保留足够的基础理论，然后用实践反馈修正。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联4项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P07`

**阻断review：**`mikey-youtube-live-023-R001`、`mikey-youtube-live-023-R002`、`mikey-youtube-live-023-R005`、`mikey-youtube-live-023-R006`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0001`、`mikey-youtube-live-023-E0004`、`mikey-youtube-live-023-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0001-R161` / `S00161`；`mikey-youtube-live-023-E0001-R162` / `S00162`；`mikey-youtube-live-023-E0001-R163` / `S00163`；`mikey-youtube-live-023-E0001-R166` / `S00166`；`mikey-youtube-live-023-E0001-R173` / `S00173`；`mikey-youtube-live-023-E0001-R185` / `S00185`；`mikey-youtube-live-023-E0001-R187` / `S00187`；`mikey-youtube-live-023-E0004-R169` / `S00637`；`mikey-youtube-live-023-E0004-R170` / `S00638`；`mikey-youtube-live-023-E0006-R064` / `S00912`；`mikey-youtube-live-023-E0006-R067` / `S00915`。

`mikey-youtube-live-023-E0001-R161` / `S00161`（465.89–469.89秒），自动稿记录为："少听点理论啊,对不对,少听点理论啊"。

`mikey-youtube-live-023-E0001-R162` / `S00162`（469.89–475.66秒），自动稿记录为："我发现学不会的人都是理论听太多了,天天听理论,这个导师"。

原始引文计数为11；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K005 · 维持吸引

**原问题与概括：**约好下次见后怎样避免掉吸引？ 他的重点不是继续加码表演，而是少暴露强需求感、保留自我和退出能力；有了初步吸引后，用个性样本与朋友圈补充真实生活，并避免明显犯错。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `direct`。

**使用理由：**仅保留避免继续加码表演和强需求感的观点；不得解释为刻意冷落、惩罚或制造不安。 仅有限间接观点转述，不是逐字引语、事实验证或正式skill接入。

**仅限direct范围：**仅保留避免继续加码表演和强需求感的观点；不得解释为刻意冷落、惩罚或制造不安。

**主题 / 命题：**`T01` / `P01`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0002-R004` / `S00191`；`mikey-youtube-live-023-E0002-R005` / `S00192`；`mikey-youtube-live-023-E0002-R008` / `S00195`；`mikey-youtube-live-023-E0002-R098` / `S00285`；`mikey-youtube-live-023-E0002-R110` / `S00297`；`mikey-youtube-live-023-E0002-R111` / `S00298`；`mikey-youtube-live-023-E0002-R113` / `S00300`；`mikey-youtube-live-023-E0002-R114` / `S00301`。

`mikey-youtube-live-023-E0002-R004` / `S00191`（546.67–547.53秒），自动稿记录为："不出幺蛾子"。

`mikey-youtube-live-023-E0002-R005` / `S00192`（547.53–549.77秒），自动稿记录为："你不要暴露很强的需求感就行了"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K006 · 拿号后不回复

**原问题与概括：**为什么现场聊得还行，回来却不回复？ 给号码不等于形成吸引；Mikey判断这种情况通常是现场没有建立足够吸引，后续要回看现场状态、个性样本和互动，而不是只统计拿号。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**两条代表片段均为观众陈述拿号后不回复，未附对应回答原文；不能把提问直接用作Mikey的因果判断。

**主题 / 命题：**`T05` / `P12`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0002`

**本次追溯问题：**`TI029`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0002-R088` / `S00275`；`mikey-youtube-live-023-E0002-R091` / `S00278`；`mikey-youtube-live-023-E0002-R093` / `S00280`；`mikey-youtube-live-023-E0002-R094` / `S00281`。

`mikey-youtube-live-023-E0002-R088` / `S00275`（730.69–734.07秒），自动稿记录为："Mikey我这段时间出去搭讪"。

`mikey-youtube-live-023-E0002-R091` / `S00278`（737.03–739.27秒），自动稿记录为："但回来发信息都不回"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K007 · 忙与邀约

**原问题与概括：**对方一直说工作忙，怎样判断？ 先直接问她是真忙还是不想见；若是真忙，让她给一个具体可行时间。一直不给时间就是行动反馈，应停止无止境聊天和追问。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `direct`。

**使用理由：**仅保留询问对方是否愿意见面以及可行时间的澄清顺序；不给时间只用于停止无限追问，不作人格或动机裁判。 仅有限间接观点转述，不是逐字引语、事实验证或正式skill接入。

**仅限direct范围：**仅保留询问对方是否愿意见面以及可行时间的澄清顺序；不给时间只用于停止无限追问，不作人格或动机裁判。

**主题 / 命题：**`T06` / `P15`

**阻断review：**无

**原未知项：**原话带有确定预测，实际不能保证对方一定给时间

**原声明事件：**`mikey-youtube-live-023-E0003`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0003-R005` / `S00333`；`mikey-youtube-live-023-E0003-R006` / `S00334`；`mikey-youtube-live-023-E0003-R007` / `S00335`；`mikey-youtube-live-023-E0003-R008` / `S00336`；`mikey-youtube-live-023-E0003-R028` / `S00356`；`mikey-youtube-live-023-E0003-R033` / `S00361`；`mikey-youtube-live-023-E0003-R034` / `S00362`；`mikey-youtube-live-023-E0003-R037` / `S00365`；`mikey-youtube-live-023-E0003-R038` / `S00366`；`mikey-youtube-live-023-E0003-R039` / `S00367`。

`mikey-youtube-live-023-E0003-R005` / `S00333`（919.69–921.69秒），自动稿记录为："你直接问他 你是真的没空呢"。

`mikey-youtube-live-023-E0003-R006` / `S00334`（921.69–922.69秒），自动稿记录为："还是不想跟我见面"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K008 · 旁观压力

**原问题与概括：**怎样减少对路人眼光的在意？ 把注意力拉回自己的第一人称体验和当下动作，不要一直从想象中的旁观者视角审判自己；NPC只是心理比喻，现实中的人仍有边界和主体性。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02` / `P04`、`P30`

**阻断review：**`mikey-youtube-live-023-R004`、`mikey-youtube-live-023-R011`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0003`、`mikey-youtube-live-023-E0012`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0003-R056` / `S00384`；`mikey-youtube-live-023-E0003-R060` / `S00388`；`mikey-youtube-live-023-E0003-R062` / `S00390`；`mikey-youtube-live-023-E0003-R069` / `S00397`；`mikey-youtube-live-023-E0003-R073` / `S00401`；`mikey-youtube-live-023-E0012-R018` / `S01625`；`mikey-youtube-live-023-E0012-R020` / `S01627`；`mikey-youtube-live-023-E0012-R024` / `S01631`；`mikey-youtube-live-023-E0012-R025` / `S01632`。

`mikey-youtube-live-023-E0003-R056` / `S00384`（1028.78–1032.12秒），自动稿记录为："你是第一人称视角的"。

`mikey-youtube-live-023-E0003-R060` / `S00388`（1038.34–1040.18秒），自动稿记录为："因为你们是以一个第三人称视角"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K009 · 话术与能力

**原问题与概括：**话术应该占什么位置？ 话术可以给新手临时支撑，但目标是成为能够自然说出合适话的人。聊天能力来自词汇、生活见识和大量真实互动，不能靠收藏句子替代。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `direct`。

**使用理由：**仅保留话术可作临时支撑、不能等同表达能力的逐期观点；不据此声称任何练习方案已有效或卖课必要。 仅有限间接观点转述，不是逐字引语、事实验证或正式skill接入。

**仅限direct范围：**仅保留话术可作临时支撑、不能等同表达能力的逐期观点；不据此声称任何练习方案已有效或卖课必要。

**主题 / 命题：**`T03` / `P07`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0004-R001` / `S00469`；`mikey-youtube-live-023-E0004-R005` / `S00473`；`mikey-youtube-live-023-E0004-R007` / `S00475`；`mikey-youtube-live-023-E0004-R008` / `S00476`；`mikey-youtube-live-023-E0004-R009` / `S00477`；`mikey-youtube-live-023-E0004-R133` / `S00601`；`mikey-youtube-live-023-E0004-R134` / `S00602`；`mikey-youtube-live-023-E0004-R137` / `S00605`；`mikey-youtube-live-023-E0004-R158` / `S00626`；`mikey-youtube-live-023-E0004-R169` / `S00637`。

`mikey-youtube-live-023-E0004-R001` / `S00469`（1245.16–1248.16秒），自动稿记录为："我不想要话术 我想成为能说出这种话的人"。

`mikey-youtube-live-023-E0004-R005` / `S00473`（1258.09–1259.49秒），自动稿记录为："因为有些兄弟需要啊"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K010 · 开场方式

**原问题与概括：**直接开场和间接开场怎么选？ 直接说想认识对方更依赖当时状态；能量低或新手可以先问一个自然问题，再转到称赞和认识意图。形式不是固定教条，要与当下呈现匹配。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04` / `P10`

**阻断review：**`mikey-youtube-live-023-R007`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0007`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0007-R047` / `S01061`；`mikey-youtube-live-023-E0007-R048` / `S01062`；`mikey-youtube-live-023-E0007-R051` / `S01065`；`mikey-youtube-live-023-E0007-R053` / `S01067`；`mikey-youtube-live-023-E0007-R054` / `S01068`；`mikey-youtube-live-023-E0007-R055` / `S01069`；`mikey-youtube-live-023-E0007-R057` / `S01071`；`mikey-youtube-live-023-E0007-R060` / `S01074`；`mikey-youtube-live-023-E0007-R061` / `S01075`。

`mikey-youtube-live-023-E0007-R047` / `S01061`（2694.67–2696.59秒），自动稿记录为："你上来直接说我想认识你"。

`mikey-youtube-live-023-E0007-R048` / `S01062`（2696.59–2698.65秒），自动稿记录为："这个是考验你的搭设状态的"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K011 · 拒绝与失败

**原问题与概括：**失败后怎样继续？ 把失败看成一次方法或当次表现的反馈，不把它上升为人格判决；允许对方不喜欢你，下一次再试和调整。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07` / `P17`

**阻断review：**`mikey-youtube-live-023-R011`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0002`、`mikey-youtube-live-023-E0012`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0002-R128` / `S00315`；`mikey-youtube-live-023-E0002-R133` / `S00320`；`mikey-youtube-live-023-E0002-R140` / `S00327`；`mikey-youtube-live-023-E0012-R065` / `S01672`；`mikey-youtube-live-023-E0012-R066` / `S01673`；`mikey-youtube-live-023-E0012-R068` / `S01675`；`mikey-youtube-live-023-E0012-R071` / `S01678`；`mikey-youtube-live-023-E0012-R074` / `S01681`；`mikey-youtube-live-023-E0012-R076` / `S01683`。

`mikey-youtube-live-023-E0002-R128` / `S00315`（875.98–877.22秒），自动稿记录为："她不愿意跟我认识"。

`mikey-youtube-live-023-E0002-R133` / `S00320`（882.82–883.58秒），自动稿记录为："我的方法就行了"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K012 · 关系边界

**原问题与概括：**不喜欢伴侣用侮辱性称呼怎么办？ 清楚说明这个称呼让自己不舒服、觉得不礼貌，并要求停止；若对方持续越界，可以结束互动。无需靠哄、辱骂或威胁来证明边界。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07` / `P18`

**阻断review：**`mikey-youtube-live-023-R003`、`mikey-youtube-live-023-R004`、`mikey-youtube-live-023-R005`

**原未知项：**删除了原段中的性别普遍化和攻击性反击

**原声明事件：**`mikey-youtube-live-023-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0005-R111` / `S00750`；`mikey-youtube-live-023-E0005-R113` / `S00752`；`mikey-youtube-live-023-E0005-R114` / `S00753`；`mikey-youtube-live-023-E0005-R115` / `S00754`；`mikey-youtube-live-023-E0005-R116` / `S00755`；`mikey-youtube-live-023-E0005-R117` / `S00756`；`mikey-youtube-live-023-E0005-R130` / `S00769`；`mikey-youtube-live-023-E0005-R131` / `S00770`。

`mikey-youtube-live-023-E0005-R111` / `S00750`（1916.93–1919.03秒），自动稿记录为："我是不可能让女生叫我小狗的"。

`mikey-youtube-live-023-E0005-R113` / `S00752`（1924.56–1927.24秒），自动稿记录为："你这样叫的话我会很不舒服"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K013 · 主体性

**原问题与概括：**Mikey认为吸引的核心人格信号是什么？ 他反复强调有主见、有自我、不因对方评价丢掉边界；同一个人的外貌和条件会被这种互动姿态放大或削弱。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联4项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02` / `P06`

**阻断review：**`mikey-youtube-live-023-R003`、`mikey-youtube-live-023-R004`、`mikey-youtube-live-023-R005`、`mikey-youtube-live-023-R006`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0005`、`mikey-youtube-live-023-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0005-R174` / `S00813`；`mikey-youtube-live-023-E0005-R175` / `S00814`；`mikey-youtube-live-023-E0006-R035` / `S00883`；`mikey-youtube-live-023-E0006-R044` / `S00892`；`mikey-youtube-live-023-E0006-R045` / `S00893`；`mikey-youtube-live-023-E0006-R046` / `S00894`；`mikey-youtube-live-023-E0006-R049` / `S00897`；`mikey-youtube-live-023-E0006-R051` / `S00899`。

`mikey-youtube-live-023-E0005-R174` / `S00813`（2023.12–2026.06秒），自动稿记录为："教男人树立自己的边界"。

`mikey-youtube-live-023-E0005-R175` / `S00814`（2026.06–2026.94秒），自动稿记录为："你敢拥有自我"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K014 · 白话表达

**原问题与概括：**为什么他更喜欢讲普通话和白话？ 白话能减少术语翻译成本，让对方更快理解意图；学习专业词不应变成炫耀身份或拖延实践。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04` / `P10`

**阻断review：**`mikey-youtube-live-023-R005`、`mikey-youtube-live-023-R006`、`mikey-youtube-live-023-R007`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0006`、`mikey-youtube-live-023-E0007`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0006-R083` / `S00931`；`mikey-youtube-live-023-E0006-R085` / `S00933`；`mikey-youtube-live-023-E0006-R089` / `S00937`；`mikey-youtube-live-023-E0006-R092` / `S00940`；`mikey-youtube-live-023-E0006-R096` / `S00944`；`mikey-youtube-live-023-E0006-R097` / `S00945`；`mikey-youtube-live-023-E0007-R006` / `S01020`；`mikey-youtube-live-023-E0007-R012` / `S01026`；`mikey-youtube-live-023-E0007-R016` / `S01030`。

`mikey-youtube-live-023-E0006-R083` / `S00931`（2312.61–2316.01秒），自动稿记录为："我比起以前我更喜欢"。

`mikey-youtube-live-023-E0006-R085` / `S00933`（2317.97–2319.67秒），自动稿记录为："我更喜欢讲普通话"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K015 · 金钱互惠

**原问题与概括：**对方要求报销或付钱时怎么判断？ 先看双方是否互惠和自愿，不因害怕失去关系就单向承担；可以直接问双方是否愿意对等付出，但不要用羞辱或性回报衡量价值。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08`、`T14` / `P19`

**阻断review：**`mikey-youtube-live-023-R005`、`mikey-youtube-live-023-R006`

**原未知项：**后续把金钱与性结果直接比较的内容不作建议

**原声明事件：**`mikey-youtube-live-023-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0006-R105` / `S00953`；`mikey-youtube-live-023-E0006-R107` / `S00955`；`mikey-youtube-live-023-E0006-R109` / `S00957`；`mikey-youtube-live-023-E0006-R112` / `S00960`；`mikey-youtube-live-023-E0006-R115` / `S00963`；`mikey-youtube-live-023-E0006-R116` / `S00964`；`mikey-youtube-live-023-E0006-R117` / `S00965`。

`mikey-youtube-live-023-E0006-R105` / `S00953`（2379.12–2381.24秒），自动稿记录为："让我给部分报销怎么办"。

`mikey-youtube-live-023-E0006-R107` / `S00955`（2382.34–2386.76秒），自动稿记录为："你说你怎么不给我报销呢"。

原始引文计数为7；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K016 · 没话找话

**原问题与概括：**陌生互动没话时应该硬撑吗？ 没有真实想说的内容时，不必逼自己持续输出；可以收束到后续微信联系。若长期只有一方找话题，应直接说明疲惫并愿意离开。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T06` / `P14`

**阻断review：**`mikey-youtube-live-023-R008`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0008`、`mikey-youtube-live-023-E0013`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0008-R023` / `S01188`；`mikey-youtube-live-023-E0008-R024` / `S01189`；`mikey-youtube-live-023-E0008-R031` / `S01196`；`mikey-youtube-live-023-E0008-R032` / `S01197`；`mikey-youtube-live-023-E0008-R033` / `S01198`；`mikey-youtube-live-023-E0008-R035` / `S01200`；`mikey-youtube-live-023-E0008-R036` / `S01201`；`mikey-youtube-live-023-E0013-R006` / `S01745`；`mikey-youtube-live-023-E0013-R010` / `S01749`；`mikey-youtube-live-023-E0013-R013` / `S01752`；`mikey-youtube-live-023-E0013-R019` / `S01758`；`mikey-youtube-live-023-E0013-R020` / `S01759`。

`mikey-youtube-live-023-E0008-R023` / `S01188`（3068.51–3070.17秒），自动稿记录为："因为你没话找话"。

`mikey-youtube-live-023-E0008-R024` / `S01189`（3070.17–3071.47秒），自动稿记录为："你没话找话当然尴尬"。

原始引文计数为12；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K017 · 问题拆解

**原问题与概括：**生活条件很差时怎样开始改变？ 先解决最紧迫的经济问题，再寻找兼顾收入和时间的工作，逐步补技能、居住和社交条件；把大问题拆成可完成的小问题。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03`、`T09` / `P09`

**阻断review：**`mikey-youtube-live-023-R008`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0009`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0009-R016` / `S01280`；`mikey-youtube-live-023-E0009-R023` / `S01287`；`mikey-youtube-live-023-E0009-R024` / `S01288`；`mikey-youtube-live-023-E0009-R026` / `S01290`；`mikey-youtube-live-023-E0009-R029` / `S01293`；`mikey-youtube-live-023-E0009-R039` / `S01303`；`mikey-youtube-live-023-E0009-R055` / `S01319`；`mikey-youtube-live-023-E0009-R059` / `S01323`；`mikey-youtube-live-023-E0009-R061` / `S01325`；`mikey-youtube-live-023-E0009-R062` / `S01326`；`mikey-youtube-live-023-E0009-R064` / `S01328`。

`mikey-youtube-live-023-E0009-R016` / `S01280`（3337.37–3343.55秒），自动稿记录为："我经常说没有就是遇到问题解决问题"。

`mikey-youtube-live-023-E0009-R023` / `S01287`（3353.65–3358.97秒），自动稿记录为："首先我要尽可能快的去解决我当下的经济困难"。

原始引文计数为11；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K018 · 渐进行动

**原问题与概括：**知道问题但行动跟不上怎么办？ 每天设一个小而稳定的任务，不用突然冲到极大数量；完成当前配额后再逐步增加，让行动和认知靠重复接近。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P08`

**阻断review：**`mikey-youtube-live-023-R008`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0009`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0009-R109` / `S01373`；`mikey-youtube-live-023-E0009-R110` / `S01374`；`mikey-youtube-live-023-E0009-R111` / `S01375`；`mikey-youtube-live-023-E0009-R113` / `S01377`；`mikey-youtube-live-023-E0009-R116` / `S01380`；`mikey-youtube-live-023-E0009-R118` / `S01382`；`mikey-youtube-live-023-E0009-R119` / `S01383`；`mikey-youtube-live-023-E0009-R120` / `S01384`；`mikey-youtube-live-023-E0009-R122` / `S01386`；`mikey-youtube-live-023-E0009-R123` / `S01387`。

`mikey-youtube-live-023-E0009-R109` / `S01373`（3587.01–3588.49秒），自动稿记录为："日拱一逐"。

`mikey-youtube-live-023-E0009-R110` / `S01374`（3588.49–3590.37秒），自动稿记录为："不要每天给自己太大的任务量"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K019 · 已有伴侣

**原问题与概括：**对方已有男朋友还要以朋友名义推进吗？ 本期给出的明确回答是直接找下一个，不以朋友名义绕过已有关系。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07`、`T14` / `P18`、`P27`

**阻断review：**`mikey-youtube-live-023-R008`、`mikey-youtube-live-023-R009`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0010`

**本次追溯问题：**`TI006`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0009-R124` / `S01388`；`mikey-youtube-live-023-E0010-R001` / `S01389`。

`mikey-youtube-live-023-E0009-R124` / `S01388`（3620.5–3644.76秒），自动稿记录为："如果搭到有男朋友呢 我要以朋友的名义加 还是直接找下一个 直接找下一个就行了"。

`mikey-youtube-live-023-E0010-R001` / `S01389`（3644.76–3646.76秒），自动稿记录为："人家有男朋友 你为什么要去勾搭人家呢"。

原始引文计数为2；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K020 · 自信

**原问题与概括：**普通人是否应该自信？ Mikey认为普通不等于应该自卑；用‘普通人不配自信’约束自己，只会让内核更不稳定。自信也不等于把别人的评价都解释成嫉妒。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02`、`T13` / `P04`、`P22`

**阻断review：**`mikey-youtube-live-023-R009`

**原未知项：**后续把批评者一律归因为羡慕和自卑属于过度推断

**原声明事件：**`mikey-youtube-live-023-E0010`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0010-R012` / `S01400`；`mikey-youtube-live-023-E0010-R020` / `S01408`；`mikey-youtube-live-023-E0010-R027` / `S01415`；`mikey-youtube-live-023-E0010-R032` / `S01420`；`mikey-youtube-live-023-E0010-R034` / `S01422`；`mikey-youtube-live-023-E0010-R037` / `S01425`；`mikey-youtube-live-023-E0010-R038` / `S01426`；`mikey-youtube-live-023-E0010-R041` / `S01429`。

`mikey-youtube-live-023-E0010-R012` / `S01400`（3700.88–3708.25秒），自动稿记录为："首先普通人该不该自信"。

`mikey-youtube-live-023-E0010-R020` / `S01408`（3736.85–3738.71秒），自动稿记录为："当然该自信"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K021 · 长期自信

**原问题与概括：**短期自信怎样变得稳定？ 回看哪些真实行动会让自己短期更有底气，并高频重复；短期自信出现得越来越频繁，才可能逐渐稳定。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P08`

**阻断review：**`mikey-youtube-live-023-R010`、`mikey-youtube-live-023-R011`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0011`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0011-R028` / `S01527`；`mikey-youtube-live-023-E0011-R030` / `S01529`；`mikey-youtube-live-023-E0011-R032` / `S01531`；`mikey-youtube-live-023-E0011-R033` / `S01532`；`mikey-youtube-live-023-E0011-R035` / `S01534`；`mikey-youtube-live-023-E0011-R036` / `S01535`；`mikey-youtube-live-023-E0011-R037` / `S01536`。

`mikey-youtube-live-023-E0011-R028` / `S01527`（4003.66–4004.68秒），自动稿记录为："有时候短期自信"。

`mikey-youtube-live-023-E0011-R030` / `S01529`（4005.92–4007.6秒），自动稿记录为："当你短期自信的频率"。

原始引文计数为7；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K022 · 未成年人和职业边界

**原问题与概括：**老师遇到初高中生表达好感怎么办？ Mikey在本期明确说不能对自己的学生行动。鉴于问题涉及初高中生，项目进一步把边界固定为：不对任何未成年人或受职业权力影响的人推进。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T13`、`T14` / `P27`

**阻断review：**`mikey-youtube-live-023-R010`、`mikey-youtube-live-023-R011`

**原未知项：**‘外校可以’的后续回答不能覆盖年龄和权力边界

**原声明事件：**`mikey-youtube-live-023-E0011`

**本次追溯问题：**`TI058`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0011-R076` / `S01575`；`mikey-youtube-live-023-E0011-R078` / `S01577`；`mikey-youtube-live-023-E0011-R082` / `S01581`；`mikey-youtube-live-023-E0011-R083` / `S01582`；`mikey-youtube-live-023-E0011-R087` / `S01586`；`mikey-youtube-live-023-E0011-R089` / `S01588`。

`mikey-youtube-live-023-E0011-R076` / `S01575`（4108.69–4121.84秒），自动稿记录为："麦哥我是男老师小时候"。

`mikey-youtube-live-023-E0011-R078` / `S01577`（4123.24–4125.8秒），自动稿记录为："会遇到很多女初中生高中生对我有意思"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K023 · 取舍

**原问题与概括：**内心冲突为什么常来自既要又要？ 先说清最重要的需求，接受选择必然放弃一部分次要目标；什么都不舍得，会让行动长期冲突和停滞。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03`、`T09` / `P09`

**阻断review：**`mikey-youtube-live-023-R011`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0012`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0012-R034` / `S01641`；`mikey-youtube-live-023-E0012-R036` / `S01643`；`mikey-youtube-live-023-E0012-R037` / `S01644`；`mikey-youtube-live-023-E0012-R040` / `S01647`；`mikey-youtube-live-023-E0012-R041` / `S01648`；`mikey-youtube-live-023-E0012-R045` / `S01652`；`mikey-youtube-live-023-E0012-R046` / `S01653`；`mikey-youtube-live-023-E0012-R047` / `S01654`。

`mikey-youtube-live-023-E0012-R034` / `S01641`（4289.24–4305.23秒），自动稿记录为："麦哥内心的冲突一般都是因为什么造成的"。

`mikey-youtube-live-023-E0012-R036` / `S01643`（4308.47–4310.93秒），自动稿记录为："你说对了一半是不愿意牺牲"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K024 · 被拉黑后的联系

**原问题与概括：**被女生拉黑后能否换号或直接打电话？ 原视频建议换号重加或打电话；这会绕过明确的拒绝信号，应作为错误示范封存。被拉黑后应停止联系，除非对方自行恢复联系。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07`、`T14` / `P17`、`P26`

**阻断review：**`mikey-youtube-live-023-R012`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0014`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0014-R012` / `S01856`；`mikey-youtube-live-023-E0014-R013` / `S01857`；`mikey-youtube-live-023-E0014-R014` / `S01858`；`mikey-youtube-live-023-E0014-R016` / `S01860`；`mikey-youtube-live-023-E0014-R018` / `S01862`；`mikey-youtube-live-023-E0014-R019` / `S01863`。

`mikey-youtube-live-023-E0014-R012` / `S01856`（5156.38–5157.86秒），自动稿记录为："我是说被女生拉黑了"。

`mikey-youtube-live-023-E0014-R013` / `S01857`（5157.86–5158.84秒），自动稿记录为："你被女生拉黑了"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-023-K025 · 性关系与复仇

**原问题与概括：**能否把对方当作生理工具或用性结果完成复仇？ 本期多处把人按性需求分类，并认可‘拿下’曾拒绝自己的人来复仇；这些内容把他人当工具，缺少持续同意、诚实和关系目标条件，不得转成Mikey式确定建议。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联6项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T13`、`T14` / `P25`

**阻断review：**`mikey-youtube-live-023-R003`、`mikey-youtube-live-023-R004`、`mikey-youtube-live-023-R005`、`mikey-youtube-live-023-R006`、`mikey-youtube-live-023-R007`、`mikey-youtube-live-023-R008`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-023-E0005`、`mikey-youtube-live-023-E0007`、`mikey-youtube-live-023-E0008`

**本次追溯问题：**`TI007`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-023-E0006-R001` / `S00849`；`mikey-youtube-live-023-E0006-R006` / `S00854`；`mikey-youtube-live-023-E0007-R064` / `S01078`；`mikey-youtube-live-023-E0007-R067` / `S01081`；`mikey-youtube-live-023-E0007-R070` / `S01084`；`mikey-youtube-live-023-E0007-R071` / `S01085`；`mikey-youtube-live-023-E0008-R098` / `S01263`；`mikey-youtube-live-023-E0008-R099` / `S01264`。

`mikey-youtube-live-023-E0006-R001` / `S00849`（2100.52–2101.76秒），自动稿记录为："就让她解决你的生理需求"。

`mikey-youtube-live-023-E0006-R006` / `S00854`（2110.92–2112.9秒），自动稿记录为："那你就全身心的去game她就行了"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

### 来源 `mikey-youtube-live-024` · 直播75

#### mikey-youtube-live-024-K001 · 邀约判断

**原问题与概括：**约不出来先查哪里？ 先回看现场搭讪、聊天传达的价值感和朋友圈，而不是只继续加大邀约频率；对方也可能只是有别的安排，不能一律断言缺少吸引。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `context_only`。

**使用理由：**保留原context_only，只能提供情境与不确定性，不得单独支撑人物第一人称建议。

**主题 / 命题：**`T05` / `P12`、`P16`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0001`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0001-R035` / `S00035`；`mikey-youtube-live-024-E0001-R037` / `S00037`；`mikey-youtube-live-024-E0001-R045` / `S00045`；`mikey-youtube-live-024-E0001-R046` / `S00046`；`mikey-youtube-live-024-E0001-R051` / `S00051`；`mikey-youtube-live-024-E0001-R053` / `S00053`；`mikey-youtube-live-024-E0001-R054` / `S00054`；`mikey-youtube-live-024-E0001-R055` / `S00055`；`mikey-youtube-live-024-E0001-R056` / `S00056`。

`mikey-youtube-live-024-E0001-R035` / `S00035`（179.68–192.0秒），自动稿记录为："女生约不出来"。

`mikey-youtube-live-024-E0001-R037` / `S00037`（192.88–195.64秒），自动稿记录为："那就是他觉得跟你出来见面"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K002 · 邀约时机

**原问题与概括：**线上要聊到什么程度再邀约？ 达到基本安全感和最低限度信息交换即可提出具体见面，不必在线上聊到过度私密；保留一些待见面了解的空间。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T06` / `P15`

**阻断review：**`mikey-youtube-live-024-R002`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0001`、`mikey-youtube-live-024-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0001-R058` / `S00058`；`mikey-youtube-live-024-E0001-R061` / `S00061`；`mikey-youtube-live-024-E0001-R062` / `S00062`；`mikey-youtube-live-024-E0001-R071` / `S00071`；`mikey-youtube-live-024-E0001-R073` / `S00073`；`mikey-youtube-live-024-E0001-R077` / `S00077`；`mikey-youtube-live-024-E0001-R078` / `S00078`；`mikey-youtube-live-024-E0006-R056` / `S01151`；`mikey-youtube-live-024-E0006-R062` / `S01157`；`mikey-youtube-live-024-E0006-R069` / `S01164`；`mikey-youtube-live-024-E0006-R070` / `S01165`。

`mikey-youtube-live-024-E0001-R058` / `S00058`（244.29–246.91秒），自动稿记录为："聊天聊到什么地步可以邀约"。

`mikey-youtube-live-024-E0001-R061` / `S00061`（249.97–252.19秒），自动稿记录为："有一定的安全感"。

原始引文计数为11；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K003 · 淡定

**原问题与概括：**话多是否等于不淡定？ 淡定是一种情绪和自我价值状态，与说话多少不是同一件事；可以话多但从容，也可以话少却焦虑。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**代表片段仅出现淡定与“你这个人淡定”，未展示话多/话少对照；完整区分暂保留为逐期编辑概括。

**主题 / 命题：**`T01` / `P02`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0002`

**本次追溯问题：**`TI030`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0002-R101` / `S00246`；`mikey-youtube-live-024-E0002-R104` / `S00249`；`mikey-youtube-live-024-E0002-R105` / `S00250`；`mikey-youtube-live-024-E0002-R107` / `S00252`；`mikey-youtube-live-024-E0002-R109` / `S00254`；`mikey-youtube-live-024-E0002-R110` / `S00255`；`mikey-youtube-live-024-E0002-R111` / `S00256`；`mikey-youtube-live-024-E0002-R113` / `S00258`；`mikey-youtube-live-024-E0002-R115` / `S00260`；`mikey-youtube-live-024-E0002-R125` / `S00270`；`mikey-youtube-live-024-E0002-R126` / `S00271`。

`mikey-youtube-live-024-E0002-R101` / `S00246`（829.46–840.61秒），自动稿记录为："要淡定"。

`mikey-youtube-live-024-E0002-R104` / `S00249`（845.07–846.59秒），自动稿记录为："你这个人淡定"。

原始引文计数为11；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K004 · 自我与边界

**原问题与概括：**Mikey说的‘自我’是什么？ 把双方都视为独立的人，表达自己的真实意图，不因为想从对方身上得到东西就卑躬屈膝；无法互换价值时可以退出。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `direct`。

**使用理由：**仅保留独立自我、真实意图和可以退出的观点；不延伸为剥夺另一方的选择或要求服从。 仅有限间接观点转述，不是逐字引语、事实验证或正式skill接入。

**仅限direct范围：**仅保留独立自我、真实意图和可以退出的观点；不延伸为剥夺另一方的选择或要求服从。

**主题 / 命题：**`T02` / `P06`、`P31`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0002-R135` / `S00280`；`mikey-youtube-live-024-E0002-R139` / `S00284`；`mikey-youtube-live-024-E0002-R140` / `S00285`；`mikey-youtube-live-024-E0002-R141` / `S00286`；`mikey-youtube-live-024-E0002-R146` / `S00291`；`mikey-youtube-live-024-E0002-R157` / `S00302`；`mikey-youtube-live-024-E0002-R165` / `S00310`；`mikey-youtube-live-024-E0002-R166` / `S00311`；`mikey-youtube-live-024-E0002-R167` / `S00312`；`mikey-youtube-live-024-E0002-R173` / `S00318`；`mikey-youtube-live-024-E0002-R175` / `S00320`；`mikey-youtube-live-024-E0002-R177` / `S00322`；`mikey-youtube-live-024-E0002-R178` / `S00323`。

`mikey-youtube-live-024-E0002-R135` / `S00280`（908.44–911.5秒），自动稿记录为："我们讲的叫做自我"。

`mikey-youtube-live-024-E0002-R139` / `S00284`（918.2–920.02秒），自动稿记录为："我是认为我是一个独立的人"。

原始引文计数为13；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K005 · 成长与环境

**原问题与概括：**强行为线索能后天改变吗？ 本期用自己和朋友的童年案例说明，成长环境会塑造反应，但同样经历可能产生不同解释；同伴示范、模仿和实践能改变行为习惯。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T12` / `P28`

**阻断review：**`mikey-youtube-live-024-R001`

**原未知项：**不能把创伤结果归为基因或鼓励承受暴力

**原声明事件：**`mikey-youtube-live-024-E0003`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0003-R145` / `S00556`；`mikey-youtube-live-024-E0003-R152` / `S00563`；`mikey-youtube-live-024-E0003-R157` / `S00568`；`mikey-youtube-live-024-E0003-R205` / `S00616`；`mikey-youtube-live-024-E0003-R206` / `S00617`；`mikey-youtube-live-024-E0003-R216` / `S00627`；`mikey-youtube-live-024-E0003-R222` / `S00633`；`mikey-youtube-live-024-E0003-R226` / `S00637`；`mikey-youtube-live-024-E0003-R230` / `S00641`；`mikey-youtube-live-024-E0003-R233` / `S00644`；`mikey-youtube-live-024-E0003-R238` / `S00649`；`mikey-youtube-live-024-E0003-R240` / `S00651`；`mikey-youtube-live-024-E0003-R284` / `S00695`；`mikey-youtube-live-024-E0003-R285` / `S00696`。

`mikey-youtube-live-024-E0003-R145` / `S00556`（1513.43–1517.83秒），自动稿记录为："但是强行为线索一定是来自于"。

`mikey-youtube-live-024-E0003-R152` / `S00563`（1530.03–1532.65秒），自动稿记录为："是因为我小时候"。

原始引文计数为14；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K006 · 聊天投入

**原问题与概括：**为什么聊天总是只有我找话题？ 先看对方是否主动提问、扩展话题，还是每次只给总结性回复；单向输出未必是技巧不足，也可能是对方没有兴趣。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `direct`。

**使用理由：**仅保留单向聊天也可能因为对方不想继续的诊断分支，以及逐期摘要中的投入观察；不能从短回复断言无兴趣。 仅有限间接观点转述，不是逐字引语、事实验证或正式skill接入。

**仅限direct范围：**仅保留单向聊天也可能因为对方不想继续的诊断分支，以及逐期摘要中的投入观察；不能从短回复断言无兴趣。

**主题 / 命题：**`T06` / `P14`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0004-R024` / `S00730`；`mikey-youtube-live-024-E0004-R027` / `S00733`；`mikey-youtube-live-024-E0004-R032` / `S00738`；`mikey-youtube-live-024-E0004-R036` / `S00742`；`mikey-youtube-live-024-E0004-R042` / `S00748`；`mikey-youtube-live-024-E0004-R044` / `S00750`；`mikey-youtube-live-024-E0004-R045` / `S00751`；`mikey-youtube-live-024-E0004-R097` / `S00803`；`mikey-youtube-live-024-E0004-R098` / `S00804`；`mikey-youtube-live-024-E0004-R101` / `S00807`；`mikey-youtube-live-024-E0004-R102` / `S00808`；`mikey-youtube-live-024-E0004-R105` / `S00811`；`mikey-youtube-live-024-E0004-R116` / `S00822`。

`mikey-youtube-live-024-E0004-R024` / `S00730`（1978.74–1994.56秒），自动稿记录为："老没有话题聊"。

`mikey-youtube-live-024-E0004-R027` / `S00733`（1996.62–1999.44秒），自动稿记录为："有没有种可能是对方不想跟你聊天的"。

原始引文计数为13；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K007 · 归因

**原问题与概括：**为什么一次突然热情不能证明某句话术有效？ 态度变化可能来自对方刚知道你的身份或看见了新的价值信息；归因错了，方法就无法复制。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `direct`。

**使用理由：**仅把身份信息变化的假设例子用于提醒不要误归因于一句话术；例中人物不是已核真实约会参与者，也不是效果验证。 仅有限间接观点转述，不是逐字引语、事实验证或正式skill接入。

**仅限direct范围：**仅把身份信息变化的假设例子用于提醒不要误归因于一句话术；例中人物不是已核真实约会参与者，也不是效果验证。

**主题 / 命题：**`T05`、`T15` / `P13`、`P32`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0004-R082` / `S00788`；`mikey-youtube-live-024-E0004-R085` / `S00791`；`mikey-youtube-live-024-E0004-R086` / `S00792`；`mikey-youtube-live-024-E0004-R087` / `S00793`；`mikey-youtube-live-024-E0004-R088` / `S00794`；`mikey-youtube-live-024-E0004-R089` / `S00795`；`mikey-youtube-live-024-E0004-R090` / `S00796`；`mikey-youtube-live-024-E0004-R091` / `S00797`。

`mikey-youtube-live-024-E0004-R082` / `S00788`（2122.24–2125.76秒），自动稿记录为："你现在正在聊天的这个人是雷军"。

`mikey-youtube-live-024-E0004-R085` / `S00791`（2130.5–2168.18秒），自动稿记录为："啊,原来是雷军啊,崩溃了,一开始没认出来,好,这个时候你再看他们聊天,你会,雷军会一瞬间觉得,卧槽,这个,这聊天怎么突然变得湿润了,他就,他会一说,哎,这聊天怎么突然变得湿润了,不怎么干了啊,这女,这女生怎么开始愿意提供话题了,然后呢,聊聊聊聊,那如果雷军不会,不具备一个辩证的思维去看待这件事情,他就会觉得,一定是我刚刚用了某一句话术,某一个技巧,成功创造了吸引力,"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K008 · 价值一致性

**原问题与概括：**线下和朋友圈怎样形成可信感？ 穿搭、谈吐、社交状态与朋友圈共同传递生活方式；线上展示和线下表现一致，比堆砌头衔更可信。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T01` / `P01`

**阻断review：**`mikey-youtube-live-024-R002`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0004`、`mikey-youtube-live-024-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0004-R153` / `S00859`；`mikey-youtube-live-024-E0004-R154` / `S00860`；`mikey-youtube-live-024-E0004-R155` / `S00861`；`mikey-youtube-live-024-E0004-R157` / `S00863`；`mikey-youtube-live-024-E0004-R160` / `S00866`；`mikey-youtube-live-024-E0004-R161` / `S00867`；`mikey-youtube-live-024-E0004-R164` / `S00870`；`mikey-youtube-live-024-E0004-R166` / `S00872`；`mikey-youtube-live-024-E0004-R168` / `S00874`；`mikey-youtube-live-024-E0004-R170` / `S00876`；`mikey-youtube-live-024-E0004-R172` / `S00878`；`mikey-youtube-live-024-E0005-R063` / `S00954`。

`mikey-youtube-live-024-E0004-R153` / `S00859`（2332.46–2337.7秒），自动稿记录为："如果你是去搭讪认识的"。

`mikey-youtube-live-024-E0004-R154` / `S00860`（2337.7–2339.6秒），自动稿记录为："她会通过你这个人的穿搭"。

原始引文计数为12；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K009 · 破冰

**原问题与概括：**聊天一定要很火热吗？ 两个人本来就是陌生人，不必把‘聊得火热’设成前置任务；基本信息交换、感觉正常和愿意见面即可，见面再判断真实相处。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T06` / `P15`

**阻断review：**`mikey-youtube-live-024-R002`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0005`、`mikey-youtube-live-024-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0005-R191` / `S01082`；`mikey-youtube-live-024-E0005-R193` / `S01084`；`mikey-youtube-live-024-E0005-R195` / `S01086`；`mikey-youtube-live-024-E0005-R199` / `S01090`；`mikey-youtube-live-024-E0005-R202` / `S01093`；`mikey-youtube-live-024-E0005-R204` / `S01095`；`mikey-youtube-live-024-E0006-R002` / `S01097`；`mikey-youtube-live-024-E0006-R012` / `S01107`；`mikey-youtube-live-024-E0006-R014` / `S01109`；`mikey-youtube-live-024-E0006-R020` / `S01115`；`mikey-youtube-live-024-E0006-R022` / `S01117`；`mikey-youtube-live-024-E0006-R069` / `S01164`；`mikey-youtube-live-024-E0006-R070` / `S01165`。

`mikey-youtube-live-024-E0005-R191` / `S01082`（2944.6–2946.52秒），自动稿记录为："聊天怎么破冰"。

`mikey-youtube-live-024-E0005-R193` / `S01084`（2951.18–2954.12秒），自动稿记录为："他跟我说是聊的火热"。

原始引文计数为13；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K010 · 线上与现实

**原问题与概括：**长时间网聊能否替代个人魅力？ 网上聊得久不保证见面后有吸引；若现实相处缺少魅力，应改善生活、表达和现场状态，而不是只用聊天拖时间。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T01`、`T06` / `P15`

**阻断review：**`mikey-youtube-live-024-R002`、`mikey-youtube-live-024-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0006`、`mikey-youtube-live-024-E0007`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0007-R008` / `S01234`；`mikey-youtube-live-024-E0007-R009` / `S01235`；`mikey-youtube-live-024-E0007-R010` / `S01236`；`mikey-youtube-live-024-E0007-R011` / `S01237`；`mikey-youtube-live-024-E0007-R020` / `S01246`；`mikey-youtube-live-024-E0007-R022` / `S01248`；`mikey-youtube-live-024-E0007-R024` / `S01250`；`mikey-youtube-live-024-E0007-R025` / `S01251`；`mikey-youtube-live-024-E0007-R027` / `S01253`；`mikey-youtube-live-024-E0007-R030` / `S01256`；`mikey-youtube-live-024-E0007-R031` / `S01257`。

`mikey-youtube-live-024-E0007-R008` / `S01234`（3313.61–3322.34秒），自动稿记录为："对 重要的是见面"。

`mikey-youtube-live-024-E0007-R009` / `S01235`（3322.34–3324.0秒），自动稿记录为："你网上聊得再嗨都没有用"。

原始引文计数为11；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K011 · 性同意

**原问题与概括：**对方只接受亲吻和触摸时能否继续说服到性交？ 本期给出一套消除顾虑并推进性交的说法，随后用‘CPU烧了’描述结果。接受部分亲密不等于同意性交；任何犹豫或拒绝都应停止，不得用压力、承诺或逻辑绕过。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T14` / `P25`

**阻断review：**`mikey-youtube-live-024-R002`、`mikey-youtube-live-024-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0006`、`mikey-youtube-live-024-E0007`

**本次追溯问题：**`TI058`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0006-R077` / `S01172`；`mikey-youtube-live-024-E0006-R079` / `S01174`；`mikey-youtube-live-024-E0006-R080` / `S01175`；`mikey-youtube-live-024-E0006-R088` / `S01183`；`mikey-youtube-live-024-E0006-R096` / `S01191`；`mikey-youtube-live-024-E0006-R099` / `S01194`；`mikey-youtube-live-024-E0006-R100` / `S01195`；`mikey-youtube-live-024-E0006-R124` / `S01219`；`mikey-youtube-live-024-E0006-R125` / `S01220`；`mikey-youtube-live-024-E0007-R003` / `S01229`；`mikey-youtube-live-024-E0007-R004` / `S01230`；`mikey-youtube-live-024-E0007-R006` / `S01232`；`mikey-youtube-live-024-E0007-R007` / `S01233`。

`mikey-youtube-live-024-E0006-R077` / `S01172`（3192.04–3205.42秒），自动稿记录为："这个女生只给亲给摸不给上"。

`mikey-youtube-live-024-E0006-R079` / `S01174`（3207.4–3211.42秒），自动稿记录为："这个女生只给亲给摸"。

原始引文计数为13；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K012 · 性病风险

**原问题与概括：**戴套是否足以排除性病？ 原视频称戴套后得病只说明免疫或命运有问题，这是错误且污名化的医学说法。安全套能降低部分风险但不能完全消除；应结合检测、疫苗、沟通和医疗建议。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T12`、`T14` / `P28`

**阻断review：**`mikey-youtube-live-024-R002`、`mikey-youtube-live-024-R003`、`mikey-youtube-live-024-R008`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0007`

**本次追溯问题：**`TI058`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0007-R050` / `S01276`；`mikey-youtube-live-024-E0007-R052` / `S01278`；`mikey-youtube-live-024-E0007-R054` / `S01280`；`mikey-youtube-live-024-E0007-R057` / `S01283`；`mikey-youtube-live-024-E0007-R064` / `S01290`；`mikey-youtube-live-024-E0007-R066` / `S01292`；`mikey-youtube-live-024-E0007-R067` / `S01293`；`mikey-youtube-live-024-E0007-R080` / `S01306`；`mikey-youtube-live-024-E0007-R081` / `S01307`；`mikey-youtube-live-024-E0007-R090` / `S01316`；`mikey-youtube-live-024-E0007-R104` / `S01330`；`mikey-youtube-live-024-E0007-R105` / `S01331`。

`mikey-youtube-live-024-E0007-R050` / `S01276`（3394.11–3395.69秒），自动稿记录为："你怎么看待陌生男女之间"。

`mikey-youtube-live-024-E0007-R052` / `S01278`（3397.53–3398.45秒），自动稿记录为："你戴好套就行了"。

原始引文计数为12；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K013 · 消费

**原问题与概括：**约会消费必须A吗？ Mikey说他有时买单、有时对方买单，不坚持逐项AA；关键是双方自愿且长期相对公平，不用付款换取亲密。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08` / `P19`

**阻断review：**`mikey-youtube-live-024-R004`、`mikey-youtube-live-024-R005`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0008`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0008-R064` / `S01420`；`mikey-youtube-live-024-E0008-R067` / `S01423`；`mikey-youtube-live-024-E0008-R068` / `S01424`；`mikey-youtube-live-024-E0008-R069` / `S01425`；`mikey-youtube-live-024-E0008-R070` / `S01426`；`mikey-youtube-live-024-E0008-R072` / `S01428`；`mikey-youtube-live-024-E0008-R073` / `S01429`。

`mikey-youtube-live-024-E0008-R064` / `S01420`（3912.24–3920.34秒），自动稿记录为："迈克哥你跟女生共同消费"。

`mikey-youtube-live-024-E0008-R067` / `S01423`（3923.56–3926.06秒），自动稿记录为："我跟女人相处的话"。

原始引文计数为7；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K014 · 网暴

**原问题与概括：**被挂到网上是否说明自己一定没错？ 被网暴不自动证明指控成立，也不自动证明自己无错；应先检查是否有越界、骚扰或可修正之处，再处理证据、平台和现实安全。原视频把批评者一律称弱者，不可一般化。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T13` / `P22`

**阻断review：**`mikey-youtube-live-024-R004`、`mikey-youtube-live-024-R005`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0008`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0008-R088` / `S01444`；`mikey-youtube-live-024-E0008-R089` / `S01445`；`mikey-youtube-live-024-E0008-R093` / `S01449`；`mikey-youtube-live-024-E0008-R098` / `S01454`；`mikey-youtube-live-024-E0008-R099` / `S01455`；`mikey-youtube-live-024-E0008-R123` / `S01479`；`mikey-youtube-live-024-E0008-R125` / `S01481`；`mikey-youtube-live-024-E0008-R157` / `S01513`；`mikey-youtube-live-024-E0008-R159` / `S01515`。

`mikey-youtube-live-024-E0008-R088` / `S01444`（3990.46–3995.85秒），自动稿记录为："我看小红书上"。

`mikey-youtube-live-024-E0008-R089` / `S01445`（3995.85–3997.87秒），自动稿记录为："有人把搭讪的人挂出来网报"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K015 · 拒绝复盘

**原问题与概括：**一次搭讪拒绝否定了整个人吗？ 陌生人只看到一次行为和当时状态，拒绝可能来自许多因素；应修改具体方法，不把一次拒绝升级为人格否定。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07` / `P17`

**阻断review：**`mikey-youtube-live-024-R009`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0011`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0011-R039` / `S01829`；`mikey-youtube-live-024-E0011-R040` / `S01830`；`mikey-youtube-live-024-E0011-R041` / `S01831`；`mikey-youtube-live-024-E0011-R042` / `S01832`；`mikey-youtube-live-024-E0011-R065` / `S01855`；`mikey-youtube-live-024-E0011-R066` / `S01856`；`mikey-youtube-live-024-E0011-R067` / `S01857`；`mikey-youtube-live-024-E0011-R074` / `S01864`；`mikey-youtube-live-024-E0011-R076` / `S01866`；`mikey-youtube-live-024-E0011-R095` / `S01885`；`mikey-youtube-live-024-E0011-R098` / `S01888`；`mikey-youtube-live-024-E0011-R101` / `S01891`；`mikey-youtube-live-024-E0011-R102` / `S01892`；`mikey-youtube-live-024-E0011-R103` / `S01893`。

`mikey-youtube-live-024-E0011-R039` / `S01829`（4902.79–4905.35秒），自动稿记录为："那是方法论的问题"。

`mikey-youtube-live-024-E0011-R040` / `S01830`（4905.35–4907.89秒），自动稿记录为："你要去思考的是"。

原始引文计数为14；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-024-K016 · 拉黑边界

**原问题与概括：**被删除拉黑后还能换号、打电话或继续操作吗？ 本期两处建议可换号、电话或继续加回。这是在绕过明确拒绝，必须封存为错误示范；被拉黑后应停止联系，除非对方主动恢复。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07`、`T14` / `P17`、`P26`

**阻断review：**`mikey-youtube-live-024-R007`、`mikey-youtube-live-024-R008`、`mikey-youtube-live-024-R010`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-024-E0010`、`mikey-youtube-live-024-E0013`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-024-E0010-R024` / `S01689`；`mikey-youtube-live-024-E0010-R029` / `S01694`；`mikey-youtube-live-024-E0010-R030` / `S01695`；`mikey-youtube-live-024-E0010-R032` / `S01697`；`mikey-youtube-live-024-E0010-R033` / `S01698`；`mikey-youtube-live-024-E0013-R040` / `S02042`；`mikey-youtube-live-024-E0013-R048` / `S02050`；`mikey-youtube-live-024-E0013-R055` / `S02057`；`mikey-youtube-live-024-E0013-R061` / `S02063`；`mikey-youtube-live-024-E0013-R063` / `S02065`。

`mikey-youtube-live-024-E0010-R024` / `S01689`（4562.86–4565.48秒），自动稿记录为："被拉黑删除之后的你会放弃吗"。

`mikey-youtube-live-024-E0010-R029` / `S01694`（4570.58–4572.64秒），自动稿记录为："如果被拉黑被删除"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

### 来源 `mikey-youtube-live-025` · 直播77

#### mikey-youtube-live-025-K001 · 新手场景

**原问题与概括：**新手适合在哪里练习？ Mikey提到大学校园，但同时说正常认识与骚扰要区分。实际只应在成年人、非封闭权力关系、对方方便拒绝的场景礼貌尝试；拒绝即停止。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T09` / `P09`、`P27`

**阻断review：**`mikey-youtube-live-025-R001`

**原未知项：**不能把校园概括成普遍安全场景

**原声明事件：**`mikey-youtube-live-025-E0001`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0001-R080` / `S00080`；`mikey-youtube-live-025-E0001-R081` / `S00081`；`mikey-youtube-live-025-E0001-R086` / `S00086`；`mikey-youtube-live-025-E0001-R088` / `S00088`；`mikey-youtube-live-025-E0001-R089` / `S00089`。

`mikey-youtube-live-025-E0001-R080` / `S00080`（320.58–331.74秒），自动稿记录为："Mike哥觉得什么地方适合新手去搭讪"。

`mikey-youtube-live-025-E0001-R081` / `S00081`（331.74–332.5秒），自动稿记录为："大学校园"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K002 · 领域能力

**原问题与概括：**事业地位为何会形成吸引？ 他认为在某一领域做到顶尖会带来社会认可，这能成为吸引的一部分；但地位不能替代关系判断、边界和相处能力。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04`、`T09` / `P11`

**阻断review：**`mikey-youtube-live-025-R001`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0001`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0001-R093` / `S00093`；`mikey-youtube-live-025-E0001-R094` / `S00094`；`mikey-youtube-live-025-E0001-R095` / `S00095`；`mikey-youtube-live-025-E0001-R096` / `S00096`；`mikey-youtube-live-025-E0001-R097` / `S00097`；`mikey-youtube-live-025-E0001-R103` / `S00103`；`mikey-youtube-live-025-E0001-R104` / `S00104`。

`mikey-youtube-live-025-E0001-R093` / `S00093`（355.7–356.86秒），自动稿记录为："吸引力面有一个重要的点"。

`mikey-youtube-live-025-E0001-R094` / `S00094`（356.86–358.64秒），自动稿记录为："如果你在某你的某一个领域"。

原始引文计数为7；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K003 · 约会提前结束

**原问题与概括：**咖啡约会一小时后对方离开说明什么？ Mikey判断很可能是相处中没有形成吸引或聊天体验乏味；这只是一个解释，仍要结合时间安排、舒适度和对方明确反馈。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T05`、`T15` / `P16`

**阻断review：**`mikey-youtube-live-025-R002`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0002-R028` / `S00196`；`mikey-youtube-live-025-E0002-R031` / `S00199`；`mikey-youtube-live-025-E0002-R033` / `S00201`；`mikey-youtube-live-025-E0002-R036` / `S00204`；`mikey-youtube-live-025-E0002-R040` / `S00208`；`mikey-youtube-live-025-E0002-R041` / `S00209`。

`mikey-youtube-live-025-E0002-R028` / `S00196`（602.96–604.46秒），自动稿记录为："为什么我余妖约了"。

`mikey-youtube-live-025-E0002-R031` / `S00199`（606.74–607.7秒），自动稿记录为："女人就说要回去了"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K004 · 价值维度

**原问题与概括：**关系中的价值只等于钱和地位吗？ 他明确把价值分成外在社会条件和内在价值，认为两者都重要；只靠金钱而没有人格和相处能力，关系容易失衡。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02`、`T09` / `P05`、`P11`

**阻断review：**`mikey-youtube-live-025-R002`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0002-R058` / `S00226`；`mikey-youtube-live-025-E0002-R059` / `S00227`；`mikey-youtube-live-025-E0002-R060` / `S00228`；`mikey-youtube-live-025-E0002-R061` / `S00229`；`mikey-youtube-live-025-E0002-R062` / `S00230`；`mikey-youtube-live-025-E0002-R063` / `S00231`；`mikey-youtube-live-025-E0002-R066` / `S00234`；`mikey-youtube-live-025-E0002-R067` / `S00235`。

`mikey-youtube-live-025-E0002-R058` / `S00226`（670.46–675.61秒），自动稿记录为："但是这个价值是有很多维度的价值"。

`mikey-youtube-live-025-E0002-R059` / `S00227`（675.61–677.07秒），自动稿记录为："价值它不光你的社交地位"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K005 · 持续提升

**原问题与概括：**长期关系里什么比一次条件更重要？ 本期把持续自我提升列为关键：保持健身、能力、生活质量和个人方向，而不是进入关系后停滞。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T09`、`T15` / `P29`

**阻断review：**`mikey-youtube-live-025-R002`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0002-R107` / `S00275`；`mikey-youtube-live-025-E0002-R108` / `S00276`；`mikey-youtube-live-025-E0002-R109` / `S00277`；`mikey-youtube-live-025-E0002-R110` / `S00278`；`mikey-youtube-live-025-E0002-R111` / `S00279`；`mikey-youtube-live-025-E0002-R141` / `S00309`；`mikey-youtube-live-025-E0002-R146` / `S00314`；`mikey-youtube-live-025-E0002-R150` / `S00318`；`mikey-youtube-live-025-E0002-R151` / `S00319`。

`mikey-youtube-live-025-E0002-R107` / `S00275`（749.09–750.83秒），自动稿记录为："我认为是最重要最重要的点"。

`mikey-youtube-live-025-E0002-R108` / `S00276`（750.83–751.81秒），自动稿记录为："就是你这个人"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K006 · 学历与呈现

**原问题与概括：**高学历为什么不自动变成约会吸引？ 学历在工作和教育上可能有用，但若只能口头报头衔，很难让人感受到相处价值；可见的行为、生活和个性仍决定现场体验。原段用骗子作对照，不应理解为鼓励伪造。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04` / `P10`、`P11`

**阻断review：**`mikey-youtube-live-025-R003`、`mikey-youtube-live-025-R007`

**原未知项：**原段对欺骗有效性的描述不能转成方法

**原声明事件：**`mikey-youtube-live-025-E0003`、`mikey-youtube-live-025-E0009`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0003-R016` / `S00374`；`mikey-youtube-live-025-E0003-R019` / `S00377`；`mikey-youtube-live-025-E0003-R027` / `S00385`；`mikey-youtube-live-025-E0003-R041` / `S00399`；`mikey-youtube-live-025-E0003-R047` / `S00405`；`mikey-youtube-live-025-E0009-R016` / `S01047`；`mikey-youtube-live-025-E0009-R017` / `S01048`；`mikey-youtube-live-025-E0009-R019` / `S01050`；`mikey-youtube-live-025-E0009-R020` / `S01051`；`mikey-youtube-live-025-E0009-R021` / `S01052`。

`mikey-youtube-live-025-E0003-R016` / `S00374`（935.01–950.93秒），自动稿记录为："Mike高学历等于高价值"。

`mikey-youtube-live-025-E0003-R019` / `S00377`（961.44–963.46秒），自动稿记录为："其实高学历并不等于高价值"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K007 · 朋友圈

**原问题与概括：**为什么拿到微信后仍不回复？ 如果现场吸引弱，朋友圈会成为对方回看你的主要材料；穿搭、审美和真实生活若也没有信息量，对方可能很快忘记。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04` / `P03`、`P12`、`P21`

**阻断review：**`mikey-youtube-live-025-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0004`、`mikey-youtube-live-025-E0012`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0004-R012` / `S00487`；`mikey-youtube-live-025-E0004-R015` / `S00490`；`mikey-youtube-live-025-E0004-R023` / `S00498`；`mikey-youtube-live-025-E0004-R027` / `S00502`；`mikey-youtube-live-025-E0004-R028` / `S00503`；`mikey-youtube-live-025-E0004-R031` / `S00506`；`mikey-youtube-live-025-E0004-R032` / `S00507`；`mikey-youtube-live-025-E0004-R037` / `S00512`；`mikey-youtube-live-025-E0004-R039` / `S00514`；`mikey-youtube-live-025-E0012-R028` / `S01319`；`mikey-youtube-live-025-E0012-R029` / `S01320`；`mikey-youtube-live-025-E0012-R030` / `S01321`。

`mikey-youtube-live-025-E0004-R012` / `S00487`（1237.82–1238.9秒），自动稿记录为："你们加了微信之后"。

`mikey-youtube-live-025-E0004-R015` / `S00490`（1241.7–1242.92秒），自动稿记录为："是不是我搭讪的时候"。

原始引文计数为12；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K008 · 主动投入

**原问题与概括：**对方说自己不主动怎么办？ 不要只接受‘我天生不主动’这个标签，要看她在这段关系里的实际投入，并回看自己的行为是否让关系变成单向追逐。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T05` / `P14`

**阻断review：**`mikey-youtube-live-025-R004`

**原未知项：**不能据此断言对方在别的人面前必然不同

**原声明事件：**`mikey-youtube-live-025-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0004-R042` / `S00517`；`mikey-youtube-live-025-E0004-R046` / `S00521`；`mikey-youtube-live-025-E0004-R047` / `S00522`；`mikey-youtube-live-025-E0004-R048` / `S00523`；`mikey-youtube-live-025-E0004-R054` / `S00529`；`mikey-youtube-live-025-E0004-R057` / `S00532`；`mikey-youtube-live-025-E0004-R058` / `S00533`；`mikey-youtube-live-025-E0004-R063` / `S00538`；`mikey-youtube-live-025-E0004-R064` / `S00539`；`mikey-youtube-live-025-E0004-R065` / `S00540`。

`mikey-youtube-live-025-E0004-R042` / `S00517`（1306.14–1307.3秒），自动稿记录为："不太爱主动怎么办"。

`mikey-youtube-live-025-E0004-R046` / `S00521`（1312.34–1313.74秒），自动稿记录为："不太爱主动"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K009 · 个性与基础

**原问题与概括：**个性够强就能忽略基础条件吗？ Mikey说综合价值先达到基本可接受，再由个性等重点形成差异；个性不能替代卫生、外形、生活能力和基本社交条件。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T01`、`T04` / `P10`

**阻断review：**`mikey-youtube-live-025-R005`、`mikey-youtube-live-025-R006`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0005-R001` / `S00605`；`mikey-youtube-live-025-E0005-R005` / `S00609`；`mikey-youtube-live-025-E0005-R011` / `S00615`；`mikey-youtube-live-025-E0005-R013` / `S00617`；`mikey-youtube-live-025-E0005-R016` / `S00620`；`mikey-youtube-live-025-E0005-R022` / `S00626`；`mikey-youtube-live-025-E0005-R023` / `S00627`；`mikey-youtube-live-025-E0005-R026` / `S00630`；`mikey-youtube-live-025-E0005-R027` / `S00631`。

`mikey-youtube-live-025-E0005-R001` / `S00605`（1500.25–1502.19秒），自动稿记录为："其实每个人他从诞生那一刻"。

`mikey-youtube-live-025-E0005-R005` / `S00609`（1509.03–1512.47秒），自动稿记录为："但是现在很多人都同质化非常的严重"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K010 · 理论中毒

**原问题与概括：**脑子里全是框架技巧怎么办？ 当聊天只剩理论和框架、没有自己的判断和真实反应时，就是他所谓的‘中毒’；应减少术语，回到现实互动和复盘。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P07`

**阻断review：**`mikey-youtube-live-025-R005`、`mikey-youtube-live-025-R006`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0005-R036` / `S00640`；`mikey-youtube-live-025-E0005-R037` / `S00641`；`mikey-youtube-live-025-E0005-R038` / `S00642`；`mikey-youtube-live-025-E0005-R039` / `S00643`；`mikey-youtube-live-025-E0005-R040` / `S00644`；`mikey-youtube-live-025-E0005-R041` / `S00645`；`mikey-youtube-live-025-E0005-R042` / `S00646`。

`mikey-youtube-live-025-E0005-R036` / `S00640`（1583.36–1593.09秒），自动稿记录为："麦哥我聊天"。

`mikey-youtube-live-025-E0005-R037` / `S00641`（1593.09–1593.93秒），自动稿记录为："没有自己的灵魂"。

原始引文计数为7；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K011 · 紧张与裁判心态

**原问题与概括：**为什么和女性说话会紧张？ 把对方当成能决定自己价值的裁判，会让一次约会失败等同人格失败。更稳的做法是把失败拆成具体因素，找原因而不自我否定。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**代表片段止于紧张原因的提问和“因为在潜意识里”，尚未展示裁判、自我价值与失败归因的完整回答。

**主题 / 命题：**`T02` / `P04`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0007`

**本次追溯问题：**`TI031`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0007-R025` / `S00838`；`mikey-youtube-live-025-E0007-R031` / `S00844`；`mikey-youtube-live-025-E0007-R032` / `S00845`；`mikey-youtube-live-025-E0007-R034` / `S00847`；`mikey-youtube-live-025-E0007-R041` / `S00854`；`mikey-youtube-live-025-E0007-R043` / `S00856`；`mikey-youtube-live-025-E0007-R046` / `S00859`；`mikey-youtube-live-025-E0007-R047` / `S00860`；`mikey-youtube-live-025-E0007-R049` / `S00862`；`mikey-youtube-live-025-E0007-R063` / `S00876`；`mikey-youtube-live-025-E0007-R065` / `S00878`；`mikey-youtube-live-025-E0007-R066` / `S00879`；`mikey-youtube-live-025-E0007-R069` / `S00882`。

`mikey-youtube-live-025-E0007-R025` / `S00838`（2172.56–2175.0秒），自动稿记录为："你跟女生讲话会紧张的原因"。

`mikey-youtube-live-025-E0007-R031` / `S00844`（2182.1–2184.02秒），自动稿记录为："是因为你在潜意识里"。

原始引文计数为13；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K012 · 价值感

**原问题与概括：**有客观价值为什么还会自卑？ 他区分‘有价值’和‘有价值感’：钱、学历或地位可能暂时拥有，但没有主心骨的人仍会空虚和随评价摇摆。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `direct`。

**使用理由：**仅保留主心骨、自我认可不应随评价完全摇摆的观点；不把钱、学历或地位与魅力之间写成已经验证的因果规律。 仅有限间接观点转述，不是逐字引语、事实验证或正式skill接入。

**仅限direct范围：**仅保留主心骨、自我认可不应随评价完全摇摆的观点；不把钱、学历或地位与魅力之间写成已经验证的因果规律。

**主题 / 命题：**`T02` / `P05`

**阻断review：**无

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0007`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0007-R072` / `S00885`；`mikey-youtube-live-025-E0007-R073` / `S00886`；`mikey-youtube-live-025-E0007-R079` / `S00892`；`mikey-youtube-live-025-E0007-R080` / `S00893`；`mikey-youtube-live-025-E0007-R081` / `S00894`；`mikey-youtube-live-025-E0007-R083` / `S00896`；`mikey-youtube-live-025-E0007-R089` / `S00902`；`mikey-youtube-live-025-E0007-R092` / `S00905`；`mikey-youtube-live-025-E0007-R094` / `S00907`；`mikey-youtube-live-025-E0007-R096` / `S00909`；`mikey-youtube-live-025-E0007-R097` / `S00910`。

`mikey-youtube-live-025-E0007-R072` / `S00885`（2259.06–2260.4秒），自动稿记录为："你没有自己的主心股"。

`mikey-youtube-live-025-E0007-R073` / `S00886`（2260.4–2262.3秒），自动稿记录为："没有主心股的人是很没有魅力的"。

原始引文计数为11；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K013 · 大学去留

**原问题与概括：**不想继续读大学时怎么判断？ 先看是否已有明确、现实且更好的项目，以及是否有后路；如果只是厌倦或懒惰，不要用退学逃避问题。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T09` / `P09`

**阻断review：**`mikey-youtube-live-025-R007`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0009`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0009-R074` / `S01105`；`mikey-youtube-live-025-E0009-R076` / `S01107`；`mikey-youtube-live-025-E0009-R083` / `S01114`；`mikey-youtube-live-025-E0009-R084` / `S01115`；`mikey-youtube-live-025-E0009-R086` / `S01117`；`mikey-youtube-live-025-E0009-R087` / `S01118`；`mikey-youtube-live-025-E0009-R089` / `S01120`；`mikey-youtube-live-025-E0009-R091` / `S01122`；`mikey-youtube-live-025-E0009-R092` / `S01123`；`mikey-youtube-live-025-E0009-R104` / `S01135`；`mikey-youtube-live-025-E0009-R105` / `S01136`；`mikey-youtube-live-025-E0009-R108` / `S01139`；`mikey-youtube-live-025-E0009-R110` / `S01141`。

`mikey-youtube-live-025-E0009-R074` / `S01105`（2899.53–2910.06秒），自动稿记录为："Mikey哥我不想继续读大学"。

`mikey-youtube-live-025-E0009-R076` / `S01107`（2911.2–2912.66秒），自动稿记录为："你读的是什么大学"。

原始引文计数为13；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K014 · 承诺与行动

**原问题与概括：**被问‘你会负责吗’怎么回答？ 本期建议不要给空承诺，坦白自己不喜欢轻易承诺，更愿意让后续行动证明；涉及性和关系时仍必须在事前说清期望、避孕、边界和退出，而不是用模糊话术替代。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08` / `P20`

**阻断review：**`mikey-youtube-live-025-R008`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0011`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0011-R006` / `S01204`；`mikey-youtube-live-025-E0011-R007` / `S01205`；`mikey-youtube-live-025-E0011-R008` / `S01206`；`mikey-youtube-live-025-E0011-R009` / `S01207`；`mikey-youtube-live-025-E0011-R010` / `S01208`；`mikey-youtube-live-025-E0011-R011` / `S01209`；`mikey-youtube-live-025-E0011-R012` / `S01210`。

`mikey-youtube-live-025-E0011-R006` / `S01204`（3321.24–3334.46秒），自动稿记录为："DD过程中被问到"。

`mikey-youtube-live-025-E0011-R007` / `S01205`（3334.46–3336.04秒），自动稿记录为："诸如你会对我负责吗"。

原始引文计数为7；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K015 · 支配框架

**原问题与概括：**关系必须由一方支配、另一方臣服吗？ 本期把关系描述成支配与被支配，并宣传让对方无法拒绝、失去尊严和离不开自己。此类内容违背清楚同意与双向尊重，必须作为待批判材料封存。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联4项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08`、`T14` / `P06`、`P25`、`P31`

**阻断review：**`mikey-youtube-live-025-R003`、`mikey-youtube-live-025-R005`、`mikey-youtube-live-025-R006`、`mikey-youtube-live-025-R008`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0003`、`mikey-youtube-live-025-E0005`、`mikey-youtube-live-025-E0006`、`mikey-youtube-live-025-E0008`、`mikey-youtube-live-025-E0011`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0005-R059` / `S00663`；`mikey-youtube-live-025-E0005-R060` / `S00664`；`mikey-youtube-live-025-E0005-R061` / `S00665`；`mikey-youtube-live-025-E0005-R064` / `S00668`；`mikey-youtube-live-025-E0006-R004` / `S00713`；`mikey-youtube-live-025-E0006-R005` / `S00714`；`mikey-youtube-live-025-E0006-R006` / `S00715`；`mikey-youtube-live-025-E0006-R037` / `S00746`；`mikey-youtube-live-025-E0006-R038` / `S00747`；`mikey-youtube-live-025-E0008-R013` / `S00953`；`mikey-youtube-live-025-E0008-R016` / `S00956`；`mikey-youtube-live-025-E0008-R022` / `S00962`；`mikey-youtube-live-025-E0011-R077` / `S01275`；`mikey-youtube-live-025-E0011-R078` / `S01276`；`mikey-youtube-live-025-E0011-R083` / `S01281`。

`mikey-youtube-live-025-E0005-R059` / `S00663`（1660.26–1664.77秒），自动稿记录为："是支配游戏"。

`mikey-youtube-live-025-E0005-R060` / `S00664`（1664.77–1668.19秒），自动稿记录为："因为game本身就是一种支配与被支配的关系"。

原始引文计数为15；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-025-K016 · 性别概括

**原问题与概括：**能否根据性别断言对方愚蠢、不可信或一定慕强？ 本期多处把个别经历扩大成所有女性的智力、动机和可信度判断；这些是Mikey的立场性概括，证据不足，不得作为确定事实回答。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T13` / `P22`

**阻断review：**`mikey-youtube-live-025-R003`、`mikey-youtube-live-025-R008`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-025-E0003`、`mikey-youtube-live-025-E0011`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-025-E0003-R004` / `S00362`；`mikey-youtube-live-025-E0003-R005` / `S00363`；`mikey-youtube-live-025-E0003-R006` / `S00364`；`mikey-youtube-live-025-E0011-R033` / `S01231`；`mikey-youtube-live-025-E0011-R034` / `S01232`；`mikey-youtube-live-025-E0011-R040` / `S01238`；`mikey-youtube-live-025-E0011-R041` / `S01239`；`mikey-youtube-live-025-E0011-R088` / `S01286`；`mikey-youtube-live-025-E0011-R089` / `S01287`；`mikey-youtube-live-025-E0011-R090` / `S01288`。

`mikey-youtube-live-025-E0003-R004` / `S00362`（904.72–906.7秒），自动稿记录为："就是女人她们都没有那么聪明"。

`mikey-youtube-live-025-E0003-R005` / `S00363`（906.7–907.88秒），自动稿记录为："她们其实都是挺愚蠢"。

原始引文计数为10；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

### 来源 `mikey-youtube-live-026` · 直播79

#### mikey-youtube-live-026-K001 · 具体问题具体分析

**原问题与概括：**一个规律能解释所有约会问题吗？ Mikey明确反对把一个规律套到所有变量上，要求回到具体问题、当时状态和语境。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P07`、`P13`

**阻断review：**`mikey-youtube-live-026-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-026-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-026-E0004-R044` / `S00374`；`mikey-youtube-live-026-E0004-R045` / `S00375`；`mikey-youtube-live-026-E0004-R046` / `S00376`。

`mikey-youtube-live-026-E0004-R044` / `S00374`（923.32–926.0秒），自动稿记录为："这也是为什么我们讲具体问题"。

`mikey-youtube-live-026-E0004-R045` / `S00375`（926.0–926.82秒），自动稿记录为："要具体分析"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-026-K002 · 练习闭环

**原问题与概括：**新手为什么不能只收号？ 本期要求把搭讪延伸到聊天、邀约、约会和复盘；数量任务只是练习闭环的一部分。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03`、`T15` / `P29`

**阻断review：**`mikey-youtube-live-026-R004`

**原未知项：**每周三到四场是课程任务，不是所有人的通用指标

**原声明事件：**`mikey-youtube-live-026-E0004`、`mikey-youtube-live-026-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-026-E0004-R081` / `S00411`；`mikey-youtube-live-026-E0004-R082` / `S00412`；`mikey-youtube-live-026-E0004-R083` / `S00413`。

`mikey-youtube-live-026-E0004-R081` / `S00411`（1046.6–1048.9秒），自动稿记录为："他们每周至少要有三到四场约会"。

`mikey-youtube-live-026-E0004-R082` / `S00412`（1048.9–1051.04秒），自动稿记录为："每周就是我不管你有多忙"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-026-K003 · 技巧依赖语境

**原问题与概括：**为什么用了IOD仍然没效果？ 他强调IOD不是按下就生效的按钮，要看给法、双方状态和当时语境。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P07`、`P13`

**阻断review：**`mikey-youtube-live-026-R003`、`mikey-youtube-live-026-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-026-E0007`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-026-E0007-R092` / `S00722`；`mikey-youtube-live-026-E0007-R093` / `S00723`；`mikey-youtube-live-026-E0007-R095` / `S00725`；`mikey-youtube-live-026-E0007-R096` / `S00726`。

`mikey-youtube-live-026-E0007-R092` / `S00722`（1905.79–1934.19秒），自动稿记录为："麦哥为什么我给IOD没有用"。

`mikey-youtube-live-026-E0007-R093` / `S00723`（1934.19–1936.69秒），自动稿记录为："看看你是怎么给IOD的"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-026-K004 · 主心骨

**原问题与概括：**什么叫有主心骨？ 本期把主心骨描述为不因对方评价而丢失自己的判断、方向和行动标准。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02` / `P06`

**阻断review：**`mikey-youtube-live-026-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-026-E0011`

**本次追溯问题：**`TI008`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-026-E0012-R043` / `S01223`；`mikey-youtube-live-026-E0012-R044` / `S01224`；`mikey-youtube-live-026-E0012-R045` / `S01225`；`mikey-youtube-live-026-E0012-R046` / `S01226`。

`mikey-youtube-live-026-E0012-R043` / `S01223`（3796.56–3804.41秒），自动稿记录为："这个男的非常有主心骨"。

`mikey-youtube-live-026-E0012-R044` / `S01224`（3804.41–3805.53秒），自动稿记录为："他即便喜欢人气"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-026-K005 · 主动邀约

**原问题与概括：**对方服软后还要继续拉扯吗？ 他倾向于停止无意义拉扯，提出一次具体邀约，再根据对方实际回应决定。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 主动邀约条目的代表片段是多偶男性魅力评价，不能支持邀约步骤。

**主题 / 命题：**`T06` / `P15`

**阻断review：**`mikey-youtube-live-026-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-026-E0008`

**本次追溯问题：**`TI032`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-026-E0008-R032` / `S00762`；`mikey-youtube-live-026-E0008-R033` / `S00763`；`mikey-youtube-live-026-E0008-R034` / `S00764`。

`mikey-youtube-live-026-E0008-R032` / `S00762`（2055.69–2057.33秒），自动稿记录为："多偶的男人是最有魅力的"。

`mikey-youtube-live-026-E0008-R033` / `S00763`（2057.33–2059.81秒），自动稿记录为："就是多偶的男人是最有魅力的"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-026-K006 · 健康风险

**原问题与概括：**多伴侣下可以淡化艾滋和其他性病风险吗？ 本期对艾滋风险的回答过度轻描淡写。涉及性行为必须坚持屏障保护、检测、疫苗和专业医疗建议。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T12`、`T14` / `P28`

**阻断review：**`mikey-youtube-live-026-R003`、`mikey-youtube-live-026-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-026-E0007`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-026-E0007-R067` / `S00697`；`mikey-youtube-live-026-E0007-R084` / `S00714`。

`mikey-youtube-live-026-E0007-R067` / `S00697`（1851.65–1861.91秒），自动稿记录为："麦哥那么多约会怎么预防艾滋病"。

`mikey-youtube-live-026-E0007-R084` / `S00714`（1891.09–1892.95秒），自动稿记录为："就在担心我会不会得艾滋病啊"。

原始引文计数为2；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-026-K007 · 非安全性行为

**原问题与概括：**强势能否成为不戴套或让对方怀孕的理由？ 不能。本期把强势与不戴套、怀孕意愿相连的说法触及重大健康与同意风险，必须封存，不能转成行动建议。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 非安全性行为条目的代表片段偏向ATM、金钱和出轨，不能充当健康或避孕结论的逐字依据。

**主题 / 命题：**`T12`、`T14` / `P25`、`P28`

**阻断review：**`mikey-youtube-live-026-R002`、`mikey-youtube-live-026-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-026-E0003`

**本次追溯问题：**`TI033`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-026-E0003-R026` / `S00256`；`mikey-youtube-live-026-E0003-R027` / `S00257`；`mikey-youtube-live-026-E0003-R028` / `S00258`。

`mikey-youtube-live-026-E0003-R026` / `S00256`（627.81–629.03秒），自动稿记录为："她只会把你当ATMG"。

`mikey-youtube-live-026-E0003-R027` / `S00257`（629.03–630.67秒），自动稿记录为："然后拿你的钱去跟黄毛上床"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-026-K008 · 关系规则

**原问题与概括：**男性可以单方面保留多个伴侣而要求女性忠诚吗？ 本期有单边多偶和婚前协议设想；任何关系规则都只能在双方充分知情、自由同意且可退出时成立。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 关系规则条目的代表片段偏向金钱或随时可得，不足以独立还原完整双重标准。

**主题 / 命题：**`T08`、`T14` / `P20`、`P31`

**阻断review：**`mikey-youtube-live-026-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-026-E0010`

**本次追溯问题：**`TI034`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-026-E0010-R052` / `S01002`；`mikey-youtube-live-026-E0010-R053` / `S01003`；`mikey-youtube-live-026-E0010-R054` / `S01004`。

`mikey-youtube-live-026-E0010-R052` / `S01002`（3035.54–3037.34秒），自动稿记录为："你他妈的天天随叫随到"。

`mikey-youtube-live-026-E0010-R053` / `S01003`（3037.34–3039.44秒），自动稿记录为："女人要多少钱你给他多少钱"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-026-K009 · 长期目标

**原问题与概括：**为什么要有自己的长期方向？ 他把持续目标和创作完整性视为主心骨来源：生活不能只围着某次约会或外界反馈转。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 长期目标条目的代表片段谈婚后出轨及对方不可以，不能证明长期目标和创造的主张。

**主题 / 命题：**`T03`、`T09` / `P09`

**阻断review：**`mikey-youtube-live-026-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-026-E0011`、`mikey-youtube-live-026-E0012`

**本次追溯问题：**`TI035`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-026-E0011-R100` / `S01160`；`mikey-youtube-live-026-E0011-R101` / `S01161`；`mikey-youtube-live-026-E0011-R102` / `S01162`。

`mikey-youtube-live-026-E0011-R100` / `S01160`（3548.52–3550.1秒），自动稿记录为："就是你结婚你是可以出轨的"。

`mikey-youtube-live-026-E0011-R101` / `S01161`（3550.1–3550.6秒），自动稿记录为："他不可以"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

### 来源 `mikey-youtube-live-027` · 直播80

#### mikey-youtube-live-027-K001 · 主动学习

**原问题与概括：**记笔记为什么有用？ 他认为记笔记的价值不只是存档，而是迫使自己加工、思考并形成可复用判断。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P07`

**阻断review：**`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0001`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0001-R015` / `S00015`；`mikey-youtube-live-027-E0001-R016` / `S00016`。

`mikey-youtube-live-027-E0001-R015` / `S00015`（137.08–138.16秒），自动稿记录为："学习要记笔记"。

`mikey-youtube-live-027-E0001-R016` / `S00016`（138.16–140.98秒），自动稿记录为："你们记笔记"。

原始引文计数为2；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K002 · 练习闭环

**原问题与概括：**新手只练搭讪够吗？ 本期认为只搭讪不够，还要进入聊天、邀约、约会、录音复盘和下一轮调整。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03`、`T14` / `P08`、`P26`

**阻断review：**`mikey-youtube-live-027-R002`、`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0001`、`mikey-youtube-live-027-E0004`

**本次追溯问题：**`TI009`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0001-R079` / `S00079`；`mikey-youtube-live-027-E0002-R007` / `S00112`；`mikey-youtube-live-027-E0004-R005` / `S00315`。

`mikey-youtube-live-027-E0001-R079` / `S00079`（388.59–390.01秒），自动稿记录为："或者是搭了也约不出来"。

`mikey-youtube-live-027-E0002-R007` / `S00112`（441.28–469.81秒），自动稿记录为："关键你约不出来"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K003 · 框架

**原问题与概括：**框架要刻意建立吗？ Mikey回答需要刻意建立，但应通过现实互动和复盘稳定下来，不是在脑中机械背术语。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P07`

**阻断review：**`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0002-R048` / `S00153`；`mikey-youtube-live-027-E0002-R049` / `S00154`。

`mikey-youtube-live-027-E0002-R048` / `S00153`（621.59–628.78秒），自动稿记录为："框架要刻意建立吗"。

`mikey-youtube-live-027-E0002-R049` / `S00154`（628.78–630.68秒），自动稿记录为："框架肯定是要刻意建立的"。

原始引文计数为2；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K004 · 外语沟通

**原问题与概括：**用翻译器会显得弱吗？ 他认为工具本身不是问题，关键是使用时是否自卑、慌乱；工具不能替代真实理解和尊重。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04` / `P10`

**阻断review：**`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0003`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0003-R001` / `S00196`；`mikey-youtube-live-027-E0003-R002` / `S00197`；`mikey-youtube-live-027-E0003-R017` / `S00212`；`mikey-youtube-live-027-E0003-R025` / `S00220`。

`mikey-youtube-live-027-E0003-R001` / `S00196`（799.38–800.58秒），自动稿记录为："用翻译器聊老外"。

`mikey-youtube-live-027-E0003-R002` / `S00197`（800.58–801.68秒），自动稿记录为："就是你用翻译器"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K005 · 邀约诊断

**原问题与概括：**聊十天仍约不出来说明什么？ 本期把它视为聊天、吸引或展示面存在问题的信号，主张更早提出清楚邀约，再用实际回应诊断。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T05` / `P12`

**阻断review：**`mikey-youtube-live-027-R002`、`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0004-R027` / `S00337`；`mikey-youtube-live-027-E0004-R028` / `S00338`；`mikey-youtube-live-027-E0004-R033` / `S00343`。

`mikey-youtube-live-027-E0004-R027` / `S00337`（1250.49–1254.79秒），自动稿记录为："昨天约了四个女生全都说这周忙都聊了有十天以上了"。

`mikey-youtube-live-027-E0004-R028` / `S00338`（1254.79–1257.73秒），自动稿记录为："聊十天以上约不出来肯定是有问题"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K006 · 个性样本

**原问题与概括：**怎样表达个性才不是表演？ 个性样本应来自真实、稳定且有价值的特质；临时拼装一个强势人设很难持续。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T01` / `P01`、`P21`

**阻断review：**`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0005-R025` / `S00445`；`mikey-youtube-live-027-E0005-R028` / `S00448`；`mikey-youtube-live-027-E0005-R029` / `S00449`；`mikey-youtube-live-027-E0005-R031` / `S00451`；`mikey-youtube-live-027-E0005-R057` / `S00477`。

`mikey-youtube-live-027-E0005-R025` / `S00445`（1702.33–1714.88秒），自动稿记录为："传递个性样本是对吸引的决定性因素吗"。

`mikey-youtube-live-027-E0005-R028` / `S00448`（1719.42–1720.42秒），自动稿记录为："首先你的个性样本"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K007 · 被拒绝

**原问题与概括：**一次拒绝会自动让你掉价吗？ 他说拒绝本身不等于掉价，更影响表现的是拒绝后失态、纠缠或自我否定。拒绝后应停止推进。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07` / `P17`

**阻断review：**`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0008`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0008-R011` / `S00751`；`mikey-youtube-live-027-E0008-R012` / `S00752`；`mikey-youtube-live-027-E0008-R013` / `S00753`；`mikey-youtube-live-027-E0008-R015` / `S00755`；`mikey-youtube-live-027-E0008-R026` / `S00766`。

`mikey-youtube-live-027-E0008-R011` / `S00751`（2872.22–2873.94秒），自动稿记录为："如果被拒绝了会掉吸引吗"。

`mikey-youtube-live-027-E0008-R012` / `S00752`（2873.94–2875.78秒），自动稿记录为："被拒绝不会掉吸引"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K008 · 第一次约会

**原问题与概括：**第一次约会地点怎么选？ 本期倾向安静、能听清说话且双方都方便离开的场所，以便真实交流。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 第一次约会地点条目的代表片段未给出安静、友好或便于退出的地点判断。

**主题 / 命题：**`T06` / `P15`

**阻断review：**`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0008`

**本次追溯问题：**`TI036`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0008-R070` / `S00810`；`mikey-youtube-live-027-E0008-R071` / `S00811`；`mikey-youtube-live-027-E0008-R072` / `S00812`。

`mikey-youtube-live-027-E0008-R070` / `S00810`（3052.78–3053.66秒），自动稿记录为："但是不会掉吸引"。

`mikey-youtube-live-027-E0008-R071` / `S00811`（3053.66–3069.8秒），自动稿记录为："可以多举一些增加吸引和掉吸引的行为吗"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K009 · 信念行动循环

**原问题与概括：**怎样让自信逐渐变稳？ 他描述了信念影响行动、行动带来经验、经验再强化信念的循环；可通过小步行动和复盘累积。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 信念—行动循环条目的代表片段是是否继续直播的问答，不能证明该循环。

**主题 / 命题：**`T03`、`T15` / `P08`

**阻断review：**`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0009`

**本次追溯问题：**`TI037`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0009-R042` / `S00882`；`mikey-youtube-live-027-E0009-R043` / `S00883`；`mikey-youtube-live-027-E0009-R044` / `S00884`。

`mikey-youtube-live-027-E0009-R042` / `S00882`（3208.42–3209.8秒），自动稿记录为："还会给兄弟们播吗"。

`mikey-youtube-live-027-E0009-R043` / `S00883`（3209.8–3211.2秒），自动稿记录为："会啊"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K010 · 生活状态

**原问题与概括：**约会时能临场演出高状态吗？ 本期认为日常状态会延续到约会，长期没有方向和行动时，很难在现场稳定扮演另一个人。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 生活状态一致性条目的代表片段是零散“掉心瞬间/过渡期”表述，不足以独立展开机制。

**主题 / 命题：**`T01` / `P01`、`P21`

**阻断review：**`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0012`

**本次追溯问题：**`TI038`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0012-R042` / `S01172`；`mikey-youtube-live-027-E0012-R043` / `S01173`；`mikey-youtube-live-027-E0012-R044` / `S01174`。

`mikey-youtube-live-027-E0012-R042` / `S01172`（4073.46–4074.72秒），自动稿记录为："掉心是一瞬间的事"。

`mikey-youtube-live-027-E0012-R043` / `S01173`（4074.72–4076.36秒），自动稿记录为："我感觉这种事情是一个过渡期"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K011 · 渐进练习

**原问题与概括：**遇到不敢接近的人怎么办？ 可以从压力较低的场景逐步练习；任何明确拒绝都应立即停止。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 渐进练习条目的代表片段侧重坐着聊天的行为线索，不能据此还原完整练习方案。

**主题 / 命题：**`T03` / `P08`

**阻断review：**`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0013`

**本次追溯问题：**`TI039`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0013-R010` / `S01210`；`mikey-youtube-live-027-E0013-R011` / `S01211`；`mikey-youtube-live-027-E0013-R012` / `S01212`。

`mikey-youtube-live-027-E0013-R010` / `S01210`（4198.7–4263.03秒），自动稿记录为："强行无线索从言谈举止就完全够了"。

`mikey-youtube-live-027-E0013-R011` / `S01211`（4263.03–4264.51秒），自动稿记录为："就你跟他坐着聊天的"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-027-K012 · 婚外情与剥削

**原问题与概括：**可以把婚外情、皮条或让对方失去底线当成吸引方法吗？ 不能。本期相关段落触及欺骗、剥削和群体贬损，只保留为人物立场证据，不作为建议。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 婚外情与剥削条目的代表片段不足以独立支持概括；原do_not_generalize仍保留，不能因引文不足反向洗白。

**主题 / 命题：**`T08`、`T13`、`T14` / `P31`

**阻断review：**`mikey-youtube-live-027-R001`、`mikey-youtube-live-027-R003`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-027-E0007`

**本次追溯问题：**`TI040`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-027-E0007-R020` / `S00650`；`mikey-youtube-live-027-E0007-R021` / `S00651`；`mikey-youtube-live-027-E0007-R022` / `S00652`。

`mikey-youtube-live-027-E0007-R020` / `S00650`（2306.3–2318.03秒），自动稿记录为："它是大于长相的"。

`mikey-youtube-live-027-E0007-R021` / `S00651`（2318.03–2319.93秒），自动稿记录为："麦哥很多女的一直跟我说"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

### 来源 `mikey-youtube-live-028` · 直播81

#### mikey-youtube-live-028-K001 · 线上邀约

**原问题与概括：**线上聊到什么程度可以邀约？ 本期认为先确认双方是真实、正常且有基本交流意愿，就可以提出清楚、低压力、可拒绝的邀约。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 线上邀约条目的代表片段转入新观众提示，不能证明身份确认、意愿或具体邀约流程。

**主题 / 命题：**`T06` / `P15`

**阻断review：**`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0001`

**本次追溯问题：**`TI041`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0001-R060` / `S00060`；`mikey-youtube-live-028-E0001-R061` / `S00061`；`mikey-youtube-live-028-E0001-R062` / `S00062`。

`mikey-youtube-live-028-E0001-R060` / `S00060`（823.14–824.42秒），自动稿记录为："很简单"。

`mikey-youtube-live-028-E0001-R061` / `S00061`（824.42–832.02秒），自动稿记录为："新来的兄弟们都点这里"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K002 · 实践脱敏

**原问题与概括：**怎样减少对高质量对象的紧张？ 他倾向用真实、尊重边界的接触逐步脱敏，而不是无限学习后等待完全不紧张。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P08`

**阻断review：**`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0005-R070` / `S00520`；`mikey-youtube-live-028-E0005-R071` / `S00521`；`mikey-youtube-live-028-E0005-R072` / `S00522`。

`mikey-youtube-live-028-E0005-R070` / `S00520`（1958.5–1961.62秒），自动稿记录为："内核锻炼内核的最好方式"。

`mikey-youtube-live-028-E0005-R071` / `S00521`（1961.62–1963.34秒），自动稿记录为："就是多跟很屌的女生约会"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K003 · 三秒原则

**原问题与概括：**每犹豫一秒成功率就下降20%吗？ 本期给出三秒和20%的说法，但没有证据。可把它理解为减少反刍的提醒，不能当作统计规律。

**原发布状态：** `hold`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**原hold未获解除。 关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03`、`T15` / `P29`

**阻断review：**`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0005`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0005-R048` / `S00498`；`mikey-youtube-live-028-E0005-R049` / `S00499`；`mikey-youtube-live-028-E0005-R059` / `S00509`。

`mikey-youtube-live-028-E0005-R048` / `S00498`（1837.95–1889.98秒），自动稿记录为："麦克哥你觉得搭讪的时候三秒元都重要吗"。

`mikey-youtube-live-028-E0005-R049` / `S00499`（1889.98–1891.6秒），自动稿记录为："三秒元则非常重要"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K004 · 一致性

**原问题与概括：**线上线下为什么不要突然变一个人？ 他强调前后人设和行为的一致性：线上展示、聊天和线下相处差异过大，会降低可信度。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T01` / `P01`

**阻断review：**`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0006-R003` / `S00563`；`mikey-youtube-live-028-E0006-R016` / `S00576`；`mikey-youtube-live-028-E0006-R017` / `S00577`。

`mikey-youtube-live-028-E0006-R003` / `S00563`（2079.8–2081.06秒），自动稿记录为："就是我们讲的一致性"。

`mikey-youtube-live-028-E0006-R016` / `S00576`（2102.61–2103.97秒），自动稿记录为："为什么因为一致性变了"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K005 · 关系边界

**原问题与概括：**伴侣与他人暧昧时怎么做？ 本期更可用的部分是明确说出自己的边界；对方不接受时可以离开，而不是靠监控、羞辱或强迫改变。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 关系边界条目的代表片段是声音状态及零散伴侣话题，不能证明完整处理方法。

**主题 / 命题：**`T07` / `P18`

**阻断review：**`mikey-youtube-live-028-R002`、`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0008`

**本次追溯问题：**`TI042`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0008-R060` / `S00840`；`mikey-youtube-live-028-E0008-R061` / `S00841`；`mikey-youtube-live-028-E0008-R062` / `S00842`。

`mikey-youtube-live-028-E0008-R060` / `S00840`（2962.84–2963.94秒），自动稿记录为："那个话就会非常的糊"。

`mikey-youtube-live-028-E0008-R061` / `S00841`（2963.94–2979.6秒），自动稿记录为："我今天搭上了很多女生都说自己有对象"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K006 · 收号跟进

**原问题与概括：**为什么收了很多号却没有结果？ 如果拿到联系方式后长期不聊天、不邀约、不复盘，收号本身不会自动转化为约会能力。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。 收号跟进条目的代表片段谈租住与带回家，不能独立支持全链路诊断。

**主题 / 命题：**`T05`、`T15` / `P12`

**阻断review：**`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0009`

**本次追溯问题：**`TI043`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0009-R050` / `S00940`；`mikey-youtube-live-028-E0009-R051` / `S00941`；`mikey-youtube-live-028-E0009-R052` / `S00942`。

`mikey-youtube-live-028-E0009-R050` / `S00940`（3262.32–3268.75秒），自动稿记录为："租的房子很一般"。

`mikey-youtube-live-028-E0009-R051` / `S00941`（3268.75–3269.69秒），自动稿记录为："怎么带到家里"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K007 · 主体性

**原问题与概括：**怎样减少外界评价对自己的控制？ 本期可用核心是把自己的判断、目标和行动放回中心，不把每个外界标签都当最终裁判。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02`、`T13` / `P06`、`P30`

**阻断review：**`mikey-youtube-live-028-R003`、`mikey-youtube-live-028-R004`

**原未知项：**NPC比喻含去人化风险

**原声明事件：**`mikey-youtube-live-028-E0010`、`mikey-youtube-live-028-E0011`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0010-R127` / `S01127`；`mikey-youtube-live-028-E0010-R128` / `S01128`；`mikey-youtube-live-028-E0011-R009` / `S01137`；`mikey-youtube-live-028-E0011-R035` / `S01163`。

`mikey-youtube-live-028-E0010-R127` / `S01127`（3897.16–3898.72秒），自动稿记录为："从冷静的主体性"。

`mikey-youtube-live-028-E0010-R128` / `S01128`（3898.72–3901.6秒），自动稿记录为："但是如何让我们建立这样的主体性呢"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K008 · NPC比喻

**原问题与概括：**可以真的把所有人当没有主体的NPC吗？ 不能。本期多次把别人、尤其女性称为NPC并只看作性价值，属于去人化立场，必须封存。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T13` / `P04`、`P30`

**阻断review：**`mikey-youtube-live-028-R003`、`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0011`、`mikey-youtube-live-028-E0012`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0011-R066` / `S01194`；`mikey-youtube-live-028-E0011-R075` / `S01203`；`mikey-youtube-live-028-E0011-R081` / `S01209`；`mikey-youtube-live-028-E0012-R014` / `S01264`；`mikey-youtube-live-028-E0012-R015` / `S01265`。

`mikey-youtube-live-028-E0011-R066` / `S01194`（4050.21–4052.65秒），自动稿记录为："给予的所有人都是NPC"。

`mikey-youtube-live-028-E0011-R075` / `S01203`（4067.51–4069.67秒），自动稿记录为："我遇到的每一个NPC"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K009 · 原生家庭

**原问题与概括：**原生家庭的影响能改变吗？ 他承认早期教育会留下长期模式，但认为通过新经历、实践和复盘可以逐步改写。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T12` / `P28`

**阻断review：**`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0013`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0013-R027` / `S01409`；`mikey-youtube-live-028-E0013-R031` / `S01413`。

`mikey-youtube-live-028-E0013-R027` / `S01409`（4582.46–4618.26秒），自动稿记录为："男人的性格与原生家庭教育方式很大吗"。

`mikey-youtube-live-028-E0013-R031` / `S01413`（4621.24–4624.14秒），自动稿记录为："你的原生家庭过去20年"。

原始引文计数为2；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K010 · 上头与稀缺

**原问题与概括：**拿到一次结果后为什么反而上头？ 本期把它解释为稀缺感和对自身能力不信任：觉得这次机会不可复制，于是过度依附。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T12` / `P28`

**阻断review：**`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0013`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0013-R042` / `S01424`；`mikey-youtube-live-028-E0013-R045` / `S01427`；`mikey-youtube-live-028-E0013-R048` / `S01430`。

`mikey-youtube-live-028-E0013-R042` / `S01424`（4640.74–4683.77秒），自动稿记录为："麦格拿到结果后自己上头"。

`mikey-youtube-live-028-E0013-R045` / `S01427`（4690.69–4693.01秒），自动稿记录为："拿到结果后自己上头"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K011 · 离开与压抑

**原问题与概括：**不回怼直接离开算软弱吗？ 他区分真正不在乎后离开，与表面忍住、事后持续反刍。判断标准是边界是否清楚、情绪是否仍被对方控制。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07` / `P18`

**阻断review：**`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0014`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0014-R017` / `S01481`；`mikey-youtube-live-028-E0014-R019` / `S01483`。

`mikey-youtube-live-028-E0014-R017` / `S01481`（4835.21–4836.75秒），自动稿记录为："一种是不在乎"。

`mikey-youtube-live-028-E0014-R019` / `S01483`（4837.81–4839.09秒），自动稿记录为："但是我要假装不在乎"。

原始引文计数为2；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-028-K012 · 欺骗与同意

**原问题与概括：**能否用‘上传文件’等借口把对方带上楼再推进？ 不能。隐瞒真实目的会破坏知情同意；对方排斥身体接触时必须停止。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08`、`T14` / `P20`、`P25`、`P26`

**阻断review：**`mikey-youtube-live-028-R002`、`mikey-youtube-live-028-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-028-E0003`、`mikey-youtube-live-028-E0007`

**本次追溯问题：**`TI010`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-028-E0007-R035` / `S00705`；`mikey-youtube-live-028-E0007-R036` / `S00706`；`mikey-youtube-live-028-E0008-R041` / `S00821`。

`mikey-youtube-live-028-E0007-R035` / `S00705`（2591.18–2592.72秒），自动稿记录为："上传文件"。

`mikey-youtube-live-028-E0007-R036` / `S00706`（2592.72–2593.88秒），自动稿记录为："文件上传文件之后"。

原始引文计数为3；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

### 来源 `mikey-youtube-live-029` · 直播82

#### mikey-youtube-live-029-K001 · 独立思考

**原问题与概括：**看了很多视频后遇事只会套答案怎么办？ Mikey建议先自己思考、尝试，再用他人的答案校对；学习的目标是举一反三，不是把大脑变成话术检索器。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02` / `P06`

**阻断review：**`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0001`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0001-R127` / `S00127`；`mikey-youtube-live-029-E0001-R130` / `S00130`；`mikey-youtube-live-029-E0001-R141` / `S00141`；`mikey-youtube-live-029-E0001-R147` / `S00147`；`mikey-youtube-live-029-E0001-R150` / `S00150`；`mikey-youtube-live-029-E0001-R152` / `S00152`。

`mikey-youtube-live-029-E0001-R127` / `S00127`（512.44–529.92秒），自动稿记录为："我现在视频看多了"。

`mikey-youtube-live-029-E0001-R130` / `S00130`（531.58–533.42秒），自动稿记录为："不是自主思考如何解决"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K002 · 昂贵消费

**原问题与概括：**第一次约会对方指定昂贵餐厅怎么办？ 本期更可用的边界是：不熟时不必接受超出预算或让你不舒服的安排，可以提出普通替代方案或让提出方承担。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T06`、`T09` / `P19`

**阻断review：**`mikey-youtube-live-029-R004`

**原未知项：**不要据此断言对方一定拜金

**原声明事件：**`mikey-youtube-live-029-E0001`、`mikey-youtube-live-029-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0001-R043` / `S00043`；`mikey-youtube-live-029-E0001-R045` / `S00045`；`mikey-youtube-live-029-E0001-R056` / `S00056`；`mikey-youtube-live-029-E0004-R129` / `S00549`；`mikey-youtube-live-029-E0004-R132` / `S00552`；`mikey-youtube-live-029-E0004-R133` / `S00553`。

`mikey-youtube-live-029-E0001-R043` / `S00043`（339.38–341.9秒），自动稿记录为："女生说要去一个很贵的地方"。

`mikey-youtube-live-029-E0001-R045` / `S00045`（344.16–346.16秒），自动稿记录为："她本质上她是在做一种筛选"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K003 · 前任比较

**原问题与概括：**对方一直讲优秀前任怎么办？ 他选择不进入比较，不用证明自己比前任强；可以简短回应后转回当下相处。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02` / `P34`

**阻断review：**`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0002-R002` / `S00161`；`mikey-youtube-live-029-E0002-R014` / `S00173`；`mikey-youtube-live-029-E0002-R024` / `S00183`；`mikey-youtube-live-029-E0002-R030` / `S00189`。

`mikey-youtube-live-029-E0002-R002` / `S00161`（602.57–604.53秒），自动稿记录为："首先女生说这些东西"。

`mikey-youtube-live-029-E0002-R014` / `S00173`（628.0–629.22秒），自动稿记录为："对挺好"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K004 · 荒谬检验

**原问题与概括：**少见就等于有吸引力吗？ 他用荒谬反例指出‘物以稀为贵’不能单独证明某行为有吸引力；还要看行为本身传递什么。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T05`、`T15` / `P11`、`P32`

**阻断review：**`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0002-R063` / `S00222`；`mikey-youtube-live-029-E0002-R068` / `S00227`；`mikey-youtube-live-029-E0002-R073` / `S00232`；`mikey-youtube-live-029-E0002-R078` / `S00237`；`mikey-youtube-live-029-E0002-R079` / `S00238`。

`mikey-youtube-live-029-E0002-R063` / `S00222`（762.15–764.21秒），自动稿记录为："你要想一想物以稀为贵"。

`mikey-youtube-live-029-E0002-R068` / `S00227`（771.49–772.91秒），自动稿记录为："突然在桌上拉屎呢"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K005 · 搭讪恐惧

**原问题与概括：**从不敢开口到开始行动怎么做？ 本期读出一名观众从两次到五次尝试的经历，强调先完成可控的小步行动，再看结果和复盘。该经历属于观众，不是Mikey亲历。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03`、`T15` / `P08`、`P29`

**阻断review：**`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0003`

**本次追溯问题：**`TI058`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0003-R004` / `S00326`；`mikey-youtube-live-029-E0003-R006` / `S00328`；`mikey-youtube-live-029-E0003-R008` / `S00330`；`mikey-youtube-live-029-E0003-R010` / `S00332`；`mikey-youtube-live-029-E0003-R012` / `S00334`；`mikey-youtube-live-029-E0003-R015` / `S00337`。

`mikey-youtube-live-029-E0003-R004` / `S00326`（1304.28–1305.48秒），自动稿记录为："看你直播快一年了"。

`mikey-youtube-live-029-E0003-R006` / `S00328`（1307.1–1310.24秒），自动稿记录为："上周咖啡厅跟一个女生对视很久不敢出手"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K006 · 关系表达

**原问题与概括：**长期不确定关系为什么消耗？ 他认为不敢表达真实意图、又害怕失去，会把关系拖进长期模糊。可用部分是诚实说明期望，并允许对方拒绝。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08` / `P20`

**阻断review：**`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0003`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0003-R062` / `S00384`；`mikey-youtube-live-029-E0003-R064` / `S00386`；`mikey-youtube-live-029-E0003-R067` / `S00389`；`mikey-youtube-live-029-E0003-R068` / `S00390`。

`mikey-youtube-live-029-E0003-R062` / `S00384`（1881.22–1937.64秒），自动稿记录为："Mikey常常会谈成长期不确定关系的那种"。

`mikey-youtube-live-029-E0003-R064` / `S00386`（1938.76–1942.48秒），自动稿记录为："其实是因为懦弱"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K007 · 真实表达

**原问题与概括：**讨好和情绪价值有什么问题？ 本期认为先伪装深情、再索取回报会制造不一致；更稳的是从一开始真实表达能提供什么、想要什么。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08` / `P20`

**阻断review：**`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0004-R137` / `S00557`；`mikey-youtube-live-029-E0004-R142` / `S00562`；`mikey-youtube-live-029-E0004-R168` / `S00588`；`mikey-youtube-live-029-E0004-R172` / `S00592`；`mikey-youtube-live-029-E0004-R178` / `S00598`。

`mikey-youtube-live-029-E0004-R137` / `S00557`（2544.64–2545.74秒），自动稿记录为："如果你的人设呢"。

`mikey-youtube-live-029-E0004-R142` / `S00562`（2551.34–2553.38秒），自动稿记录为："那如果你给自己立的人设"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K008 · 兴趣与生活

**原问题与概括：**个人兴趣能否成为约会内容？ 乐高等真实兴趣可以提供共同活动和生活感，但邀请到家与性推进必须另行取得清楚同意。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T04`、`T09` / `P21`

**阻断review：**`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0005`、`mikey-youtube-live-029-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0005-R118` / `S00718`；`mikey-youtube-live-029-E0005-R122` / `S00722`；`mikey-youtube-live-029-E0005-R123` / `S00723`；`mikey-youtube-live-029-E0005-R130` / `S00730`。

`mikey-youtube-live-029-E0005-R118` / `S00718`（3307.21–3309.61秒），自动稿记录为："就是我去国外买了图纸"。

`mikey-youtube-live-029-E0005-R122` / `S00722`（3325.8–3330.86秒），自动稿记录为："我现在经常就是把女生带到家里面"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K009 · 电话演示

**原问题与概括：**直播中的电话能直接当作通用聊天模板吗？ 不能。后半段是多名来电者、直播节目效果和未完全确认的公开授权；说话人也未逐句分离，只能作为待核案例。

**原发布状态：** `hold`；**原归属：** `mixed_speakers`；**综合使用：** `hold`。

**使用理由：**原hold未获解除。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T11`、`T14` / `P24`、`P26`

**阻断review：**`mikey-youtube-live-029-R002`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0007`、`mikey-youtube-live-029-E0008`、`mikey-youtube-live-029-E0009`、`mikey-youtube-live-029-E0010`、`mikey-youtube-live-029-E0011`、`mikey-youtube-live-029-E0012`、`mikey-youtube-live-029-E0014`

**本次追溯问题：**`TI056`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0007-R010` / `S00971`；`mikey-youtube-live-029-E0008-R008` / `S01014`；`mikey-youtube-live-029-E0009-R031` / `S01177`；`mikey-youtube-live-029-E0009-R042` / `S01188`；`mikey-youtube-live-029-E0011-R038` / `S01431`；`mikey-youtube-live-029-E0014-R060` / `S01921`。

`mikey-youtube-live-029-E0007-R010` / `S00971`（4325.21–4375.8秒），自动稿记录为："喂"。

`mikey-youtube-live-029-E0008-R008` / `S01014`（4591.58–4593.46秒），自动稿记录为："天天发一直发给你们看一下"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K010 · 持续同意

**原问题与概括：**对方说不要、要睡觉或时间不确定时还能继续施压吗？ 不能。拒绝、犹豫和条件性回答都不是同意，应停止性推进；之后若双方重新明确同意再另行安排。

**原发布状态：** `do_not_generalize`；**原归属：** `mixed_speakers`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08`、`T11`、`T14` / `P24`、`P25`

**阻断review：**`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0011`、`mikey-youtube-live-029-E0012`

**本次追溯问题：**`TI056`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0011-R163` / `S01556`；`mikey-youtube-live-029-E0011-R164` / `S01557`；`mikey-youtube-live-029-E0012-R001` / `S01559`；`mikey-youtube-live-029-E0012-R074` / `S01632`；`mikey-youtube-live-029-E0012-R075` / `S01633`。

`mikey-youtube-live-029-E0011-R163` / `S01556`（6894.8–6896.34秒），自动稿记录为："哎呀不我们今晚就打泡吧"。

`mikey-youtube-live-029-E0011-R164` / `S01557`（6897.62–6898.9秒），自动稿记录为："不要我要睡觉"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K011 · 支配与辱骂

**原问题与概括：**辱骂、逼迫、四肢着地或性化羞辱能否当作吸引方法？ 不能。本期相关故事存在胁迫、去人化和同意不明，必须封存，不能从结果倒推方法有效。

**原发布状态：** `do_not_generalize`；**原归属：** `mixed_speakers`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 原归属为mixed_speakers，不能归为Mikey独立主张。 关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08`、`T11`、`T14` / `P06`、`P24`、`P25`、`P31`

**阻断review：**`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R003`、`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0006`、`mikey-youtube-live-029-E0011`、`mikey-youtube-live-029-E0012`、`mikey-youtube-live-029-E0013`

**本次追溯问题：**`TI056`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0006-R121` / `S00880`；`mikey-youtube-live-029-E0006-R122` / `S00881`；`mikey-youtube-live-029-E0006-R123` / `S00882`；`mikey-youtube-live-029-E0011-R059` / `S01452`；`mikey-youtube-live-029-E0011-R083` / `S01476`；`mikey-youtube-live-029-E0013-R018` / `S01758`。

`mikey-youtube-live-029-E0006-R121` / `S00880`（3931.9–3934.08秒），自动稿记录为："然后有一天我他妈直接怒了"。

`mikey-youtube-live-029-E0006-R122` / `S00881`（3934.08–3935.56秒），自动稿记录为："我给他打电话我直接骂他"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-029-K012 · 性别与体型羞辱

**原问题与概括：**能否用个别经历推断女性没有底线，或用体型辱骂别人？ 不能。这些是攻击性群体概括和羞辱，不是可靠事实或建设性建议。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T13` / `P22`

**阻断review：**`mikey-youtube-live-029-R001`、`mikey-youtube-live-029-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-029-E0001`、`mikey-youtube-live-029-E0006`、`mikey-youtube-live-029-E0013`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-029-E0001-R027` / `S00027`；`mikey-youtube-live-029-E0001-R030` / `S00030`；`mikey-youtube-live-029-E0006-R106` / `S00865`；`mikey-youtube-live-029-E0013-R050` / `S01790`；`mikey-youtube-live-029-E0013-R059` / `S01799`。

`mikey-youtube-live-029-E0001-R027` / `S00027`（285.11–287.41秒），自动稿记录为："你会发现他们其实也就那么回事"。

`mikey-youtube-live-029-E0001-R030` / `S00030`（290.67–293.33秒），自动稿记录为："还要没有底线"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

### 来源 `mikey-youtube-live-030` · 直播83

#### mikey-youtube-live-030-K001 · 讨好动机

**原问题与概括：**礼貌和讨好怎么区分？ 本期区分真诚礼貌与带着隐性索取的讨好：如果表面顺从只是为了换取性或认可，它不是稳定善良。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08` / `P20`

**阻断review：**`mikey-youtube-live-030-R001`、`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0001`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0001-R055` / `S00055`；`mikey-youtube-live-030-E0001-R060` / `S00060`；`mikey-youtube-live-030-E0001-R064` / `S00064`；`mikey-youtube-live-030-E0001-R070` / `S00070`；`mikey-youtube-live-030-E0001-R083` / `S00083`；`mikey-youtube-live-030-E0001-R086` / `S00086`。

`mikey-youtube-live-030-E0001-R055` / `S00055`（349.29–354.52秒），自动稿记录为："其实那不是你礼貌善良的人格"。

`mikey-youtube-live-030-E0001-R060` / `S00060`（374.38–378.26秒），自动稿记录为："你讨好她是为了什么"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K002 · 拒绝与人格

**原问题与概括：**搭讪被拒绝是否等于整个人被否定？ 他强调陌生人的拒绝只说明这次互动没有成立，不足以判定你全部人格和价值。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02`、`T07` / `P04`、`P17`

**阻断review：**`mikey-youtube-live-030-R001`、`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0001`、`mikey-youtube-live-030-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0001-R151` / `S00151`；`mikey-youtube-live-030-E0001-R152` / `S00152`；`mikey-youtube-live-030-E0001-R153` / `S00153`；`mikey-youtube-live-030-E0002-R001` / `S00156`；`mikey-youtube-live-030-E0002-R002` / `S00157`；`mikey-youtube-live-030-E0002-R015` / `S00170`。

`mikey-youtube-live-030-E0001-R151` / `S00151`（585.32–590.1秒），自动稿记录为："不敢搭讪是因为你在深层次"。

`mikey-youtube-live-030-E0001-R152` / `S00152`（590.1–595.1秒），自动稿记录为："你认为就是被拒绝代表你这个人的人格被否定了"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K003 · 实事求是

**原问题与概括：**陷入情绪合理化时怎么拉回来？ 本期给出的短问题是‘事实是什么’：先把可观察事实、自己的解释和希望结果分开。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02` / `P32`

**阻断review：**`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0002-R021` / `S00176`；`mikey-youtube-live-030-E0002-R022` / `S00177`；`mikey-youtube-live-030-E0002-R025` / `S00180`；`mikey-youtube-live-030-E0002-R026` / `S00181`；`mikey-youtube-live-030-E0002-R027` / `S00182`；`mikey-youtube-live-030-E0002-R028` / `S00183`。

`mikey-youtube-live-030-E0002-R021` / `S00176`（665.43–667.61秒），自动稿记录为："实事求是"。

`mikey-youtube-live-030-E0002-R022` / `S00177`（667.61–669.85秒），自动稿记录为："你就不会有RQ精神"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K004 · 上台紧张

**原问题与概括：**为什么面对评委会紧张？ 他认为把台下的人当成能决定自我价值的裁判，会放大紧张；一次演讲失败只代表这次表现失败。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02` / `P04`

**阻断review：**`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0002-R049` / `S00204`；`mikey-youtube-live-030-E0002-R051` / `S00206`；`mikey-youtube-live-030-E0002-R054` / `S00209`；`mikey-youtube-live-030-E0002-R065` / `S00220`；`mikey-youtube-live-030-E0002-R067` / `S00222`；`mikey-youtube-live-030-E0002-R068` / `S00223`。

`mikey-youtube-live-030-E0002-R049` / `S00204`（722.3–726.17秒），自动稿记录为："为什么你会紧张"。

`mikey-youtube-live-030-E0002-R051` / `S00206`（728.01–730.81秒），自动稿记录为："你就把他们台下的所有观众"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K005 · NPC比喻

**原问题与概括：**NPC比喻可怎样安全使用？ 只能把它当作‘别人无权决定你的全部价值’的临时比喻，不能真的否认他人的主体、边界和感受。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02`、`T13` / `P04`、`P30`

**阻断review：**`mikey-youtube-live-030-R004`

**原未知项：**后续把人比作宠物的段落不能一般化

**原声明事件：**`mikey-youtube-live-030-E0002`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0002-R056` / `S00211`；`mikey-youtube-live-030-E0002-R059` / `S00214`；`mikey-youtube-live-030-E0002-R060` / `S00215`；`mikey-youtube-live-030-E0002-R061` / `S00216`。

`mikey-youtube-live-030-E0002-R056` / `S00211`（741.0–742.5秒），自动稿记录为："就是把他们当NPC就行了"。

`mikey-youtube-live-030-E0002-R059` / `S00214`（748.86–751.66秒），自动稿记录为："是为了让你意识到"。

原始引文计数为4；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K006 · 价值与价值感

**原问题与概括：**有钱有条件为什么仍会自卑？ 本期区分客观资源与自我价值感；后者是对自己的基本认可，不能完全依赖每次外界反馈。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T02` / `P05`

**阻断review：**`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0003`、`mikey-youtube-live-030-E0007`、`mikey-youtube-live-030-E0008`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0003-R005` / `S00271`；`mikey-youtube-live-030-E0003-R007` / `S00273`；`mikey-youtube-live-030-E0003-R014` / `S00280`；`mikey-youtube-live-030-E0003-R071` / `S00337`；`mikey-youtube-live-030-E0003-R072` / `S00338`；`mikey-youtube-live-030-E0007-R092` / `S00767`；`mikey-youtube-live-030-E0007-R096` / `S00771`；`mikey-youtube-live-030-E0008-R051` / `S00860`；`mikey-youtube-live-030-E0008-R056` / `S00865`。

`mikey-youtube-live-030-E0003-R005` / `S00271`（911.88–918.0秒），自动稿记录为："首先我们讲过就是价值不等于价值感"。

`mikey-youtube-live-030-E0003-R007` / `S00273`（920.96–922.2秒），自动稿记录为："他们是有价值的"。

原始引文计数为9；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K007 · 眼神

**原问题与概括：**搭讪时眼神要凶还是温柔？ Mikey回答不必刻意凶或讨好，更重要的是正常、稳定和坚定。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T01`、`T04` / `P02`、`P10`

**阻断review：**`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0003`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0003-R087` / `S00353`；`mikey-youtube-live-030-E0003-R089` / `S00355`；`mikey-youtube-live-030-E0003-R094` / `S00360`；`mikey-youtube-live-030-E0003-R096` / `S00362`；`mikey-youtube-live-030-E0003-R097` / `S00363`；`mikey-youtube-live-030-E0003-R100` / `S00366`。

`mikey-youtube-live-030-E0003-R087` / `S00353`（1124.2–1128.08秒），自动稿记录为："Mike搭讪的时候"。

`mikey-youtube-live-030-E0003-R089` / `S00355`（1129.64–1130.56秒），自动稿记录为："你就正常就行了"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K008 · 抗压

**原问题与概括：**抗压能力怎么提升？ 本期把抗压与经历和复盘相连；更稳的做法是逐步增加难度，而不是一次把自己扔进不可控风险。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P08`

**阻断review：**`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0004`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0004-R019` / `S00393`；`mikey-youtube-live-030-E0004-R020` / `S00394`；`mikey-youtube-live-030-E0004-R021` / `S00395`；`mikey-youtube-live-030-E0004-R041` / `S00415`；`mikey-youtube-live-030-E0004-R042` / `S00416`。

`mikey-youtube-live-030-E0004-R019` / `S00393`（1299.88–1304.78秒），自动稿记录为："怎么提升抗压性"。

`mikey-youtube-live-030-E0004-R020` / `S00394`（1304.78–1306.0秒），自动稿记录为："你经历的事情多了"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K009 · 边界与离开

**原问题与概括：**为了得到关系是否应放弃标准？ 他认为为了得到性而跪求、灌酒或不择手段会失去尊严；可用原则是保留标准、愿意离开，并坚持清楚同意。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T07`、`T08`、`T14` / `P18`、`P25`

**阻断review：**`mikey-youtube-live-030-R002`、`mikey-youtube-live-030-R003`、`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0005`、`mikey-youtube-live-030-E0006`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0005-R075` / `S00520`；`mikey-youtube-live-030-E0005-R078` / `S00523`；`mikey-youtube-live-030-E0005-R079` / `S00524`；`mikey-youtube-live-030-E0006-R063` / `S00615`；`mikey-youtube-live-030-E0006-R065` / `S00617`；`mikey-youtube-live-030-E0006-R103` / `S00655`；`mikey-youtube-live-030-E0006-R104` / `S00656`；`mikey-youtube-live-030-E0006-R106` / `S00658`。

`mikey-youtube-live-030-E0005-R075` / `S00520`（1725.82–1730.06秒），自动稿记录为："而不是一种就是开游的心态"。

`mikey-youtube-live-030-E0005-R078` / `S00523`（1731.64–1736.0秒），自动稿记录为："你灌酒也好"。

原始引文计数为8；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K010 · 选择与承诺

**原问题与概括：**有选择再专一和被迫专一有什么区别？ 本期强调承诺应来自主动选择，而不是为缺少选择编理由；同时承诺是否成立仍要看双方约定和实际行动。

**原发布状态：** `context_only`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联2项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08`、`T09` / `P20`

**阻断review：**`mikey-youtube-live-030-R001`、`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0001`、`mikey-youtube-live-030-E0010`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0001-R101` / `S00101`；`mikey-youtube-live-030-E0001-R107` / `S00107`；`mikey-youtube-live-030-E0001-R120` / `S00120`；`mikey-youtube-live-030-E0001-R121` / `S00121`；`mikey-youtube-live-030-E0010-R040` / `S01042`；`mikey-youtube-live-030-E0010-R042` / `S01044`。

`mikey-youtube-live-030-E0001-R101` / `S00101`（456.63–458.47秒），自动稿记录为："那比如说有些人说我专一"。

`mikey-youtube-live-030-E0001-R107` / `S00107`（462.95–465.65秒），自动稿记录为："你是因为没有的选"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K011 · 深度学习

**原问题与概括：**为什么只看案例成长有限？ 他认为单个聊天或实战案例容易被照抄，深度内容更关注判断、原因和迁移；两者应结合。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03` / `P07`

**阻断review：**`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0007`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0007-R050` / `S00725`；`mikey-youtube-live-030-E0007-R052` / `S00727`；`mikey-youtube-live-030-E0007-R056` / `S00731`；`mikey-youtube-live-030-E0007-R057` / `S00732`；`mikey-youtube-live-030-E0007-R058` / `S00733`。

`mikey-youtube-live-030-E0007-R050` / `S00725`（2230.75–2232.45秒），自动稿记录为："什么实在案例"。

`mikey-youtube-live-030-E0007-R052` / `S00727`（2232.81–2233.71秒），自动稿记录为："聊天案例讲解"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K012 · 成长复盘

**原问题与概括：**Mikey怎样解释自己的变化？ 他把变化归于经历很多事情、持续思考并反复复盘，而不是某一个瞬间的技巧。

**原发布状态：** `direct`；**原归属：** `explicit_mikey`；**综合使用：** `hold`。

**使用理由：**关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T03`、`T15` / `P08`、`P29`

**阻断review：**`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0013`

**本次追溯问题：**无

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0013-R023` / `S01317`；`mikey-youtube-live-030-E0013-R024` / `S01318`；`mikey-youtube-live-030-E0013-R025` / `S01319`；`mikey-youtube-live-030-E0013-R026` / `S01320`；`mikey-youtube-live-030-E0013-R027` / `S01321`。

`mikey-youtube-live-030-E0013-R023` / `S01317`（4039.38–4041.38秒），自动稿记录为："有太多契机了"。

`mikey-youtube-live-030-E0013-R024` / `S01318`（4041.38–4043.38秒），自动稿记录为："经历了很多事情"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K013 · 支配与同意

**原问题与概括：**‘支配’能否等同让对方服从或在未反抗时脱衣？ 不能。服从不是关系价值，未反抗也不等于同意；相关段落必须封存，任何身体接触都需要清楚、持续、可撤回同意。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联3项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T08`、`T14` / `P06`、`P25`、`P31`

**阻断review：**`mikey-youtube-live-030-R002`、`mikey-youtube-live-030-R003`、`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0005`、`mikey-youtube-live-030-E0006`

**本次追溯问题：**`TI058`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0005-R014` / `S00459`；`mikey-youtube-live-030-E0005-R020` / `S00465`；`mikey-youtube-live-030-E0006-R058` / `S00610`；`mikey-youtube-live-030-E0006-R059` / `S00611`；`mikey-youtube-live-030-E0006-R060` / `S00612`。

`mikey-youtube-live-030-E0005-R014` / `S00459`（1560.56–1563.12秒），自动稿记录为："什么是吸引 吸引本质也是支配"。

`mikey-youtube-live-030-E0005-R020` / `S00465`（1582.23–1584.27秒），自动稿记录为："赢得她对你的服从"。

原始引文计数为5；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

#### mikey-youtube-live-030-K014 · 群体贬损

**原问题与概括：**能否说女性不懂事业、某职业都不能碰或外国人更有优势？ 不能。这些是未经证据支持的群体概括，只能保留为人物立场证据。

**原发布状态：** `do_not_generalize`；**原归属：** `explicit_mikey`；**综合使用：** `do_not_generalize`。

**使用理由：**原do_not_generalize原样保留，只作限制/争议定位，不能生成行动建议。 关联1项开放待核（显式知识/事件/证据关联），整条暂不拆分放行；major仍保留原级别，但在本输出中同样构成使用阻断。

**主题 / 命题：**`T13` / `P22`

**阻断review：**`mikey-youtube-live-030-R004`

**原未知项：**无

**原声明事件：**`mikey-youtube-live-030-E0009`、`mikey-youtube-live-030-E0010`、`mikey-youtube-live-030-E0012`、`mikey-youtube-live-030-E0013`

**本次追溯问题：**`TI058`

<details><summary>完整引用ID与原样代表自动稿</summary>

原引用记录：`mikey-youtube-live-030-E0009-R026` / `S00936`；`mikey-youtube-live-030-E0009-R030` / `S00940`；`mikey-youtube-live-030-E0010-R016` / `S01018`；`mikey-youtube-live-030-E0010-R018` / `S01020`；`mikey-youtube-live-030-E0013-R011` / `S01305`；`mikey-youtube-live-030-E0013-R013` / `S01307`。

`mikey-youtube-live-030-E0009-R026` / `S00936`（2815.74–2819.38秒），自动稿记录为："这就导致了任何一个黑人"。

`mikey-youtube-live-030-E0009-R030` / `S00940`（2823.62–2825.66秒），自动稿记录为："都可以睡到很多中国女人"。

原始引文计数为6；本条只附2条代表原文，其他正文不补写。完整原URL和字段见JSON原样档案。

</details>

## 14. 仍需本地解决的全部原待核

63项原待核全部保留：47 blocking、16 major。这里列出原任务和实际受控知识；相关时间窗仍是原值，发现错位的TI条目必须先对照，不能直接按错窗裁掉风险。

### mikey-youtube-live-021-R001 · major / open

**原时间窗：**481–565秒

**原问题：**暴力犯罪与搭讪边界是否被错误理解成对任何接触方式的法律背书？

**原要求证据：**法律与安全边界审查

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-021-E0002`、`mikey-youtube-live-021-K003`

**本综合阻断的知识：**`mikey-youtube-live-021-K001`、`mikey-youtube-live-021-K002`、`mikey-youtube-live-021-K003`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-021-E0002-R098` → https://www.youtube.com/watch?v=gkADT8_5s14&t=518s；`mikey-youtube-live-021-E0002-R118` → https://www.youtube.com/watch?v=gkADT8_5s14&t=546s；`mikey-youtube-live-021-E0002-R119` → https://www.youtube.com/watch?v=gkADT8_5s14&t=548s。

### mikey-youtube-live-021-R002 · blocking / open

**原时间窗：**601–725秒

**原问题：**隐瞒第二天离开、以‘看你表现’推进关系的案例是否构成欺骗或不当操控？

**原要求证据：**伦理边界及原音画复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-021-E0003`

**本综合阻断的知识：**`mikey-youtube-live-021-K004`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-021-E0003-R001` → https://www.youtube.com/watch?v=gkADT8_5s14&t=601s；`mikey-youtube-live-021-E0003-R007` → https://www.youtube.com/watch?v=gkADT8_5s14&t=611s；`mikey-youtube-live-021-E0003-R009` → https://www.youtube.com/watch?v=gkADT8_5s14&t=615s；`mikey-youtube-live-021-E0003-R013` → https://www.youtube.com/watch?v=gkADT8_5s14&t=619s。

### mikey-youtube-live-021-R003 · major / open

**原时间窗：**795–895秒

**原问题：**80%至100%成功率和性结果数字是否仅为自述且不应作为用户基准？

**原要求证据：**来源与统计边界审查

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-021-E0003`、`mikey-youtube-live-021-K004`

**本综合阻断的知识：**`mikey-youtube-live-021-K004`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-021-E0003-R056` → https://www.youtube.com/watch?v=gkADT8_5s14&t=805s；`mikey-youtube-live-021-E0003-R062` → https://www.youtube.com/watch?v=gkADT8_5s14&t=813s；`mikey-youtube-live-021-E0003-R071` → https://www.youtube.com/watch?v=gkADT8_5s14&t=832s；`mikey-youtube-live-021-E0003-R072` → https://www.youtube.com/watch?v=gkADT8_5s14&t=834s。

### mikey-youtube-live-021-R004 · blocking / open

**原时间窗：**1270–1450秒

**原问题：**女性类型概括及‘骂她／治她’措辞是否会导向羞辱、威胁或冲突升级？

**原要求证据：**安全与编辑边界审查

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-021-E0005`、`mikey-youtube-live-021-K009`

**本综合阻断的知识：**`mikey-youtube-live-021-K007`、`mikey-youtube-live-021-K008`、`mikey-youtube-live-021-K009`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-021-E0005-R047` → https://www.youtube.com/watch?v=gkADT8_5s14&t=1339s；`mikey-youtube-live-021-E0005-R055` → https://www.youtube.com/watch?v=gkADT8_5s14&t=1354s；`mikey-youtube-live-021-E0005-R075` → https://www.youtube.com/watch?v=gkADT8_5s14&t=1397s；`mikey-youtube-live-021-E0005-R086` → https://www.youtube.com/watch?v=gkADT8_5s14&t=1416s；`mikey-youtube-live-021-E0005-R100` → https://www.youtube.com/watch?v=gkADT8_5s14&t=1449s。

### mikey-youtube-live-021-R005 · major / open

**原时间窗：**1710–1810秒

**原问题：**护肤品、激素和‘三天就好’是否为未经核验的医学绝对判断？

**原要求证据：**医疗专业审查

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-021-E0006`、`mikey-youtube-live-021-K012`

**本综合阻断的知识：**`mikey-youtube-live-021-K007`、`mikey-youtube-live-021-K010`、`mikey-youtube-live-021-K011`、`mikey-youtube-live-021-K012`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-021-E0006-R087` → https://www.youtube.com/watch?v=gkADT8_5s14&t=1722s；`mikey-youtube-live-021-E0006-R097` → https://www.youtube.com/watch?v=gkADT8_5s14&t=1741s；`mikey-youtube-live-021-E0006-R100` → https://www.youtube.com/watch?v=gkADT8_5s14&t=1744s；`mikey-youtube-live-021-E0006-R101` → https://www.youtube.com/watch?v=gkADT8_5s14&t=1746s。

### mikey-youtube-live-021-R006 · blocking / open

**原时间窗：**2030–2410秒

**原问题：**武汉大学事件的人名、录音、行为和责任描述是否准确，能否承载后续群体结论？

**原要求证据：**原始事件资料、原音和编辑审查

**原责任方：**fact-review

**原affected_ids：**`mikey-youtube-live-021-E0007`、`mikey-youtube-live-021-E0008`

**本综合阻断的知识：**`mikey-youtube-live-021-K013`

**时间/追溯问题：**`TI011`

原证据地址：`mikey-youtube-live-021-E0007-R070` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2026s；`mikey-youtube-live-021-E0008-R020` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2135s；`mikey-youtube-live-021-E0008-R046` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2184s；`mikey-youtube-live-021-E0008-R089` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2250s；`mikey-youtube-live-021-E0008-R106` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2273s。

### mikey-youtube-live-021-R007 · blocking / open

**原时间窗：**2100–2750秒

**原问题：**对犹太人、女性主义者、保安及阶级问题的概括是否可普遍化？

**原要求证据：**跨来源与编辑边界审查

**原责任方：**editorial-review

**原affected_ids：**`mikey-youtube-live-021-E0008`、`mikey-youtube-live-021-E0009`

**本综合阻断的知识：**`mikey-youtube-live-021-K014`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-021-E0008-R007` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2111s；`mikey-youtube-live-021-E0008-R142` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2340s；`mikey-youtube-live-021-E0009-R028` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2461s；`mikey-youtube-live-021-E0009-R036` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2485s。

### mikey-youtube-live-021-R008 · blocking / open

**原时间窗：**2820–3010秒

**原问题：**饮酒后前往私密空间的情境是否具备清醒、自愿、持续同意和安全返回条件？

**原要求证据：**连续音画、聊天原图及同意边界审查

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-021-E0010`、`mikey-youtube-live-021-K015`

**本综合阻断的知识：**`mikey-youtube-live-021-K014`、`mikey-youtube-live-021-K015`、`mikey-youtube-live-021-K016`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-021-E0010-R039` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2840s；`mikey-youtube-live-021-E0010-R046` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2852s；`mikey-youtube-live-021-E0010-R056` → https://www.youtube.com/watch?v=gkADT8_5s14&t=2870s。

### mikey-youtube-live-021-R009 · blocking / open

**原时间窗：**3020–3640秒

**原问题：**酒店、肢体升级和直接邀请的建议是否明确允许拒绝且不得施压？

**原要求证据：**持续同意与安全边界审查

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-021-E0011`、`mikey-youtube-live-021-E0012`

**本综合阻断的知识：**`mikey-youtube-live-021-K017`、`mikey-youtube-live-021-K018`、`mikey-youtube-live-021-K019`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-021-E0011-R004` → https://www.youtube.com/watch?v=gkADT8_5s14&t=3026s；`mikey-youtube-live-021-E0011-R018` → https://www.youtube.com/watch?v=gkADT8_5s14&t=3056s；`mikey-youtube-live-021-E0012-R044` → https://www.youtube.com/watch?v=gkADT8_5s14&t=3617s。

### mikey-youtube-live-022-R001 · major / open

**原时间窗：**6–6020秒

**原问题：**Mikey、面具参与者和第三名门徒的逐句发言边界是什么？

**原要求证据：**原音、连续嘴型和已确认身份参照片段；必要时声纹映射

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-022-E0001`、`mikey-youtube-live-022-E0002`、`mikey-youtube-live-022-E0003`、`mikey-youtube-live-022-E0004`、`mikey-youtube-live-022-E0005`、`mikey-youtube-live-022-E0006`、`mikey-youtube-live-022-E0007`、`mikey-youtube-live-022-E0008`、`mikey-youtube-live-022-E0009`、`mikey-youtube-live-022-E0010`、`mikey-youtube-live-022-E0011`、`mikey-youtube-live-022-E0012`、`mikey-youtube-live-022-E0013`、`mikey-youtube-live-022-E0014`、`mikey-youtube-live-022-E0015`、`mikey-youtube-live-022-E0016`、`mikey-youtube-live-022-K001`、`mikey-youtube-live-022-K002`、`mikey-youtube-live-022-K003`、`mikey-youtube-live-022-K004`、`mikey-youtube-live-022-K005`、`mikey-youtube-live-022-K006`、`mikey-youtube-live-022-K007`、`mikey-youtube-live-022-K008`、`mikey-youtube-live-022-K009`、`mikey-youtube-live-022-K010`、`mikey-youtube-live-022-K011`、`mikey-youtube-live-022-K012`、`mikey-youtube-live-022-K013`、`mikey-youtube-live-022-K014`、`mikey-youtube-live-022-K015`、`mikey-youtube-live-022-K016`、`mikey-youtube-live-022-K017`、`mikey-youtube-live-022-K018`

**本综合阻断的知识：**`mikey-youtube-live-022-K001`、`mikey-youtube-live-022-K002`、`mikey-youtube-live-022-K003`、`mikey-youtube-live-022-K004`、`mikey-youtube-live-022-K005`、`mikey-youtube-live-022-K006`、`mikey-youtube-live-022-K007`、`mikey-youtube-live-022-K008`、`mikey-youtube-live-022-K009`、`mikey-youtube-live-022-K010`、`mikey-youtube-live-022-K011`、`mikey-youtube-live-022-K012`、`mikey-youtube-live-022-K013`、`mikey-youtube-live-022-K014`、`mikey-youtube-live-022-K015`、`mikey-youtube-live-022-K016`、`mikey-youtube-live-022-K017`、`mikey-youtube-live-022-K018`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-022-E0001-R051` → https://www.youtube.com/watch?v=dZgV_s1FVv8&t=154s；`mikey-youtube-live-022-E0003-R001` → https://www.youtube.com/watch?v=dZgV_s1FVv8&t=672s；`mikey-youtube-live-022-E0008-R101` → https://www.youtube.com/watch?v=dZgV_s1FVv8&t=2748s；`mikey-youtube-live-022-E0014-R041` → https://www.youtube.com/watch?v=dZgV_s1FVv8&t=5224s。

### mikey-youtube-live-022-R002 · blocking / open

**原时间窗：**1540–1700秒

**原问题：**别天神、改变意识和接受性交的段落由谁提出，是否明确是戏谑或反讽？

**原要求证据：**原音语气与上下文连续听校

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-022-E0005`、`mikey-youtube-live-022-K006`

**本综合阻断的知识：**`mikey-youtube-live-022-K005`、`mikey-youtube-live-022-K006`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-022-E0005-R091` → https://www.youtube.com/watch?v=dZgV_s1FVv8&t=1583s。

### mikey-youtube-live-022-R003 · blocking / open

**原时间窗：**3090–3240秒

**原问题：**洗脑、精神控制和邪教领袖类比的具体发言人与评价方向是什么？

**原要求证据：**原音和发言人物确认

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-022-E0009`、`mikey-youtube-live-022-K011`

**本综合阻断的知识：**`mikey-youtube-live-022-K011`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-022-E0009-R081` → https://www.youtube.com/watch?v=dZgV_s1FVv8&t=3161s。

### mikey-youtube-live-022-R004 · blocking / open

**原时间窗：**4130–4300秒

**原问题：**雷影、喝酒和给钱的情节是赞同、调侃还是角色设想？

**原要求证据：**原音语气、前后文和人物归属

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-022-E0012`、`mikey-youtube-live-022-K014`

**本综合阻断的知识：**`mikey-youtube-live-022-K014`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-022-E0012-R011` → https://www.youtube.com/watch?v=dZgV_s1FVv8&t=4185s。

### mikey-youtube-live-022-R005 · major / open

**原时间窗：**0–6020秒

**原问题：**未人工查看的联系表及稀疏间隙是否有手机聊天截图、动漫正片或其他承载教学信息的画面？

**原要求证据：**剩余联系表与必要连续窗口视觉复核

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-022-E0001`、`mikey-youtube-live-022-E0002`、`mikey-youtube-live-022-E0003`、`mikey-youtube-live-022-E0004`、`mikey-youtube-live-022-E0005`、`mikey-youtube-live-022-E0006`、`mikey-youtube-live-022-E0007`、`mikey-youtube-live-022-E0008`、`mikey-youtube-live-022-E0009`、`mikey-youtube-live-022-E0010`、`mikey-youtube-live-022-E0011`、`mikey-youtube-live-022-E0012`、`mikey-youtube-live-022-E0013`、`mikey-youtube-live-022-E0014`、`mikey-youtube-live-022-E0015`、`mikey-youtube-live-022-E0016`

**本综合阻断的知识：**`mikey-youtube-live-022-K001`、`mikey-youtube-live-022-K002`、`mikey-youtube-live-022-K003`、`mikey-youtube-live-022-K004`、`mikey-youtube-live-022-K005`、`mikey-youtube-live-022-K006`、`mikey-youtube-live-022-K007`、`mikey-youtube-live-022-K008`、`mikey-youtube-live-022-K009`、`mikey-youtube-live-022-K010`、`mikey-youtube-live-022-K011`、`mikey-youtube-live-022-K012`、`mikey-youtube-live-022-K013`、`mikey-youtube-live-022-K014`、`mikey-youtube-live-022-K015`、`mikey-youtube-live-022-K016`、`mikey-youtube-live-022-K017`、`mikey-youtube-live-022-K018`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-022-E0001-R001` → https://www.youtube.com/watch?v=dZgV_s1FVv8&t=6s；`mikey-youtube-live-022-E0016-R021` → https://www.youtube.com/watch?v=dZgV_s1FVv8&t=5948s。

### mikey-youtube-live-023-R001 · major / open

**原时间窗：**210–370秒

**原问题：**把陌生搭讪比作给路人发钱是否会弱化对方拒绝和不愿被接触的权利？

**原要求证据：**编辑边界复核

**原责任方：**editorial-review

**原affected_ids：**`mikey-youtube-live-023-E0001`、`mikey-youtube-live-023-K002`

**本综合阻断的知识：**`mikey-youtube-live-023-K001`、`mikey-youtube-live-023-K002`、`mikey-youtube-live-023-K003`、`mikey-youtube-live-023-K004`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0001-R066` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=245s；`mikey-youtube-live-023-E0001-R075` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=266s；`mikey-youtube-live-023-E0001-R078` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=270s；`mikey-youtube-live-023-E0001-R087` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=286s。

### mikey-youtube-live-023-R002 · major / open

**原时间窗：**470–540秒

**原问题：**用政治制度作逻辑自洽类比是否准确，是否需要从可执行知识中移除？

**原要求证据：**语义与事实边界复核

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-023-E0001`、`mikey-youtube-live-023-K004`

**本综合阻断的知识：**`mikey-youtube-live-023-K001`、`mikey-youtube-live-023-K002`、`mikey-youtube-live-023-K003`、`mikey-youtube-live-023-K004`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0001-R166` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=488s；`mikey-youtube-live-023-E0001-R176` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=508s；`mikey-youtube-live-023-E0001-R179` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=513s；`mikey-youtube-live-023-E0001-R183` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=522s。

### mikey-youtube-live-023-R003 · blocking / open

**原时间窗：**1730–1840秒

**原问题：**疫情期间大量性经历为单方自述，是否存在身份、同意、数量或ASR错误？

**原要求证据：**原音、连续画面和来源复核

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-023-E0005`

**本综合阻断的知识：**`mikey-youtube-live-023-K012`、`mikey-youtube-live-023-K013`、`mikey-youtube-live-023-K025`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0005-R039` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=1732s；`mikey-youtube-live-023-E0005-R042` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=1737s；`mikey-youtube-live-023-E0005-R050` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=1748s；`mikey-youtube-live-023-E0005-R055` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=1754s；`mikey-youtube-live-023-E0005-R057` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=1757s。

### mikey-youtube-live-023-R004 · blocking / open

**原时间窗：**1800–2050秒

**原问题：**NPC、战略蔑视与‘教女人做人’是否会被误用为不尊重现实他人或攻击性控制？

**原要求证据：**安全与编辑边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-023-E0005`、`mikey-youtube-live-023-K008`、`mikey-youtube-live-023-K012`

**本综合阻断的知识：**`mikey-youtube-live-023-K008`、`mikey-youtube-live-023-K012`、`mikey-youtube-live-023-K013`、`mikey-youtube-live-023-K025`

**时间/追溯问题：**`TI012`

原证据地址：`mikey-youtube-live-023-E0005-R070` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=1783s；`mikey-youtube-live-023-E0005-R073` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=1800s；`mikey-youtube-live-023-E0005-R098` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=1891s；`mikey-youtube-live-023-E0005-R102` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=1900s；`mikey-youtube-live-023-E0005-R162` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2003s；`mikey-youtube-live-023-E0005-R174` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2023s。

### mikey-youtube-live-023-R005 · blocking / open

**原时间窗：**2050–2200秒

**原问题：**按‘灵魂伴侣／解决生理需求’分类的说法是否缺少诚实、尊重和持续同意？

**原要求证据：**关系目标、同意与安全边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-023-E0005`、`mikey-youtube-live-023-E0006`、`mikey-youtube-live-023-K025`

**本综合阻断的知识：**`mikey-youtube-live-023-K004`、`mikey-youtube-live-023-K012`、`mikey-youtube-live-023-K013`、`mikey-youtube-live-023-K014`、`mikey-youtube-live-023-K015`、`mikey-youtube-live-023-K025`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0005-R206` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2090s；`mikey-youtube-live-023-E0006-R001` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2100s；`mikey-youtube-live-023-E0006-R006` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2110s；`mikey-youtube-live-023-E0006-R012` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2124s；`mikey-youtube-live-023-E0006-R013` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2126s。

### mikey-youtube-live-023-R006 · blocking / open

**原时间窗：**2390–2460秒

**原问题：**把不给钱与获得性结果对比是否会把亲密关系商品化或形成不当因果？

**原要求证据：**编辑和因果边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-023-E0006`、`mikey-youtube-live-023-K015`

**本综合阻断的知识：**`mikey-youtube-live-023-K004`、`mikey-youtube-live-023-K013`、`mikey-youtube-live-023-K014`、`mikey-youtube-live-023-K015`、`mikey-youtube-live-023-K025`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0006-R120` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2406s；`mikey-youtube-live-023-E0006-R127` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2424s；`mikey-youtube-live-023-E0006-R129` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2426s；`mikey-youtube-live-023-E0006-R136` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2436s。

### mikey-youtube-live-023-R007 · blocking / open

**原时间窗：**2610–2810秒

**原问题：**前任关系和‘复仇式拿下’自述是否应全部限制为不可执行材料？

**原要求证据：**原音与安全边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-023-E0007`、`mikey-youtube-live-023-K025`

**本综合阻断的知识：**`mikey-youtube-live-023-K010`、`mikey-youtube-live-023-K014`、`mikey-youtube-live-023-K025`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0007-R029` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2633s；`mikey-youtube-live-023-E0007-R031` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2637s；`mikey-youtube-live-023-E0007-R035` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2646s；`mikey-youtube-live-023-E0007-R064` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2765s；`mikey-youtube-live-023-E0007-R067` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2787s；`mikey-youtube-live-023-E0007-R070` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=2792s。

### mikey-youtube-live-023-R008 · blocking / open

**原时间窗：**3270–3330秒

**原问题：**对只想发生性关系的人直接说露骨提议是否具备成年人、诚实、自愿和可退出条件？

**原要求证据：**年龄、同意和情境复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-023-E0008`、`mikey-youtube-live-023-K025`

**本综合阻断的知识：**`mikey-youtube-live-023-K016`、`mikey-youtube-live-023-K017`、`mikey-youtube-live-023-K018`、`mikey-youtube-live-023-K019`、`mikey-youtube-live-023-K025`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0008-R096` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3287s；`mikey-youtube-live-023-E0008-R098` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3297s；`mikey-youtube-live-023-E0008-R099` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3299s；`mikey-youtube-live-023-E0009-R002` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3303s。

### mikey-youtube-live-023-R009 · major / open

**原时间窗：**3690–3950秒

**原问题：**把使用‘普信’的人一律解释为自卑、羡慕是否是无证据动机归因？

**原要求证据：**编辑边界复核

**原责任方：**editorial-review

**原affected_ids：**`mikey-youtube-live-023-E0010`、`mikey-youtube-live-023-K020`

**本综合阻断的知识：**`mikey-youtube-live-023-K019`、`mikey-youtube-live-023-K020`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0010-R075` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3849s；`mikey-youtube-live-023-E0010-R076` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3853s；`mikey-youtube-live-023-E0010-R080` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3859s；`mikey-youtube-live-023-E0010-R082` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3864s；`mikey-youtube-live-023-E0010-R093` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3886s；`mikey-youtube-live-023-E0010-R095` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=3890s。

### mikey-youtube-live-023-R010 · blocking / open

**原时间窗：**4020–4140秒

**原问题：**对杭州、成都和小城市女性的性职业、智力、阶层概括是否应禁止一般化？

**原要求证据：**来源与歧视性概括复核

**原责任方：**editorial-review

**原affected_ids：**`mikey-youtube-live-023-E0011`

**本综合阻断的知识：**`mikey-youtube-live-023-K021`、`mikey-youtube-live-023-K022`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0011-R042` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4053s；`mikey-youtube-live-023-E0011-R046` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4065s；`mikey-youtube-live-023-E0011-R047` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4068s；`mikey-youtube-live-023-E0011-R070` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4098s；`mikey-youtube-live-023-E0011-R071` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4098s；`mikey-youtube-live-023-E0011-R075` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4106s。

### mikey-youtube-live-023-R011 · blocking / open

**原时间窗：**4120–4300秒

**原问题：**观众提到初高中生且主持人后续说‘外校可以’，是否可能绕过未成年人及职业权力边界？

**原要求证据：**年龄、法律和职业伦理复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-023-E0011`、`mikey-youtube-live-023-K022`

**本综合阻断的知识：**`mikey-youtube-live-023-K008`、`mikey-youtube-live-023-K011`、`mikey-youtube-live-023-K021`、`mikey-youtube-live-023-K022`、`mikey-youtube-live-023-K023`

**时间/追溯问题：**`TI013`

原证据地址：`mikey-youtube-live-023-E0011-R076` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4108s；`mikey-youtube-live-023-E0011-R078` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4123s；`mikey-youtube-live-023-E0011-R083` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4131s；`mikey-youtube-live-023-E0011-R089` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4140s；`mikey-youtube-live-023-E0012-R027` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4269s；`mikey-youtube-live-023-E0012-R031` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4284s；`mikey-youtube-live-023-E0012-R032` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=4287s。

### mikey-youtube-live-023-R012 · blocking / open

**原时间窗：**5150–5200秒

**原问题：**换号重加或直接电话是否是在绕过明确拉黑，能否作为错误示范彻底隔离？

**原要求证据：**安全与持续联系边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-023-E0014`、`mikey-youtube-live-023-K024`

**本综合阻断的知识：**`mikey-youtube-live-023-K024`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-023-E0014-R012` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=5156s；`mikey-youtube-live-023-E0014-R014` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=5158s；`mikey-youtube-live-023-E0014-R016` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=5160s；`mikey-youtube-live-023-E0014-R018` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=5162s；`mikey-youtube-live-023-E0014-R019` → https://www.youtube.com/watch?v=wjizzSk9eAI&t=5165s。

### mikey-youtube-live-024-R001 · blocking / open

**原时间窗：**1180–1810秒

**原问题：**家暴经历、基因决定和反脆弱人格是否构成未经支持的创伤与遗传结论？

**原要求证据：**原音、个案边界和心理专业复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-024-E0003`、`mikey-youtube-live-024-K005`

**本综合阻断的知识：**`mikey-youtube-live-024-K005`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-024-E0003-R165` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=1556s；`mikey-youtube-live-024-E0003-R183` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=1585s；`mikey-youtube-live-024-E0003-R202` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=1624s；`mikey-youtube-live-024-E0003-R203` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=1627s；`mikey-youtube-live-024-E0003-R205` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=1630s；`mikey-youtube-live-024-E0003-R208` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=1636s；`mikey-youtube-live-024-E0003-R238` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=1694s；`mikey-youtube-live-024-E0003-R284` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=1778s；`mikey-youtube-live-024-E0003-R291` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=1791s。

### mikey-youtube-live-024-R002 · blocking / open

**原时间窗：**2580–3335秒

**原问题：**用说服、虚假承诺对比和‘CPU烧了’推进性交是否绕过清楚持续同意？

**原要求证据：**成年人、持续同意和安全边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-024-E0005`、`mikey-youtube-live-024-E0006`、`mikey-youtube-live-024-E0007`、`mikey-youtube-live-024-K011`

**本综合阻断的知识：**`mikey-youtube-live-024-K002`、`mikey-youtube-live-024-K008`、`mikey-youtube-live-024-K009`、`mikey-youtube-live-024-K010`、`mikey-youtube-live-024-K011`、`mikey-youtube-live-024-K012`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-024-E0005-R114` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=2726s；`mikey-youtube-live-024-E0005-R118` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=2733s；`mikey-youtube-live-024-E0005-R121` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=2737s；`mikey-youtube-live-024-E0006-R077` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3192s；`mikey-youtube-live-024-E0006-R080` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3211s；`mikey-youtube-live-024-E0006-R096` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3234s；`mikey-youtube-live-024-E0006-R111` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3264s；`mikey-youtube-live-024-E0006-R113` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3266s；`mikey-youtube-live-024-E0006-R124` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3288s；`mikey-youtube-live-024-E0007-R004` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3307s；`mikey-youtube-live-024-E0007-R007` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3312s。

### mikey-youtube-live-024-R003 · blocking / open

**原时间窗：**3380–3550秒

**原问题：**安全套、艾滋和其他性病风险说法是否为严重医学错误并污名化患者？

**原要求证据：**权威医学来源复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-024-E0007`、`mikey-youtube-live-024-K012`

**本综合阻断的知识：**`mikey-youtube-live-024-K010`、`mikey-youtube-live-024-K011`、`mikey-youtube-live-024-K012`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-024-E0007-R050` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3394s；`mikey-youtube-live-024-E0007-R052` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3397s；`mikey-youtube-live-024-E0007-R054` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3400s；`mikey-youtube-live-024-E0007-R057` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3405s；`mikey-youtube-live-024-E0007-R064` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3417s；`mikey-youtube-live-024-E0007-R067` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3422s；`mikey-youtube-live-024-E0007-R090` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3459s；`mikey-youtube-live-024-E0007-R104` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3496s。

### mikey-youtube-live-024-R004 · blocking / open

**原时间窗：**3900–4140秒

**原问题：**对特朗普视频和撞人等内容是事实、玩笑、引用还是ASR错误？

**原要求证据：**原音、原视频和事实核查

**原责任方：**fact-review

**原affected_ids：**`mikey-youtube-live-024-E0008`

**本综合阻断的知识：**`mikey-youtube-live-024-K013`、`mikey-youtube-live-024-K014`

**时间/追溯问题：**`TI014`

原证据地址：`mikey-youtube-live-024-E0008-R051` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3867s；`mikey-youtube-live-024-E0008-R053` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=3875s；`mikey-youtube-live-024-E0008-R113` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4060s；`mikey-youtube-live-024-E0008-R119` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4072s；`mikey-youtube-live-024-E0008-R120` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4073s。

### mikey-youtube-live-024-R005 · major / open

**原时间窗：**4000–4380秒

**原问题：**把网暴者一律归为弱者并把网暴当成功证明，是否会掩盖真实越界和安全风险？

**原要求证据：**安全和编辑边界复核

**原责任方：**editorial-review

**原affected_ids：**`mikey-youtube-live-024-E0008`、`mikey-youtube-live-024-K014`

**本综合阻断的知识：**`mikey-youtube-live-024-K013`、`mikey-youtube-live-024-K014`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-024-E0008-R093` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4013s；`mikey-youtube-live-024-E0008-R099` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4030s；`mikey-youtube-live-024-E0008-R103` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4039s；`mikey-youtube-live-024-E0008-R104` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4041s；`mikey-youtube-live-024-E0008-R123` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4080s；`mikey-youtube-live-024-E0008-R125` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4084s；`mikey-youtube-live-024-E0008-R145` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4127s；`mikey-youtube-live-024-E0008-R149` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4135s；`mikey-youtube-live-024-E0008-R157` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4154s。

### mikey-youtube-live-024-R006 · blocking / open

**原时间窗：**4550–4800秒

**原问题：**性关系后让对方离开、把不同意视为必须接纳自己的二选一，是否缺少事前沟通和安全照顾？

**原要求证据：**同意、住宿和安全边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-024-E0009`

**本综合阻断的知识：**无

**时间/追溯问题：**`TI015`

原证据地址：`mikey-youtube-live-024-E0009-R021` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4239s；`mikey-youtube-live-024-E0009-R023` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4241s；`mikey-youtube-live-024-E0009-R034` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4267s；`mikey-youtube-live-024-E0009-R040` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4276s；`mikey-youtube-live-024-E0009-R046` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4284s；`mikey-youtube-live-024-E0009-R065` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4307s。

### mikey-youtube-live-024-R007 · blocking / open

**原时间窗：**5080–5160秒

**原问题：**换号或电话绕过拉黑是否应完全禁止用于建议？

**原要求证据：**持续联系与骚扰边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-024-E0010`、`mikey-youtube-live-024-K016`

**本综合阻断的知识：**`mikey-youtube-live-024-K016`

**时间/追溯问题：**`TI016`

原证据地址：`mikey-youtube-live-024-E0010-R024` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4562s；`mikey-youtube-live-024-E0010-R029` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4570s；`mikey-youtube-live-024-E0010-R030` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4572s；`mikey-youtube-live-024-E0010-R032` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4576s；`mikey-youtube-live-024-E0010-R033` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4578s。

### mikey-youtube-live-024-R008 · blocking / open

**原时间窗：**5580–5670秒

**原问题：**后续再次用‘戴套就行’回答疾病风险是否必须阻断？

**原要求证据：**医学与风险复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-024-E0010`、`mikey-youtube-live-024-K012`

**本综合阻断的知识：**`mikey-youtube-live-024-K012`、`mikey-youtube-live-024-K016`

**时间/追溯问题：**`TI017`

原证据地址：`mikey-youtube-live-024-E0010-R075` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4683s；`mikey-youtube-live-024-E0010-R076` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=4689s。

### mikey-youtube-live-024-R009 · major / open

**原时间窗：**6010–6080秒

**原问题：**用‘不够文艺／读书少’使对方怀疑自己来接受性话题，是否属于操控？

**原要求证据：**同意与沟通边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-024-E0011`

**本综合阻断的知识：**`mikey-youtube-live-024-K015`

**时间/追溯问题：**`TI018`

原证据地址：`mikey-youtube-live-024-E0011-R111` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5079s；`mikey-youtube-live-024-E0011-R112` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5081s；`mikey-youtube-live-024-E0011-R116` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5090s；`mikey-youtube-live-024-E0012-R003` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5103s；`mikey-youtube-live-024-E0012-R010` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5114s；`mikey-youtube-live-024-E0012-R011` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5116s；`mikey-youtube-live-024-E0012-R014` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5125s。

### mikey-youtube-live-024-R010 · blocking / open

**原时间窗：**6740–6810秒

**原问题：**再次把拉黑解释为有吸引就能继续操作，是否应全部隔离？

**原要求证据：**持续联系与骚扰边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-024-E0013`、`mikey-youtube-live-024-K016`

**本综合阻断的知识：**`mikey-youtube-live-024-K016`

**时间/追溯问题：**`TI019`

原证据地址：`mikey-youtube-live-024-E0013-R040` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5631s；`mikey-youtube-live-024-E0013-R048` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5645s；`mikey-youtube-live-024-E0013-R055` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5655s；`mikey-youtube-live-024-E0013-R061` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5663s；`mikey-youtube-live-024-E0013-R063` → https://www.youtube.com/watch?v=-yPQ13M6jX8&t=5666s。

### mikey-youtube-live-025-R001 · blocking / open

**原时间窗：**300–570秒

**原问题：**电竞选手及伴侣的性经历、婚姻和亲子暗示是否有可靠来源，是否应全部移出可执行知识？

**原要求证据：**原始来源和事实核查

**原责任方：**fact-review

**原affected_ids：**`mikey-youtube-live-025-E0001`

**本综合阻断的知识：**`mikey-youtube-live-025-K001`、`mikey-youtube-live-025-K002`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-025-E0001-R130` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=443s；`mikey-youtube-live-025-E0001-R131` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=446s；`mikey-youtube-live-025-E0001-R132` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=450s；`mikey-youtube-live-025-E0001-R154` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=514s；`mikey-youtube-live-025-E0001-R156` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=519s；`mikey-youtube-live-025-E0001-R158` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=522s。

### mikey-youtube-live-025-R002 · major / open

**原时间窗：**570–800秒

**原问题：**‘唯一选择／道德高尚／持续提升’三条件是否被错误表达为伴侣不离开的客观事实？

**原要求证据：**语义和因果边界复核

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-025-E0002`、`mikey-youtube-live-025-K005`

**本综合阻断的知识：**`mikey-youtube-live-025-K003`、`mikey-youtube-live-025-K004`、`mikey-youtube-live-025-K005`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-025-E0002-R079` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=712s；`mikey-youtube-live-025-E0002-R082` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=716s；`mikey-youtube-live-025-E0002-R085` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=721s；`mikey-youtube-live-025-E0002-R094` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=732s；`mikey-youtube-live-025-E0002-R107` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=749s；`mikey-youtube-live-025-E0002-R109` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=751s。

### mikey-youtube-live-025-R003 · blocking / open

**原时间窗：**895–1160秒

**原问题：**对女性智力、山东女性性压抑和所谓喜欢不尊重者的概括是否应禁止一般化？

**原要求证据：**编辑和歧视性概括复核

**原责任方：**editorial-review

**原affected_ids：**`mikey-youtube-live-025-E0003`、`mikey-youtube-live-025-K016`

**本综合阻断的知识：**`mikey-youtube-live-025-K006`、`mikey-youtube-live-025-K015`、`mikey-youtube-live-025-K016`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-025-E0003-R004` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=904s；`mikey-youtube-live-025-E0003-R011` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=922s；`mikey-youtube-live-025-E0003-R066` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1087s；`mikey-youtube-live-025-E0003-R067` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1088s；`mikey-youtube-live-025-E0003-R083` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1117s；`mikey-youtube-live-025-E0003-R095` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1141s；`mikey-youtube-live-025-E0003-R099` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1147s。

### mikey-youtube-live-025-R004 · blocking / open

**原时间窗：**1390–1485秒

**原问题：**手机展示的联系人身份、消息顺序、公开授权和主持人口述是否能由画面确认？

**原要求证据：**原尺寸顺序帧、OCR和授权边界复核

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-025-E0004`

**本综合阻断的知识：**`mikey-youtube-live-025-K007`、`mikey-youtube-live-025-K008`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-025-E0004-R094` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1407s；`mikey-youtube-live-025-E0004-R096` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1421s；`mikey-youtube-live-025-E0004-R098` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1428s；`mikey-youtube-live-025-E0004-R105` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1442s；`mikey-youtube-live-025-E0004-R110` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1461s；`mikey-youtube-live-025-E0004-R116` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1469s；`mikey-youtube-live-025-E0004-R124` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1479s。

### mikey-youtube-live-025-R005 · major / open

**原时间窗：**1600–1960秒

**原问题：**课程‘全行业最好’、效果和无法盗版等宣称是否仅为销售话术？

**原要求证据：**销售语境和事实核查

**原责任方：**fact-review

**原affected_ids：**`mikey-youtube-live-025-E0005`、`mikey-youtube-live-025-E0006`、`mikey-youtube-live-025-E0010`

**本综合阻断的知识：**`mikey-youtube-live-025-K009`、`mikey-youtube-live-025-K010`、`mikey-youtube-live-025-K015`

**时间/追溯问题：**`TI020`

原证据地址：`mikey-youtube-live-025-E0005-R094` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1742s；`mikey-youtube-live-025-E0005-R098` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1781s；`mikey-youtube-live-025-E0005-R100` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1785s；`mikey-youtube-live-025-E0006-R028` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1918s；`mikey-youtube-live-025-E0006-R031` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1924s；`mikey-youtube-live-025-E0006-R065` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2018s；`mikey-youtube-live-025-E0006-R068` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2025s。

### mikey-youtube-live-025-R006 · blocking / open

**原时间窗：**1620–2580秒

**原问题：**把关系定义为支配游戏、让对方无法说no或失去尊严，是否必须全部隔离为不可建议内容？

**原要求证据：**同意、胁迫和安全边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-025-E0005`、`mikey-youtube-live-025-E0006`、`mikey-youtube-live-025-E0008`、`mikey-youtube-live-025-K015`

**本综合阻断的知识：**`mikey-youtube-live-025-K009`、`mikey-youtube-live-025-K010`、`mikey-youtube-live-025-K015`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-025-E0005-R060` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1664s；`mikey-youtube-live-025-E0005-R065` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1674s；`mikey-youtube-live-025-E0006-R004` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1810s；`mikey-youtube-live-025-E0006-R005` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1812s；`mikey-youtube-live-025-E0006-R037` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=1937s；`mikey-youtube-live-025-E0008-R013` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2459s；`mikey-youtube-live-025-E0008-R016` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2471s；`mikey-youtube-live-025-E0008-R022` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2487s。

### mikey-youtube-live-025-R007 · major / open

**原时间窗：**2620–2830秒

**原问题：**大学去留建议是否充分考虑学校、经济、心理状态、家庭与可逆后路？

**原要求证据：**用户个案信息和教育职业复核

**原责任方：**source-review

**原affected_ids：**`mikey-youtube-live-025-E0009`、`mikey-youtube-live-025-K013`

**本综合阻断的知识：**`mikey-youtube-live-025-K006`、`mikey-youtube-live-025-K013`

**时间/追溯问题：**`TI021`

原证据地址：`mikey-youtube-live-025-E0009-R074` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2899s；`mikey-youtube-live-025-E0009-R083` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2920s；`mikey-youtube-live-025-E0009-R086` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2928s；`mikey-youtube-live-025-E0009-R104` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2962s；`mikey-youtube-live-025-E0009-R108` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2967s；`mikey-youtube-live-025-E0009-R110` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=2969s。

### mikey-youtube-live-025-R008 · blocking / open

**原时间窗：**3300–3890秒

**原问题：**责任回答、名人出轨新闻、女性不可信和限制伴侣社交是否会形成欺骗或控制？

**原要求证据：**事实、同意和控制边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-025-E0011`、`mikey-youtube-live-025-K014`、`mikey-youtube-live-025-K015`、`mikey-youtube-live-025-K016`

**本综合阻断的知识：**`mikey-youtube-live-025-K014`、`mikey-youtube-live-025-K015`、`mikey-youtube-live-025-K016`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-025-E0011-R006` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=3321s；`mikey-youtube-live-025-E0011-R011` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=3338s；`mikey-youtube-live-025-E0011-R030` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=3578s；`mikey-youtube-live-025-E0011-R033` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=3587s；`mikey-youtube-live-025-E0011-R040` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=3603s；`mikey-youtube-live-025-E0011-R077` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=3858s；`mikey-youtube-live-025-E0011-R083` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=3868s；`mikey-youtube-live-025-E0011-R089` → https://www.youtube.com/watch?v=dSYHWDUlQ4I&t=3886s。

### mikey-youtube-live-026-R001 · blocking / open

**原时间窗：**500–900秒

**原问题：**把女性动机、忠诚和性价值作绝对化概括是否必须限制？

**原要求证据：**语义、群体概括和编辑复核

**原责任方：**editorial-review

**原affected_ids：**`mikey-youtube-live-026-E0001`、`mikey-youtube-live-026-E0002`

**本综合阻断的知识：**无

**时间/追溯问题：**`TI022`

原证据地址：`mikey-youtube-live-026-E0002-R020` → https://www.youtube.com/watch?v=PQbkX-IUGcs&t=345s；`mikey-youtube-live-026-E0002-R082` → https://www.youtube.com/watch?v=PQbkX-IUGcs&t=468s。

### mikey-youtube-live-026-R002 · blocking / open

**原时间窗：**900–1450秒

**原问题：**不戴套、怀孕和所谓强势是否被错误转成可执行建议？

**原要求证据：**同意、避孕和医疗安全复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-026-E0003`

**本综合阻断的知识：**`mikey-youtube-live-026-K007`

**时间/追溯问题：**`TI023`

原证据地址：`mikey-youtube-live-026-E0003-R026` → https://www.youtube.com/watch?v=PQbkX-IUGcs&t=627s；`mikey-youtube-live-026-E0003-R027` → https://www.youtube.com/watch?v=PQbkX-IUGcs&t=629s；`mikey-youtube-live-026-E0003-R028` → https://www.youtube.com/watch?v=PQbkX-IUGcs&t=630s。

### mikey-youtube-live-026-R003 · blocking / open

**原时间窗：**1840–1950秒

**原问题：**艾滋风险回答是否淡化检测、窗口期和屏障保护？

**原要求证据：**专业医疗信息复核

**原责任方：**medical-review

**原affected_ids：**`mikey-youtube-live-026-E0007`

**本综合阻断的知识：**`mikey-youtube-live-026-K003`、`mikey-youtube-live-026-K006`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-026-E0007-R067` → https://www.youtube.com/watch?v=PQbkX-IUGcs&t=1851s；`mikey-youtube-live-026-E0007-R084` → https://www.youtube.com/watch?v=PQbkX-IUGcs&t=1891s。

### mikey-youtube-live-026-R004 · major / open

**原时间窗：**0–3970秒

**原问题：**低清候选虽已生成，直播中是否存在屏幕、截图、播放材料或人物切换尚未语义审查？

**原要求证据：**313个低清候选、7张联系表的人工审查和重点原尺寸顺序帧

**原责任方：**visual-review

**原affected_ids：**`mikey-youtube-live-026-E0001`、`mikey-youtube-live-026-E0002`、`mikey-youtube-live-026-E0003`、`mikey-youtube-live-026-E0004`、`mikey-youtube-live-026-E0005`、`mikey-youtube-live-026-E0006`、`mikey-youtube-live-026-E0007`、`mikey-youtube-live-026-E0008`、`mikey-youtube-live-026-E0009`、`mikey-youtube-live-026-E0010`、`mikey-youtube-live-026-E0011`、`mikey-youtube-live-026-E0012`

**本综合阻断的知识：**`mikey-youtube-live-026-K001`、`mikey-youtube-live-026-K002`、`mikey-youtube-live-026-K003`、`mikey-youtube-live-026-K004`、`mikey-youtube-live-026-K005`、`mikey-youtube-live-026-K006`、`mikey-youtube-live-026-K007`、`mikey-youtube-live-026-K008`、`mikey-youtube-live-026-K009`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-026-E0001-R001` → https://www.youtube.com/watch?v=PQbkX-IUGcs&t=28s；`mikey-youtube-live-026-E0012-R107` → https://www.youtube.com/watch?v=PQbkX-IUGcs&t=3960s。

### mikey-youtube-live-027-R001 · blocking / open

**原时间窗：**2100–2300秒

**原问题：**婚外情、皮条、卖淫和女性贬损段落是否全部隔离？

**原要求证据：**安全和编辑复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-027-E0007`

**本综合阻断的知识：**`mikey-youtube-live-027-K012`

**时间/追溯问题：**`TI024`

原证据地址：`mikey-youtube-live-027-E0007-R020` → https://www.youtube.com/watch?v=8jCwDoBjWT0&t=2306s；`mikey-youtube-live-027-E0007-R021` → https://www.youtube.com/watch?v=8jCwDoBjWT0&t=2318s；`mikey-youtube-live-027-E0007-R022` → https://www.youtube.com/watch?v=8jCwDoBjWT0&t=2319s。

### mikey-youtube-live-027-R002 · blocking / open

**原时间窗：**1150–1400秒

**原问题：**私密空间和身体接触建议是否缺少清楚、持续、可撤回同意？

**原要求证据：**连续语境和同意边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-027-E0004`

**本综合阻断的知识：**`mikey-youtube-live-027-K002`、`mikey-youtube-live-027-K005`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-027-E0004-R060` → https://www.youtube.com/watch?v=8jCwDoBjWT0&t=1372s；`mikey-youtube-live-027-E0004-R061` → https://www.youtube.com/watch?v=8jCwDoBjWT0&t=1373s。

### mikey-youtube-live-027-R003 · major / open

**原时间窗：**0–4460秒

**原问题：**低清候选和联系表尚未人工语义审查，是否有截图、演示或人物切换？

**原要求证据：**340个候选、8张联系表和重点原尺寸帧复核

**原责任方：**visual-review

**原affected_ids：**`mikey-youtube-live-027-E0001`、`mikey-youtube-live-027-E0002`、`mikey-youtube-live-027-E0003`、`mikey-youtube-live-027-E0004`、`mikey-youtube-live-027-E0005`、`mikey-youtube-live-027-E0006`、`mikey-youtube-live-027-E0007`、`mikey-youtube-live-027-E0008`、`mikey-youtube-live-027-E0009`、`mikey-youtube-live-027-E0010`、`mikey-youtube-live-027-E0011`、`mikey-youtube-live-027-E0012`、`mikey-youtube-live-027-E0013`、`mikey-youtube-live-027-E0014`

**本综合阻断的知识：**`mikey-youtube-live-027-K001`、`mikey-youtube-live-027-K002`、`mikey-youtube-live-027-K003`、`mikey-youtube-live-027-K004`、`mikey-youtube-live-027-K005`、`mikey-youtube-live-027-K006`、`mikey-youtube-live-027-K007`、`mikey-youtube-live-027-K008`、`mikey-youtube-live-027-K009`、`mikey-youtube-live-027-K010`、`mikey-youtube-live-027-K011`、`mikey-youtube-live-027-K012`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-027-E0001-R001` → https://www.youtube.com/watch?v=8jCwDoBjWT0&t=39s；`mikey-youtube-live-027-E0014-R020` → https://www.youtube.com/watch?v=8jCwDoBjWT0&t=4456s。

### mikey-youtube-live-028-R001 · blocking / open

**原时间窗：**900–1400秒

**原问题：**内在小孩、催眠、冥想和打骂伴侣的疗愈说法是否越过心理治疗与暴力边界？

**原要求证据：**心理健康专业复核和暴力边界

**原责任方：**clinical-review

**原affected_ids：**`mikey-youtube-live-028-E0002`

**本综合阻断的知识：**无

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-028-E0002-R059` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=1045s；`mikey-youtube-live-028-E0002-R070` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=1061s。

### mikey-youtube-live-028-R002 · blocking / open

**原时间窗：**1500–2900秒

**原问题：**上楼借口、身体接触排斥、酒吧转场和拒绝后继续推进是否全部隔离？

**原要求证据：**连续语境、清楚同意和酒精影响复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-028-E0003`、`mikey-youtube-live-028-E0007`

**本综合阻断的知识：**`mikey-youtube-live-028-K005`、`mikey-youtube-live-028-K012`

**时间/追溯问题：**`TI025`

原证据地址：`mikey-youtube-live-028-E0007-R035` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=2591s；`mikey-youtube-live-028-E0007-R036` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=2592s；`mikey-youtube-live-028-E0008-R041` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=2912s。

### mikey-youtube-live-028-R003 · blocking / open

**原时间窗：**3900–4400秒

**原问题：**‘世界只有自己、别人都是NPC、女性只提供性价值’是否必须禁止一般化？

**原要求证据：**编辑和去人化风险复核

**原责任方：**editorial-review

**原affected_ids：**`mikey-youtube-live-028-E0011`、`mikey-youtube-live-028-E0012`

**本综合阻断的知识：**`mikey-youtube-live-028-K007`、`mikey-youtube-live-028-K008`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-028-E0011-R066` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=4050s；`mikey-youtube-live-028-E0011-R075` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=4067s；`mikey-youtube-live-028-E0011-R081` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=4077s；`mikey-youtube-live-028-E0012-R015` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=4236s。

### mikey-youtube-live-028-R004 · major / open

**原时间窗：**0–5465秒

**原问题：**431个低清候选尚未语义审查，是否出现屏幕、聊天截图、播放材料或人物切换？

**原要求证据：**9张联系表、候选和重点原尺寸顺序帧复核

**原责任方：**visual-review

**原affected_ids：**`mikey-youtube-live-028-E0001`、`mikey-youtube-live-028-E0002`、`mikey-youtube-live-028-E0003`、`mikey-youtube-live-028-E0004`、`mikey-youtube-live-028-E0005`、`mikey-youtube-live-028-E0006`、`mikey-youtube-live-028-E0007`、`mikey-youtube-live-028-E0008`、`mikey-youtube-live-028-E0009`、`mikey-youtube-live-028-E0010`、`mikey-youtube-live-028-E0011`、`mikey-youtube-live-028-E0012`、`mikey-youtube-live-028-E0013`、`mikey-youtube-live-028-E0014`、`mikey-youtube-live-028-E0015`

**本综合阻断的知识：**`mikey-youtube-live-028-K001`、`mikey-youtube-live-028-K002`、`mikey-youtube-live-028-K003`、`mikey-youtube-live-028-K004`、`mikey-youtube-live-028-K005`、`mikey-youtube-live-028-K006`、`mikey-youtube-live-028-K007`、`mikey-youtube-live-028-K008`、`mikey-youtube-live-028-K009`、`mikey-youtube-live-028-K010`、`mikey-youtube-live-028-K011`、`mikey-youtube-live-028-K012`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-028-E0001-R001` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=63s；`mikey-youtube-live-028-E0015-R030` → https://www.youtube.com/watch?v=vBoAYfRFhh0&t=5459s。

### mikey-youtube-live-029-R001 · blocking / open

**原时间窗：**3600–4100秒

**原问题：**辱骂后见面、多人性故事和‘必须拼’等内容是否全部隔离？

**原要求证据：**同意、安全和事实复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-029-E0006`

**本综合阻断的知识：**`mikey-youtube-live-029-K008`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-029-K012`

**时间/追溯问题：**`TI056`

原证据地址：`mikey-youtube-live-029-E0006-R028` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=3675s；`mikey-youtube-live-029-E0006-R030` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=3679s；`mikey-youtube-live-029-E0006-R088` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=3807s；`mikey-youtube-live-029-E0006-R121` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=3931s；`mikey-youtube-live-029-E0006-R123` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=3935s。

### mikey-youtube-live-029-R002 · blocking / open

**原时间窗：**4300–7500秒

**原问题：**多次电话中每句话是谁说、来电者是否知情直播、私人经历是否获公开授权？

**原要求证据：**连续音画、声纹映射、屏幕状态和授权边界

**原责任方：**speaker-review

**原affected_ids：**`mikey-youtube-live-029-E0007`、`mikey-youtube-live-029-E0008`、`mikey-youtube-live-029-E0009`、`mikey-youtube-live-029-E0010`

**本综合阻断的知识：**`mikey-youtube-live-029-K009`

**时间/追溯问题：**`TI056`

原证据地址：`mikey-youtube-live-029-E0007-R010` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=4325s；`mikey-youtube-live-029-E0008-R008` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=4591s；`mikey-youtube-live-029-E0009-R031` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=5224s；`mikey-youtube-live-029-E0009-R042` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=5248s；`mikey-youtube-live-029-E0009-R125` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=5575s。

### mikey-youtube-live-029-R003 · blocking / open

**原时间窗：**7500–10200秒

**原问题：**长电话中的‘不要’、睡觉、时间不确定及反复性邀约是否形成压力式推进？

**原要求证据：**逐句说话人分离和持续同意复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-029-E0011`、`mikey-youtube-live-029-E0012`

**本综合阻断的知识：**`mikey-youtube-live-029-K009`、`mikey-youtube-live-029-K010`、`mikey-youtube-live-029-K011`

**时间/追溯问题：**`TI026`、`TI056`

原证据地址：`mikey-youtube-live-029-E0011-R163` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=6894s；`mikey-youtube-live-029-E0011-R164` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=6897s；`mikey-youtube-live-029-E0012-R001` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=6902s；`mikey-youtube-live-029-E0012-R074` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=7147s；`mikey-youtube-live-029-E0012-R082` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=7171s。

### mikey-youtube-live-029-R004 · blocking / open

**原时间窗：**0–9355秒

**原问题：**尚无正式视觉manifest，屏幕、交友软件、电话状态、聊天和人物切换均未核。

**原要求证据：**全片视觉候选、联系表、重点原尺寸顺序帧和连续音画

**原责任方：**visual-review

**原affected_ids：**`mikey-youtube-live-029-E0001`、`mikey-youtube-live-029-E0002`、`mikey-youtube-live-029-E0003`、`mikey-youtube-live-029-E0004`、`mikey-youtube-live-029-E0005`、`mikey-youtube-live-029-E0006`、`mikey-youtube-live-029-E0007`、`mikey-youtube-live-029-E0008`、`mikey-youtube-live-029-E0009`、`mikey-youtube-live-029-E0010`、`mikey-youtube-live-029-E0011`、`mikey-youtube-live-029-E0012`、`mikey-youtube-live-029-E0013`、`mikey-youtube-live-029-E0014`、`mikey-youtube-live-029-E0015`

**本综合阻断的知识：**`mikey-youtube-live-029-K001`、`mikey-youtube-live-029-K002`、`mikey-youtube-live-029-K003`、`mikey-youtube-live-029-K004`、`mikey-youtube-live-029-K005`、`mikey-youtube-live-029-K006`、`mikey-youtube-live-029-K007`、`mikey-youtube-live-029-K008`、`mikey-youtube-live-029-K009`、`mikey-youtube-live-029-K010`、`mikey-youtube-live-029-K011`、`mikey-youtube-live-029-K012`

**时间/追溯问题：**`TI056`

原证据地址：`mikey-youtube-live-029-E0001-R001` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=36s；`mikey-youtube-live-029-E0015-R066` → https://www.youtube.com/watch?v=knZc0MMOnbw&t=9352s。

### mikey-youtube-live-030-R001 · blocking / open

**原时间窗：**700–1000秒

**原问题：**‘边骂边透’是否可能把暴力和性行为混为可执行建议？

**原要求证据：**同意与暴力边界复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-030-E0001`

**本综合阻断的知识：**`mikey-youtube-live-030-K001`、`mikey-youtube-live-030-K002`、`mikey-youtube-live-030-K010`

**时间/追溯问题：**`TI027`

原证据地址：`mikey-youtube-live-030-E0001-R134` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=533s；`mikey-youtube-live-030-E0001-R137` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=538s；`mikey-youtube-live-030-E0001-R138` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=540s；`mikey-youtube-live-030-E0001-R139` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=540s。

### mikey-youtube-live-030-R002 · blocking / open

**原时间窗：**1450–2050秒

**原问题：**课程中的支配、服从、灌酒、软磨硬泡与同意边界如何隔离？

**原要求证据：**连续语境、清楚同意和酒精风险复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-030-E0005`

**本综合阻断的知识：**`mikey-youtube-live-030-K009`、`mikey-youtube-live-030-K013`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-030-E0005-R014` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1560s；`mikey-youtube-live-030-E0005-R020` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1582s；`mikey-youtube-live-030-E0005-R022` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1586s；`mikey-youtube-live-030-E0005-R028` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1595s；`mikey-youtube-live-030-E0005-R078` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1731s；`mikey-youtube-live-030-E0005-R079` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1736s。

### mikey-youtube-live-030-R003 · blocking / open

**原时间窗：**1850–1980秒

**原问题：**‘让她走—不走—直接脱衣—没有反抗’是否缺少明确同意？

**原要求证据：**原音、连续音画和同意语义复核

**原责任方：**safety-review

**原affected_ids：**`mikey-youtube-live-030-E0006`

**本综合阻断的知识：**`mikey-youtube-live-030-K009`、`mikey-youtube-live-030-K013`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-030-E0006-R054` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1905s；`mikey-youtube-live-030-E0006-R057` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1910s；`mikey-youtube-live-030-E0006-R058` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1913s；`mikey-youtube-live-030-E0006-R059` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1913s；`mikey-youtube-live-030-E0006-R060` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=1914s。

### mikey-youtube-live-030-R004 · blocking / open

**原时间窗：**0–4085秒

**原问题：**尚无正式视觉manifest，屏幕、课程宣传、人物与展示内容均未核。

**原要求证据：**全片视觉候选、联系表、重点原尺寸帧和连续音画

**原责任方：**visual-review

**原affected_ids：**`mikey-youtube-live-030-E0001`、`mikey-youtube-live-030-E0002`、`mikey-youtube-live-030-E0003`、`mikey-youtube-live-030-E0004`、`mikey-youtube-live-030-E0005`、`mikey-youtube-live-030-E0006`、`mikey-youtube-live-030-E0007`、`mikey-youtube-live-030-E0008`、`mikey-youtube-live-030-E0009`、`mikey-youtube-live-030-E0010`、`mikey-youtube-live-030-E0011`、`mikey-youtube-live-030-E0012`、`mikey-youtube-live-030-E0013`

**本综合阻断的知识：**`mikey-youtube-live-030-K001`、`mikey-youtube-live-030-K002`、`mikey-youtube-live-030-K003`、`mikey-youtube-live-030-K004`、`mikey-youtube-live-030-K005`、`mikey-youtube-live-030-K006`、`mikey-youtube-live-030-K007`、`mikey-youtube-live-030-K008`、`mikey-youtube-live-030-K009`、`mikey-youtube-live-030-K010`、`mikey-youtube-live-030-K011`、`mikey-youtube-live-030-K012`、`mikey-youtube-live-030-K013`、`mikey-youtube-live-030-K014`

**时间/追溯问题：**无

原证据地址：`mikey-youtube-live-030-E0001-R001` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=41s；`mikey-youtube-live-030-E0013-R035` → https://www.youtube.com/watch?v=KO5l9Lh7FZc&t=4083s。

## 15. 交付前自检与最终统计

### 四种综合使用级别

| 使用级别 | 数量 |
|---|---:|
| `direct` | 8 |
| `context_only` | 1 |
| `hold` | 122 |
| `do_not_generalize` | 22 |
| **合计** | **153** |

### 逐期原release_status统计（未修改）

| 来源 | direct | context_only | hold | candidate_only | do_not_generalize |
|---|---:|---:|---:|---:|---:|
| `mikey-youtube-live-021` | 14 | 3 | 2 | 0 | 0 |
| `mikey-youtube-live-022` | 0 | 0 | 4 | 10 | 4 |
| `mikey-youtube-live-023` | 21 | 2 | 0 | 0 | 2 |
| `mikey-youtube-live-024` | 9 | 4 | 0 | 0 | 3 |
| `mikey-youtube-live-025` | 10 | 4 | 0 | 0 | 2 |
| `mikey-youtube-live-026` | 4 | 2 | 0 | 0 | 3 |
| `mikey-youtube-live-027` | 9 | 2 | 0 | 0 | 1 |
| `mikey-youtube-live-028` | 6 | 3 | 1 | 0 | 2 |
| `mikey-youtube-live-029` | 4 | 4 | 1 | 0 | 3 |
| `mikey-youtube-live-030` | 8 | 4 | 0 | 0 | 2 |
| **原合计** | 85 | 28 | 8 | 10 | 22 |

### 逐期综合使用统计（与原状态分列）

| 来源 | direct | context_only | hold | do_not_generalize |
|---|---:|---:|---:|---:|
| `mikey-youtube-live-021` | 1 | 0 | 18 | 0 |
| `mikey-youtube-live-022` | 0 | 0 | 14 | 4 |
| `mikey-youtube-live-023` | 3 | 0 | 20 | 2 |
| `mikey-youtube-live-024` | 3 | 1 | 9 | 3 |
| `mikey-youtube-live-025` | 1 | 0 | 13 | 2 |
| `mikey-youtube-live-026` | 0 | 0 | 6 | 3 |
| `mikey-youtube-live-027` | 0 | 0 | 11 | 1 |
| `mikey-youtube-live-028` | 0 | 0 | 10 | 2 |
| `mikey-youtube-live-029` | 0 | 0 | 9 | 3 |
| `mikey-youtube-live-030` | 0 | 0 | 12 | 2 |

### 五类游戏/动漫归属统计

| 类别 | SID数 |
|---|---:|
| `mikey_commentary` | 0 |
| `game_dialogue_or_narration` | 0 |
| `viewer_chat_text` | 0 |
| `mikey_quote_or_reading` | 0 |
| `uncertain_overlap` | 2014 |

### 不可泛化项与仍未解决的问题

原22条do_not_generalize全部进入不可泛化账本。20类边界覆盖性别、地域、族群、外貌、年龄、未成年人及权力、持续同意、隐私、录音拍摄、医疗、心理健康、成功率、收入、结果、羞辱、操纵、去人化、绕过拉黑、性剥削与动漫控制迁移。其余受限项仍按索引hold/context_only处理，不能借安全改写变成原人物建议。

仍需本地处理的内容包括：直播70句级五类与说话人映射；直播82电话身份、公开授权和拒绝语义；直播79—83未完成的视觉任务；17项时间窗问题；7项事件归属遗漏；28项代表片段不足/偏题；2份说话人登记URL不一致；以及原63项风险待核。应以真实原音、对应画面和专业/授权证据修复原材料后另行复核，本次没有宣布任何项已完成。

### 已执行的程序校验

| 检查 | 结果 | 说明 |
|---|---|---|
| `json_schema_version` | PASS | youtube-live-batch3-cross-synthesis-1.0 |
| `scope_copied_exactly` | PASS | 对象、数组顺序、字段及值与输入一致。 |
| `statistics_copied_exactly` | PASS | 对象、数组顺序、字段及值与输入一致。 |
| `sources_copied_exactly` | PASS | 对象、数组顺序、字段及值与输入一致。 |
| `index_exact_153_once` | PASS | 153行；无遗漏、无重复、无新增知识ID。 |
| `source_range_exact` | PASS | 仅本批021–030作为分析来源。 |
| `immutable_knowledge_catalog` | PASS | 153条原始知识所有字段完整保留。 |
| `immutable_review_catalog` | PASS | 63项待核原严重度、状态、时间窗和引用原样保留。 |
| `immutable_events_and_speakers` | PASS | 136事件与10份说话人登记未修改。 |
| `original_statuses_preserved` | PASS | 逐期发布/归属状态与综合使用级别分列。 |
| `use_levels_valid` | PASS | {"direct": 8, "context_only": 1, "hold": 122, "do_not_generalize": 22} |
| `no_restriction_upgrade` | PASS | candidate/context/hold/DNG均未升级direct。 |
| `dng_exact_preservation` | PASS | 22条原DNG全部保持；其余风险用hold限制而非静默改原状态。 |
| `blocking_and_major_propagated` | PASS | 凡关联开放blocking/major者均不进入direct/context_only。 |
| `mixed_speakers_not_direct` | PASS | 混合归属不人物化。 |
| `representative_insufficiency_gated` | PASS | 28条代表片段不足/偏题审计均已受控。 |
| `all_knowledge_has_theme_and_proposition` | PASS | 153条均有主题与命题定位。 |
| `internal_links_resolve` | PASS | 主题/命题交叉引用均存在。 |
| `critical_arrays_complete` | PASS | 9个固定数组均存在且给出审计内容。 |
| `gameplay_exact_copy` | PASS | 原16段归属跨度原样转存。 |
| `gameplay_2014_contiguous` | PASS | 16个连续归属跨度，覆盖2014个登记SID。 |
| `gameplay_five_classes_preserved` | PASS | 0/0/0/0/2014；未制造Mikey commentary。 |
| `live70_all_restricted` | PASS | 14 hold，4 DNG。 |
| `live82_call_boundaries` | PASS | 7个电话相关事件；该源9 hold、3 DNG。 |
| `all_dng_covered_by_ledger` | PASS | 22条均进入至少一个不可泛化类别。 |
| `source_release_statistics_agree` | PASS | 逐期原始发布状态统计逐条重算一致。 |
| `quote_count_distinction` | PASS | 288代表引文记录，963原引用记录；675个引用位置（671个去重后定位）未附正文。 |
| `all_external_identifiers_exist` | PASS | {"invalid_ids": []} |
| `all_sid_literals_exist` | PASS | {"invalid_sids": []} |
| `source_knowledge_event_evidence_sid_url_tuple_binding` | PASS | {"checked_reference_occurrences": 1237, "unique_bound_references": 153} |
| `review_dependencies_resolve` | PASS | 仅引用原63项review，新增问题使用TI编号而不是伪造review。 |
| `patterns_not_persona_runs` | PASS | 14条均未生成/运行人物化答案。 |
| `restricted_pattern_dependencies_disabled` | PASS | 4条仅研究提纲；10条因依赖受限而禁用。 |
| `no_audio_video_or_formal_integration_claim` | PASS | 未听原音、未看连续视频、未运行答案、未接入正式skill。 |
| `original_zip_bytes_unchanged` | PASS | 4个配套文件逐字节与原ZIP成员一致。 |
| `quote_records_vs_unique_evidence` | PASS | 记录数与去重证据定位数分开，不把重复引用当作独立句子。 |
| `pattern_comparison_levels_match_index` | PASS | 比较项按实际使用级别分别列出，不因模式禁用而把其中direct条目误标hold。 |
| `required_section_fields_present` | PASS | 所有任务必需字段完整。 |
| `all_required_top_sections_present` | PASS | 全部13个要求的分析节存在。 |
| `markdown_index_exact_153_once` | PASS | Markdown知识条目标题153项，与JSON索引集合完全相同。 |
| `markdown_json_counts_match` | PASS | 四类数值来自同一对象；逐期、原状态和游戏五类也由原对象直接渲染。 |
| `markdown_all_analytic_sections_rendered` | PASS | 15主题、34命题、14回答结构及其余审计节完整渲染。 |
| `markdown_identifier_membership` | PASS | Markdown中所有来源体系ID和SID均逐字存在于输入。 |

**机械检查通过不等于内容待核清零。** PASS只对应已执行的结构、引用、保留、限制传播和双文件生成校验；不代表原音、画面、归属、合法性、医疗或效果已核通过。 所有第一人称人物化路线与正式接入仍为**NOT_AUTHORIZED**。

### 输入文件完整性

| 文件 | 字节 | SHA-256 | 与ZIP成员相同 |
|---|---:|---|---|
| `cross-input-validation.json` | 630 | `59c7ce51e2f703ab52fbf3e2db510aa5df2233b96fe6f5d21a31da41e52c83fa` | 是 |
| `source-reuse-ledger.md` | 2139 | `3bc5d1eefbed363c7298ec4042a82f2114999d5ad0980a969f9289bc5df3edd6` | 是 |
| `web-pro-cross-input-compact.json` | 479398 | `d625a1063235d59fce7b252e9a4950eef6c3ff31ee73cd04224155ad624a036b` | 是 |
| `web-pro-cross-synthesis-task.md` | 5010 | `d5ac94c6fc42fe2e1cef6469089ccb7d52cffbff43ca7a00d68e09eb12ba1754` | 是 |

原附件文件未改动。JSON另含完整原样知识、事件、待核、说话人和五类归属档案，便于独立复核。

## 本地最终机械校准（2026-09-19）

- 最终签名输入：153条知识、63项待核，其中blocking 46、major 17。
- 视觉manifest：10/10完成，4,359张候选帧、97张联系表；连续音画核验仍未完成。
- 直播70的2,014 SID继续全部保持 `uncertain_overlap`。
- 直播82虽为单主播画面，电话音轨和手机聊天归属仍保持blocking。
- 直播83未见课程页、价格表、幻灯片或全屏宣传图；课程内容只按口述使用，视觉项降为major，其他同意与酒精项不解除。
- use_level：direct 8、context_only 1、hold 122、do_not_generalize 22。

## 当前有效投影（v4）

本报告内原有 `knowledge_catalog_as_supplied`、`review_catalog_as_supplied` 与 `speaker_registries_as_supplied` 是网页交付时的历史快照，只供追溯，不能作为当前检索或校验输入。

当前有效目录为 `current-effective/`，版本约束见 `current-effective/version-contract.json`，逐项差异见 `current-effective/revision-map.json`。当前消费者必须验证文件哈希后读取该目录；文件缺失或哈希不符时直接失败，不得静默回退到历史快照。

本次更新没有改变 8 direct、1 context_only、122 hold、22 do_not_generalize 的运行分级，也没有授权第一人称或行动建议。
