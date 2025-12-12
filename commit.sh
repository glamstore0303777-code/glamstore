#!/bin/bash
export GIT_PAGER=cat
git add core/migrations/0042_populate_lotes_and_vencimiento.py
git commit -m "Fix migration 0042: Use lowercase column name fechavencimiento for PostgreSQL"
git push origin main
