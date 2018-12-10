from django.views.static import serve as staticserve
from . import settings
# import webapps.settings as settings
def serve(request, what):
	print('In staticserve')
	response = staticserve(request, what, document_root=settings.STATIC_ROOT)
	response['Cache-Control'] = 'no-cache'
	return response
