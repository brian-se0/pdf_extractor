from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def run_ocrmypdf(
    input_pdf: Path,
    output_pdf: Path,
    force_ocr: bool = False,
) -> tuple[bool, str | None]:
    if shutil.which("ocrmypdf") is None:
        return False, "ocrmypdf binary not found on PATH"

    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    command = ["ocrmypdf", "--quiet", "--optimize", "0"]
    if force_ocr:
        command.append("--force-ocr")
    else:
        command.append("--skip-text")

    command.extend([str(input_pdf), str(output_pdf)])

    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)

    if completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip() or "unknown OCR error"
        return False, message

    return True, None
