# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    code = models.CharField(db_column='Code', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    changes = models.CharField(db_column='Changes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    languages = models.CharField(db_column='Languages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    credit = models.IntegerField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    p1 = models.IntegerField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    p2 = models.IntegerField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
    p3 = models.IntegerField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
    p4 = models.IntegerField(db_column='P4', blank=True, null=True)  # Field name made lowercase.
    p5 = models.IntegerField(db_column='P5', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    curriculumid = models.ForeignKey('Curriculum', models.DO_NOTHING, db_column='curriculumid')

    class Meta:
        managed = False
        db_table = 'course'


class Curriculum(models.Model):
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    degreeprogramid = models.ForeignKey('Degreeprogram', models.DO_NOTHING, db_column='degreeprogramid')

    class Meta:
        managed = False
        db_table = 'curriculum'


class Degreeprogram(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'degreeprogram'


class Group(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=20)  # Field name made lowercase.
    degreeprogramid = models.ForeignKey(Degreeprogram, models.DO_NOTHING, db_column='degreeprogramid')

    class Meta:
        managed = False
        db_table = 'group'


class Implementation(models.Model):
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')

    class Meta:
        managed = False
        db_table = 'implementation'


class Person(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=7)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person'


class PersonDegreeprogram(models.Model):
    personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='personid', primary_key=True)
    degreeprogramid = models.ForeignKey(Degreeprogram, models.DO_NOTHING, db_column='degreeprogramid')

    class Meta:
        managed = False
        db_table = 'person_degreeprogram'
        unique_together = (('personid', 'degreeprogramid'),)


class PersonImplementation(models.Model):
    personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='personid', primary_key=True)
    implementationid = models.ForeignKey(Implementation, models.DO_NOTHING, db_column='implementationid')

    class Meta:
        managed = False
        db_table = 'person_implementation'
        unique_together = (('personid', 'implementationid'),)


class Room(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=50)  # Field name made lowercase.
    seats = models.IntegerField(db_column='Seats', blank=True, null=True)  # Field name made lowercase.
    topic = models.CharField(db_column='Topic', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class RoomImplementation(models.Model):
    roomid = models.ForeignKey(Room, models.DO_NOTHING, db_column='roomid', primary_key=True)
    implementationid = models.ForeignKey(Implementation, models.DO_NOTHING, db_column='implementationid')

    class Meta:
        managed = False
        db_table = 'room_implementation'
        unique_together = (('roomid', 'implementationid'),)


class Subgroup(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=20)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30)  # Field name made lowercase.
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'subgroup'


class SubgroupImplementation(models.Model):
    subgroupid = models.ForeignKey(Subgroup, models.DO_NOTHING, db_column='subgroupid', primary_key=True)
    implementationid = models.ForeignKey(Implementation, models.DO_NOTHING, db_column='implementationid')

    class Meta:
        managed = False
        db_table = 'subgroup_implementation'
        unique_together = (('subgroupid', 'implementationid'),)
