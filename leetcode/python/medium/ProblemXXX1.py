# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
"""
Input: HTML tag string in single line without any spaces

<div><span></p></div>

<div></div><p></p>


Conditions:
1) if valid html, return True
2) if invalid html and it can be fixed by just only 1 change, return the first tag we need to change.
    span


stack = ["div"], remaing string = </div><p></p>
stack = [], remaing string = <p></p>
stack = ["p"], remaing string = </p>
stack = [], remaing string = ""

if len(stack) == 0:
    return True
return stack[-1]


stack = ["div"], remaing string = <span></p></div>
stack = ["div", "span"], remaing string = </p></div>
stack = ["div", "span"], remaing string = </div>

Time: O(n)
Space: O(n/2) -> O(n)
"""
class Solution:
    def validateHtmlTags(self, htmlTags: str) -> str:
        stack = []
        l = len(htmlTags)
        i = 0
        while i < l:
            if htmlTags[i] == "<":
                curr_tag = ""
                i += 1
                isEndTag = htmlTags[i] == "/"
                if isEndTag:
                    i += 1

                while htmlTags[i] != ">":
                    curr_tag += htmlTags[i]
                    i += 1

                if not isEndTag:
                    stack.append(curr_tag)
                elif isEndTag and curr_tag == stack[-1]:
                    stack.pop()
                else:
                    return stack[-1]
            i += 1

        return "true" if len(stack) == 0 else stack[-1]

    def validateHtmlTags2(self, htmlTags: str) -> str:
        # Advanced: for tags including content
        stack = []
        l = len(htmlTags)
        i = 0
        while i < l:
            if htmlTags[i] == "<":
                curr_tag = ""
                i += 1
                isEndTag = htmlTags[i] == "/"
                if isEndTag:
                    i += 1

                while htmlTags[i] != ">":
                    curr_tag += htmlTags[i]
                    i += 1

                # Ignore content
                while i < l and htmlTags[i] != "<":
                    i += 1

                if not isEndTag:
                    stack.append(curr_tag)
                elif isEndTag and curr_tag == stack[-1]:
                    stack.pop()
                else:
                    return stack[-1]
            i += 1

        return "true" if len(stack) == 0 else stack[-1]

# Problem XXX1
# Link: from Ken
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("<div><span></p></div>", "span"),
        ("<div></div><p></p>", "true"),
        ("<div><div><span></p></div></div>", "span"),
        ("<div><span><div></div></p></div>", "span"),
        ("<div></div><div><div></div><p></a></div>", "p"),
        ("<div><div><b></b></div></p>", "div"),
        ("<div></div><p><em><i></b></em></p>", "i")
    ]
    for case, expected in cases:
        if s.validateHtmlTags(case) != expected:
            print(f"Case is: {case}")
            print(f"Expected is: {expected}")
            raise Exception("Wrong Answer")
