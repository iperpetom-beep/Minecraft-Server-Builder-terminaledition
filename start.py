#!/usr/bin/env python3

import subprocess
import os

# Путь к Python в виртуальном окружении
venv_python = os.path.join(os.getcwd(), "venv", "bin", "python")

# Запуск менеджера
subprocess.run([venv_python, "-m", "mcmanager"])