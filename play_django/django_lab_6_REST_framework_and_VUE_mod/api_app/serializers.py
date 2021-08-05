from rest_framework import serializers

from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'first_name', 
            'last_name', 
            'cohort', 
            'favorite_topic', 
            'favorite_teacher', 
            'capstone'
            )

    
# merrit here uses a 'nested serializer'

# see https://www.django-rest-framework.org/api-guide/serializers/
# From https://learndjango.com/tutorials/django-rest-framework-tutorial-todo-api :
    # A traditional Django app needs a dedicated url, view, and template to translate information from that database onto a webpage. In DRF we instead need a url, view, and a serializer. The url controls access to the API endpoints, views control the logic of the data being sent, and the serializer performs the magic of converting our information into a format suitable for transmission over the internet, JSON.
    # If you're new to APIs then serializers are probably the most confusing part of the equation. A normal webpage requires HTML, CSS, and JavaScript (usually). But our API is only sending data in the JSON format. No HTML. No CSS. Just data. The serializer translates our Django models into JSON and then the client app translates JSON into a full-blown webpage. The reverse, deserialization, also occurs when our API accepts a user input--for example submitting a new todo--which is translated from HTML into JSON then converted into our Django model.
    # So to repeat one last time: urls control access, views control logic, and serializers transform data into something we can send over the internet.
