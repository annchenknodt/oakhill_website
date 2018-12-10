from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from django.utils.translation import ugettext_lazy as _, ugettext
from .models import Contact

class InputForm(forms.ModelForm):
	class Meta:
		model=Contact
		fields=['name_last','name_first','email','phone','address_st1','address_st2','address_city','address_state','address_zip']
		labels={
			"name_last": "Last Name",
			"name_first": "First Name",
			"address_st1": "Street Line 1",
			"address_st2": "Street Line 2",
			"address_city": "City",
			"address_state": "State",
			"address_zip": "Zip Code",
		}
	def __init__(self, *args, **kwargs):
		super(InputForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = ""
		self.helper.form_method = "POST"
		# self.helper.field_class = 'col-sm-4'
		# self.helper.form_class = 'form-horizontal'
		# self.helper.label_class = 'col-lg-2'
		# self.helper.field_class = 'col-lg-8'
		self.helper.form_show_labels = False		
		self.helper.form_class = 'form-horizontal'
		self.fields['name_last'].help_text = "Last"
		self.fields['name_first'].help_text = "First"
		self.fields['address_st1'].help_text = "Street Line 1"
		self.fields['address_st2'].help_text = "Street Line 2"
		self.fields['address_city'].help_text = "City"
		self.fields['address_state'].help_text = "State"
		self.fields['address_zip'].help_text = "Zip Code"
		self.helper.layout = layout.Layout(
			layout.Fieldset(
				_("Name"),
				layout.Div(
					layout.Div("name_last", css_class="col-xs-6"),
					layout.Div("name_first", css_class="col-xs-6"),
					css_class='row-fluid',
				),	
			),	
			layout.Fieldset(
				_("Email"),
				layout.Field("email"),
			),	
			layout.Fieldset(
				_("Phone Number"),
				layout.Field("phone"),
			),	
			layout.Fieldset(
				_("Property Address"),
				layout.Div("address_st1",placeholder="Street Line 1"),
				layout.Div("address_st2",placeholder="Street Line 2"),
				layout.Div(   	
					layout.Div("address_city", css_class="col-xs-4",placeholder="City"),
					layout.Div("address_state", css_class="col-xs-4",placeholder="State"),
					layout.Div("address_zip", css_class="col-xs-4",placeholder="Zip Code"),
					css_class='row-fluid',
				),
			),
			bootstrap.FormActions(
				layout.Submit('submit', _('Get an offer')),
			)
        )

# class InputForm(forms.ModelForm):
# 	class Meta:
# 		model=Contact
# 		fields=['name_last','name_first','email','phone',
# 		'address_st1','address_st2','address_city','address_state','address_zip'
# 			]
# 		# labels={
# 		# 	"name_last": "Last Name",
# 		# 	"name_first": "First Name",
# 		# 	"address_st": "Address street",
# 		# }

# 	def __init__(self, *args, **kwargs):
# 		super(InputForm, self).__init__(*args, **kwargs)

# 		self.helper = FormHelper()
# 		self.helper.form_action = ""
# 		self.helper.form_method = "POST"
# 		self.helper.field_class = 'col-sm-4'
# 		self.helper.form_show_labels = False		
# 		self.helper.form_class = 'form-horizontal'
# 		self.fields['address_st1'].help_text = "Street Line 1"
# 		self.fields['address_st2'].help_text = "Street Line 2"
# 		self.fields['address_city'].help_text = "City"
# 		self.fields['address_state'].help_text = "State"
# 		self.fields['address_zip'].help_text = "Zip Code"
# 		# self.fields['my_field'].label = False

# 		self.helper.layout = layout.Layout(
# 		    layout.Fieldset(
# 		    	_("Name"),
# 		    	layout.Div(
# 		    		layout.Div("name_last", css_class="col-xs-6"),
# 		    		layout.Div("name_first", css_class="col-xs-6"),
# 			    	css_class='row-fluid',
# 			    ),	
# 		    ),	
# 		    layout.Fieldset(
# 		    	_("Email"),
# 		    	layout.Field("email"),
# 		    ),	
# 		    layout.Fieldset(
# 		    	_("Phone Number"),
# 		    	layout.Field("phone"),
# 		    ),	
# 		    layout.Fieldset(
# 		    	_("Property Address"),
# 		    	layout.Field("address_st1"),
# 		    	layout.Field("address_st2"),
# 		    	layout.Div(   	
# 			    	layout.Div("address_city", css_class="col-xs-4"),
# 			    	layout.Div("address_state", css_class="col-xs-4"),
# 			    	layout.Div("address_zip", css_class="col-xs-4"),
# 			    	css_class='row-fluid',
# 				),
# 		    ),
#             bootstrap.FormActions(
# 				layout.Submit('submit', _('Get an offer')),
#             )
#         )

