from django.contrib.auth.models import User
from .models import Course, Curriculum, Degreeprogram, Group, Implementation, Person, PersonDegreeprogram, PersonImplementation, Room, RoomImplementation, Subgroup, SubgroupImplementation
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, CourseSerializer, CurriculumSerializer, DegreeprogramSerializer, ImplementationSerializer, PersonSerializer, PersonDegreeprogramSerializer, PersonImplementationSerializer, RoomSerializer, RoomImplementationSerializer, SubgroupSerializer, SubgroupImplementationSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
	
class CourseViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
	
class CurriculumViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
	
class DegreeprogramViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Degreeprogram.objects.all()
    serializer_class = DegreeprogramSerializer
	
class ImplementationViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Implementation.objects.all()
    serializer_class = ImplementationSerializer
	
class PersonViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
	
class PersonDegreeprogramViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = PersonDegreeprogram.objects.all()
    serializer_class = PersonDegreeprogramSerializer
	
class PersonImplementationViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = PersonImplementation.objects.all()
    serializer_class = PersonImplementationSerializer
	
class RoomViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
	
class RoomImplementationViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = RoomImplementation.objects.all()
    serializer_class = RoomImplementationSerializer
	
class SubgroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Subgroup.objects.all()
    serializer_class = SubgroupSerializer
	
class SubgroupImplementationViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = SubgroupImplementation.objects.all()
    serializer_class = SubgroupImplementationSerializer