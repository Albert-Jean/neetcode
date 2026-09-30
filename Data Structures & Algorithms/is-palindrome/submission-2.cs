public class Solution {
    public bool IsPalindrome(string s) {
        bool result=false;      
        s=s.ToLower();
        s=Regex.Replace(s, "[^\\w\\._]", "");
          if(s.Length==1){
            return true;
        }
        s=s.Replace(" ",string.Empty);//remove whitespace
        char[] charArray = s.ToCharArray();
        for(int i=0; i<s.Length/2;i++){
            if(charArray[i]==charArray[(s.Length-1)-i]){            
             result =true;
            }
            else{
                return false;
            }
        }
        return result;
    }
}
