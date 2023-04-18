from django.db import models

class WorkCategory(models.Model):
    name = models.CharField('Название категории', max_length=255, blank=True, null=True)

class WorkType(models.Model):
    category = models.ForeignKey(WorkCategory,on_delete=models.CASCADE,blank=False,null=True,related_name='types')
    name = models.CharField('Название работы', max_length=255, blank=True, null=True)
    norma = models.DecimalField('Норма часы', blank=False, null=True,decimal_places=2,max_digits=4)

class Client(models.Model):
    car = models.CharField('Марка', max_length=255, blank=True, null=True)
    model = models.CharField('Модель', max_length=255, blank=True, null=True)
    year = models.CharField('Год выпуска ТС', max_length=255, blank=True, null=True)
    vin = models.CharField('VIN', max_length=255, blank=True, null=True)
    number = models.CharField('Гос номер', max_length=255, blank=True, null=True)
    owner = models.CharField('Имя владельца', max_length=255, blank=True, null=True)
    phones = models.TextField('Телефоны для связи', blank=True, null=True)
    need_to_repare = models.TextField('Жалобы клиента ', blank=True, null=True)
    done_work = models.TextField('Проведенные работы', blank=True, null=True)
    date_come = models.DateField('Дата обращения клиента', blank=True, null=True)
    date_ready = models.DateField('Дата ремонта', blank=True, null=True)

    notes = models.TextField('Замечания', blank=True, null=True)


