from django.db import models

class Editora(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    class Meta:
        indexes = [models.Index(fields=['nome'], name="idx_editora_nome")]  
        ordering = ['nome']
        db_table = 'editora'
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'livros': [livro.to_dict() for livro in self.livros.all()]
        }
    def clean(self):
        if not self.nome:
            raise ValueError("O nome é obrigatório.")
        if len(self.nome)<3:
            raise ValueError("O nome deve ter ao menos 3 caracteres.")

    def __str__(self):
        return self.nome