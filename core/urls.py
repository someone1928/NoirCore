from django.contrib import admin
from django.urls import path
from main import views as main_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main pages
    path('', main_views.home, name='home'),
    path('profile/', main_views.profile, name='profile'),
    path('articles/', main_views.articles, name='articles'),
    path('projects/', main_views.projects, name='projects'),
    path('researches/', main_views.researches, name='researches'),
    path('notes/', main_views.notes, name='notes'),
    path('aboutus/', main_views.aboutus, name='aboutus'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Upload
    path('upload/project/', main_views.upload_project, name='upload_project'),
    path('upload/note/', main_views.upload_note, name='upload_note'),

    # Dashboard
    path('dashboard/', main_views.dashboard, name='dashboard'),

    # Project CRUD
    path('project/edit/<int:pk>/', main_views.edit_project, name='edit_project'),
    path('project/delete/<int:pk>/', main_views.delete_project, name='delete_project'),

    # Note CRUD
    path('note/edit/<int:pk>/', main_views.edit_note, name='edit_note'),
    path('note/delete/<int:pk>/', main_views.delete_note, name='delete_note'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
