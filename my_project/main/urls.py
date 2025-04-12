from django.urls import path
from .views import home, freelancer_dashboard, create_gig, client_dashboard, gig_detail, view_gig, edit_gig

urlpatterns = [
    path('', home, name='home'),  # Homepage
    path('freelancer_dashboard/', freelancer_dashboard, name='freelancer_dashboard'),  # For freelancer dashboard
    path('client_dashboard/', client_dashboard, name='client_dashboard'),  # Client dashboard view

    # Client-specific gig detail page
    path('gig/<int:gig_id>/', gig_detail, name='gig_detail'),

    # Freelancer gig management
    path('freelancer/create_gig/', create_gig, name='create_gig'),
    path('freelancer/view_gig/<int:gig_id>/', view_gig, name='view_gig'),
    path('freelancer/edit_gig/<int:gig_id>/edit/', edit_gig, name='edit_gig'),


]
