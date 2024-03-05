class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        index = 0
        needleStart = needle[0]

        while (index < len(haystack)):
            if haystack[index] == needleStart:
                if self.checkPresence(haystack[index:], needle):
                    return index

            index += 1

        return -1

    def checkPresence(self, shortenedHaystack, needle):
        if len(needle) > len(shortenedHaystack):
            return False

        for index, char in enumerate(needle):
            if shortenedHaystack[index] != char:
                return False

        return True
