# 692. Top K Frequent Words
# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
#
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.

# 思路
# 可以看到，本题有两个排序关键字：
#
# 词频 倒序排列
# 若词频相同，按字母顺序排序 正序排列
# 接下来我们看看如何在python里一次对两个关键字进行排序

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        hash = collections.Counter(words)
        res = sorted(hash, key=lambda word:(-hash[word], word))
        return res[:k]

# 用小顶堆维护，统计词频，用类封装词和词频，重写运算符

import heapq, collections

class Word:
    def __init__(self, word, fre):
        self.word = word
        self.fre = fre
    def __lt__(self, other):
        if self.fre != other.fre:
            return self.fre < other.fre
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = collections.Counter(words)
        heap = []

        for word, fre in cnt.items():
            heapq.heappush(heap, Word(word, fre))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(reverse=True)
        return [x.word for x in heap]
