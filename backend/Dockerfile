# ベースイメージ
FROM python:3.11

# 作業ディレクトリの設定
WORKDIR /app/

# 必要なPythonパッケージのインストール
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# アプリケーションファイルをコピー
COPY ./ /app/

# コマンドの実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
