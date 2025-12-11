from django.db import models


class ConfiguracionGlobal(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='id')
    margen_ganancia = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=10,
        db_column='margen_ganancia',
        help_text="Porcentaje de ganancia global para todos los productos (ej: 10 para 10%)"
    )
    fecha_actualizacion = models.DateTimeField(auto_now=True, db_column='fecha_actualizacion')
    
    class Meta:
        db_table = 'configuracion_global'
        managed = False
        app_label = 'core'
        verbose_name = 'Configuración Global'
        verbose_name_plural = 'Configuración Global'
    
    def __str__(self):
        return f"Margen de Ganancia: {self.margen_ganancia}%"
    
    @classmethod
    def get_margen_ganancia(cls):
        """Obtiene el margen de ganancia global, crea uno si no existe"""
        config, created = cls.objects.get_or_create(pk=1)
        return float(config.margen_ganancia)
