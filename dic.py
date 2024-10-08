from collections import defaultdict

class Dict:
  def __init__(self, dic):
    words = open(dic).read().splitlines()

    self.dict = defaultdict(lambda: False)
    
    for word in words:
      self.dict[word] = True

  def is_valid_word(self, word):
    return self.dict[word]
