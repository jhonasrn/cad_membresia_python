from django.db import models

class Membro(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50)
    situacao_atual = models.CharField(max_length=100)
    aliancado_ativo = models.BooleanField(default=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    naturalidade = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    nacionalidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    telefone_emergencia = models.CharField(max_length=15)
    email = models.EmailField()
    tipo_membro = models.CharField(max_length=100)
    mae = models.CharField(max_length=255)
    pai = models.CharField(max_length=255)
    nome_conjugue = models.CharField(max_length=255, null=True, blank=True)
    data_casamento = models.DateField(null=True, blank=True)
    igreja_batismo = models.CharField(max_length=100)
    data_batismo = models.DateField()
    tipo_admissao = models.CharField(max_length=100)
    pastor_que_batizou = models.CharField(max_length=100)
    data_admissao = models.DateField()
    congregacao = models.CharField(max_length=100)
    funcao_igreja = models.CharField(max_length=100)
    ministerio = models.CharField(max_length=100)
    observacoes = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='fotos_membros/', null=True, blank=True)
    hoje_casamento = models.BooleanField(default=False)
    este_mes_casamento = models.BooleanField(default=False)
    idade_casamento = models.IntegerField(null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    tem_filhos = models.BooleanField(default=False)  # Adicionado o campo 'tem_filhos'
    
    def __str__(self):
        return self.nome

    @property
    def filhos(self):
        return self.filhos.all()  # Relacionamento com os filhos

# Relacionamento de Filho
class Filho(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    membro = models.ForeignKey(Membro, related_name='filhos', on_delete=models.CASCADE)  # Relacionamento com Membro
    
    def __str__(self):
        return self.nome
