class Solution(object):
    def replaceWords(self, dictionary, sentence):
        data = set(dictionary)
        string = sentence.split()
        result = []
        for word in string:
            found = False
            for i in range(len(word)+1):
                prefix = word[:i]
                if prefix in data:
                    result.append(prefix)
                    found = True
                    break
            if not found:
                result.append(word)
            
            
        
        return " ".join(x for x in result)


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
        

sol = Solution()
print(sol.replaceWords(dictionary,sentence))