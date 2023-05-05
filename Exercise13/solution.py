class ThresholdEqual(object):
  threshold = 0

  def __init__(self, x):
    self.x = x

  def __eq__(self, other):
    if isinstance(other, ThresholdEqual) and (abs(self.x - other.x) <= ThresholdEqual.threshold):
      return True
    return False