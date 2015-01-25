from django.contrib import admin

from vote.models import Response, Constituency, Party

admin.site.register(Response)
admin.site.register(Constituency)
admin.site.register(Party)
