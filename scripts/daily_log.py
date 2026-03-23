import datetime
import os
from pathlib import Path
from zoneinfo import ZoneInfo

today = datetime.datetime.now(ZoneInfo("Asia/Tokyo")).date()
output_path = os.getenv("DAILY_LOG_OUTPUT_PATH", "tmp/daily_log.md")
log_path = Path(output_path)
branch = os.getenv("GITHUB_REF_NAME", "dev")
status = os.getenv("LOG_STATUS", "Success")

entry = f"- {today}\n  - 作業内容: TODO\n  - ブランチ: {branch}\n  - Actions結果: {status}\n"

log_path.parent.mkdir(parents=True, exist_ok=True)
with open(log_path, "a", encoding="utf-8") as f:
    f.write(entry)