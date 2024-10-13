import time
import os
import uuid

# 1. 現在のUnixタイムスタンプをミリ秒単位で取得
timestamp = int(time.time() * 1000)

# 2. UUIDを生成
unique_id = str(uuid.uuid4())

# 3. hugo new コマンドのフォルダ名を生成（ミリ秒タイムスタンプ + UUID）
command = f"hugo new posts/{timestamp}-{unique_id}/index.md"

# 4. コマンドを実行して、新しい記事フォルダとindex.mdを作成
os.system(command)

# 5. 実行されたコマンドを表示
print(f"Executed: {command}")
