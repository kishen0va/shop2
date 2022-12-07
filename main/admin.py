from django.contrib import admin


from .models import Category, Brand, Clothes

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_description', 'category_slug', )
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name', 'category_description')

    def __str__(self) -> str:
        return super().__str__()


class BrandAdmin(admin.ModelAdmin):
    list_display =  ('id', 'brand_name', 'brand_description', 'brand_slug', ) 
    list_display_links = ('brand_name', 'brand_description', 'brand_slug')  
    list_filter = ('brand_name', 'brand_description', 'brand_slug', )
    

class ClothersAdmin(admin.ModelAdmin):
    list_display = ('id', 'clothes_name', 'clothes_description', 'clothes_slug', 'clothes_type', 'clothes_season', 'clothes_price', 'clothes_image', 'clothes_brand', 'clothes_category', )
    list_display_links = ('id',  )
    list_filter = ('id', 'clothes_name', )
   

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Clothes, ClothersAdmin)
