---
title: "GitHub Pagesでカスタムドメインを設定する"
emoji: "📄"
type: "tech"
topics: ["githubpages"]
published: true
published_at: 2024-12-30
---

## 1. Custom domainの検証

乗っ取り攻撃を回避するために、カスタムドメインをリポジトリに追加する前に検証することがお勧めされています。

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site?platform=linux

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages

### User site

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages#verifying-a-domain-for-your-user-site

### Organization site

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages#verifying-a-domain-for-your-organization-site

## 2. Custom domainの設定 ①

`Custom domain` に取得したドメインを入力して `Save` する。

![](/images/11/1.png)

Apexドメインを使う場合、Aレコード/AAAAレコードを追加する。

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

また、Apexドメインを使う場合、wwwサブドメインの設定を行うことがお勧めされています。

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site?platform=linux#configuring-an-apex-domain-and-the-www-subdomain-variant

![](/images/11/2.png)

## 3. Custom domainの設定 ②

① の冒頭で設定した `Custom domain` で、 `✔ DNS check successful` と表示されることを確認する。

![](/images/11/3.png)
