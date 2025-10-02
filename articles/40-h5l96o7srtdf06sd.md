---
title: "ZennのGitHub連携の記事投稿にて、type: techと指定しているのに、ideaになってしまう"
emoji: "📝"
type: "tech"
topics: ["zenn"]
published: true
published_at: 2025-10-02
---

## 事象

- GitHub連携を利用して、zenn記事の公開をしている
- markdown内に、type: "tech"を指定しているにもかかわらず、"idea"として表示されていた
- zenn-dev/zenn-communityで聞いてみた
  - [markdownメタデータのtype: "tech"が反映されない · Issue #734 · zenn-dev/zenn-community](https://github.com/zenn-dev/zenn-community/issues/734)

## 原因

https://zenn.dev/tech-or-idea

> 判断がむずかしい場合はどちらを選んでも構いません。ただし、運営側で通知なく変更を行うことがあります。（自動で変更が行われることもあります。おかしければご報告ください）

まず、Tech/Ideaについて、運営側で設定を変更する場合があるとのこと。変更された場合には、GitHubのtypeと齟齬が生じます。

> Webエディタ上では運営による変更があった場合はその文言を確認いただけるのですが、GitHub連携のユーザーにはそれが伝わりづらい問題があり、通知の方法を検討しています。

とのことで、変更があった場合の通知方法を検討中とのことでした。
