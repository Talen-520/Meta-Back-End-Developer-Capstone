# Meta-Back-End-Developer-Capstone
In order to test functionality of this project, setup environment by following:

install pipenv
```
pip install pipenv
```

modify python version inside Pipfile
```
[requires]
python_version = "your_python_version"
```


active shell:
```
pipenv shell
```

modify setting.py database setting

then you are good to go with these url end point

project level
```
    path('admin/', admin.site.urls), 
    path('api/', include('Restaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))

```
app level

```
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token), # token function path, this method only accept http post call
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/',views.BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:id>/',views.BookingDetailView.as_view(), name='booking-detail'),
    path('message/', views.msg),
```

switch branch by 
```
git checkout -B branchone
```


Push the changes to the GitHub repository

Use the command 

git push –u origin <branch-name>.
```
git push -u origin main
git push –u origin branchone
```