from django.shortcuts import render

from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers
from core.models import Recipe,Tag,Ingredient


class RecipeView(viewsets.ModelViewSet):
    """ Recipe Model Viewset"""

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrive recipe details which belongs to the logedin user"""
        return self.queryset.filter(user = self.request.user).order_by('-id')


    def get_serializer_class(self):

        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)


class BaseRecipeAttrViewset(mixins.DestroyModelMixin
                            ,mixins.UpdateModelMixin
                            ,mixins.ListModelMixin
                            ,viewsets.GenericViewSet):
    """Base viewset for recipe attributes"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user).order_by('-name')

class TagViewSet(BaseRecipeAttrViewset):

    """manage Tag View for tag model"""

    serializer_class = serializers.TagSeializer
    queryset = Tag.objects.all()




class IngredientViewset(BaseRecipeAttrViewset):
    """manage ingredient in DB"""

    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()
