# Generated by Django 2.0.4 on 2018-06-04 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AssetManage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mapped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Domain', models.CharField(blank=True, max_length=50, null=True, verbose_name='域名')),
                ('mapped_status', models.BooleanField(default=True, verbose_name='是否启用')),
                ('start_time', models.DateField(null=True, verbose_name='开启时间')),
                ('end_time', models.DateField(null=True, verbose_name='关闭时间')),
                ('request_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='申请人邮箱')),
                ('action_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='操作人邮箱')),
                ('Mapped_description', models.TextField(blank=True, null=True, verbose_name='映射备注')),
                ('request_order', models.CharField(blank=True, max_length=50, null=True, verbose_name='申请单号')),
                ('request_user', models.CharField(blank=True, max_length=50, null=True, verbose_name='申请人')),
                ('request_user_num', models.CharField(blank=True, max_length=50, null=True, verbose_name='员工编号')),
                ('request_user_department', models.CharField(blank=True, max_length=50, null=True, verbose_name='申请部门')),
                ('telephone', models.CharField(blank=True, max_length=50, null=True, verbose_name='联系电话')),
                ('mapped_updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('LANPort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LANport_for_mapped', to='AssetManage.Port_Info', verbose_name='内网端口')),
                ('LANip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LANip_for_mapped', to='AssetManage.Asset', verbose_name='内网IP')),
                ('Mapped_user', models.ManyToManyField(blank=True, related_name='mapped_to_user', to=settings.AUTH_USER_MODEL)),
                ('WANPort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WANport_for_mapped', to='AssetManage.Port_Info', verbose_name='外网端口')),
                ('WANip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WANip_for_mapped', to='AssetManage.Asset', verbose_name='外网IP')),
            ],
        ),
    ]