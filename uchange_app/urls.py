from django.conf.urls import patterns,url

from uchange_app import views

urlpatterns=patterns('',
    url(r'^$',views.self,name='self'),
    
    url(r'^profile/$',views.self_profile,name='self_profile'),
    url(r'^profile/(?P<visit_id>\d+)/$',views.profile,name='profile'),
    url(r'^profile/(?P<visit_id>\d+)/history/$',views.person_history,name='person_history'),
                     
    url(r'^item/$',views.item_list,name='item_list'),
    url(r'^item/(?P<item_id>\d+)/$',views.item_detail,name='detail'),
    url(r'^item/(?P<item_id>\d+)/post_comment/$',views.post_comment,name='post_comment'),
    url(r'^item/(?P<item_id>\d+)/history/$',views.item_history,name='item_history'),
    
    url(r'^item/(?P<item_id>\d+)/accept/$',views.accept,name='accept'),
    url(r'^item/(?P<item_id>\d+)/request/$',views.request,name='request'),
    url(r'^request/$',views.request_list,name='request_list'),
    url(r'^myrequest/$',views.myrequest,name='myrequest'),
    
    url(r'^result/$',views.result,name='result'),
                     
    url(r'^init/$',views.init,name='init'),
    url(r'^init_item/$',views.init_item,name='init_item'),
    url(r'^init_item/operate/$',views.init_item_operate,name='init_item_operate'),
    url(r'^edit_item/$',views.edit_item,name='edit_item'),
    url(r'^edit_item/operate/$',views.edit_item_operate,name='edit_item_operate'),
    
    url(r'^edit_profile/$',views.edit_profile, name='edit_profile'),
    url(r'^edit_profile/operate/$',views.edit_profile_operate, name='edit_profile_operate'),
)