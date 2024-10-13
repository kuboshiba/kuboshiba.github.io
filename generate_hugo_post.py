import time
import os
import uuid
import random
import shutil

# 1. 現在のUnixタイムスタンプをミリ秒単位で取得
timestamp = int(time.time() * 1000)

# 2. UUIDを生成
unique_id = str(uuid.uuid4())

# 3. 背景画像が保存されているディレクトリ
background_dir = "./assets/img/background"

# 4. ディレクトリから画像ファイルをランダムに選択
background_images = [f for f in os.listdir(background_dir) if os.path.isfile(os.path.join(background_dir, f))]
selected_image = random.choice(background_images)

# 5. 画像ファイルの拡張子を取得
_, file_extension = os.path.splitext(selected_image)

# 6. hugo new コマンドのフォルダ名を生成（ミリ秒タイムスタンプ + UUID）
new_post_dir = f"posts/{timestamp}-{unique_id}"

# 7. 新しい記事フォルダが存在しない場合は作成する
os.makedirs(new_post_dir, exist_ok=True)

# 8. hugo new コマンドを実行して、新しい記事フォルダとindex.mdを作成
command = f"hugo new {new_post_dir}/index.md"
os.system(command)

# 9. ランダムで選ばれた画像を新しいフォルダに "featured.{拡張子}" としてコピー
destination_path = f"content/{new_post_dir}/featured{file_extension}"
shutil.copy(os.path.join(background_dir, selected_image), destination_path)

# 10. 実行されたコマンドと画像のコピーを表示
print(f"Executed: {command}")
print(f"Copied: {selected_image} to {destination_path}")
