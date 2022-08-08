from django.urls import re_path, path
from restful_api.Controller.BusinessOwner import BOController, ProjectController

urlpatterns = [
    re_path(
        r'^api/checkowner/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', BOController.BusinessOwnerController.checkemail),
    re_path(r'^api/businessowner/registration/$',
            BOController.BusinessOwnerController.businessowner_registration),
    re_path(r'^api/project/$', ProjectController.ProjectController.projectEntry),
    re_path(r'^api/business-checkemail/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$',
            BOController.BusinessOwnerController.business_verification),
    re_path(r'^api/verification-entry$',
            BOController.BusinessOwnerController.business_verification_record),
    re_path(
        r'^api/check-email-counts/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$', BOController.BusinessOwnerController.business_verification_checkcounts),
    # re_path(r'^api/check-before-sending/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
    #         BOController.BusinessOwnerController.business_check_beforesend),
    re_path(r'^api/check-email-verification/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
            BOController.BusinessOwnerController.business_verify_email),
    re_path(r'^api/business-update-with-send/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$',
            BOController.BusinessOwnerController.business_update_with_sendemail)
]