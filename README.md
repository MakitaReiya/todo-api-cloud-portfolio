# TODO API Cloud Portfolio

FastAPIを用いたTODO管理APIです。
転職用ポートフォリオとして作成しており、今後AWS上での実行、Docker化、TerraformによるIaC化、監視設定まで拡張予定です。

## 概要
このアプリは、TODOを管理するためのシンプルなAPIです。
現在はFastAPIで基本的なAPIを実装中で、Swagger UIから動作確認できます。

## 目的
このプロジェクトでは、以下を示すことを目的にしています。
- Python を使った API 開発ができること
- FastAPI を使ってシンプルな CRUD API を実装できること
- PostgreSQL と連携したデータ管理ができること
- Docker でローカル実行環境を整えられること
- AWS(ECS, RDS, ALB など) にデプロイできること
- Terraform による IaC 化ができること
- CloudWatch / SNS を使った監視の基礎を実装できること

## 使用技術

### 現在
- Python
- FastAPI
- Uvicorn

### 今後追加予定
- PostgreSQL
- SQLAlchemy
- Docker
- AWS ECS Fargate
- AWS RDS
- AWS ALB
- Terraform
- GitHub Actions
- CloudWatch
- SNS

## API 一覧

### Health Check
- `GET /health`

### Todo
- `POST /todos`
- `GET /todos`
- `GET /todos/{id}`
- `PUT /todos/{id}`
- `DELETE /todos/{id}`

## 現在の実装状況
- [x] FastAPI環境構築
- [x] ヘルスチェックAPI (`GET /health`)
- [x] TODO作成API (`POST /todos`)
- [x] TODO一覧取得API (`GET /todos`)
- [x] TODO詳細取得API (`GET /todos/{id}`)
- [x] TODO更新API (`PUT /todos/{id}`)
- [x] TODO削除API (`DELETE /todos/{id}`)
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

### 2. ライブラリをインストール
```bash
pip install fastapi uvicorn

### 3. サーバー起動
```bash
uvicorn app.main:app --reload

### 4. アクセス
```bash
- Swagger UI: http://127.0.0.1:8000/docs
- Health Check: http://127.0.0.1:8000/health

## ディレクトリ構成

todo-api-cloud-portfolio/
├── app/
│   └── main.py
├── README.md
└── venv/


## Author

GitHub 上で継続的に更新予定です。

---

# README を反映したらやること

ターミナルでこれを実行。

```bash
git add README.md
git commit -m "Update README"
git push
