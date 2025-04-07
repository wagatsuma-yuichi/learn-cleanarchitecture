### 起動する場合
```bash
cd 001_simple_cleanarchitecture
pip install -r requirements.txt
APP_ENV=develop uvicorn main:app --host 0.0.0.0 --port 8000
```