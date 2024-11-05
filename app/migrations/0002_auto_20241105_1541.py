# Generated by Django 3.1.2 on 2024-11-05 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Mensaje'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre Completo'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='notice',
            field=models.BooleanField(verbose_name='Aviso'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type_enquiry',
            field=models.IntegerField(choices=[(1, 'Consulta'), (2, 'Reclamo'), (2, 'Sugerencia'), (2, 'Felicitaciones')], verbose_name='Tipo de consulta'),
        ),
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='products',
            name='fabrication_date',
            field=models.DateField(verbose_name='Fecha de Fabricación'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_new',
            field=models.BooleanField(verbose_name='Nuevo'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre de Producto'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='Precio'),
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='app.products')),
            ],
        ),
    ]
