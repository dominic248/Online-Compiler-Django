from rest_framework import serializers

from django.contrib.auth import get_user_model

Users = get_user_model()


class UsersCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Users
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "picture",
        ]

    def create(self, validated_data):
        password=validated_data.pop("password")
        user = Users.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    



class UsersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    current_user = serializers.SerializerMethodField("curruser")

    class Meta:
        model = Users
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "current_user",
            "picture",
        ]

    def curruser(self, obj):
        try:
            # print(self.context["request"].user.id)
            return self.context["request"].user.id
        except:
            pass
