import shutil
import datetime
import os

# المجلد اللي عايز تعمله باك اب
source_folder = "my_data"
backup_folder = "backup"

# تأكد إن فولدر الباك أب موجود
os.makedirs(backup_folder, exist_ok=True)

# اسم الملف الجديد مع التاريخ
backup_name = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"

# عمل نسخة مضغوطة من الفولدر
shutil.make_archive(os.path.join(backup_folder, backup_name.replace(".zip","")), 'zip', source_folder)

print("✅ Backup created:", backup_name)
