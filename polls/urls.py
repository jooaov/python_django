from django.urls import path

#importar tudo de views
from . import views
#namespace das rotas para diferenciar referencias as rotas
app_name = 'polls'
#definindo lista de urls
#pega as vars recebidas na rota e imprime na tela
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    #recebe variaveis pela url definindo o tipo ou n
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]