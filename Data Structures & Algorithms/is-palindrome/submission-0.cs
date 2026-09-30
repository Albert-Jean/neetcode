public class Solution {
    public bool IsPalindrome(string s) {
        bool result=false;
        s=s.ToLower();
        s=s.Replace(" ",string.Empty);//remove whitespace
        s=Regex.Replace(s, "[^\\w\\._]", "");
        char[] charArray = s.ToCharArray();
        for(int i=0; i<s.Length/2;i++){
            if(charArray[i]==charArray[(s.Length-1)-i]){
             Console.WriteLine("DEBUT_"+charArray[i]+"_FIN"+charArray[(s.Length-1)-i]);
             result =true;
            }
            else{
                return false;
            }
        }
        Console.WriteLine(s);
        return result;
    }
}
