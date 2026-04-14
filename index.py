from pathlib import Path
import json

models_dir = Path("models")
files = sorted([p.name for p in models_dir.glob("*.glb")])

with open(models_dir / "index.json", "w", encoding="utf-8") as f:
    json.dump(files, f, indent=2)

print("index.json updated with", len(files), "files")