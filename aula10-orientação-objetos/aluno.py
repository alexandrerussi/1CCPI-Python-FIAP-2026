from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplina = {}

    def matricular(self, disciplina: Disciplina):
        """Adicionar a disciplina a lista de disciplinas vinculada ao aluno"""
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Disciplina, nota:float):
        """Adicionar a nota do aluno no dict referente a 1 disciplina"""
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def media_por_d(self, d: Disciplina) -> float:
        notas = self.notas_por_disciplina.get(d.nome, [])
        if not notas:
            return 0
        return sum(notas) / len(notas)

    def media_geral(self) -> float:
        medias_por_disciplina = []
        for d in self.disciplinas:
            media_d = self.media_por_d(d)
            medias_por_disciplina.append(media_d)

        return sum(medias_por_disciplina) / len(medias_por_disciplina)