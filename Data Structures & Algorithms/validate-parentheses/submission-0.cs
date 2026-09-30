public class Solution {
    public bool IsValid(string s) {
        Dictionary<int,char> openBracket = new Dictionary<int,char>();
        bool result = false;
        char[] charArray = s.ToCharArray();
        for(int i=0;i<s.Length;i++){
            switch (charArray[i]){
                case '(':
                case '[':
                case '{':
                    openBracket[i]=charArray[i];
                break; 
                case ')':
                case '}':
                case ']':
                    if(openBracket.ContainsValue(InvertBracket(charArray[i]))){
                        result=true;
                        var myKey = openBracket.FirstOrDefault(x => x.Value == InvertBracket(charArray[i])).Key;
                        if(myKey>i){
                           return false;
                        }    
                    }
                    break;               
            }           
        }
         return result;
    }
    public char InvertBracket(char bracket){
        switch(bracket){
            case ')':
                return '(';
                break;
            case ']':
                return '[';
                break;
            case '}':
                return '{';
                break;
            default: 
                return 'e';
            break;
        }
    }
}
