import datetime
from pathlib import Path

today = datetime.date.today()
log_path = Path(f"C:/Users/TKC/Dropbox/logseq/Logseq_graph/journals/{today:%Y_%m_%d}.md")  # Dropbox連携している場所

branch = "dev"  # これは環境変数でもOK
status = "Success"

entry = f"- {today}\n  - 作業内容: TODO\n  - ブランチ: {branch}\n  - Actions結果: {status}\n"

log_path.parent.mkdir(parents=True, exist_ok=True)
with open(log_path, "a", encoding="utf-8") as f:
    f.write(entry)