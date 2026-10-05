# mikey-practice-002 正式视觉复核记录

## 范围

- 来源：`shizhan/2.一约拿下假兴趣女（精讲系列）.mp4`，容器时长 `2249.595011` 秒。
- 实际查看视觉小样的235个低清候选、5张标准联系表、12张大联系表，并回抽11个原尺寸节点；最终只把3张已脱敏帧复制到正式 item。
- 全部检查都是静帧序列／原帧，没有连续播放片段，也没有听原音。因此原音核验0秒、连续画面核验0秒。
- 证据来自 `research/shizhan/visual-pilot/items/mikey-practice-002/visual/`；正式候选目录中的另一批图片不冒称为已看。

```jsonl
{"review_id": "mikey-practice-002-V0001", "source_id": "mikey-practice-002", "source_revision": "sha256:b51c9fd748c03844665a056cec10a0407192bfbb51875d799eb8738e783dd1c0", "start": 0.0, "end": 2249.595011, "method": "contact_sheet", "frame_ids": ["survey/survey-0001.jpg", "survey/survey-0002.jpg", "survey/survey-0003.jpg", "survey/survey-0004.jpg", "survey/survey-0005.jpg", "survey-large/survey-large-001.jpg", "survey-large/survey-large-002.jpg", "survey-large/survey-large-003.jpg", "survey-large/survey-large-004.jpg", "survey-large/survey-large-005.jpg", "survey-large/survey-large-006.jpg", "survey-large/survey-large-007.jpg", "survey-large/survey-large-008.jpg", "survey-large/survey-large-009.jpg", "survey-large/survey-large-010.jpg", "survey-large/survey-large-011.jpg", "survey-large/survey-large-012.jpg"], "reviewer": "local_subagent", "status": "checked", "finding": "查看全部235个候选及5张标准、12张大联系表，最长候选间隔10秒；只支持场景与动作定位。", "affected_event_ids": ["mikey-practice-002-E0001", "mikey-practice-002-E0002", "mikey-practice-002-E0003", "mikey-practice-002-E0004", "mikey-practice-002-E0005", "mikey-practice-002-E0006", "mikey-practice-002-E0007", "mikey-practice-002-E0008", "mikey-practice-002-E0009", "mikey-practice-002-E0010", "mikey-practice-002-E0011", "mikey-practice-002-E0012", "mikey-practice-002-E0013", "mikey-practice-002-E0014", "mikey-practice-002-E0015", "mikey-practice-002-E0016", "mikey-practice-002-E0017", "mikey-practice-002-E0018", "mikey-practice-002-E0019", "mikey-practice-002-E0020"]}
{"review_id": "mikey-practice-002-V0002", "source_id": "mikey-practice-002", "source_revision": "sha256:b51c9fd748c03844665a056cec10a0407192bfbb51875d799eb8738e783dd1c0", "start": 437.0, "end": 437.0, "method": "original_frame", "frame_ids": ["research/shizhan/items/mikey-practice-002/visual/selected-fullres-redacted/001-00-07-17-open-palm-and-commentary-redacted.jpg"], "reviewer": "local_subagent", "status": "checked", "finding": "开放手掌动作与复盘标签同屏，必须分开可见动作和讲解含义。", "affected_event_ids": ["mikey-practice-002-E0005"]}
{"review_id": "mikey-practice-002-V0003", "source_id": "mikey-practice-002", "source_revision": "sha256:b51c9fd748c03844665a056cec10a0407192bfbb51875d799eb8738e783dd1c0", "start": 1117.0, "end": 1117.0, "method": "original_frame", "frame_ids": ["research/shizhan/items/mikey-practice-002/visual/selected-fullres-redacted/002-00-18-37-phone-disengagement-redacted.jpg"], "reviewer": "local_subagent", "status": "checked", "finding": "参与者低头使用手机；后续抽样又重新参与。", "affected_event_ids": ["mikey-practice-002-E0011"]}
{"review_id": "mikey-practice-002-V0004", "source_id": "mikey-practice-002", "source_revision": "sha256:b51c9fd748c03844665a056cec10a0407192bfbb51875d799eb8738e783dd1c0", "start": 1275.0, "end": 1275.0, "method": "original_frame", "frame_ids": ["research/shizhan/items/mikey-practice-002/visual/selected-fullres-redacted/003-00-21-15-seat-layout-redacted.jpg"], "reviewer": "local_subagent", "status": "checked", "finding": "私密房间初始座位与距离基线；不证明后续移动因果。", "affected_event_ids": ["mikey-practice-002-E0013"]}
{"review_id": "mikey-practice-002-V0005", "source_id": "mikey-practice-002", "source_revision": "sha256:b51c9fd748c03844665a056cec10a0407192bfbb51875d799eb8738e783dd1c0", "start": 1239.0, "end": 1245.0, "method": "original_frame", "frame_ids": [], "reviewer": "local_subagent", "status": "checked", "finding": "20:39餐吧、20:45私密房间，确认硬切及缺失转场过程；临时未遮挡帧已删除。", "affected_event_ids": ["mikey-practice-002-E0012"]}
{"review_id": "mikey-practice-002-V0006", "source_id": "mikey-practice-002", "source_revision": "sha256:b51c9fd748c03844665a056cec10a0407192bfbb51875d799eb8738e783dd1c0", "start": 1367.79, "end": 1935.4, "method": "original_frame", "frame_ids": [], "reviewer": "local_subagent", "status": "checked", "finding": "原尺寸节点仅用于确认距离构图与遮挡变化；敏感画面不保存、不作露骨描述，不能支持连续动作链。", "affected_event_ids": ["mikey-practice-002-E0014", "mikey-practice-002-E0015", "mikey-practice-002-E0016"]}
```

## 场景／切换

00:00—00:23用后文餐吧和私密房间素材作预告。正片主体先是餐吧第一人称实录与右下画中画复盘；20:39仍在餐吧，20:45已经切到蓝紫灯光的私密房间。移动、真实邀约、目的地说明和同意过程没有展示。2055.51秒后讲解者明确说拍摄结束，之后为结果自述、观众评论和课程营销。

## 角色

右下画中画按Mikey后期讲解者 `PM` 暂定归属；第一人称镜头佩戴者为 `P01`，不能因为画面文字出现“学员”就断定其身份；参与者为 `P02`。ASR没有说话人标签，所有逐句轮次仍待原音锚定。

## 重点动作／消息

- 07:17：参与者开放手掌；“底线测试”等含义来自讲解层。
- 18:37：参与者低头玩手机；稍后抽样又抬头、做手势，不能单向解释为没兴趣或生气。
- 21:15：私密房间初始座位提供后续距离变化基线。
- 27—32分钟：画面构图更近且多次遮挡；没有连续回看，不能复原谁先发起每次身体接触。

## 画面对文字的新增或纠正

1. 本片是实录加事后复盘，不是Mikey现场耳返指导。
2. “假兴趣”“测试”“隐性支配”“吸引爆炸”是讲解／红字解释，画面只能提供笑、手势、玩手机、重新参与、座位与距离等可见反馈。
3. 20:39—20:45硬切证明转场过程缺失，不能由到达私密房间倒推参与者知道真实理由并同意。
4. 参与者玩手机后又重新参与，单一行为信号存在多种解释。

## 隐私

正式保留的3张帧均已遮挡参与者脸部、画中画人物脸、联系方式、屏幕和私密区域。未遮挡原尺寸临时帧已删除。1367.79—1935.40只做必要非露骨登记，不保存或描述敏感动作细节。

## 待核

优先级最高的是：确认镜头佩戴者身份和说话层；补齐或确认20:39—20:45转场协商缺口；受控核对座位靠近、身体接触、“不要”以及后续调整的顺序；确认2055.51秒后结果只属自述。全部见 `review-needed.md`。
