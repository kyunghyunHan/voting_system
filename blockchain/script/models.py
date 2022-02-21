from sqlalchemy import Column, Integer, String, FetchedValue
from database import Base

class Election(Base):
	__tablename__ = "elections"

	title = Column(String(255))
	major = Column(String(255))
	college = Column(String(255))
	content = Column(String(255))
	election_start_time = Column(String(255))
	election_end_time = Column(String(255))
	state = Column(Integer, server_default=FetchedValue())
	id = Column(Integer, primary_key=True)
	admin_id = Column(String(255))

class Candidate(Base):
	__tablename__ = 'candidates'

	student_id = Column(String(255))
	name = Column(String(255))
	major = Column(String(255))
	college = Column(String(255))
	thumbnail = Column(String(255))
	resume = Column(String(255))
	id = Column(Integer, primary_key=True)
	election_id = Column(Integer)


class Voting(Base):
	__tablename__ = 'votings'

	id = Column(Integer, primary_key=True)
	candidate_id = Column(Integer)
	election_id = Column(Integer)
	auto_hash = Column(String(255))