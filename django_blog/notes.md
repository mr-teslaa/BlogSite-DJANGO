#   in `models.py`:
-   `auto_now_add=True` can't be modified later we want to change that, so we will use `default=timezone.now` and from timzonenow we need to import that `from django.utils import timezone`
-   `on_delete=models.CASCADE` in here we are just telling django that what we will do if the creator of that post get deleted, we can set that the user is deleted or something, but in this case we will say that we will delete the post if the user is also deleted. that's what exactly `CASCADE` argument does.
-   for watching SQL code of the database model, we need to run this command `python manage.py sqlmigrate blog 001` in here 001 is the id of migration table, you will find this in terminal (cmd) when the migration is done
-   if we want to query all post of a user we can follow the step of flask like getting the user id and then query that over post model but django give us much more flexibility, we can use `{usermodel}.{modelname}_set.all()` in our case it will be `user.post_set.all()` where user will be a specific use like user1 or user2. 


#   create super user for accessing django admin page
-   `python manage.py createsuperuser`
    but it is showing us an error like to such table `auth_user` so we need to make migration for that first, for that
-   `python manage.py makemigrations`
    it shows that NO changes detected, which means we have to push the migrations, for that
-   `python manage.py migrate`

## now we are good to create a super user using the command `python manage.py createsuperuser`