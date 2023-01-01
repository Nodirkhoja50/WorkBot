from rest_framework import serializers

from users.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','company_name','main_language','base_salary')