from import_export import resources
from .models import FoodSales
 
class FoodResource(resources.ModelResource):
    class Meta:
        model = FoodSales