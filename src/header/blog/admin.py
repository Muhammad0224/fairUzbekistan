from django.contrib import admin
from .models import Message, School, UserProfile, Days
# Register your models here.




class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at', 'status')
    list_display_links = ('id', 'name')
    search_fields = ('content', )
    list_filter = ('status', )

    # bitta news ochilganda ko'rinadigan maydonlar
    fields = ('name', 'email', 'content', 'status', 'created_at', 'updated_at')
    # faqat ko'rishga ruhsat berilgan qatorlar
    readonly_fields = ('updated_at',  'created_at')

    #yuqori qismga ham save va delete qilish buttonlari
    save_on_top = True


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contract_num', 'created_at', 'contract_finish', 'status', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'contract_num')
    list_filter = ('status', )

    # bitta news ochilganda ko'rinadigan maydonlar
    fields = ('name', 'address', 'phone', 'contract_num', 'contract_finish', 'status', 'created_at', 'updated_at')
    # faqat ko'rishga ruhsat berilgan qatorlar
    readonly_fields = ('created_at', 'updated_at')

    save_on_top = True


admin.site.register(Message, MessageAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(UserProfile)
admin.site.register(Days)