from django.conf.urls import patterns, include, url
from django.contrib import admin
from lead_admin.views import AdminDashBoardView
from lead_admin.views import AdminStudentsEditView
from lead_admin.views import AdminStudentsAddView
from lead_admin.views import AdminStudentsEditViewAjax
from lead_admin.views import AdminStaffEditView
from lead_admin.views import AdminStaffAddView
from lead_admin.views import AdminStaffEditViewAjax
from lead_admin.views import AdminBatchAddView
from lead_admin.views import AdminBatchEditViewAjax
from lead_admin.views import AdminBatchEditView
from lead_admin.views import AdminDivisionEditView
from lead_admin.views import AdminDivisionEditViewAjax

from lead_admin.views import AdminSubjectAddView
from lead_admin.views import AdminSubjectEditView
from lead_admin.views import AdminSubjectEditViewAjax


from lead_admin.views import AdminSubMapEditView
from lead_admin.views import AdminSubMapEditViewAjax

from lead_admin.views import MentorAddView
from lead_admin.views import AdminMentorEditView
from lead_admin.views import AdminMentorEditViewAjax

from lead_admin.views import AdminAttendanceView
from lead_admin.views import AdminAttendanceSubView
from lead_admin.views import AdminAttendanceAjaxView
from lead_admin.views import AdminAttendanceDeleteAjaxView

from lead_admin.views import  AdminConfirmLeaveView
from lead_admin.views import  AdminConfirmLeaveEditView
from lead_admin.views import  AdminLeaveEditView

from lead_admin.views import OdAddView
from lead_admin.views import OdEditViewAjax
from lead_admin.views import OdEditView


from lead_admin.views import is_lead_admin
from django.contrib.auth.decorators import user_passes_test

urlpatterns = patterns('',

    url(r'^$',  (AdminDashBoardView.as_view())),
    url(r'^students/$',  (AdminStudentsAddView.as_view())),
    url(r'^students/edit/(.*)$',  (AdminStudentsEditView.as_view())), #Populate modal form for edit
    url(r'^students/editajax/$',  (AdminStudentsEditViewAjax.as_view())), #populate table and manage delete post
    
    url(r'^staff/$',  (AdminStaffAddView.as_view())),
    url(r'^staff/edit/(.*)$',  (AdminStaffEditView.as_view())), #Populate modal form for edit
    url(r'^staff/editajax/$',  (AdminStaffEditViewAjax.as_view())), #populate table 
    
    url(r'^batch/$',  (AdminBatchAddView.as_view())),#Populate both batch and div forms
    url(r'^batch/edit/(.*)$', (AdminBatchEditView.as_view())),#Populate  modal for edit
    url(r'^batch/editajax/$', (AdminBatchEditViewAjax.as_view())), # Populate batch table
    
    url(r'^div/edit/(.*)$',  (AdminDivisionEditView.as_view())),#Populate modal for edit division
    url(r'^div/editajax/$', (AdminDivisionEditViewAjax.as_view())), # Populate div table and manage delete post
    
    url(r'^subject/$',  (AdminSubjectAddView.as_view())),#Populate both subject and map forms
    url(r'^subject/edit/(.*)$', ( AdminSubjectEditView.as_view())),#Populate  modal for edit
    url(r'^subject/editajax/$', ( AdminSubjectEditViewAjax.as_view())), # Populate batch table
    
    url(r'^map/edit/(.*)$', (AdminSubMapEditView.as_view())),#Populate modal for edit division
    url(r'^map/editajax/$', (AdminSubMapEditViewAjax.as_view())), # Populate map table and manage delete post
    
    url(r'^mentors/$',(MentorAddView.as_view())),
    url(r'^mentors/edit/(.*)$',(AdminMentorEditView.as_view())),
    url(r'^mentors/editajax/$',(AdminMentorEditViewAjax.as_view())),          	
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    
    url(r'^attendance/$',(AdminAttendanceView.as_view())),
    url(r'^attendance/subs/(\d+)/$',(AdminAttendanceSubView.as_view())),
    url(r'^attendance/subs/(\d+)/(\d{4})/(\d+)/(\d+)/(\d+)/$',(AdminAttendanceAjaxView.as_view())),
    url(r'^attendance/pullrecords/$',(AdminAttendanceDeleteAjaxView.as_view())),	   
	
	url(r'leave/$',(AdminConfirmLeaveView.as_view())),
	url(r'leave/editajax/(.*)$',(AdminConfirmLeaveEditView.as_view())),
	url(r'leave/edit/$',(AdminLeaveEditView.as_view())),
	
	url(r'^Od/$',OdAddView.as_view()),
    url(r'^Od/edit/$',OdEditView.as_view()),
    url(r'^Od/editajax/(.*)$',OdEditViewAjax.as_view()),
  )
