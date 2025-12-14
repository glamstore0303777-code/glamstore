"""
Migration to fix column case sensitivity in detallepedido table.
PostgreSQL stores quoted identifiers with their original case.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_drop_subcategoria_fk'),
    ]

    operations = [
        migrations.RunSQL(
            # Rename camelCase columns to lowercase
            sql="""
                DO $$
                BEGIN
                    -- Rename precioUnitario to preciounitario if exists
                    IF EXISTS (
                        SELECT 1 FROM information_schema.columns 
                        WHERE table_name = 'detallepedido' AND column_name = 'precioUnitario'
                    ) THEN
                        ALTER TABLE detallepedido RENAME COLUMN "precioUnitario" TO preciounitario;
                    END IF;
                    
                    -- Rename idDetallePedido if exists
                    IF EXISTS (
                        SELECT 1 FROM information_schema.columns 
                        WHERE table_name = 'detallepedido' AND column_name = 'idDetallePedido'
                    ) THEN
                        ALTER TABLE detallepedido RENAME COLUMN "idDetallePedido" TO iddetallepedido;
                    END IF;
                    
                    -- Rename idPedido if exists
                    IF EXISTS (
                        SELECT 1 FROM information_schema.columns 
                        WHERE table_name = 'detallepedido' AND column_name = 'idPedido'
                    ) THEN
                        ALTER TABLE detallepedido RENAME COLUMN "idPedido" TO idpedido;
                    END IF;
                    
                    -- Rename idProducto if exists
                    IF EXISTS (
                        SELECT 1 FROM information_schema.columns 
                        WHERE table_name = 'detallepedido' AND column_name = 'idProducto'
                    ) THEN
                        ALTER TABLE detallepedido RENAME COLUMN "idProducto" TO idproducto;
                    END IF;
                END $$;
            """,
            reverse_sql="SELECT 1;",  # No reverse needed
        ),
    ]
