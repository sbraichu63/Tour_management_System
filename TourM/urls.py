from django.urls import path
from . import views
from .views import ad_homeView, pack_detailView, homeView, UpdatePostView, DeletePostView, payment_page, receipt_view, enroll_view

urlpatterns = [
    path('ad-home/', ad_homeView.as_view(), name="ad_homeView"),
    path('details/edit/<int:pk>/', UpdatePostView.as_view(), name="UpdatePost"),
    path('details/<int:pk>/delete', DeletePostView.as_view(), name="DeletePost"),
   
    path('info/', views.infoView, name="infoView"),
    path('packView/', views.PackView, name="PackView"),
    path('package/', homeView.as_view(), name="homeView"),
    path('details/<int:pk>', pack_detailView.as_view(), name="pack_detailView"),

    # ✅ ENROLL FLOW
    path('enroll/<int:post_id>/', views.enroll_view, name='enroll'),

    # ✅ PAYMENT FLOW
    path('payment/<int:booking_id>/', payment_page, name='payment'),
    path('receipt/<int:payment_id>/', receipt_view, name='receipt'),

    path('api/packages/', views.api_packages, name='api_packages'),

    path('user_csv', views.user_csv, name="user_csv"),
    path('enroll_csv', views.enroll_csv, name="enroll_csv"),
    path('user_pdf', views.user_pdf, name="user_pdf"),

    path('enrolled/', views.En_usersView, name="enrolled"),

    path('aboutus/', views.aboutus, name="aboutus"),
    path('seasons/', views.seasons, name="seasons"),
    
    path('', views.homepage, name="homepage"),

    path('logout/', views.logout_view, name='logout'),
]