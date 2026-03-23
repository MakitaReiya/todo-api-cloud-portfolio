# TODO API Cloud Portfolio

FastAPIを用いたTODO管理APIです。
転職用ポートフォリオとして作成しており、今後AWS上での実行、Docker化、TerraformによるIaC化、監視設定まで拡張予定です。

## 概要
このアプリは、TODOを管理するためのシンプルなAPIです。
現在はFastAPIで基本的なAPIを実装中で、Swagger UIから動作確認できます。

## 使用技術
- Python
- FastAPI
- Uvicorn

## 現在の実装状況
- [x] FastAPI環境構築
- [x] ヘルスチェックAPI (`GET /health`)
- [ ] TODO作成API (`POST /todos`)
- [ ] TODO一覧取得API (`GET /todos`)
- [ ] TODO詳細取得API (`GET /todos/{id}`)
- [ ] TODO更新API (`PUT /todos/{id}`)
- [ ] TODO削除API (`DELETE /todos/{id}`)
- [ ] PostgreSQL連携
- [ ] Docker化
- [ ] AWSデプロイ
- [ ] Terraform化
- [ ] CloudWatch監視
- [ ] SNS通知

## 起動方法

### 1. 仮想環境を有効化
```bash
source venv/bin/activate
