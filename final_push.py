#!/usr/bin/env python3
import subprocess
import os
import sys

os.chdir('C:\\ProyectoF\\glamstore')

# Disable pager completely
os.environ['GIT_PAGER'] = ''
os.environ['PAGER'] = ''
os.environ['LESS'] = ''

try:
    # Add the file
    print("Adding file...")
    subprocess.run(['git', 'add', 'core/migrations/0042_populate_lotes_and_vencimiento.py'], 
                   env=os.environ, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Commit
    print("Committing...")
    subprocess.run(['git', 'commit', '-m', 
                    'Fix migration 0042: Use lowercase column name fechavencimiento for PostgreSQL'],
                   env=os.environ, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Push
    print("Pushing...")
    subprocess.run(['git', 'push', 'origin', 'main'],
                   env=os.environ, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("✓ Done!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
