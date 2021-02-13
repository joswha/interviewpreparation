def printParenthesis(string, n): 
    if(n > 0): 
        paren(string, 0, n, 0, 0)
  
def paren(string, pos, n, left, right): 
      
    if(right == n): 
        for i in string: 
            print(i, end = "") 
        print()
        return
    else: 
        if(left > right): 
            string[pos] = ')'
            paren(string, pos + 1, n, left, right + 1)
        if(left < n): 
            string[pos] = '('
            paren(string, pos + 1, n, left + 1, right) 
  
n = 3
string = [""] * 2 * n
printParenthesis(string, n)