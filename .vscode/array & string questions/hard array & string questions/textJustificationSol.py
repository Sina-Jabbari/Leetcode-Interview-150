class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        buffer = []
        buflen = 0
        for word in words:
            #check if adding word exceeds maxWidth
            if buflen + len(buffer) + len(word) > maxWidth:
                #add spaces evenly
                for n in range(maxWidth - buflen): #for the difference between current buffer and max of buffer will be filled with spaces
                    if len(buffer) == 1:##edge case
                        buffer[0] += ' '
                    else:       
                        buffer[n % (len(buffer) - 1)] += ' '
                        #this will go into each space between words as n loops, keeping the distribution open
            
                #add buffer to result
                result.append(''.join(buffer))
                #reset buf
                buffer, buflen = [], 0
            
            #add word to buffer
            buffer.append(word)
            buflen += len(word)

        #last line gets cut off, handle this case:
        result.append(' '.join(buffer).ljust(maxWidth))

        return result
