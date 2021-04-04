from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.forms.models import ModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from data.forms import TaskForm
from data.models import Task, AuxilioEmergencial, CotasParlamentares
from data.tasks import update_dataset


class AddOnlyAdmin:
    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True


class TaskAdmin(admin.ModelAdmin):
    list_display = ['dataset', 'provider_date', 'source_date', 'status',
                    'approved', 'is_active', 'creation_date',
                    'last_modification_date']

    list_filter = ['dataset', 'status', 'provider_date', 'source_date',
                   'is_active']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = TaskForm
            self.readonly_fields = []
        return super(TaskAdmin, self).get_form(request, obj, **kwargs)

    def add_view(self, request, form_url='', extra_context=None):
        self.model = Task
        if request.method == 'POST':
            opts = self.model._meta
            if self.has_view_or_change_permission(request):
                post_url = reverse('admin:%s_%s_changelist' %
                                   (opts.app_label, opts.model_name),
                                   current_app=self.admin_site.name)
                preserved_filters = self.get_preserved_filters(request)
                post_url = add_preserved_filters(
                    {'preserved_filters': preserved_filters, 'opts': opts},
                    post_url)

                values = self.get_changeform_initial_data(request)

                form = TaskForm(request.POST, request.FILES)
                form.fields['dataset'].initial = values['dataset']
                form.fields['source_format'].initial = values['source_format']

                if form.is_valid():
                    self._update_dataset(form)
                    self.message_user(request, "Dataset success updated",
                                      messages.SUCCESS)
                else:
                    print(form.errors)
                    self.message_user(request, "Error",
                                      messages.ERROR)
            else:
                post_url = reverse('admin:index',
                                   current_app=self.admin_site.name)
            return HttpResponseRedirect(post_url)
        return self.changeform_view(request, None, form_url, extra_context)

    def _update_dataset(self, form):
        task = form.save()
        update_dataset.apply_async([task.id])


class AuxilioEmergencialAdmin(AddOnlyAdmin, TaskAdmin):
    list_display = ['ano_disponibilizacao',
                    'mes_disponibilizacao', 'uf', 'nome_municipio',
                    'nis_beneficiario', 'cpf_beneficiario',
                    'nome_beneficiario', 'nis_responsavel',
                    'cpf_responsavel', 'nome_responsavel',
                    'enquadramento', 'parcela',
                    'observacao', 'valor_beneficio']

    search_fields = ['nis_beneficiario', 'nome_beneficiario',
                     'nis_responsavel', 'nome_responsavel']
    list_filter = ['ano_disponibilizacao', 'mes_disponibilizacao', 'uf',
                   'enquadramento', 'parcela']

    def get_changelist(self, request, **kwargs):
        self.model = AuxilioEmergencial
        return super(AuxilioEmergencialAdmin, self) \
            .get_changelist(request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = ModelForm
            self.readonly_fields = self.list_display
        return super(AuxilioEmergencialAdmin, self).get_form(request, obj,
                                                             **kwargs)

    def get_changeform_initial_data(self, request):
        return {
            'dataset': Task.AUXILIO_EMERGENCIAL,
            'source_format': Task.CSV
        }


class CotasParlamentaresAdmin(AddOnlyAdmin, TaskAdmin):
    list_display = ['parlamentar', 'nuLegislatura', 'sgUF',
                    'partido', 'txtDescricao', 'fornecedor',
                    'passageiro', 'trecho']
    list_filter = ['parlamentar', 'nuLegislatura', 'partido',
                   'txtDescricao', 'fornecedor', 'passageiro']

    def get_changelist(self, request, **kwargs):
        self.model = CotasParlamentares
        return super(CotasParlamentaresAdmin, self) \
            .get_changelist(request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = ModelForm
            self.readonly_fields = self.list_display
        return super(CotasParlamentaresAdmin, self).get_form(request, obj,
                                                             **kwargs)

    def get_changeform_initial_data(self, request):
        return {
            'dataset': Task.COTAS_PARLAMENTARES,
            'source_format': Task.ZIP
        }


admin.site.register(Task, TaskAdmin)

admin.site.register(AuxilioEmergencial, AuxilioEmergencialAdmin)
admin.site.register(CotasParlamentares, CotasParlamentaresAdmin)
