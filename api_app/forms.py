from django.forms import ModelForm, fields
from api_app.models import IrisModel

class IrisForm(ModelForm):
    class Meta:
        model = IrisModel
        fields = ['sepal_length','sepal_width','petal_length','petal_width','iris_class']