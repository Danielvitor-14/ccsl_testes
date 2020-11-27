from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class publishedManager(models.Manager):
    '''def get_queryset(self):
        return super(publishedManager,self).get_queryset()\
                                           .filter(status='publicado')'''


class Post(models.Model):# Classe com os posts do django
    # Variavel com opções de 'status'.
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
		
    ) 
	
    titulo = models.CharField(max_length=250) # Acrescentar o campo de preenchimento de texto "normal" com limitação de caractere.
    slug   = models.SlugField(max_length=250) # Acrescentar o campo de preenchimento de texto separado por caractere especifico.
    autor  = models.ForeignKey(User,
                                on_delete=models.CASCADE) #?
    
    conteudo  = models.TextField() # Campo de texto

    publicado = models.DateTimeField(default=timezone.now)
    criado    = models.DateTimeField(auto_now_add=True)
    alterado  = models.DateTimeField(auto_now=True)

    status    = models.CharField(max_length=15,
                                    choices=STATUS,
                                    default='rascunho') # Definir o campo status apartir das opções da variavel 'STATUS'.

    published = publishedManager()

	#def get_absolute_url(self):
	#	return reverse('post_detail',args=[self.pk])

    class Meta:
        ordering = ('publicado',) # Ordenar pelo conteudo do campo status.

    def __str__(self): #?
        return self.titulo




# Create your models here.
