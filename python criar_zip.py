import zipfile

# Estrutura de arquivos e conteúdos
estrutura = {
    "sst-gestao-ocupacional/requirements.txt": "django\ndjangorestframework\npsycopg2\n",
    "sst-gestao-ocupacional/README.md": "# Sistema SST - Gestão Ocupacional\n\nBackend em Django com API REST.\n",
    "sst-gestao-ocupacional/sst_system/urls.py": """from django.contrib import admin
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
""",
    # Colaboradores
    "sst-gestao-ocupacional/colaboradores/models.py": """from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    setor = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
""",
    "sst-gestao-ocupacional/colaboradores/serializers.py": """from rest_framework import serializers
from .models import Colaborador

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'
""",
    "sst-gestao-ocupacional/colaboradores/views.py": """from rest_framework import viewsets
from .models import Colaborador
from .serializers import ColaboradorSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
""",
    # Clínicas
    "sst-gestao-ocupacional/clinicas/models.py": """from django.db import models

class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
""",
    "sst-gestao-ocupacional/clinicas/serializers.py": """from rest_framework import serializers
from .models import Clinica

class ClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinica
        fields = '__all__'
""",
    "sst-gestao-ocupacional/clinicas/views.py": """from rest_framework import viewsets
from .models import Clinica
from .serializers import ClinicaSerializer

class ClinicaViewSet(viewsets.ModelViewSet):
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer
""",
    # Exames e ASO
    "sst-gestao-ocupacional/exames/models.py": """from django.db import models
from colaboradores.models import Colaborador
from clinicas.models import Clinica

class Exame(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    data = models.DateField()

    def __str__(self):
        return f"{self.tipo} - {self.colaborador.nome}"

class ASO(models.Model):
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='aso/')
    validade = models.DateField()

    def __str__(self):
        return f"ASO - {self.exame.colaborador.nome}"
""",
    "sst-gestao-ocupacional/exames/serializers.py": """from rest_framework import serializers
from .models import Exame, ASO

class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = '__all__'

class ASOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ASO
        fields = '__all__'
""",
    "sst-gestao-ocupacional/exames/views.py": """from rest_framework import viewsets
from .models import Exame, ASO
from .serializers import ExameSerializer, ASOSerializer

class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer

class ASOViewSet(viewsets.ModelViewSet):
    queryset = ASO.objects.all()
    serializer_class = ASOSerializer
""",
    # Documentos
    "sst-gestao-ocupacional/documentos/models.py": """from django.db import models
from colaboradores.models import Colaborador

class PGR(models.Model):
    setor = models.CharField(max_length=100)
    riscos = models.TextField()
    medidas = models.TextField()

    def __str__(self):
        return f"PGR - {self.setor}"

class PCMSO(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    exames = models.ManyToManyField('exames.Exame')
    vinculo_pgr = models.ForeignKey(PGR, on_delete=models.CASCADE)

    def __str__(self):
        return f"PCMSO - {self.colaborador.nome}"
""",
    "sst-gestao-ocupacional/documentos/serializers.py": """from rest_framework import serializers
from .models import PGR, PCMSO

class PGRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGR
        fields = '__all__'

class PCMSOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCMSO
        fields = '__all__'
""",
    "sst-gestao-ocupacional/documentos/views.py": """from rest_framework import viewsets
from .models import PGR, PCMSO
from .serializers import PGRSerializer, PCMSOSerializer

class PGRViewSet(viewsets.ModelViewSet):
    queryset = PGR.objects.all()
    serializer_class = PGRSerializer

class PCMSOViewSet(viewsets.ModelViewSet):
    queryset = PCMSO.objects.all()
    serializer_class = PCMSOSerializer
"""
}

# Criar o ZIP
with zipfile.ZipFile("sst-gestao-ocupacional.zip", "w") as zipf:
    for caminho, conteudo in estrutura.items():
        zipf.writestr(caminho, conteudo)

print("✅ Pacote ZIP criado: sst-gestao-ocupacional.zip")git add .
git commit -m "Upload do backend completo SST"
git push origin main
