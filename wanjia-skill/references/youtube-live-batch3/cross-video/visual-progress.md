# YouTube直播第三批视觉进度

更新时间（UTC）：`2026-09-19T15:09:51.293175+00:00`

本页由10份最终视觉manifest重新聚合，并同时核对候选JPG、联系表JPG及600秒分块manifest。

| 来源 | 直播 | 类型 | 分块 | 候选/文件 | 联系表/文件 | 校验 |
|---|---:|---|---:|---:|---:|---|
| mikey-youtube-live-021 | 68 | 直播低密度 | 7 | 302/302 | 7/7 | passed |
| mikey-youtube-live-022 | 70 | 动漫讨论加密 | 11 | 820/820 | 18/18 | passed |
| mikey-youtube-live-023 | 72 | 直播低密度 | 10 | 435/435 | 10/10 | passed |
| mikey-youtube-live-024 | 75 | 直播低密度 | 10 | 402/402 | 9/9 | passed |
| mikey-youtube-live-025 | 77 | 直播低密度 | 7 | 291/291 | 7/7 | passed |
| mikey-youtube-live-026 | 79 | 直播低密度 | 7 | 313/313 | 7/7 | passed |
| mikey-youtube-live-027 | 80 | 直播低密度 | 8 | 340/340 | 8/8 | passed |
| mikey-youtube-live-028 | 81 | 直播低密度 | 10 | 431/431 | 9/9 | passed |
| mikey-youtube-live-029 | 82 | 直播低密度 | 16 | 693/693 | 15/15 | passed |
| mikey-youtube-live-030 | 83 | 直播低密度 | 7 | 332/332 | 7/7 | passed |

## 汇总

- 逐期：10/10 通过。
- 600秒分块manifest：93份。
- 候选帧：4359条manifest记录，对应4359个JPG。
- 联系表：97条manifest记录，对应97个JPG。
- 缺失引用：候选0，联系表0；未引用JPG：候选0，联系表0。

## 直播70重点

- `mikey-youtube-live-022`：11分块，820候选帧，18联系表；manifest要求显式区分Mikey评论、动漫台词/旁白、观众文字、Mikey转述和重叠不明。

## 边界

视觉候选和联系表只用于定位画面信息，不等于已经理解视频，也不等于连续音画核验。直播70中动漫角色、旁白、剧情、字幕和观众文字不得自动归给Mikey。
