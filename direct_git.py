#!/usr/bin/env python3
import os
import sys

# Change to repo directory
os.chdir('C:\\ProyectoF\\glamstore')

# Disable pager
os.environ['GIT_PAGER'] = ''
os.environ['PAGER'] = ''

# Execute git commands directly
os.system('git add core/migrations/0042_populate_lotes_and_vencimiento.py')
os.system('git commit -m "Fix migration 0042: Use lowercase column name fechavencimiento for PostgreSQL"')
os.system('git push origin main')

print("Done!")
