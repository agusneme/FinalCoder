from django.urls import path
from blogs import views


urlpatterns = [
    path("blogs/", views.BlogList.as_view(), name="blogs_listas"),
    path("blogs2/", views.BlogList2.as_view(), name="blogs_listas2"),
    path("entregar/", views.BlogCreate.as_view(), name="blogs_crear"),
    path("consignas/", views.BlogCreate2.as_view(), name="blogs_consignas"),


    path("detalle/<pk>/", views.BlogDetail.as_view(), name ="blogs_detalles"),
    path("editar/<pk>/", views.BlogUpdate.as_view(), name ="blogs_actualizar"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="blogs_eliminar"),



    path("editar2/<pk>/", views.BlogUpdate2.as_view(), name ="blogs_actualizar2"),
    path("borrar2/<pk>/", views.BlogDelete2.as_view(), name ="blogs_eliminar2"),
    path("detalle2/<pk>/", views.BlogDetail2.as_view(), name ="blogs_detalles2"),

  
  ##  path("entrar/", views.BlogLogin.as_view(), name="blogs_iniciarsesion"),
    path("salir/", views.BlogLogout.as_view(), name="blogs_desconectar"),
    path("about/", views.About.as_view(), name="about" ),
    path("", views.Index.as_view(), name="Index" ),

]