# Web Application Load Testing with Locust

このプロジェクトは、Pythonの負荷テストツールLocustを使用して、Webアプリケーションの負荷テストを行うためのスクリプトです。

## 概要

このスクリプトは以下の機能を提供します：

1. Webアプリケーションへのログイン
2. ログイン後の特定ページへのアクセス

これらの操作を多数の仮想ユーザーで同時に実行することで、アプリケーションの負荷耐性をテストします。

## 必要条件

- Python 3.7以上
- Locust

## インストール

1. このリポジトリをクローンまたはダウンロードします。

2. 必要なパッケージをインストールします：

`pip install locust`


## 使用方法

1. `locustfile.py` 内の以下の項目を、テスト対象のWebアプリケーションに合わせて変更します：

- `your_email@example.com`
- `your_password`
- `https://your-website.com`

2. コマンドラインで以下のコマンドを実行してLocustを起動します：

3. ブラウザで `http://localhost:8089` にアクセスします。

4. Web UIで必要なパラメータ（同時ユーザー数、秒間のユーザー増加率）を設定し、テストを開始します。

## カスタマイズ

- `WebAppUser` クラス内の `access_specific_page` メソッドを修正することで、ログイン後のユーザー行動をカスタマイズできます。
- 新しいタスクを追加する場合は、`@task` デコレータを使用して新しいメソッドを作成します。

## 注意事項

- このスクリプトは教育および開発目的のみで使用してください。
- 実際の運用環境で負荷テストを行う場合は、必ず事前に許可を得てください。
- テスト用のアカウントを使用し、実際のユーザーデータを使用しないよう注意してください。
