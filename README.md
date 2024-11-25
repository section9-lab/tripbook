
# FastAPI + Vercel

```
tripbook/
├── app/
│   ├── __init__.py         # 空文件，用于标记 app 是一个 Python 包
│   ├── main.py             # FastAPI 主入口
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py       # 路由定义
│   │   ├── models.py       # Pydantic 模型
│   │   ├── schemas.py      # 数据输入/输出
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py       # 配置管理
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models.py       # SQLAlchemy 模型
│   │   ├── database.py      # 数据库连接
├── requirements.txt        # Python 依赖
└── vercel.json             # Vercel 配置

```

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.
