from django.contrib import admin
from .models import IntelCpu, amdCpu, nvidia, ram, radeon, hdd, ssd, intelMB, amdMB

admin.site.register(IntelCpu)
admin.site.register(amdCpu)
admin.site.register(nvidia)
admin.site.register(ram)
admin.site.register(radeon)
admin.site.register(hdd)
admin.site.register(ssd)
admin.site.register(intelMB)
admin.site.register(amdMB)
# Register your models here.
