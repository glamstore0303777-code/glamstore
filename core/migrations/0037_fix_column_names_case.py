# Migration to fix column name case sensitivity issues

from django.db import migrations

def fix_column_names(apps, schema_editor):
    """Rename columns from camelCase to lowercase to match Django models"""
    
    # List of column renames: (table, old_name, new_name)
    renames = [
        ('productos', 'idProducto', 'idproducto'),
        ('productos', 'nombreProducto', 'nombreproducto'),
        ('productos', 'cantidadDisponible', 'cantidaddisponible'),
        ('productos', 'fechaIngreso', 'fechaingreso'),
        ('productos', 'fechaVencimiento', 'fechavencimiento'),
        ('productos', 'idCategoria', 'idcategoria'),
        ('productos', 'idSubcategoria', 'idsubcategoria'),
        # Usuarios table columns
        ('usuarios', 'idUsuario', 'idusuario'),
        ('usuarios', 'id_rol', 'id_rol'),
        ('usuarios', 'idcliente', 'idcliente'),
        ('usuarios', 'fechacreacion', 'fechacreacion'),
        ('usuarios', 'reset_token', 'reset_token'),
        ('usuarios', 'reset_token_expires', 'reset_token_expires'),
        ('usuarios', 'ultimoacceso', 'ultimoacceso'),
    ]
    
    for table, old_col, new_col in renames:
        if old_col != new_col:  # Only rename if different
            try:
                schema_editor.execute(f"""
                    ALTER TABLE {table} RENAME COLUMN "{old_col}" TO "{new_col}";
                """)
            except Exception as e:
                # Column might already be renamed or not exist, continue
                print(f"Skipping rename {table}.{old_col}: {str(e)}")

def reverse_fix(apps, schema_editor):
    """Reverse the column renames (not recommended in production)"""
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_create_tables_from_sql'),
    ]

    operations = [
        migrations.RunPython(fix_column_names, reverse_fix),
    ]
