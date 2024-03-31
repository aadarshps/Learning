# Generated by Django 2.2.6 on 2021-09-08 13:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='RtUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('type', models.IntegerField(null=True)),
                ('rollno', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=20, null=True)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='registration.Course')),
                ('questions', models.ManyToManyField(to='registration.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='ExamSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_start', models.DateTimeField()),
                ('exam_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='registration.Exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=50)),
                ('option2', models.CharField(max_length=50)),
                ('option3', models.CharField(max_length=50)),
                ('option4', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Semester')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Semester'),
        ),
        migrations.AddField(
            model_name='exam',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Subject'),
        ),
        migrations.AddField(
            model_name='answer',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Course'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ansr', to='registration.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Semester'),
        ),
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Subject'),
        ),
        migrations.AddField(
            model_name='rtuser',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Course'),
        ),
        migrations.AddField(
            model_name='rtuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='rtuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
