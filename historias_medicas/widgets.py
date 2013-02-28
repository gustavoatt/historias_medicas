from django.forms import widgets

class AppendedInput(widgets.TextInput):
	_HTML_FORMAT = ('<div class="input-append">'
	                	'{}'
	                	'<span class="add-on">{}</span>'
	                '</div>'	
	                )

	def __init__(self, append_text, *args, **kwargs):
		self.append_text = append_text
		super(AppendedInput, self).__init__(*args, **kwargs)

	def render(self, name, value, attrs=None):
		parent_html = super(AppendedInput, self).render(name,value, attrs)
		return self._HTML_FORMAT.format(parent_html, self.append_text)