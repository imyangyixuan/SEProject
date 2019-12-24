# Generated by Django 3.0 on 2019-12-24 02:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('userEmail', models.EmailField(max_length=254, verbose_name='email')),
                ('userName', models.CharField(max_length=12, verbose_name='userName')),
                ('projectCode', models.CharField(max_length=12, verbose_name='code')),
                ('instruction', models.CharField(max_length=140, verbose_name='instruction')),
                ('result', models.BooleanField(default=False, verbose_name='result')),
                ('check', models.BooleanField(default=False, verbose_name='check')),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('taskId', models.IntegerField(verbose_name='taskId')),
                ('userId', models.IntegerField(default=0, verbose_name='userId')),
                ('username', models.CharField(default='', max_length=12, verbose_name='name')),
                ('name', models.CharField(max_length=12, verbose_name='name')),
                ('content', models.TextField(verbose_name='content')),
                ('file', models.FileField(upload_to='commit/', verbose_name='file')),
                ('commitTime', models.DateField(default=django.utils.timezone.now, verbose_name='commitTime')),
            ],
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('projectCode', models.CharField(max_length=12, verbose_name='code')),
                ('userEmail', models.EmailField(max_length=254, verbose_name='email')),
                ('instruction', models.CharField(max_length=140, verbose_name='instruction')),
                ('result', models.BooleanField(default=False, verbose_name='result')),
                ('check', models.BooleanField(default=False, verbose_name='check')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('isUser', models.BooleanField(default=True, verbose_name='isUser')),
                ('userId', models.IntegerField(verbose_name='userId')),
                ('projectId', models.IntegerField(verbose_name='projectId')),
                ('content', models.TextField(verbose_name='content')),
                ('fromWho', models.CharField(max_length=12, verbose_name='fromWho')),
                ('pushTime', models.DateField(auto_now_add=True, verbose_name='pushTime')),
                ('isSend', models.BooleanField(default=False, verbose_name='isSend')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=12, verbose_name='name')),
                ('code', models.CharField(max_length=12, verbose_name='code')),
                ('describe', models.CharField(max_length=140, verbose_name='describe')),
                ('creator', models.EmailField(default='', max_length=254, verbose_name='email')),
                ('buildTime', models.DateField(auto_now_add=True, verbose_name='buildTime')),
                ('lastUpdateTime', models.DateField(auto_now=True, verbose_name='lastUpdateTime')),
                ('memberNum', models.IntegerField(verbose_name='memberNum')),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('isUser', models.BooleanField(default=True, verbose_name='isUser')),
                ('userId', models.IntegerField(default=0, verbose_name='userId')),
                ('projectId', models.IntegerField(default=0, verbose_name='projectId')),
                ('name', models.CharField(default='null', max_length=120, verbose_name='name')),
                ('file', models.FileField(upload_to='file/', verbose_name='file')),
            ],
        ),
        migrations.CreateModel(
            name='shipUserProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEsite.Project')),
            ],
        ),
        migrations.CreateModel(
            name='shipUserTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=12, verbose_name='name')),
                ('nameProject', models.CharField(default='', max_length=12, verbose_name='name')),
                ('code', models.CharField(default='', max_length=12, verbose_name='code')),
                ('content', models.TextField(verbose_name='content')),
                ('editTime', models.DateField(auto_now_add=True, verbose_name='editTime')),
                ('pushTime', models.DateField(auto_now_add=True, verbose_name='pushTime')),
                ('deadLine', models.DateField(auto_now_add=True, verbose_name='deadLine')),
                ('isPushed', models.BooleanField(default=False, verbose_name='isPushed')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=16, verbose_name='password')),
                ('name', models.CharField(max_length=12, verbose_name='name')),
                ('profile', models.TextField(default='', verbose_name='profile')),
                ('work', models.CharField(max_length=12, verbose_name='work')),
                ('phone', models.CharField(max_length=11, verbose_name='phone')),
                ('createTime', models.DateField(auto_now_add=True, verbose_name='creaetTime')),
                ('isVerificated', models.BooleanField(default=False, verbose_name='isVerificated')),
                ('isFreezed', models.BooleanField(default=False, verbose_name='isFreezed')),
                ('projectInCharge', models.ManyToManyField(through='SEsite.shipUserProject', to='SEsite.Project')),
                ('taskInCharge', models.ManyToManyField(through='SEsite.shipUserTask', to='SEsite.Task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='member',
            field=models.ManyToManyField(through='SEsite.shipUserTask', to='SEsite.User'),
        ),
        migrations.AddField(
            model_name='shipusertask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEsite.Task'),
        ),
        migrations.AddField(
            model_name='shipusertask',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEsite.User'),
        ),
        migrations.AddField(
            model_name='shipuserproject',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEsite.User'),
        ),
        migrations.CreateModel(
            name='shipProjectTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEsite.Project')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEsite.Task')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='member',
            field=models.ManyToManyField(through='SEsite.shipUserProject', to='SEsite.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='task',
            field=models.ManyToManyField(through='SEsite.shipProjectTask', to='SEsite.Task'),
        ),
    ]
