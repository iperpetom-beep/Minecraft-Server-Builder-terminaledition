#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ -d "venv" ] && [ -x "venv/bin/python" ]; then
  PYTHON_EXEC="${SCRIPT_DIR}/venv/bin/python"
else
  PYTHON_EXEC="$(command -v python3 || command -v python || true)"
fi

if [ -z "$PYTHON_EXEC" ]; then
  echo "Python 3 не найден. Установите Python 3 и повторите попытку."
  exit 1
fi

"$PYTHON_EXEC" start.py
