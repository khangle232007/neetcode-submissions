class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = {}
        # sort each string alphabetically and group them into groups
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word not in diction:
                diction[sorted_word] = [strs[i]]
            else:     
                diction[sorted_word].append(strs[i])
        
        #extract the key based on the values of each keys
        return list(diction.values())
            

            