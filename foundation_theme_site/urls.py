from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
    url(r"^profiles/", include("idios.urls")),
    url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),
    
    url(r"^featured_shuffle/$", direct_to_template, {
        "template": "designs/featured_shuffle.html",
    }, name="home"),
    
    url(r"^column_flip/$", direct_to_template, {
        "template": "designs/column_flip.html",
    }, name="home"),
    
    url(r"^gallery_design/$", direct_to_template, {
        "template": "designs/gallery_design.html",
    }, name="home"),
    
    url(r"^mondrian/$", direct_to_template, {
        "template": "designs/mondrian.html",
    }, name="home"),    
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
