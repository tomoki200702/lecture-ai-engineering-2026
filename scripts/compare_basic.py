"""同じ質問を各モデルに3回ずつ送り、実際の出力を保存する。"""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("models", nargs="+", help="比較するモデル名")
    parser.add_argument("--question", default="LoRAとは何ですか？")
    parser.add_argument("--output", default="lectures/01/results.json")
    args = parser.parse_args()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEYを環境変数に設定してください。")

    root = Path(__file__).resolve().parents[1]
    output = root / args.output
    results = []
    for model in args.models:
        for repeat in range(1, 4):
            print(f"{model} {repeat}/3", flush=True)
            try:
                run = subprocess.run(
                    [sys.executable, "-m", "app.ask", args.question],
                    cwd=root,
                    env={**os.environ, "AIE_MODEL": model, "PYTHONIOENCODING": "utf-8"},
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=180,
                )
            except subprocess.TimeoutExpired:
                run = subprocess.CompletedProcess([], 124, "", "180秒でタイムアウト")
            results.append({
                "model": model,
                "repeat": repeat,
                "question": args.question,
                "exit_code": run.returncode,
                "output": run.stdout.replace(api_key, "[REDACTED]"),
                "error": run.stderr.replace(api_key, "[REDACTED]"),
            })
            output.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            time.sleep(5)
    print(f"保存先: {output}")


if __name__ == "__main__":
    main()
