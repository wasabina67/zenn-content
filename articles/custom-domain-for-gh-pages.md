---
title: "GitHub Pagesでカスタムドメインを設定する"
emoji: "🌊"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["github", "githubpages"]
published: true
published_at: 2024-08-04
---

# はじめに

GitHub Pagesでカスタムドメインを設定する手順をメモしておきます。

# Custom domainの設定 ①

`Custom domain` に取得したドメインを入力して Save します。

![](https://github.com/user-attachments/assets/31218dd0-093c-40d9-a0df-46a2a05e591e)

# カスタムドメインの検証

後述の [Managing a custom domain for your GitHub Pages site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site?platform=linux) のTipsより、ドメインの設定前に**ドメインの検証**をすることがお勧めされています。

`User site` / `Organization site` それぞれで検証方法が記載されています。

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages

### User site

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages#verifying-a-domain-for-your-user-site

### Organization site

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages#verifying-a-domain-for-your-organization-site

# カスタムドメインの設定

Apexドメインを使う場合、Aレコード/AAAAレコードを追加します。

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

```
USERNAME-or-ORGANIZATION.github.io
```

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site?platform=linux

今回使用したムームードメインでは、以下のような見え方になりました。

![](https://github.com/user-attachments/assets/4494227e-6d01-4eb2-bdc2-aeb5143f4b5f)

# Custom domainの設定 ②

①で設定した `Custom domain` で、 `✔ DNS check successful` と表示されることを確認します。

![](https://github.com/user-attachments/assets/de076050-e573-4a67-bd8d-49ef5e05a6a3)
