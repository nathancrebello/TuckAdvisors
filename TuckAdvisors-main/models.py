from sqlalchemy import Integer, Text, Column
from db import Base

# model representing gptOutput table
class gptOutput(Base):
    __tablename__ = "gptOutput"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable = False) 