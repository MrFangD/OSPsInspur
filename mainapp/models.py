from django.db import models
from mptt.models import MPTTModel
from ckeditor.fields import RichTextField


class Area(MPTTModel):
    name = models.CharField('模块名称', max_length=50, unique=True)
    parent_area = models.ForeignKey('self', verbose_name='父节点', null=True, blank=True, related_name='children')
    community = RichTextField('内容', null=True, blank=True)

    class Meta:
        verbose_name = '商贸版'
        verbose_name_plural = verbose_name

    class MPTTMeta:
        parent_attr = 'parent_area'

    def __str__(self):
        return self.name


class fourm(models.Model):
    fourm_userid = models.IntegerField('用户ID')
    fourm_plate = models.CharField('论坛板块', max_length=60)
    fourm_title = models.CharField('主题题目', max_length=200)
    fourm_content = RichTextField('主题内容')
    fourm_time = models.DateTimeField('发布时间', auto_now_add=True)
    fourm_count = models.IntegerField('浏览次数', null=True, blank=True)
    fourm_answerid = models.IntegerField('回复人ID',  null=True, blank=True)
    fourm_answercontent = RichTextField('回复内容',  null=True, blank=True)

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.fourm_title


class answer(models.Model):
    fourm_id = models.IntegerField('主题ID')
    answer_user = models.CharField('回复人', max_length=50)
    answer_content = RichTextField('回复内容')

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.answer_user