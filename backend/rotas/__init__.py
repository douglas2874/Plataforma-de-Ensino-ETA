from .rota_usuarios import usuarios_bp
from .rota_turmas import turma_bp
from .rota_aulas import aulas_bp
from .rota_atividades import atividades_bp
from.rota_teste import teste_bp

blueprints = [usuarios_bp, teste_bp, turma_bp, aulas_bp, atividades_bp]