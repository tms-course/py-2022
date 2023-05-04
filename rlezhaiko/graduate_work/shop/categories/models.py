from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=128, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=128, blank=True, null=True, unique=True)


    def __str__(self) -> str:
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        
        return ' / '.join(full_path[::-1])


    class MPTTMeta:
        order_insertion_by = ['name']




# class Category(models.Model):
#     name = models.CharField(max_length=128, blank=False)
#     parent_id = models.IntegerField(null=True, blank=True)
#     # slug = models.SlugField(max_length=128, unique=True)
#     slug = models.SlugField(max_length=128, blank=True, null=True, unique=True)

#     class Meta:
#         indexes = [
#             models.Index(fields=['name']),
#             models.Index(fields=['slug']),
#         ]