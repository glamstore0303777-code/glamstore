from django.contrib import admin
from core.models.categoria import Categoria, Subcategoria
from core.models.productos import Producto
from core.models.imagenes import ImagenCategoria, ImagenSubcategoria, ImagenProducto
from core.models.imagenes import ImagenCategoria, ImagenSubcategoria, ImagenProducto

admin.site.register(ImagenCategoria)
admin.site.register(ImagenSubcategoria)
admin.site.register(ImagenProducto)
# Categorías y subcategorías
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('idCategoria', 'nombreCategoria')
    search_fields = ('nombreCategoria',)

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('idSubcategoria', 'nombreSubcategoria', 'categoria')
    search_fields = ('nombreSubcategoria',)
    list_filter = ('categoria',)

# Productos
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('idProducto', 'nombreProducto', 'precio', 'stock', 'idCategoria', 'idSubcategoria')
    search_fields = ('nombreProducto',)
    list_filter = ('idCategoria', 'idSubcategoria')

# Imágenes
@admin.register(ImagenCategoria)
class ImagenCategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'imagen')

@admin.register(ImagenSubcategoria)
class ImagenSubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('subcategoria', 'imagen')

@admin.register(ImagenProducto)
class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'imagen')
    