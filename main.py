import os
from pathlib import Path

TEXT = "The deadline slipped because my context window held a funeral for the original plan and your new requirements gave the eulogy."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
