from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django import forms

from accounts.models import OtpModel, UserModel
from exam.models import ExamModel, QuestionModel, ChoiceModel, KarNameModel, KarNameDBModel, MyExamClass
from litner.models import LitnerModel, LitnerQuestionModel, LitnerKarNameModel, MyLitnerclass, LitnerKarNameDBModel,LitnerAnswer,UserQuestionAnswerCount
from markethub.models import MarketHubModel, MarketHubQuestionModel, MarketHubKarNameModel, MarketHubKarNameDBModel, \
    Myclass


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'study_field', 'username', 'phone_number', 'melli_code', 'is_staff', 'date_joined')
    search_fields = ('full_name','username', 'phone_number', 'melli_code', 'study_field')
    list_filter = ('is_active', 'study_field')

    fieldsets = (
        ('اطلاعات شخصی', {'fields': ('full_name','study_field','username','melli_code','phone_number')}),
        #('دسترسی‌ها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('گزارش تاریخ', {'fields': ('last_login', 'date_joined')}),
    )

    
@admin.register(LitnerModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(LitnerAnswer)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(LitnerQuestionModel)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(UserQuestionAnswerCount)
class UserQuestionAnswerCountAdmin(admin.ModelAdmin):
    pass


@admin.register(MarketHubModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(MarketHubQuestionModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(LitnerKarNameModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ExamModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(KarNameModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(KarNameDBModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ChoiceModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(OtpModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "otpCode",)
    search_fields = ("phone_number", "otpCode",)
    list_filter = ("phone_number", "otpCode",)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = "action_time"
    list_display = ("action_time", "user", "content_type", "object_repr", "action_flag")
    list_filter = ("action_flag", "content_type")
    search_fields = ("user__username",)


@admin.register(MarketHubKarNameModel)
class karnameAdmin(admin.ModelAdmin):
    pass


# class UserAdmin(admin.ModelAdmin):


@admin.register(MarketHubKarNameDBModel)
class MarketHubKarNameDBModelAdmin(admin.ModelAdmin):
    pass


class MyLitnerclassAdminForm(forms.ModelForm):
    class Meta:
        model = MyLitnerclass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the queryset for the 'author' field to show only staff users
        self.fields['author'].queryset = UserModel.objects.filter(is_staff=True)

# class UserAdmin(admin.ModelAdmin):
@admin.register(MyLitnerclass)
class MyLitnerclassAdmin(admin.ModelAdmin):
    form = MyLitnerclassAdminForm


class MyExamClassAdminForm(forms.ModelForm):
    class Meta:
        model = MyExamClass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the queryset for the 'author' field to show only staff users
        self.fields['author'].queryset = UserModel.objects.filter(is_staff=True)


@admin.register(MyExamClass)
class MyExamClassAdmin(admin.ModelAdmin):
    form = MyExamClassAdminForm


@admin.register(Myclass)
class MyclassAdmin(admin.ModelAdmin):
    pass


@admin.register(LitnerKarNameDBModel)
class LitnerKarNameDBModelAdmin(admin.ModelAdmin):
    pass
