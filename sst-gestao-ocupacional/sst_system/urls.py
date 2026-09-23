from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from colaboradores.views import ColaboradorViewSet
from clinicas.views import ClinicaViewSet
from exames.views import ExameViewSet, ASOViewSet
from documentos.views import PGRViewSet, PCMSOViewSet

router = routers.DefaultRouter()
router.register(r'colaboradores', ColaboradorViewSet)
router.register(r'clinicas', ClinicaViewSet)
router.register(r'exames', ExameViewSet)
router.register(r'aso', ASOViewSet)
router.register(r'pgr', PGRViewSet)
router.register(r'pcmso', PCMSOViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
