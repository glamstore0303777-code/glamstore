# Generated migration to fix duplicate column issue

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_producto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
    ]
