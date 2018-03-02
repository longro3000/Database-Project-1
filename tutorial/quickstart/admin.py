# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import Course, Curriculum, Degreeprogram, Group, Implementation, Person, PersonDegreeprogram, PersonImplementation, Room, RoomImplementation, Subgroup, SubgroupImplementation

admin.site.register(Course)
admin.site.register(Curriculum)
admin.site.register(Degreeprogram)
admin.site.register(Group)
admin.site.register(Implementation)
admin.site.register(Person)
admin.site.register(PersonDegreeprogram)
admin.site.register(PersonImplementation)
admin.site.register(Room)
admin.site.register(RoomImplementation)
admin.site.register(Subgroup)
admin.site.register(SubgroupImplementation)
