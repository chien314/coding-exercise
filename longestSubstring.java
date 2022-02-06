// TC:O(2*n)
// SC:O(min(m,n)), where m is the size of the hashset bounded by the size of the string n and the size of the charset m.

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> distinct = new HashSet<>(); // create a char set array
        int fast = 0;
        int slow = 0;
        int longest = 0;
        
        while (fast < s.length()){
            if (distinct.contains(s.charAt(fast))){
                distinct.remove(s.charAt(slow++));
            }else{
                distinct.add(s.charAt(fast++));
                longest = Math.max(longest,fast-slow);
            }
        }
        return longest;
    }
}
