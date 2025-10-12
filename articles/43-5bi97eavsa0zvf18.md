---
title: "5つのPDF生成ライブラリ"
emoji: "📝"
type: "idea"
topics: ["reports", "pdf"]
published: true
published_at: 2025-10-12
---

## 1. prawnpdf/prawn

https://github.com/prawnpdf/prawn

**言語**: Ruby

**概要**: RubyでPDFを生成するための純粋なRubyライブラリ。外部依存なしで動作し、テキスト、画像、グラフィックスを含む複雑なPDF文書を作成できる。

**特徴**:
- シンプルで直感的なAPI
- テーブル、画像、グラフィックスのサポート
- 多言語・UTF-8サポート
- カスタムフォントの使用が可能

**使用例**:

```ruby
require "prawn"

Prawn::Document.generate("hello.pdf") do
  text "Hello World!"
end
```

## 2. pdfme/pdfme

https://github.com/pdfme/pdfme

**言語**: TypeScript/JavaScript

**概要**: TypeScriptで書かれた、テンプレートベースのPDF生成ライブラリ。ブラウザとNode.js両方で動作する。デザイナーを使ってテンプレートを作成し、データを流し込むことでPDFを生成できる。

**特徴**:
- テンプレートデザイナー付属
- ブラウザとNode.js両対応
- JSONベースのテンプレート定義
- 動的なPDF生成に最適

## 3. bpampuch/pdfmake

https://github.com/bpampuch/pdfmake

**言語**: JavaScript

**概要**: クライアントサイドとサーバーサイド両方で動作する、JavaScriptベースのPDF生成ライブラリ。宣言的な文書定義により、複雑なレイアウトを簡単に作成できる。

**特徴**:
- クライアント/サーバーサイド対応
- テーブル、リスト、画像のサポート
- カスタムフォント対応
- 宣言的な文書定義

**使用例**:

```javascript
const pdfMake = require('pdfmake/build/pdfmake');

const docDefinition = {
  content: [
    'Hello World!'
  ]
};

pdfMake.createPdf(docDefinition).download('document.pdf');
```

## 4. QuestPDF/QuestPDF

https://github.com/QuestPDF/QuestPDF

**言語**: C#

**概要**: .NET向けのモダンなPDF生成ライブラリ。Fluent APIを使用して、複雑なレイアウトを簡潔なコードで記述できる。商用利用には有償ライセンスが必要。

**特徴**:
- Fluent APIによる直感的な記述
- レスポンシブなレイアウト
- 豊富なコンポーネント
- 高速なレンダリング

**使用例**:

```csharp
using QuestPDF.Fluent;
using QuestPDF.Helpers;

Document.Create(container =>
{
    container.Page(page =>
    {
        page.Content().Text("Hello World!");
    });
}).GeneratePdf("document.pdf");
```

## 5. parallax/jsPDF

https://github.com/parallax/jsPDF

**言語**: JavaScript

**概要**: クライアントサイドでPDFを生成するための、最も広く使われているJavaScriptライブラリの一つ。ブラウザ内で完結するため、サーバーへのアップロードが不要。

**特徴**:
- ブラウザ内でPDF生成
- プラグインシステムによる拡張性
- HTML to PDF変換サポート
- テキスト、画像、図形の描画

**使用例**:

```javascript
const { jsPDF } = window.jspdf;
const doc = new jsPDF();

doc.text("Hello World!", 10, 10);
doc.save("document.pdf");
```
