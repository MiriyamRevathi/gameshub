import os
import shutil
import stat
import subprocess
import zipfile

BASE_DIR = r"C:\Users\miriy\.gemini\antigravity\scratch\python-games-main\python-games-main"
ZIP_PATH = r"C:\Users\miriy\.gemini\antigravity\scratch\python-games-main.zip"

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

# 1. Remove any nested venv / virtualenv directories
for root, dirs, files in os.walk(BASE_DIR):
    for d in list(dirs):
        if d in ["venv", ".venv", "env"]:
            p = os.path.join(root, d)
            try:
                shutil.rmtree(p, onerror=remove_readonly)
                print(f"Removed virtual environment directory: {p}")
            except Exception as e:
                print(f"Could not remove {p}: {e}")

# 2. Commit license changes in git
def git(args):
    cmd = ["git"] + args
    res = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error ({' '.join(cmd)}): {res.stderr}")
    return res

git(["add", "-A"])
git(["commit", "-m", "chore(license): transition to proprietary UNLICENSED model and remove open source files"])

# 3. Clean temporary helper scripts
for f in ["fix_license.py", "package_and_finalize.py"]:
    p = os.path.join(BASE_DIR, f)
    if os.path.exists(p):
        os.remove(p)

# 4. Rebuild updated zip archive
parent_dir = os.path.dirname(BASE_DIR)
if os.path.exists(ZIP_PATH):
    try:
        os.remove(ZIP_PATH)
    except Exception:
        pass

with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file == "clean_venvs_and_commit.py":
                continue
            full_path = os.path.join(root, file)
            if not os.path.exists(full_path):
                continue
            rel_path = os.path.relpath(full_path, parent_dir)
            zipf.write(full_path, rel_path)

zip_size_mb = round(os.path.getsize(ZIP_PATH) / (1024 * 1024), 2)
print(f"Updated zip archive successfully created at {ZIP_PATH} ({zip_size_mb} MB)")

if os.path.exists(os.path.join(BASE_DIR, "clean_venvs_and_commit.py")):
    os.remove(os.path.join(BASE_DIR, "clean_venvs_and_commit.py"))
print("All complete!")
