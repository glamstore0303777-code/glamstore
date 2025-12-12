#!/usr/bin/env python3
import os

os.chdir('C:\\ProyectoF\\glamstore')
os.environ['GIT_PAGER'] = ''
os.environ['PAGER'] = ''

# Execute git commands
exit_code = os.system('git add core/migrations/0042_populate_lotes_and_vencimiento.py')
print(f"Add exit code: {exit_code}")

exit_code = os.system('git commit -m "Fix migration 0042: Use lowercase column name fechavencimiento for PostgreSQL"')
print(f"Commit exit code: {exit_code}")

exit_code = os.system('git push origin main')
print(f"Push exit code: {exit_code}")
