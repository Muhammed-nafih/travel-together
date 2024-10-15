from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
				
				path('',views.Home,name='Home'),
				path('Registration/',views.Registration,name='Registration'),
				path('User_Login/',views.User_Login,name='User_Login'),
				path('Profile/',views.Profile,name='Profile'),
				path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
				path('Manage_Groups/',views.Manage_Groups,name='Manage_Groups'),
				path('Add_Group/',views.Add_Group,name='Add_Group'),
				path('View_Groups/',views.View_Groups,name='View_Groups'),
				path('Join/<int:id>',views.Join,name='Join'),
				path('View_Members/<int:id>',views.View_Members,name='View_Members'),
				path('Delete_Group/<int:id>',views.Delete_Group,name='Delete_Group'),
				path('View_Request/<int:id>',views.View_Request,name='View_Request'),
				path('View_Chat/<int:id>',views.View_Chat,name='View_Chat'),
				path('Update_Status/',views.Update_Status,name='Update_Status'),
				path('Add_Comment/',views.Add_Comment,name='Add_Comment'),
				path('Update_Group/',views.Update_Group,name='Update_Group'),
				path('Logout/',views.Logout,name='Logout'),
				
					
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)