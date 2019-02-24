from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from django.utils.translation import ugettext_lazy as _, ugettext
from .models import Contact, Unsubscribe

class InputForm(forms.ModelForm):
	class Meta:
		model=Contact
		fields=['name_last','name_first','email','phone','address_st1','address_st2','address_city','address_state','address_zip','comments']
		# labels={
		# 	"name_last": "Last Name",
		# 	"name_first": "First Name",
		# 	"address_st1": "Street L 1",
		# 	"address_st2": "Street Line 2",
		# 	"address_city": "City",
		# 	"address_state": "State",
		# 	"address_zip": "Zip Code",
		# }
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_action = ""
		self.helper.form_method = "POST"
		self.helper.form_show_labels = False		
		self.helper.form_class = 'form-horizontal'
		self.fields['name_last'].help_text = "Last Name"
		self.fields['name_first'].help_text = "First Name"
		self.fields['email'].help_text = "Email Address"
		self.fields['phone'].help_text = "Phone Number"
		self.fields['address_st1'].help_text = "Street Line 1"
		self.fields['address_st2'].help_text = "Street Line 2"
		self.fields['address_city'].help_text = "City"
		self.fields['address_state'].help_text = "State"
		self.fields['address_zip'].help_text = "Zip Code"
		self.helper.layout = layout.Layout(
			layout.Fieldset(
				_("Contact Info"),
				layout.Row(
					layout.Column("name_last",css_class='form-group col-6 mb-0'),
					layout.Column("name_first",css_class='form-group col-6 mb-0'),
					css_class='form-row'
				),
				layout.Row(
					layout.Column("email",css_class='form-group col-6 mb-0'),
					layout.Column("phone",css_class='form-group col-6 mb-0'),
					css_class='form-row'
				),
			),
			layout.Fieldset(
				_("Property Address"),
				layout.Row(
					layout.Column("address_st1",css_class='form-group col-12 mb-0'),
					css_class='form-row'
				),
				layout.Row(
					layout.Column("address_st2",css_class='form-group col-12 mb-0'),
					css_class='form-row'
				),			
				layout.Row(
					layout.Column("address_city",css_class='form-group col-6 mb-0'),
					layout.Column("address_state",css_class='form-group col-4 mb-0'),
					layout.Column("address_zip",css_class='form-group col-2 mb-0'),
					css_class='form-row'
				),		
			),
			layout.Fieldset(
				_("Additional Comments"),
				layout.Row(
					layout.Column("comments",css_class='form-group col-12 mb-0'),
					css_class='form-row'
				),		
			),
			layout.ButtonHolder(
				layout.Submit('submit', _('Get an offer')),
			)				
		)

class UnsubForm(forms.ModelForm):
	class Meta:
		model=Unsubscribe
		fields=['address_st1','address_st2','address_city','address_state','address_zip']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_action = ""
		self.helper.form_method = "POST"
		self.helper.form_show_labels = False		
		self.helper.form_class = 'form-horizontal'
		self.fields['address_st1'].help_text = "Street Line 1"
		self.fields['address_st2'].help_text = "Street Line 2"
		self.fields['address_city'].help_text = "City"
		self.fields['address_state'].help_text = "State"
		self.fields['address_zip'].help_text = "Zip Code"
		self.helper.layout = layout.Layout(
			layout.Fieldset(
				_("Mailing Address"),
				layout.Row(
					layout.Column("address_st1",css_class='form-group col-12 mb-0'),
					css_class='form-row'
				),
				layout.Row(
					layout.Column("address_st2",css_class='form-group col-12 mb-0'),
					css_class='form-row'
				),			
				layout.Row(
					layout.Column("address_city",css_class='form-group col-6 mb-0'),
					layout.Column("address_state",css_class='form-group col-4 mb-0'),
					layout.Column("address_zip",css_class='form-group col-2 mb-0'),
					css_class='form-row'
				),		
			),
			layout.ButtonHolder(
				layout.Submit('submit', _('Unsubscribe')),
				css_class='col-12'
			)				
		)
           