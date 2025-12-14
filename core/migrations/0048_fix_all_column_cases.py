"""
Migration to fix ALL column case sensitivity issues across tables.
Uses pg_attribute to check actual column names (case-sensitive).
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_fix_detallepedido_columns'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                DO $$
                DECLARE
                    col_record RECORD;
                BEGIN
                    -- Fix detallepedido table columns
                    FOR col_record IN 
                        SELECT attname 
                        FROM pg_attribute 
                        WHERE attrelid = 'detallepedido'::regclass 
                        AND attnum > 0 
                        AND NOT attisdropped
                    LOOP
                        -- Rename precioUnitario
                        IF col_record.attname = 'precioUnitario' THEN
                            EXECUTE 'ALTER TABLE detallepedido RENAME COLUMN "precioUnitario" TO preciounitario';
                        END IF;
                        -- Rename idDetallePedido
                        IF col_record.attname = 'idDetallePedido' THEN
                            EXECUTE 'ALTER TABLE detallepedido RENAME COLUMN "idDetallePedido" TO iddetallepedido';
                        END IF;
                    END LOOP;
                    
                    -- Fix pedidos table columns
                    FOR col_record IN 
                        SELECT attname 
                        FROM pg_attribute 
                        WHERE attrelid = 'pedidos'::regclass 
                        AND attnum > 0 
                        AND NOT attisdropped
                    LOOP
                        IF col_record.attname = 'idPedido' THEN
                            EXECUTE 'ALTER TABLE pedidos RENAME COLUMN "idPedido" TO idpedido';
                        END IF;
                        IF col_record.attname = 'fechaCreacion' THEN
                            EXECUTE 'ALTER TABLE pedidos RENAME COLUMN "fechaCreacion" TO fechacreacion';
                        END IF;
                        IF col_record.attname = 'idCliente' THEN
                            EXECUTE 'ALTER TABLE pedidos RENAME COLUMN "idCliente" TO idcliente';
                        END IF;
                        IF col_record.attname = 'idRepartidor' THEN
                            EXECUTE 'ALTER TABLE pedidos RENAME COLUMN "idRepartidor" TO idrepartidor';
                        END IF;
                    END LOOP;
                    
                    -- Fix clientes table columns
                    FOR col_record IN 
                        SELECT attname 
                        FROM pg_attribute 
                        WHERE attrelid = 'clientes'::regclass 
                        AND attnum > 0 
                        AND NOT attisdropped
                    LOOP
                        IF col_record.attname = 'idCliente' THEN
                            EXECUTE 'ALTER TABLE clientes RENAME COLUMN "idCliente" TO idcliente';
                        END IF;
                    END LOOP;
                    
                    -- Fix repartidores table columns  
                    FOR col_record IN 
                        SELECT attname 
                        FROM pg_attribute 
                        WHERE attrelid = 'repartidores'::regclass 
                        AND attnum > 0 
                        AND NOT attisdropped
                    LOOP
                        IF col_record.attname = 'idRepartidor' THEN
                            EXECUTE 'ALTER TABLE repartidores RENAME COLUMN "idRepartidor" TO idrepartidor';
                        END IF;
                    END LOOP;
                    
                END $$;
            """,
            reverse_sql="SELECT 1;",
        ),
    ]
