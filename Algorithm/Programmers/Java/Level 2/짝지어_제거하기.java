import java.util.Stack;
class Solution
{
    Stack<Character> stk = new Stack();
    public int solution(String s)
    {
        for(char c : s.toCharArray()) {
            if(stk.empty()) {
                stk.add(c);
                continue;
            }
            
            if(stk.peek().equals(c)) {
                stk.pop();
                continue;
            }
                       
            stk.add(c);
        }

        return stk.empty() ? 1 : 0;
    }
}