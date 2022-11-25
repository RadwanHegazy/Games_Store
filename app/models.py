from django.db import models

# Create your models here.


class Category (models.Model) :
    name = models.CharField(max_length=100)

    def __str__(self) :
        return f'{self.name}'


class Game (models.Model) :
    category = models.ForeignKey(Category,related_name='game_category',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    main_image = models.TextField(max_length=1000)
    download_link = models.TextField(max_length=10000)
    os = models.CharField(max_length=100)
    all_photos = models.TextField(max_length=1000)

    def __str__(self) :
        return f'{self.name}'

if __name__ == '__main__' :
    Game()