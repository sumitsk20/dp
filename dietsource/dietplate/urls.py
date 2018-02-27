"""
Definition of urls for notesformca.
"""
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.index , name="index" ),
    url(r'^about/$', views.about , name="about" ),
    url(r'^contact/$', views.contact , name="contact" ),
    url(r'^contact/success/$', views.contact_success , name="contact_success"),
    url(r'^book-appointment/$', views.book_appointment , name="book_appointment"),
    # url(r'^chaining/', include('smart_selects.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    #url(r'^service/', include("services.urls", namespace='service')),
    url(r'^', include('blog.urls', namespace = 'blog')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
