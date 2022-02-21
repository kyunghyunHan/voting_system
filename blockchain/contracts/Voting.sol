pragma solidity ^0.4.24;

/**
 * The contractName contract does this and that...
 */
contract Voting {

	struct Election {
		uint uid;
		string title;
		uint start_time;
		uint end_time;
		bool doesExist;
		uint totalVotesCount;
		uint candidatesNum;
	}

	struct Voter {
		uint uid;
		uint candidateID;
		uint electionID;
	}

	struct Candidate {
		uint uid;
		string name;
		string major;
		bool doesExist;
		uint electionID;
		uint theTotalVotes;
	}

	mapping(uint => Election) elections;
	mapping(uint => Candidate) candidates;
	mapping(uint => Voter) voters;

	uint lastElectionId;
	uint lastVoterId;
	uint lastCandidateId;


	function addElection(uint uid, string title, uint start_time, uint end_time) public {
		elections[uid] = Election(uid,title,start_time,end_time,true,0,0);
		lastElectionId = uid;
	}

	function addCandidate(uint uid, string name, string major, uint electionId) public {
		candidates[uid] = Candidate(uid, name,major,true,electionId,0);
		elections[electionId].candidatesNum = elections[electionId].candidatesNum+1;
		lastCandidateId = uid;
	}

	function vote(uint uid, uint candidateId , uint electionId) public {
		if(elections[electionId].doesExist == true && candidates[candidateId].doesExist ==true) {
			voters[uid] = Voter(uid,candidateId, electionId);
			elections[electionId].totalVotesCount = elections[electionId].totalVotesCount++;
			candidates[candidateId].theTotalVotes = candidates[candidateId].theTotalVotes++;
			lastVoterId = uid;
		}
	}

	function getNumOfCandidates(uint electionId) public view returns(uint) {
		return elections[electionId].candidatesNum;
	}

	function getNumOfVoters(uint electionId) public view returns(uint) {
		return elections[electionId].totalVotesCount;
	}

	function getElection(uint electionId) public view returns(uint, string, uint, uint, uint, uint) {
		return (elections[electionId].uid, elections[electionId].title, elections[electionId].start_time, elections[electionId].end_time, elections[electionId].totalVotesCount, elections[electionId].candidatesNum);
	}

	function getCandidate(uint candidateId) public view returns(uint, string, string, uint, uint) {
		return (candidates[candidateId].uid, candidates[candidateId].name, candidates[candidateId].major, candidates[candidateId].electionID,candidates[candidateId].theTotalVotes);
	}

	function getVote(uint voteId) public view returns(uint, uint, uint) {
		return (voters[voteId].uid, voters[voteId].candidateID, voters[voteId].electionID);
	}

	function getLastElectionId() public view returns(uint) {
		return lastElectionId;
	}

	function getLastVoterId() public view returns(uint) {
		return lastVoterId;
	}

	function getLastCandidateId() public view returns(uint) {
		return lastCandidateId;
	}

	function getLastElection() public view returns(uint, string, uint, uint, uint, uint) {
		return (elections[lastElectionId].uid, elections[lastElectionId].title, elections[lastElectionId].start_time, elections[lastElectionId].end_time, elections[lastElectionId].totalVotesCount, elections[lastElectionId].candidatesNum);
	}

	function getLastCandidate() public view returns(uint, string, string, uint, uint) {
		return (candidates[lastCandidateId].uid, candidates[lastCandidateId].name, candidates[lastCandidateId].major, candidates[lastCandidateId].electionID,candidates[lastCandidateId].theTotalVotes);
	}

	function getLastVoter() public view returns(uint, uint, uint) {
		return (voters[lastVoterId].uid, voters[lastVoterId].candidateID, voters[lastVoterId].electionID);
	}
}
