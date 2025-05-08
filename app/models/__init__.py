from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from .user import User


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    role = Column(String)  # 'admin' or 'customer'

    subscription = relationship("Subscription", back_populates="user", uselist=False)
    usage = relationship("Usage", back_populates="user")


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)

    subscriptions = relationship("Subscription", back_populates="plan")
    permissions = relationship("Permission", back_populates="plan")


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    endpoint = Column(String)
    description = Column(String)
    plan_id = Column(Integer, ForeignKey("plans.id"))

    plan = relationship("Plan", back_populates="permissions")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan_id = Column(Integer, ForeignKey("plans.id"))

    user = relationship("User", back_populates="subscription")
    plan = relationship("Plan", back_populates="subscriptions")


class Usage(Base):
    __tablename__ = "usage"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    endpoint = Column(String)
    count = Column(Integer, default=0)
    restricted = Column(Boolean, default=False)

    user = relationship("User", back_populates="usage")
