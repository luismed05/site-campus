from django.db import models
from modelchoices import Choices


# model de Post
class Post(models.Model):

    titulo = models.CharField(max_length=100)

    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)

    conteudo = models.TextField(max_length=1000)

    post_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__ (self):
        return self.titulo

    def get_asolute_url(self):
        return reverse ('detalhe_post', args=[str(self.id)])


# model de Autor   

class Autor(models.Model):

    SEMESTRE_CHOICES = (
        ('1' , '2019/1'),
        ('2' , '2018/2'),
        ('3' , '2018/1'),
        ('4' , '2017/2'),
    )

    autor_avatar = models.ImageField(upload_to='assets/images', blank=True, null=True)

    primeiro_nome = models.CharField(max_length=100)

    sobrenome = models.CharField(max_length=100)

    nome_completo = models.CharField(max_length=100)

    semestre = models.CharField(max_length=1, choices=SEMESTRE_CHOICES, blank=False, null=False)

    class Meta:
        ordering = ['primeiro_nome', 'sobrenome']

    def get_absolute_url(self):
        return reverse('detalhe_autor', args=[str(self.id)])

    def __str__(self):
        return f'{self.primeiro_nome} {self.sobrenome}'
