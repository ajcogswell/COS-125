import random as ran
# File: ajCogswell_election.py
# Author: Aj Cogswell
# Date: 11/1/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: aks user for voters and candidates. assigns each candidate a vote from each voter between
# 1-5. Lowest vote wins.
# Collaborations: None
NUMCANDIDATES = 5

def main():
    numVoters, candidates, rankChoices = electionSetup()
    voteList = votingRecord(numVoters, candidates)
    voteList = generateVoteID(voteList)
    voteList = generateRankChoice(voteList, rankChoices)
    candidateDict = calcVotes(candidates, voteList)
    findWinningCandidate(candidateDict)
    reSim()

def electionSetup():
    numVoters = int(input("How many voters are in the pool: \n"))
    candidates = []
    rankChoices = []
    for i in range(0, NUMCANDIDATES):
        rankChoices.append(i+1)
    for i in range(NUMCANDIDATES):
        canName = input(f"What is the name of candidate {i+1}")
        candidates.append(canName)
    return numVoters, candidates, rankChoices

def votingRecord(voters, candidates):
    voteList = []
    for i in range(voters):
        voterDict = {}
        voterDict['voteID'] = 0
        for i in candidates:
            voterDict[i] = 0
        voteList.append(voterDict)
    return voteList

def generateVoteID(voteList):
    voteID = 0
    for i in voteList:
        voteID = ran.randint(0,100000000)
        if i["voteID"] == voteID:
            voteID = ran.randint(0,100000000)
        i["voteID"] = voteID
    return(voteList)
    
def generateRankChoice(voteList, rankChoices):
    for i in voteList:
        votes = list(rankChoices)
        ran.shuffle(votes) 
        listPos = 0
        for j in i:
            if j != 'voteID':
                i[j] = votes[listPos]
                listPos +=1
    return(voteList)

def calcVotes(candidates, voteList):
    candidateDict = {}
    for i in candidates:
        candidateDict[i]=0
    
    for i in voteList:
        for j in i:
            if j != 'voteID':
                rankedVote = i[j]
                candidateDict[j] += rankedVote
    return(candidateDict)

def findWinningCandidate(candidateDict):
    winningScore = 0
    winningName = None

    for i in candidateDict:
        votes = candidateDict[i]
        votes = int(votes)
        if votes < winningScore or winningScore == 0:
            winningScore = votes
            winningName = i
    print(f"The votes are as follows: {candidateDict}. Lower is better. ")
    print(f"{winningName} won the election with {winningScore} points.")

def reSim():
    replay = None
    replayPrompt = input("Would you like to simulate another election?\n").lower()
    if replayPrompt == 'y' or replayPrompt == 'yes':
        replay = True
    elif replayPrompt == 'n' or replayPrompt == 'no':
        replay = False
    else:
        print("input not recognized.")

    if replay:
        main()

main()