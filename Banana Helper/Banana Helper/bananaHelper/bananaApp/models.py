from django.db import models

class offer(models.Model):
    name = models.CharField(max_length = 70)
    price = models.CharField(max_length = 30)
    offer_id = models.IntegerField(unique=True)
    user = models.EmailField(max_length = 50, unique=True)
    description = models.CharField(max_length = 1000, default= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum, purus ac mattis molestie, quam purus condimentum elit, in vestibulum mi quam ac lectus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla posuere, dolor id vehicula fermentum, erat augue vestibulum purus, non lobortis ex turpis bibendum purus. Duis semper, lorem in efficitur euismod, quam ligula placerat ligula, eu rhoncus ligula nisl ut lorem. Aliquam vitae risus hendrerit, vestibulum lorem sit amet, semper nibh. Etiam tellus velit, sollicitudin eget sagittis et, lobortis ut urna. Etiam dui lacus, venenatis in faucibus ac, posuere sit amet orci. Proin sodales turpis nec felis sollicitudin volutpat. Nullam at libero id arcu porttitor mollis vel ac lacus. Curabitur ac vehicula sapien. Duis id augue tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras pulvinar nec sem in varius. Vestibulum efficitur ut arcu malesuada pulvinar. Mauris porta magna id bibendum egestas. Sed luctus vitae risus feugiat euismod.")

    def __str__(self):
        return self.name + ' ' + self.price
# Create your models here.
