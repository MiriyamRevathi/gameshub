import os
import re

BASE_DIR = r"C:\Users\miriy\.gemini\antigravity\scratch\python-games-main\python-games-main"

# 1. Remove open source LICENSE file if present
for root, dirs, files in os.walk(BASE_DIR):
    for f in files:
        if f.upper().startswith("LICENSE") or f.upper().startswith("COPYING"):
            p = os.path.join(root, f)
            os.remove(p)
            print(f"Removed license file: {p}")

# 2. Update package.json
pkg_json = os.path.join(BASE_DIR, "package.json")
if os.path.exists(pkg_json):
    with open(pkg_json, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r'"license":\s*"[^"]*"', '"license": "UNLICENSED"', content)
    with open(pkg_json, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated package.json: license -> UNLICENSED")

# 3. Update package-lock.json
pkg_lock = os.path.join(BASE_DIR, "package-lock.json")
if os.path.exists(pkg_lock):
    with open(pkg_lock, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r'"license":\s*"[^"]*"', '"license": "UNLICENSED"', content)
    with open(pkg_lock, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated package-lock.json: license -> UNLICENSED")

# 4. Update pyproject.toml
pyproj = os.path.join(BASE_DIR, "pyproject.toml")
if os.path.exists(pyproj):
    with open(pyproj, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r'license\s*=\s*"[^"]*"', 'license = "Proprietary"', content)
    with open(pyproj, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated pyproject.toml: license -> Proprietary")

# 5. Update README.md
readme = os.path.join(BASE_DIR, "README.md")
if os.path.exists(readme):
    with open(readme, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("MIT License", "Proprietary - All Rights Reserved")
    content = content.replace("MIT", "Proprietary")
    with open(readme, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated README.md: license references -> Proprietary")

print("License configuration updated successfully.")
