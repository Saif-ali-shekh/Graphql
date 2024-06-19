

import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphql import GraphQLError

class UserType(DjangoObjectType):
    class Meta:
        model =CustomUser
        fields=['id', 'name','email']
        
class AutherType(DjangoObjectType):
    class Meta:
        model =Author
        

class BooksType(DjangoObjectType):
    class Meta:
        model =Book
        
        
class Query(graphene.ObjectType):
    all_user=graphene.List(UserType)
    all_auther =graphene.List(AutherType)
    all_books =graphene.List(BooksType)
    UserTypeBy_id =graphene.Field(UserType , User_id =graphene.Int(required =True))
    AutherType_id =graphene.Field(AutherType ,aurther_id =graphene.Int(required =True))
    BooksTypeBy_id =graphene.Field(BooksType , books_id =graphene.Int(required =True))
    
    def resolve_all_user(self ,request ):
        return CustomUser.objects.all()
    
    def resolve_all_auther(self ,request ):
        return Author.objects.all()
    
    def resolve_all_books(self ,request ):
        return Book.objects.all()
    
    def resolve_UserTypeBy_id(self, request,User_id):
        try:
            return CustomUser.objects.get(id=User_id)
        # except CustomUser.DoesNotExist:
        #     return None
        except CustomUser.DoesNotExist:
            raise GraphQLError(f"User with id {id} does not exist")
    def resolve_author_by_id(self, info, id):
        try:
            return Author.objects.get(pk=id)
        except Author.DoesNotExist:
            raise GraphQLError(f"Author with id {id} does not exist")  
    def resolve_book_by_id(self, info, id):
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist:
            raise GraphQLError(f"Book with id {id} does not exist")
        
class CreateCustomUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        name = graphene.String()
        age = graphene.Int()
        # address = graphene.String()
        # city = graphene.String()
        # country = graphene.String()

    user = graphene.Field(UserType )

    def mutate(root, info, username, email, password, name=None, age=None):
        user = CustomUser(
            username=username,
            email=email,
            name=name,
            age=age,
            
        )
        user.set_password(password)
        user.save()
        return CreateCustomUser(user=user)
    
class UpdateCustomUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        name = graphene.String()
        age = graphene.Int()
        address = graphene.String()
        city = graphene.String()
        country = graphene.String()

    user = graphene.Field(UserType)

    def mutate(root, info, id, username=None, email=None, password=None, name=None, age=None, address=None, city=None, country=None):
        try:
            user = CustomUser.objects.get(pk=id)
            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.set_password(password)
            if name:
                user.name = name
            if age is not None:
                user.age = age
            if address:
                user.address = address
            if city:
                user.city = city
            if country:
                user.country = country
            user.save()
            return UpdateCustomUser(user=user)
        except CustomUser.DoesNotExist:
            return None
        
class DeleteCustomUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        try:
            user = CustomUser.objects.get(pk=id)
            user.delete()
            return DeleteCustomUser(success=True)
        except CustomUser.DoesNotExist:
            return DeleteCustomUser(success=False)

#for adding and changes data
class Mutation(graphene.ObjectType):
    create_user = CreateCustomUser.Field()  ###USE RESPONSE DATA IN WEB SCHEMA 
    #whose fiels define in object type . only whose field show in response , but we can do update also
    update_user = UpdateCustomUser.Field() 
    delete_user = DeleteCustomUser.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)  #schema  containnes 2 parameter to show in browser
