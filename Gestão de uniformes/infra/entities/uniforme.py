from __future__ import annotations
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base


class Uniforme(Base):
    __tablename__ = 'uniformes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(unique=True, nullable=False)
    ativo: Mapped[bool] = mapped_column(default=True, nullable=False)
    emprestimos = relationship("Empretimo", back_populates="uniforme", cascade="save-update")

    def __repr__(self):
        return f'Uniforme[nome= {self.nome}].'
