from django.db import models
from mptt.models import MPTTModel


class Area(MPTTModel):
    name = models.CharField('模块名称', max_length=50, unique=True)
    parent_area = models.ForeignKey('self', verbose_name='父节点', null=True, blank=True, related_name='children')
    community = models.TextField('内容', null=True, blank=True)

    class Meta:
        verbose_name = '商贸版'
        verbose_name_plural = verbose_name

    class MPTTMeta:
        parent_attr = 'parent_area'

    def __str__(self):
        return self.name
