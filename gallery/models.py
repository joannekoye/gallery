from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self, id):
        self.objects.filter(id=id).delete()

    def update_location(self, id, new_location):
        self.objects.filter(id=id).update(location= new_location)

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()

    def delete_category(self, id):
        self.objects.filter(id = id).delete()
    
    def update_category(self, id, new_category):
        self.objects.filter(id = id).update(category = new_category)

class Image(models.Model):
    img_path = models.ImageField(upload_to= 'images/')
    img_name = models.CharField(max_length=30)
    img_desc = models.TextField(blank=True)
    img_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    img_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.img_name
    
    def save_image(self):
        self.save()

    def delete_image(self, id):
        self.objects.filter(id = id).delete()
    
    def update_image(self, id, new_path):
        self.objects.filter(id = id).update(img_path = new_path)

    def get_image_by_id(self, id):
        img = self.objects.get(pk = id)
        return img
    
    @classmethod
    def filter_by_location(cls):
        images = cls.objects.order_by('img_location')
        return images
    
    @classmethod
    def search_image(cls, search_category):
        images = cls.objects.filter(img_category__category__icontains = search_category)
        return images

    class Meta:
        ordering = ['img_name']
