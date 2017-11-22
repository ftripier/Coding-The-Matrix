def structure_voting(politician):
  split = politician.strip().split()
  return {
    "name": split[0],
    "affiliation": split[1],
    "state": split[2],
    "voting_record": [int(x) for x in split[3:]]
  }

def create_voting_dict():
  f = open('voting_record_dump109.txt')
  voting_list = list(f)
  structured = [structure_voting(politician) for politician in voting_list]
  politician_map = {politician["name"]: politician for politician in structured}
  return politician_map

def dot_product(a, b):  
  return sum([c * d for (c, d) in zip(a, b)])

def policy_compare(sen_a, sen_b, voting_dict):
  voting_a = voting_dict[sen_a]["voting_record"]
  voting_b = voting_dict[sen_b]["voting_record"]
  return dot_product(voting_a, voting_b)

def most_similar(to_sen, voting_dict):
  to_sen_voting = voting_dict[to_sen]["voting_record"]

  highest_similarity = float('-inf')
  most_similar_senator = None
  for senator in voting_dict:
    if senator == to_sen:
      continue
    compare_voting = voting_dict[senator]["voting_record"]
    compared = dot_product(to_sen_voting, compare_voting)
    if compared > highest_similarity:
      highest_similarity = compared
      most_similar_senator = senator

  return most_similar_senator

def least_similar(to_sen, voting_dict):
  to_sen_voting = voting_dict[to_sen]["voting_record"]

  least_similarity = float('inf')
  most_similar_senator = None
  for senator in voting_dict:
    if senator == to_sen:
      continue
    compare_voting = voting_dict[senator]["voting_record"]
    compared = dot_product(to_sen_voting, compare_voting)
    if compared < least_similarity:
      least_similarity = compared
      most_similar_senator = senator

  return most_similar_senator

def find_average_similarity(sen, sen_set, voting_dict):
  if len(sen_set) == 0:
    return 0.0
  similarities = [
    dot_product(voting_dict[sen]["voting_record"], voting_dict[compare_sen]["voting_record"]) for compare_sen in sen_set
  ]
  return sum(similarities)/len(similarities)

def vector_addition(a, b):
  added = [c + d for (c, d) in zip(a, b)]
  longer = a if len(a) > b else b
  return added + longer[len(added):]

def find_average_record(sen_set, voting_dict):
  vectors = [voting_dict[sen]["voting_record"] for sen in voting_dict]
  if len(vectors) == 0:
    return 0

  accumulated = []
  for vec in vectors:
    accumulated = vector_addition(accumulated, vec)
  return sum(accumulated)/len(vectors)

def bitter_rivals(voting_dict):
  lowest_agreement = float('inf')
  rivals_pair = None
  for sen in voting_dict:
    sen_voting = voting_dict[sen]["voting_record"]
    for compared in voting_dict:
      compared_voting = voting_dict[compared]["voting_record"]
      similarity = dot_product(sen_voting, compared_voting)
      if similarity < lowest_agreement:
        lowest_agreement = similarity
        rivals_pair = (sen, compared)
  
  return rivals_pair
      
    
