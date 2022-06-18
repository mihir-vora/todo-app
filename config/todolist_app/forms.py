from django import forms

from .models import TodoTask


class TODOLISTFORM(forms.ModelForm):
	class Meta:
		model = TodoTask
		fields = ['todoName', 'content']

	def __init__(self, *args, **kwargs):
		super(TODOLISTFORM, self).__init__(*args, **kwargs)
		self.fields['todoName'].widget.attrs.update({
				'class' : 'form-group form-control font-weight-bold',
				'autocomplete' : 'off'
			})
		self.fields['content'].widget.attrs.update({
				'class' : 'form-group form-control font-weight-bold',
				'autocomplete' : 'off'

			})

class EDITLISTFORM(forms.ModelForm):
	class Meta:
		model = TodoTask
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(EDITLISTFORM, self).__init__(*args, **kwargs)
		self.fields['todoName'].widget.attrs.update({
				'class' : 'form-group form-control font-weight-bold',
				'autocomplete' : 'off'
			})
		self.fields['content'].widget.attrs.update({
				'class' : 'form-group form-control font-weight-bold',
				'autocomplete' : 'off'

			})


