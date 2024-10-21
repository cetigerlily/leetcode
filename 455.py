class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child_pointer, cookie_pointer = 0, 0
        while child_pointer < len(g) and cookie_pointer < len(s):
            current_child = g[child_pointer]
            current_cookie = s[cookie_pointer]

            if current_cookie >= current_child:
                child_pointer += 1
                cookie_pointer += 1
            else:
                cookie_pointer += 1
        return child_pointer
