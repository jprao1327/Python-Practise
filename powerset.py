def get_power_set(s):
  power_set=[[]]
  for elem in s:
    # iterate over the sub sets so far
    for sub_set in power_set:
      # add a new subset consisting of the subset at hand added elem to it
      # effectively doubling the sets resulting in the 2^n sets in the powerset of s.
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set
get_power_set([1,2,3])  
  
