'''
For example,

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
1
2
Corner Cases:

Did you consider the case where path = “/../”? 
In this case, you should return “/”.

Another corner case is the path might contain multiple slashes ‘/’ together, such as “/home//foo/”. 
In this case, you should ignore redundant slashes and return “/home/foo”.
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = list()
        pathArr = path.split('/')
        for dir in pathArr:
            if not dir or dir == '.':
                continue
            if dir == '..':
                if stack:
                    stack.pop()
            else:                
                stack.append(dir)
        return '/' + '/'.join(stack)

sol=Solution()
print sol.simplifyPath("/a/./b/../../c/")