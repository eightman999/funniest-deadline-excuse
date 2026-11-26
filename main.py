import os
from pathlib import Path

TEXT = "Sorry I missed the deadline: I finished on time in three parallel drafts, and then you picked the timeline where I did not."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
