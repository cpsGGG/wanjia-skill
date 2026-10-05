# YouTube公开直播第二批：来源复用账本

正式对照为173来源；本批结论：10 unique、0 reuse、0 suspected。

| 来源 | 直播 | 结论 | 权重建议 | 主要证据 |
|---|---:|---|---:|---|
| `mikey-youtube-live-011` | 47 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |
| `mikey-youtube-live-012` | 49 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |
| `mikey-youtube-live-013` | 50 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |
| `mikey-youtube-live-014` | 53 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |
| `mikey-youtube-live-015` | 54 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |
| `mikey-youtube-live-016` | 57 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |
| `mikey-youtube-live-017` | 58 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |
| `mikey-youtube-live-018` | 59 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |
| `mikey-youtube-live-019` | 61 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |
| `mikey-youtube-live-020` | 62 | unique | 1 | 无身份/SHA/规范化全文/40字符窗/故事板重复 |

## 特殊边界

直播58/59虽判为整期来源unique，但游戏剧情、旁白、观众文字与Mikey评论共用音轨；来源唯一不等于观点归属已确认。跨期使用必须保留五类归属标签。

## 限制

- SHA-256 uniqueness excludes byte-identical files but not all differently encoded copies.
- The prior storyboard audits strongly reject visual duplicates but cannot rule out audio-only reuse with entirely replaced visuals.
- The gameplay classification is based on sparse visual checkpoints, not continuous viewing or completed speaker diarization.
- The normalized-text audit covers exact full-text equality and exact continuous 40-character windows; shorter paraphrase, translated reuse, or heavily edited retellings can still exist.
