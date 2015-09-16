from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=25)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    fruit_eaten = models.ManyToManyField(Fruit, through='FruitEaten')

    def __str__(self):
        return self.text

    def total_calories(self):
        sum = 0
        for fruit, eaten in zip(self.fruit_eaten.all(), self.fruiteaten_set.all()):
            sum += eaten.qty * fruit.calories
        return sum

    def meal_size(self):
        cal = self.total_calories()
        if cal > 1000:
            return 'large'
        elif cal > 500:
            return 'medium'
        else:
            return 'small'

class FruitEaten(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    qty = models.IntegerField('quantity', default=0)

    class Meta:
        unique_together = ('post', 'fruit')

    def __str__(self):
        return str(self.qty) + ' ' + self.fruit.name