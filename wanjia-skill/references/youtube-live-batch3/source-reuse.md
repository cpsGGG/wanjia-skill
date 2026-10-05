# YouTube公开直播第三批：来源复用账本

正式对照为183来源；本批结论：10 unique、0 reuse、0 suspected。

| 来源 | 直播 | 结论 | 权重建议 | 主要证据 |
|---|---:|---|---:|---|
| `mikey-youtube-live-021` | 68 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |
| `mikey-youtube-live-022` | 70 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |
| `mikey-youtube-live-023` | 72 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |
| `mikey-youtube-live-024` | 75 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |
| `mikey-youtube-live-025` | 77 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |
| `mikey-youtube-live-026` | 79 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |
| `mikey-youtube-live-027` | 80 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |
| `mikey-youtube-live-028` | 81 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |
| `mikey-youtube-live-029` | 82 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |
| `mikey-youtube-live-030` | 83 | unique | 1 | 无身份、源SHA、规范化全文或40字符窗重复 |

## 特殊边界

直播70含播放材料/动漫内容，来源唯一不等于其中每句话属于Mikey；跨期使用必须保留人物与内容层归属。直播82含多次电话，来电者发言不能归给Mikey。

## 限制

- This is a whole-episode duplicate precheck, not a partial-reuse audit.
- Visual mismatch can rule out the same preserved video recording but cannot rule out audio-only reuse with entirely replaced visuals.
- Only retained-source media or retained storyboards were available for direct content comparison before batch-3 ASR.
- Similar titles, livestream templates, and near-equal duration were treated only as candidate generators, never as proof of duplication.
- Isolated matching windows are phrase or case reuse candidates, not full-episode duplicates; inspect high-count pairs before integration.
