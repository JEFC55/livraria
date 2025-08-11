from django.db import models
import datetime
from autor.models import Autor
from editora.models import Editora
class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, related_name='livros', on_delete=models.CASCADE)
    descricao = models.TextField()
    data_lancamento = models.DateField()
    editora = models.ForeignKey(Editora, related_name='livros', on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        autor= kwargs.pop('autor', None)
        super().__init__(*args, **kwargs)
        if autor:
            self.autor = autor
            
    class Meta:
        ordering = ["titulo"]
        db_table = 'tb_livro'
        constraints = [
            models.UniqueConstraint(fields=['titulo', 'autor'], name='unique_titulo_autor')
        ]
        
    def to_dict(self):
        self= self
        return {
            'id': self.id,
            'titulo':self.titulo,
            'editora':self.editora.nome,
            'data_lancamento':self.data_lancamento,
        }
        
    def clean(self):
        if not self.data_lancamento:
            self.data_lancamento =datetime.now().date()
        if not self.titulo:
            raise ValueError("O titulo é obrigatório.")#raise acaba com o metodo a partir da classe que o puxa
        if not self.autor:
            raise ValueError("O autor é obrigatório.")
        
    def __str__(self):
        return self.titulo
