#!/usr/bin/env python3
import subprocess
import os

os.chdir('C:\\ProyectoF\\glamstore')

# Disable pager
os.environ['GIT_PAGER'] = 'cat'

try:
    # Add the file
    subprocess.run(['git', 'add', 'core/migrations/0042_populate_lotes_and_vencimiento.py'], 
                   check=True, capture_output=True, text=True)
    print("✓ File added")
    
    # Commit
    result = subprocess.run(['git', 'commit', '-m', 
                            'Fix migration 0042: Use lowercase column name fechavencimiento for PostgreSQL'],
                           check=True, capture_output=True, text=True)
    print("✓ Commit created")
    print(result.stdout)
    
    # Push
    result = subprocess.run(['git', 'push', 'origin', 'main'],
                           check=True, capture_output=True, text=True)
    print("✓ Pushed to GitHub")
    print(result.stdout)
    
except subprocess.CalledProcessError as e:
    print(f"✗ Error: {e}")
    print(f"stdout: {e.stdout}")
    print(f"stderr: {e.stderr}")
