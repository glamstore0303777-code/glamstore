# Migration to rename database columns from camelCase to lowercase
# This is necessary because PostgreSQL stores unquoted identifiers in lowercase

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_fix_column_case_sensitivity'),
    ]

    operations = [
        # Rename Producto columns
        migrations.RunSQL(
            sql="""
            ALTER TABLE productos 
            RENAME COLUMN "idProducto" TO idproducto;
            """,
            reverse_sql="""
            ALTER TABLE productos 
            RENAME COLUMN idproducto TO "idProducto";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE productos 
            RENAME COLUMN "nombreProducto" TO nombreproducto;
            """,
            reverse_sql="""
            ALTER TABLE productos 
            RENAME COLUMN nombreproducto TO "nombreProducto";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE productos 
            RENAME COLUMN "cantidadDisponible" TO cantidaddisponible;
            """,
            reverse_sql="""
            ALTER TABLE productos 
            RENAME COLUMN cantidaddisponible TO "cantidadDisponible";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE productos 
            RENAME COLUMN "fechaIngreso" TO fechaingreso;
            """,
            reverse_sql="""
            ALTER TABLE productos 
            RENAME COLUMN fechaingreso TO "fechaIngreso";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE productos 
            RENAME COLUMN "fechaVencimiento" TO fechavencimiento;
            """,
            reverse_sql="""
            ALTER TABLE productos 
            RENAME COLUMN fechavencimiento TO "fechaVencimiento";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE productos 
            RENAME COLUMN "idCategoria" TO idcategoria;
            """,
            reverse_sql="""
            ALTER TABLE productos 
            RENAME COLUMN idcategoria TO "idCategoria";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE productos 
            RENAME COLUMN "idSubcategoria" TO idsubcategoria;
            """,
            reverse_sql="""
            ALTER TABLE productos 
            RENAME COLUMN idsubcategoria TO "idSubcategoria";
            """,
            state_operations=[],
        ),
        
        # Rename Pedido columns
        migrations.RunSQL(
            sql="""
            ALTER TABLE pedidos 
            RENAME COLUMN "idPedido" TO idpedido;
            """,
            reverse_sql="""
            ALTER TABLE pedidos 
            RENAME COLUMN idpedido TO "idPedido";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE pedidos 
            RENAME COLUMN "fechaCreacion" TO fechacreacion;
            """,
            reverse_sql="""
            ALTER TABLE pedidos 
            RENAME COLUMN fechacreacion TO "fechaCreacion";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE pedidos 
            RENAME COLUMN "idCliente" TO idcliente;
            """,
            reverse_sql="""
            ALTER TABLE pedidos 
            RENAME COLUMN idcliente TO "idCliente";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE pedidos 
            RENAME COLUMN "idRepartidor" TO idrepartidor;
            """,
            reverse_sql="""
            ALTER TABLE pedidos 
            RENAME COLUMN idrepartidor TO "idRepartidor";
            """,
            state_operations=[],
        ),
        
        # Rename DetallePedido columns
        migrations.RunSQL(
            sql="""
            ALTER TABLE detallepedido 
            RENAME COLUMN "idDetallePedido" TO iddetallepedido;
            """,
            reverse_sql="""
            ALTER TABLE detallepedido 
            RENAME COLUMN iddetallepedido TO "idDetallePedido";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE detallepedido 
            RENAME COLUMN "idPedido" TO idpedido;
            """,
            reverse_sql="""
            ALTER TABLE detallepedido 
            RENAME COLUMN idpedido TO "idPedido";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE detallepedido 
            RENAME COLUMN "idProducto" TO idproducto;
            """,
            reverse_sql="""
            ALTER TABLE detallepedido 
            RENAME COLUMN idproducto TO "idProducto";
            """,
            state_operations=[],
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE detallepedido 
            RENAME COLUMN "precioUnitario" TO preciounitario;
            """,
            reverse_sql="""
            ALTER TABLE detallepedido 
            RENAME COLUMN preciounitario TO "precioUnitario";
            """,
            state_operations=[],
        ),
        
        # Rename Repartidor columns
        migrations.RunSQL(
            sql="""
            ALTER TABLE repartidores 
            RENAME COLUMN "idRepartidor" TO idrepartidor;
            """,
            reverse_sql="""
            ALTER TABLE repartidores 
            RENAME COLUMN idrepartidor TO "idRepartidor";
            """,
            state_operations=[],
        ),
    ]
