from django.db import models


class Shop(models.Model):
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return '[{}| Shop {}]'.format(self.id, self.name)

    name = models.CharField(max_length=250, verbose_name="Имя")
    address = models.CharField(max_length=250, null=True, verbose_name="Адрес")
    staff_amount = models.IntegerField(verbose_name="Количество персонала")


class Department(models.Model):
    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"

    def __str__(self):
        return '[{}| Dep {}]'.format(self.id, self.sphere)

    sphere = models.CharField(max_length=250, verbose_name="Отдел")
    staff_amount = models.IntegerField(verbose_name="Количество персонала")
    description = models.TextField(verbose_name="Описание отдела")
    shop = models.ForeignKey(Shop, related_name='departments',
                             on_delete=models.CASCADE, verbose_name="Магазин")


class Item(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return '[{}| Item {} from {}]'.format(self.id, self.name,
                                              self.department.shop.name)

    name = models.CharField(max_length=250, verbose_name="Имя товара")
    description = models.TextField(null=True, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    department = models.ForeignKey(Department, related_name='items',
                                   on_delete=models.CASCADE,
                                   verbose_name="Департамент")
    image = models.ImageField(upload_to='items/', verbose_name='Изображение',
                              null=True, blank=True)
    is_sold = models.BooleanField(verbose_name='Продан', default=False)
    creation_date = models.DateField(verbose_name='Дата создания', null=True,
                                     blank=True)
