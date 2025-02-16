# === ARISS_Python_Test.py ================================================
"""
| NAME: ARISS Python Test
| BY: Ken McCaughey (N3FZX)
| ON: 2025-02-16
| PROJECT: ARISS
| SCRIPT: ARISS_Python_Test.py
| VERSION: 1.1.0
| STATUS: Final version.
| SPDX-FileCopyrightText: 2025 Ken McCaughey
| SPDX-License-Identifier: Creative Commons Attribution-ShareAlike 4.0

PURPOSE:
  Test script for new Python users.
  
  Also helps to verify Python libraries for various ARISS tools was loaded
  properly using pip or other means.

"""

# === LIBRARIES (must be first) ===
from docxtpl import DocxTemplate  # Not used, but does verify it exists.
from datetime import datetime
from datetime import timedelta
import sys

# Version info
version_date = '2025-02-16'
version = '1.1.0'

# ========================================================================
# MAIN
# ========================================================================

# Print welcome message.
print()
print('Python script: ARISS Python Test.py')
print('           V.:', version)
print('           By: Ken McCaughey, N3FZX')
print('           On:', version_date)
print()
print('This is a simple test script for new Python users.')
print('It is intended to make sure scripts can be executed.')
print()
print('Hello World!')
print()

currentDateAndTime = datetime.now()  # Get date/time from computer.
print("The current date and time is", currentDateAndTime)

print()
print('Success! Congratulations, you just ran a Python script.')
print()

# End of script
