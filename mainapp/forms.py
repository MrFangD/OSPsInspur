"""
    @Time: 2018/4/17 17:01
    @Author:fangDD
"""
from django import forms


class fourm_content(forms.Form):
    plate = forms.CharField(max_length=60)
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)