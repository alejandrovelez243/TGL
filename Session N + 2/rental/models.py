from django.db import models
from utils.models import BaseModel
from film.models import Film
from customer.models import Customer

class Inventory(BaseModel):
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

# Create your models here.
class Rental(BaseModel):
    inventor_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    return_date = models.DateField()

    def __str__(self):
        return str(self.id)
