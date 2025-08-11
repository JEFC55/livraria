from django.db import models

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    class Meta:
        db_table = 'autor' #nome da tabela
        ordering = ['nome'] # ordenação padrão
        indexes = [models.Index(fields=['nome'], name="idx_autor_nome")]#indices https://www.mongodb.com/pt-br/docs/manual/indexes/
    def to_dict(self):
        return {
            'id': self.id,
            'nome':self.nome,
            'livros': [livro.to_dict() for livro in self.livros.all()]
        }
        
    def clean(self):
        if not self.nome:
            raise ValueError("O nome é obrigatório.")
        if len(self.nome)<3:
            raise ValueError("O nome deve ter ao menos 3 caracteres.")
        
    def __str__(self):
        return self.nome
