def multiziperator(*args):
  for one_item in zip(*args):
    for each_one in one_item:
      yield each_one