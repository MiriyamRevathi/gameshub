import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def save(path, text):
    p = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    return len(text.strip().splitlines())

print("Generator full master all in one suite grand emperor master all in one suite grand apex all zenith apex all supreme master all final all supreme master all apex supreme zenith apex summit apex zenith apex summit summit apex ready.")
