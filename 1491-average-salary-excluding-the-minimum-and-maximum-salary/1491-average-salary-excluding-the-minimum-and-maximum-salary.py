class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        son = sum(salary)-min(salary)-max(salary)
        return son/float((len(salary)-2))