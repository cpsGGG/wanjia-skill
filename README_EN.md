<p align="center"><img src="assets/cover.png" alt="Two facing sculptures representing conversation and judgement" width="100%" /></p>
<h1 align="center">玩家.skill · Wanjia</h1>
<p align="center"><strong>Ask a concrete question. Understand the reasoning behind the answer.</strong></p>
<p align="center"><a href="https://github.com/cpsGGG/wanjia-skill/releases/latest">Download</a> · <a href="README.md">中文</a> · <a href="docs/how-it-works.md">How it works</a></p>

A source-grounded conversational skill built from materials by Mikey, the creator of 搭讪玩家. It organizes ideas, reasoning and methods from videos, courses, livestreams and posts so you can ask about attraction, conversation, invitations and relationships, understand the relevant judgement, and consider a next step.

Answers aim to reflect the reasoning and expression found in the materials. This is a simulation based on sources, not Mikey speaking or endorsing the project.

## An example

**How do I choose photos for a dating profile?**

An illustrative simulated answer, not a verbatim quotation:

> Start with what each photo communicates. In this discussion, a photo can present you as attractive or convey the value you want to show. Keep it natural; editing should not turn your features into someone else's.

Checking a shortlist for what it conveys and whether you remain recognizable is an editorial application to dating profiles. The source discussion concerned social-feed photos; this example does not promise matches. See [the source and exact context](docs/photo-example.md).

## What it does

- Finds relevant discussions and explains their reasons and conditions.
- Compares apparently conflicting advice across situations.
- Uses reviewed methods to suggest specific actions and observations.
- Provides source references and lets you read the surrounding text.

The library contains **512 source records and 3,649 knowledge entries**, including 209 community posts. Records include reused and research materials; collection size is distinct from the scope approved for simulated answers. See [scope](docs/scope.md).

## Install

Use a Codex environment with local file access and Python execution. **Python 3.10+** is required; the retrieval tools have no third-party dependencies.

1. Download and extract the [latest release](https://github.com/cpsGGG/wanjia-skill/releases/latest).
2. Copy the entire `wanjia-skill` folder to `~/.agents/skills/wanjia-skill/`, or to your project's `.agents/skills/`. On Windows, the personal location is `%USERPROFILE%\.agents\skills\wanjia-skill\`.
3. Invoke `$wanjia-skill` in Codex. Restart Codex if it does not appear.

Copy the full folder, including its knowledge and scripts. See [installation](INSTALL.md) and the [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Try it

```text
$wanjia-skill

My conversations feel like interviews. Ask for the context that matters,
then use the relevant materials to explain the problem and suggest one next step.
```

You can also ask how to choose dating-profile photos, why an interaction feels stiff, or when two different ideas about neediness apply. Describe the situation, what you tried and the response you received.

## How it works

The skill retrieves relevant entries and reads their surrounding source text. Reasons, conditions, attribution and conflicts remain attached to the knowledge. Answers distinguish source views, editorial synthesis and inferences about your new situation. Unresolved material retains its limits; original transcripts and correction records are stored separately.

See [implementation](docs/how-it-works.md), [source scope](docs/scope.md) and [contributing](CONTRIBUTING.md).

## Attribution and license

Original code and authored documentation use [MIT](LICENSE). Source texts, quotations and images retain their original authors' and third parties' rights; see [notices](THIRD_PARTY_NOTICES.md). Runtime permission to use a method is distinct from copyright permission. Transcription, identity and case-context questions remain in some materials; real-world effectiveness is not uniformly validated.

The cover is AI-generated. See [contents](CONTENTS.md) and [changelog](CHANGELOG.md).
