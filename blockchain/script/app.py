#-*- coding: utf-8 -*-

from database import session, Base, engine
from models import Election, Candidate, Voting
from web3 import Web3
import json
import time
import datetime
import sys

with open("/home/ubuntu/script/voting/build/contracts/Voting.json", 'r') as f:
		js = json.load(f)
		abi = js['abi']
		address = js['networks']['42']['address']

w3 = Web3(Web3.HTTPProvider("https://kovan.infura.io/v3/613e792e8a704ba1a4e370cf1236e24f"))
# w3.eth.defaultAccount = w3.eth.accounts[0]
w3.eth.defaultAccount = "0xd52Fb557d3f350e88157f89851e98C0368010CF4"

adr = w3.toChecksumAddress(address)
voting = w3.eth.contract(address=adr,abi=abi)

Base.metadata.create_all(bind=engine)

def convertUnix(t):
	return int(time.mktime(datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S").timetuple()))

def addElection():
	lastElectionId = voting.functions.getLastElectionId().call()
	elections = session.query(Election).filter(Election.id > lastElectionId).all()

	for elec in elections:
		tx_hash = voting.functions.addElection(elec.id,elec.title,
			convertUnix(elec.election_start_time),convertUnix(elec.election_end_time))
		tx_hash.transact()

	print(voting.functions.getLastElection().call())

def addCandidate():
	lastCandidateId = voting.functions.getLastCandidateId().call()
	candidates = session.query(Candidate).filter(Candidate.id > lastCandidateId).all()

	for can in candidates:
		tx_hash = voting.functions.addCandidate(can.id, can.name, can.major, can.election_id)
		tx_hash.transact()

	print(voting.functions.getLastCandidate().call())

def vote():
	lastVoterId = voting.functions.getLastVoterId().call()
	votes =session.query(Voting).filter(Voting.id > lastVoterId).all()

	for v in votes:
		tx_hash = voting.functions.vote(v.id, v.candidate_id, v.election_id)
		tx_hash.transact()

	print(voting.functions.getLastVoter().call())

if sys.argv[1] == "election":
	addElection()
elif sys.argv[1] == "candidate":
	addCandidate()
elif sys.argv[1] == "vote":
	vote()



