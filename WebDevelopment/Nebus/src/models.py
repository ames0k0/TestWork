from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Organization(Base):
    __tablename__ = "organization"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    # Relations
    building: Mapped["Building"] = relationship(back_populates="organization")
    activities: Mapped[list["Activity"]] = relationship()

    def __repr__(self) -> str:
        return f"Организация(id={self.id}, name={self.name})"


class Building(Base):
    __tablename__ = "building"

    address: Mapped[str]
    longitude: Mapped[int]
    latitude: Mapped[int]

    # Relations
    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organization.id"),
        primary_key=True,
    )
    organization: Mapped["Organization"] = relationship(back_populates="building")

    def __repr__(self) -> str:
        return f"Здания(address={self.address})"


class Activity(Base):
    __tablename__ = "activity"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    depth: Mapped[int]

    # Relations
    parent_id: Mapped[int] = mapped_column(ForeignKey("node.id"))
    children = relationship("Activity", lazy="joined", join_depth=3)
    organization_id: Mapped[int] = mapped_column(ForeignKey("Organization.id"))

    def __repr__(self) -> str:
        return f"Деятельность(address={self.name})"
