from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from usuario import views

urlpatterns = [
    path("crear/", views.SignUpView.as_view(), name ="usuario_iniciarsesion"),
    path("profile/<pk>/", views.BloggerProfile.as_view(), name ="usuario_perfil"),
    path("editar/<pk>/", views.BloggerUpdate.as_view(), name ="usuario_editar"),
    path("entrar/", views.BlogLogin.as_view(), name="blogs_iniciarsesion"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
