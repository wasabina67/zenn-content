---
title: "ZodでTypeScriptのバリデーションを型安全に行う"
emoji: "🔍"
type: "tech"
topics: ["zod", "typescript"]
published: true
published_at: 2025-10-05
---

## Zodとは

ZodはTypeScript向けのスキーマ宣言およびバリデーションライブラリです。
スキーマから型を自動推論できるため、型定義とバリデーションロジックを二重管理する必要がありません。

## インストール

```bash
npm install zod
```

## 基本的な使い方

### スキーマの定義

```typescript
import { z } from 'zod';

const UserSchema = z.object({
  name: z.string(),
  age: z.number().min(0),
  email: z.string().email(),
});

// スキーマから型を推論
type User = z.infer<typeof UserSchema>;
```

### バリデーション

```typescript
// 成功例
const validData = {
  name: "太郎",
  age: 25,
  email: "taro@example.com"
};
const result = UserSchema.parse(validData); // OK

// 失敗例
const invalidData = {
  name: "太郎",
  age: -1,
  email: "invalid-email"
};
UserSchema.parse(invalidData); // ZodErrorがthrowされる
```

### エラーハンドリング

```typescript
const result = UserSchema.safeParse(data);

if (result.success) {
  console.log(result.data); // バリデーション済みデータ
} else {
  console.log(result.error); // エラー詳細
}
```

## よく使う型

```typescript
// プリミティブ型
z.string()
z.number()
z.boolean()
z.date()

// オプショナル・デフォルト値
z.string().optional()
z.number().default(0)

// 配列・オブジェクト
z.array(z.string())
z.object({ key: z.string() })

// ユニオン型
z.union([z.string(), z.number()])
```

## 参考資料

https://zod.dev/
