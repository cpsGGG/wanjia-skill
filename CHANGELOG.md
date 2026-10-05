# 更新记录

## v0.2.1 · 首次公开发行

- 独立发布玩家.skill完整本地技能，重写中英文README、安装入口和使用示例。
- 新增AI生成封面、贡献说明、发行构建工具和跨平台校验。
- 公开副本遮盖联系号码片段与私人审核会话定位，保留来源、SID、时间和修订登记；本地原件保留。
- 知识数量、来源计权、已审定回答与动作范围保持；公开分发不扩大运行许可。

以下保留此前本地维护记录；其中“未公开”等词指当时阶段。

# 发布记录

## v0.2.1

在第一版基础上，按最终ready.json和实际guide-root生成完整第二版修补包。512条来源记录（303视频类、209社区帖），3649条知识；其中来源原条3544、限定概念原子54、有限方法51。视频文字334097段、社区文字533段。

- 延续已交付v0.2.0的512来源、3649知识及117有限表达内含51动作；98子条逐条审核和原有字段/映射修补不重复或扩大。（包内依据：`wanjia-skill/references/v2-remediation-summary.json`）
- 回读现在逐段显示27条已有音频校正候选、真实状态和未决限制；S02543否定方向相反的旧自动稿不能再被当作确定读法，原稿不覆盖。（包内依据：`wanjia-skill/references/audio-correction-evidence/navigation.json`）
- 三份既有网页音频结果与比较记录提供包内导航；候选、原时轴和未独立听校状态保留。（包内依据：`wanjia-skill/references/audio-correction-evidence/audio-review-comparison.json`）
- 100旧原件按自行查找和用户说明已删除处理，不再追问目录；修正候选/未部署及旧待答的当前说明，原CSV快照保留。（包内依据：`wanjia-skill/references/current-operational-status.json`）
- 直播011的12项旧任务可定位到实际原记录；3746原任务及另410记录分列，目录不充当内容通过。（包内依据：`wanjia-skill/references/current-review-status/README.md`）
- 两项现存聊天展示核对到可见页面结构；live017的静帧VFR重建代理明确不能当连续动作画面。（包内依据：`wanjia-skill/references/current-review-status/visual-narrow-readback.json`）
- 刷新长片11候选已补现存文字与旧知识的具体比较，按重复/语境差异/仍未证新颖分别保留；人物身份和准入未放开。（包内依据：`wanjia-skill/references/current-review-status/refresh-r003-text-comparison.json`）

保留未解决事项：

- 303视频来源未记录全片逐句听校完成；172缺正常完整音频，100旧原件按已删除处理。原音画依赖问题仍缺证据，存在素材也不等于已听校。（包内依据：`wanjia-skill/references/current-operational-status.json`）
- 3746原待核未因目录或子条审核整体关闭；截图遮盖/缺页、身份、同意和授权、第三方事实及真实效果按原任务保持限制。（包内依据：`wanjia-skill/references/current-review-status/remaining-task-routing-summary.json`）
- 11新片候选的文字比较不认证逐句声音到身份或穷尽全库新颖性，不新增正式知识/方法、独立案例计权或运行许可。（包内依据：`wanjia-skill/references/current-review-status/refresh-r003-text-comparison.json`）
- 6条私教遮盖核心及2个hold负例仍关闭；用户尚未对本维护包的口吻和实际使用效果作验收。（包内依据：`wanjia-skill/references/v2-permission-review/private-teaching-a-accepted-review.json`）

本次构建不新增蒸馏、不改变源正文或许可，只复制已冻结的结果；没有线上发布、全局安装或新的全面音画/效果认证。
