# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Emp(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'emp'


class SoftwareEngineers(models.Model):
    id = models.TextField(blank=True, null=True)
    full_name = models.TextField(db_column='Full name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    profile_url = models.TextField(db_column='Profile url', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_name = models.TextField(db_column='First name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.TextField(db_column='Last name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    avatar = models.TextField(db_column='Avatar', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    birthday = models.TextField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    summary = models.TextField(db_column='Summary', blank=True, null=True)  # Field name made lowercase.
    twitter = models.TextField(db_column='Twitter', blank=True, null=True)  # Field name made lowercase.
    phone_1 = models.TextField(db_column='Phone 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_1_type = models.TextField(db_column='Phone 1 type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_2 = models.TextField(db_column='Phone 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_2_type = models.TextField(db_column='Phone 2 type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_3 = models.TextField(db_column='Phone 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_3_type = models.TextField(db_column='Phone 3 type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    messenger_1 = models.TextField(db_column='Messenger 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    messenger_1_type = models.TextField(db_column='Messenger 1 type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    messenger_2 = models.TextField(db_column='Messenger 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    messenger_2_type = models.TextField(db_column='Messenger 2 type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    messenger_3 = models.TextField(db_column='Messenger 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    messenger_3_type = models.TextField(db_column='Messenger 3 type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    website_1 = models.TextField(db_column='Website 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    website_2 = models.TextField(db_column='Website 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    website_3 = models.TextField(db_column='Website 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_1 = models.TextField(db_column='Organization 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_title_1 = models.TextField(db_column='Organization Title 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_start_1 = models.TextField(db_column='Organization Start 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_end_1 = models.TextField(db_column='Organization End 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_description_1 = models.TextField(db_column='Organization Description 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_location_1 = models.TextField(db_column='Organization Location 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_url_1 = models.TextField(db_column='Organization LI URL 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_id_1 = models.IntegerField(db_column='Organization LI ID 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_2 = models.TextField(db_column='Organization 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_title_2 = models.TextField(db_column='Organization Title 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_start_2 = models.TextField(db_column='Organization Start 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_end_2 = models.TextField(db_column='Organization End 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_description_2 = models.TextField(db_column='Organization Description 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_location_2 = models.TextField(db_column='Organization Location 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_url_2 = models.TextField(db_column='Organization LI URL 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_id_2 = models.IntegerField(db_column='Organization LI ID 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_3 = models.TextField(db_column='Organization 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_title_3 = models.TextField(db_column='Organization Title 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_start_3 = models.TextField(db_column='Organization Start 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_end_3 = models.TextField(db_column='Organization End 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_description_3 = models.TextField(db_column='Organization Description 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_location_3 = models.TextField(db_column='Organization Location 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_url_3 = models.TextField(db_column='Organization LI URL 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_id_3 = models.TextField(db_column='Organization LI ID 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_4 = models.TextField(db_column='Organization 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_title_4 = models.TextField(db_column='Organization Title 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_start_4 = models.TextField(db_column='Organization Start 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_end_4 = models.TextField(db_column='Organization End 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_description_4 = models.TextField(db_column='Organization Description 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_location_4 = models.TextField(db_column='Organization Location 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_url_4 = models.TextField(db_column='Organization LI URL 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_id_4 = models.TextField(db_column='Organization LI ID 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_5 = models.TextField(db_column='Organization 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_title_5 = models.TextField(db_column='Organization Title 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_start_5 = models.TextField(db_column='Organization Start 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_end_5 = models.TextField(db_column='Organization End 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_description_5 = models.TextField(db_column='Organization Description 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_location_5 = models.TextField(db_column='Organization Location 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_url_5 = models.TextField(db_column='Organization LI URL 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_id_5 = models.TextField(db_column='Organization LI ID 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_6 = models.TextField(db_column='Organization 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_title_6 = models.TextField(db_column='Organization Title 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_start_6 = models.TextField(db_column='Organization Start 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_end_6 = models.TextField(db_column='Organization End 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_description_6 = models.TextField(db_column='Organization Description 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_location_6 = models.TextField(db_column='Organization Location 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_url_6 = models.TextField(db_column='Organization LI URL 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_id_6 = models.TextField(db_column='Organization LI ID 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_7 = models.TextField(db_column='Organization 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_title_7 = models.TextField(db_column='Organization Title 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_start_7 = models.TextField(db_column='Organization Start 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_end_7 = models.TextField(db_column='Organization End 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_description_7 = models.TextField(db_column='Organization Description 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_location_7 = models.TextField(db_column='Organization Location 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_url_7 = models.TextField(db_column='Organization LI URL 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_li_id_7 = models.TextField(db_column='Organization LI ID 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_1 = models.TextField(db_column='Education 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_degree_1 = models.TextField(db_column='Education Degree 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_fos_1 = models.TextField(db_column='Education FOS 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_grade_1 = models.TextField(db_column='Education Grade 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_start_1 = models.IntegerField(db_column='Education Start 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_end_1 = models.IntegerField(db_column='Education End 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_description_1 = models.TextField(db_column='Education Description 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_2 = models.TextField(db_column='Education 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_degree_2 = models.TextField(db_column='Education Degree 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_fos_2 = models.TextField(db_column='Education FOS 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_grade_2 = models.TextField(db_column='Education Grade 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_start_2 = models.TextField(db_column='Education Start 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_end_2 = models.TextField(db_column='Education End 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_description_2 = models.TextField(db_column='Education Description 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_3 = models.TextField(db_column='Education 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_degree_3 = models.TextField(db_column='Education Degree 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_fos_3 = models.TextField(db_column='Education FOS 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_grade_3 = models.TextField(db_column='Education Grade 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_start_3 = models.TextField(db_column='Education Start 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_end_3 = models.TextField(db_column='Education End 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_description_3 = models.TextField(db_column='Education Description 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skills = models.TextField(db_column='Skills', blank=True, null=True)  # Field name made lowercase.
    followers = models.TextField(db_column='Followers', blank=True, null=True)  # Field name made lowercase.
    relationship = models.IntegerField(db_column='Relationship', blank=True, null=True)  # Field name made lowercase.
    connected_at = models.TextField(db_column='Connected at', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    industry = models.TextField(db_column='Industry', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'software engineers'
