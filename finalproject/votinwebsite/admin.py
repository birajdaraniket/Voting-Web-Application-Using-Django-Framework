from django.contrib import admin

from votinwebsite.models import contact
from votinwebsite.models import login
from votinwebsite.models import partyregistration
from votinwebsite.models import signup
from votinwebsite.models import result
from votinwebsite.models import count
# Register your models here.
admin.site.register(partyregistration)

admin.site.register(contact)
admin.site.register(count)

admin.site.register(login)
admin.site.register(signup)
admin.site.register(result)





