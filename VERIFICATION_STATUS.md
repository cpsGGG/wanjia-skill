# 核验范围

`package-manifest.json` 绑定本公开副本的全部分发文件；`FREEZE_INPUT.json` 绑定当前技能树、来源计数与运行许可。`PUBLICATION_CHANGES.json` 记录公开遮盖与历史输入的区别，原本地 v0.2.1 不被覆盖。

`python tools/verify_package.py` 检查文件 SHA/长度、来源与知识数量、包内资源、限定 payload 及当前运行许可；`python tools/smoke_check.py` 实际执行检索、带知识绑定的回读、音频校正候选提示与拒绝路线。GitHub Actions 在 Windows/Linux 与 Python 3.10/3.13 上运行这两项检查，具体状态见 Actions 页面。

当前测量为512条来源记录、3649条知识，117条允许有限模拟表达，内含51项有限动作。其余全文、邻近段和历史不继承这些许可；许可 ID、authority 和运行脚本的 SHA 随冻结记录保存。

这些检查不认证整库逐句听校、人物身份、本人口吻、现实效果或全部疑点已解决。303个视频来源未记录全片逐句听校完成，缺原音画和案例上下文的事项继续保留限制；具体资料状态见 [docs/scope.md](docs/scope.md) 及技能内的当前状态与待核记录。

分发工具拒绝覆盖既有 ZIP，并逐项核对成品字节和 CRC。历史制作记录中的“未部署”“未发布”、旧本机路径或旧输入 SHA 是当时的记录；当前安装入口、公开副本完整性和网上发行以本仓库及本版清单为准，不扩大运行许可。
