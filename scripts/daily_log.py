import datetime

log_path = "C:/Users/TKC/Dropbox/logseq/Logseq_graph/pages/contents.md"  # Dropbox連携している場所
today = datetime.date.today()

branch = "dev"  # これは環境変数でもOK
status = "Success"

entry = f"- {today}\n  - 作業内容: TODO\n  - ブランチ: {branch}\n  - Actions結果: {status}\n"

with open(log_path, "a") as f:
    f.write(entry)