class Solution(object):
    def replaceWords(self, dictionary, sentence):
        data = {}
        for x in dictionary:
            ch = x[0]
            if ch not in data:
                data[ch] = [x]
            else:
                data[ch].append(x)
                data[ch].sort(key=len)
        string = sentence.split(" ")
        for x in range(len(string)):
            if string[x][0] in data:
                arr = data[string[x][0]]
                for y in arr:
                    if y in string[x]:
                        string[x] = y
                        break
        return " ".join(x for x in string)


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
        

sol = Solution()
print(sol.replaceWords(dictionary,sentence))