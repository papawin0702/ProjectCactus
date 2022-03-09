from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = "หมวดหมู่"
        verbose_name_plural = "หมวดหมู่"
    name = models.CharField(max_length=255, verbose_name="ชื่อ")
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    detail = models.TextField(verbose_name="รายละเอียด",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        verbose_name = "หมวดหมู่ย่อย"
        verbose_name_plural = "หมวดหมู่ย่อย"
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="ชื่อ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category.name) + ":" + self.name

    @property
    def fullname(self):
        return self.category.name + str(self.category.id)


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    price = models.FloatField(null=True, blank=True, )
    detail = models.TextField()
    category = models.ManyToManyField(SubCategory)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name