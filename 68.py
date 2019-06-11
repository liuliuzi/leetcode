class  Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        _lenth =len(words)
        i=0
        retArr=[]
        newlineStartIndex=0
        
        newlineLen=0
        def processNewLine(newlineStartIndex,i):
            newlineArr=words[newlineStartIndex:i]
            #print "processNewLine",newlineArr
            wordlen=0
            for x in newlineArr:
                wordlen=wordlen+len(x)
            spaceNum=len(newlineArr)-1
            if spaceNum!=0:
                basicSpaceLen=(maxWidth-wordlen)/spaceNum
                additionSpaceLen=(maxWidth-wordlen)%spaceNum
            else:
                basicSpaceLen=maxWidth-wordlen
                additionSpaceLen=0
            #print wordlen,(maxWidth-wordlen),spaceNum,basicSpaceLen,additionSpaceLen
            retStr=""

            for i in range(len(newlineArr)):
                retStr=retStr+newlineArr[i]
                if i!=len(newlineArr)-1 and spaceNum!=0: #not need handle last words space           
                    if i<=additionSpaceLen-1:
                        retStr=retStr+"*"+ basicSpaceLen*"*"
                    else:
                        retStr=retStr+ basicSpaceLen*"*"
                elif spaceNum==0:
                    retStr=retStr+ basicSpaceLen*"*"
                    

            #print "processNewLine result :",retStr
            return retStr

        #print range(_lenth)
        for i in range(_lenth):
            #print "i:",i
            if newlineLen+1+len(words[i])>maxWidth:
                #print "prepea",newlineStartIndex,i
                retArr.append(processNewLine(newlineStartIndex,i))
                newlineStartIndex=i
                newlineLen=0
                if i==_lenth-1:
                    retArr.append(processNewLine(newlineStartIndex,i+1))
            else:
                #print "else"
                newlineLen=newlineLen+1+len(words[i])

        return retArr


sol=Solution()
for x in sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16):
    print x
