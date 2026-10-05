# YouTube公开直播第三批删除前审计

审计日期：2026-09-28。

## 结论

- 63项旧review均有唯一处置；没有遗漏或重复。
- 6项旧“视觉未审”记录可关闭：后续已完成全套联系表普查与关键帧记录；直播70的18张联系表本轮补看完。
- 17项需要外部事实、医学、法律或规范判断；原片只能证明说过什么，不能解决真伪。
- 16项已由第三批现行权限边界保守隔离，继续保持非第一人称、非行动建议；原片不会解除该限制。
- 24项仍需要连续音画/原音上下文，本轮已裁成18段证据片；直播82电话另有1段360p/12fps连续画面代理。
- 证据清单共19项，703,322,161字节（约0.655 GiB）；10个原片共13,803,011,308字节（约12.854 GiB）。在保留本证据包以及既有全文、联系表、关键帧的前提下，删除原片预计净释放13,099,689,147字节（约12.200 GiB）。
- 正式 `mikey-guide` 未修改；原视频未删除。

## 核验结果

- `delete-readiness-validation.json`：130项机械检查全部通过。
- 逐文件检查：存在且非0字节、SHA-256匹配、时长与原窗口误差小于1秒、音轨存在；视频证据均含视频轨。
- 10个原片仍在原目录，合计字节数与交付说明一致。
- 删除就绪文件树内没有0字节中断文件。

## 证据保留原则

- 每个连续证据窗口默认前后各保留12秒，并合并重叠区间。
- 短窗口保留音视频；超过15分钟的连续窗口优先保留64kbps Opus原音，避免为了广义逐句说话人映射复制近整片。
- 直播82电话段除连续原音外，另保留360p/12fps连续画面代理，用于判断主播是否在操作手机、展示屏幕、离席或出现人物切换。
- 直播70不保留整片视频作为删除必要条件；只保留三段实际受影响的动漫/多人高风险窗口。另有全片轻量音频放在 `supplementary/`，不计入必要证据包。

## 63项逐条处置

| review | 严重度 | 处置 | 原片删除后依据 |
|---|---|---|---|
| `mikey-youtube-live-021-R001` | major | 仍开放：外部事实/医学法律/规范核验 | 暴力犯罪与搭讪边界是否被错误理解成对任何接触方式的法律背书？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-021-R002` | blocking | 仍开放：连续证据已保留 | 隐瞒第二天离开、以‘看你表现’推进关系的案例是否构成欺骗或不当操控？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-021-clip-01-00589-00737.mp4` |
| `mikey-youtube-live-021-R003` | major | 保守隔离：不再依赖原片 | 80%至100%成功率和性结果数字是否仅为自述且不应作为用户基准？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-021-R004` | blocking | 保守隔离：不再依赖原片 | 女性类型概括及‘骂她／治她’措辞是否会导向羞辱、威胁或冲突升级？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-021-R005` | major | 仍开放：外部事实/医学法律/规范核验 | 护肤品、激素和‘三天就好’是否为未经核验的医学绝对判断？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-021-R006` | blocking | 仍开放：外部事实/医学法律/规范核验 | 武汉大学事件的人名、录音、行为和责任描述是否准确，能否承载后续群体结论？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-021-R007` | blocking | 仍开放：外部事实/医学法律/规范核验 | 对犹太人、女性主义者、保安及阶级问题的概括是否可普遍化？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-021-R008` | blocking | 仍开放：连续证据已保留 | 饮酒后前往私密空间的情境是否具备清醒、自愿、持续同意和安全返回条件？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-021-clip-02-02808-03652.mp4` |
| `mikey-youtube-live-021-R009` | blocking | 仍开放：连续证据已保留 | 酒店、肢体升级和直接邀请的建议是否明确允许拒绝且不得施压？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-021-clip-02-02808-03652.mp4` |
| `mikey-youtube-live-022-R001` | major | 保守隔离：不再依赖原片 | Mikey、面具参与者和第三名门徒的逐句发言边界是什么？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-022-R002` | blocking | 仍开放：连续证据已保留 | 别天神、改变意识和接受性交的段落由谁提出，是否明确是戏谑或反讽？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-022-clip-01-01528-01712.mp4` |
| `mikey-youtube-live-022-R003` | blocking | 仍开放：连续证据已保留 | 洗脑、精神控制和邪教领袖类比的具体发言人与评价方向是什么？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-022-clip-02-03078-03252.mp4` |
| `mikey-youtube-live-022-R004` | blocking | 仍开放：连续证据已保留 | 雷影、喝酒和给钱的情节是赞同、调侃还是角色设想？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-022-clip-03-04118-04312.mp4` |
| `mikey-youtube-live-022-R005` | major | 已关闭：视觉普查已完成 | 未人工查看的联系表及稀疏间隙是否有手机聊天截图、动漫正片或其他承载教学信息的画面？<br>原记录所称视觉未审已过时；全套联系表已查看，关键画面已记录。低密度普查固有限制不再单独要求保留原片。 |
| `mikey-youtube-live-023-R001` | major | 保守隔离：不再依赖原片 | 把陌生搭讪比作给路人发钱是否会弱化对方拒绝和不愿被接触的权利？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-023-R002` | major | 仍开放：外部事实/医学法律/规范核验 | 用政治制度作逻辑自洽类比是否准确，是否需要从可执行知识中移除？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-023-R003` | blocking | 仍开放：连续证据已保留 | 疫情期间大量性经历为单方自述，是否存在身份、同意、数量或ASR错误？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-023-clip-01-01718-01852.mp4` |
| `mikey-youtube-live-023-R004` | blocking | 保守隔离：不再依赖原片 | NPC、战略蔑视与‘教女人做人’是否会被误用为不尊重现实他人或攻击性控制？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-023-R005` | blocking | 保守隔离：不再依赖原片 | 按‘灵魂伴侣／解决生理需求’分类的说法是否缺少诚实、尊重和持续同意？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-023-R006` | blocking | 保守隔离：不再依赖原片 | 把不给钱与获得性结果对比是否会把亲密关系商品化或形成不当因果？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-023-R007` | blocking | 保守隔离：不再依赖原片 | 前任关系和‘复仇式拿下’自述是否应全部限制为不可执行材料？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-023-R008` | blocking | 仍开放：连续证据已保留 | 对只想发生性关系的人直接说露骨提议是否具备成年人、诚实、自愿和可退出条件？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-023-clip-02-03258-03342.mp4` |
| `mikey-youtube-live-023-R009` | major | 仍开放：外部事实/医学法律/规范核验 | 把使用‘普信’的人一律解释为自卑、羡慕是否是无证据动机归因？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-023-R010` | blocking | 仍开放：外部事实/医学法律/规范核验 | 对杭州、成都和小城市女性的性职业、智力、阶层概括是否应禁止一般化？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-023-R011` | blocking | 仍开放：连续证据已保留 | 观众提到初高中生且主持人后续说‘外校可以’，是否可能绕过未成年人及职业权力边界？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-023-clip-03-03926-04517.mp4` |
| `mikey-youtube-live-023-R012` | blocking | 仍开放：连续证据已保留 | 换号重加或直接电话是否是在绕过明确拉黑，能否作为错误示范彻底隔离？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-023-clip-04-05138-05212.mp4` |
| `mikey-youtube-live-024-R001` | blocking | 仍开放：外部事实/医学法律/规范核验 | 家暴经历、基因决定和反脆弱人格是否构成未经支持的创伤与遗传结论？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-024-R002` | blocking | 仍开放：连续证据已保留 | 用说服、虚假承诺对比和‘CPU烧了’推进性交是否绕过清楚持续同意？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-024-clip-01-02568-03347.mp4` |
| `mikey-youtube-live-024-R003` | blocking | 仍开放：外部事实/医学法律/规范核验 | 安全套、艾滋和其他性病风险说法是否为严重医学错误并污名化患者？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-024-R004` | blocking | 仍开放：连续证据已保留 | 对特朗普视频和撞人等内容是事实、玩笑、引用还是ASR错误？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-024-clip-02-03588-05407.opus` |
| `mikey-youtube-live-024-R005` | major | 仍开放：外部事实/医学法律/规范核验 | 把网暴者一律归为弱者并把网暴当成功证明，是否会掩盖真实越界和安全风险？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-024-R006` | blocking | 仍开放：连续证据已保留 | 性关系后让对方离开、把不同意视为必须接纳自己的二选一，是否缺少事前沟通和安全照顾？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-024-clip-02-03588-05407.opus` |
| `mikey-youtube-live-024-R007` | blocking | 仍开放：连续证据已保留 | 换号或电话绕过拉黑是否应完全禁止用于建议？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-024-clip-02-03588-05407.opus` |
| `mikey-youtube-live-024-R008` | blocking | 仍开放：连续证据已保留 | 后续再次用‘戴套就行’回答疾病风险是否必须阻断？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-024-clip-02-03588-05407.opus` |
| `mikey-youtube-live-024-R009` | major | 仍开放：连续证据已保留 | 用‘不够文艺／读书少’使对方怀疑自己来接受性话题，是否属于操控？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-024-clip-02-03588-05407.opus` |
| `mikey-youtube-live-024-R010` | blocking | 仍开放：连续证据已保留 | 再次把拉黑解释为有吸引就能继续操作，是否应全部隔离？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-024-clip-03-05437-05785.mp4` |
| `mikey-youtube-live-025-R001` | blocking | 仍开放：外部事实/医学法律/规范核验 | 电竞选手及伴侣的性经历、婚姻和亲子暗示是否有可靠来源，是否应全部移出可执行知识？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-025-R002` | major | 仍开放：外部事实/医学法律/规范核验 | ‘唯一选择／道德高尚／持续提升’三条件是否被错误表达为伴侣不离开的客观事实？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-025-R003` | blocking | 仍开放：外部事实/医学法律/规范核验 | 对女性智力、山东女性性压抑和所谓喜欢不尊重者的概括是否应禁止一般化？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-025-R004` | blocking | 仍开放：连续证据已保留 | 手机展示的联系人身份、消息顺序、公开授权和主持人口述是否能由画面确认？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-025-clip-01-01378-01497.mp4` |
| `mikey-youtube-live-025-R005` | major | 仍开放：外部事实/医学法律/规范核验 | 课程‘全行业最好’、效果和无法盗版等宣称是否仅为销售话术？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-025-R006` | blocking | 保守隔离：不再依赖原片 | 把关系定义为支配游戏、让对方无法说no或失去尊严，是否必须全部隔离为不可建议内容？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-025-R007` | major | 仍开放：外部事实/医学法律/规范核验 | 大学去留建议是否充分考虑学校、经济、心理状态、家庭与可逆后路？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-025-R008` | blocking | 保守隔离：不再依赖原片 | 责任回答、名人出轨新闻、女性不可信和限制伴侣社交是否会形成欺骗或控制？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-026-R001` | blocking | 仍开放：外部事实/医学法律/规范核验 | 把女性动机、忠诚和性价值作绝对化概括是否必须限制？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-026-R002` | blocking | 仍开放：连续证据已保留 | 不戴套、怀孕和所谓强势是否被错误转成可执行建议？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-026-clip-01-00515-00831.mp4` |
| `mikey-youtube-live-026-R003` | blocking | 仍开放：外部事实/医学法律/规范核验 | 艾滋风险回答是否淡化检测、窗口期和屏障保护？<br>需外部事实、医学/法律资料或规范判断；原视频只能证明说过什么，不能解决真伪或规范问题。完整文字与证据定位已保留。 |
| `mikey-youtube-live-026-R004` | major | 已关闭：视觉普查已完成 | 低清候选虽已生成，直播中是否存在屏幕、截图、播放材料或人物切换尚未语义审查？<br>原记录所称视觉未审已过时；全套联系表已查看，关键画面已记录。低密度普查固有限制不再单独要求保留原片。 |
| `mikey-youtube-live-027-R001` | blocking | 保守隔离：不再依赖原片 | 婚外情、皮条、卖淫和女性贬损段落是否全部隔离？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-027-R002` | blocking | 仍开放：连续证据已保留 | 私密空间和身体接触建议是否缺少清楚、持续、可撤回同意？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-027-clip-01-01138-01412.mp4` |
| `mikey-youtube-live-027-R003` | major | 已关闭：视觉普查已完成 | 低清候选和联系表尚未人工语义审查，是否有截图、演示或人物切换？<br>原记录所称视觉未审已过时；全套联系表已查看，关键画面已记录。低密度普查固有限制不再单独要求保留原片。 |
| `mikey-youtube-live-028-R001` | blocking | 保守隔离：不再依赖原片 | 内在小孩、催眠、冥想和打骂伴侣的疗愈说法是否越过心理治疗与暴力边界？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-028-R002` | blocking | 仍开放：连续证据已保留 | 上楼借口、身体接触排斥、酒吧转场和拒绝后继续推进是否全部隔离？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-028-clip-01-02521-03138.mp4` |
| `mikey-youtube-live-028-R003` | blocking | 保守隔离：不再依赖原片 | ‘世界只有自己、别人都是NPC、女性只提供性价值’是否必须禁止一般化？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-028-R004` | major | 已关闭：视觉普查已完成 | 431个低清候选尚未语义审查，是否出现屏幕、聊天截图、播放材料或人物切换？<br>原记录所称视觉未审已过时；全套联系表已查看，关键画面已记录。低密度普查固有限制不再单独要求保留原片。 |
| `mikey-youtube-live-029-R001` | blocking | 保守隔离：不再依赖原片 | 辱骂后见面、多人性故事和‘必须拼’等内容是否全部隔离？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-029-R002` | blocking | 仍开放：连续证据已保留 | 多次电话中每句话是谁说、来电者是否知情直播、私人经历是否获公开授权？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-029-clip-01-04288-07517.opus`<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-029-call-visual-proxy-04288-07517.mp4` |
| `mikey-youtube-live-029-R003` | blocking | 仍开放：连续证据已保留 | 长电话中的‘不要’、睡觉、时间不确定及反复性邀约是否形成压力式推进？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-029-clip-01-04288-07517.opus`<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-029-call-visual-proxy-04288-07517.mp4` |
| `mikey-youtube-live-029-R004` | blocking | 已关闭：视觉普查已完成 | 尚无正式视觉manifest，屏幕、交友软件、电话状态、聊天和人物切换均未核。<br>原记录所称视觉未审已过时；全套联系表已查看，关键画面已记录。低密度普查固有限制不再单独要求保留原片。 |
| `mikey-youtube-live-030-R001` | blocking | 保守隔离：不再依赖原片 | ‘边骂边透’是否可能把暴力和性行为混为可执行建议？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-030-R002` | blocking | 保守隔离：不再依赖原片 | 课程中的支配、服从、灌酒、软磨硬泡与同意边界如何隔离？<br>内容已维持非第一人称、非行动建议的限制；问题属于使用边界，原片不会解除限制，全文和证据定位足以继续保守处理。 |
| `mikey-youtube-live-030-R003` | blocking | 仍开放：连续证据已保留 | ‘让她走—不走—直接脱衣—没有反抗’是否缺少明确同意？<br>`research/youtube-live-batch3/delete-readiness/evidence-clips/mikey-youtube-live-030-clip-01-01838-01992.mp4` |
| `mikey-youtube-live-030-R004` | major | 已关闭：视觉普查已完成 | 全7张联系表未见课程页、价格表、幻灯片或全屏宣传图；课程内容只能按单人口述使用，稀疏普查仍不能排除极短展示或解除同意相关疑点。<br>原记录所称视觉未审已过时；全套联系表已查看，关键画面已记录。低密度普查固有限制不再单独要求保留原片。 |

## 文件索引

- `review-disposition-candidate.json`：63项机器可读的唯一处置。
- `evidence-clip-manifest.json`：来源时间、覆盖review、文件大小、SHA-256及ffprobe信息。
- `delete-readiness-validation.json`：130项校验结果和净释放计算。
- `evidence-clips/`：删除原片后必须保留的19个证据文件。
- `supplementary/`：非删除必要的补充材料。

## 限制

- “删除就绪”表示后续仍需解决的问题不再依赖13.8GB原片；不表示24项连续语义问题或17项外部事实问题已经判真。
- 压缩代理不适合恢复极小屏幕文字；这类已知截图仍以既有原尺寸关键帧、联系表和文字证据为准。
- 若要把当前受限知识升级为Mikey第一人称或行动建议，仍须重新进行人物归属、同意和外部事实审计；删除原片后不能凭压缩证据包自动升级。
