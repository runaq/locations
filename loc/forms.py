# fairytale/characters/forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Fieldset, ButtonHolder
from crispy_forms.bootstrap import FormActions

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('first_name', 'last_name', 'address', 'lat', 'lot', 'phone_number', )
 
        def __init__(self, *args, **kwargs):
            # call original initializator
            super(PostForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
            self.helper = FormHelper()
            self.helper.layout = Layout( Fieldset('first_name', 'last_name'), 'address', Fieldset('lat', 'lot'), 'phone_number' ,)
        # form tag attributes
            self.helper.form_class = 'form-horizontal'
            self.helper.form_method = 'post'
            self.helper.form_action = reverse('post_list')

        # twitter bootstrap styles
            self.helper.help_text_inline = True
            self.helper.html5_required = True
            self.helper.label_class = 'col-sm-2 control-label'
            self.helper.field_class = 'col-sm-6'
            

        # form buttons
   

        first_name=forms.CharField(max_length=15, label='Имя')
        last_name=forms.CharField(max_length=25,  label='Фамилия')
        address=forms.CharField(max_length=200, label='Адрес')
        lat=forms.DecimalField(max_digits=10, decimal_places=8, label='Широта')
        lot=forms.DecimalField(max_digits=11, decimal_places=8, label='Долгота')
        phone_number= forms.CharField(label='Телефон', widget= forms.TextInput (attrs={'placeholder':'Enter your first name'}))  