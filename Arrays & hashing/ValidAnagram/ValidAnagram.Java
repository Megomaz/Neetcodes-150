class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        Map<Character,Integer> checkerS = new HashMap<>();
        Map<Character,Integer> checkerT = new HashMap<>();

        for (int i = 0; i < s.length(); i++){
            checkerS.put(s.charAt(i), checkerS.getOrDefault(s.charAt(i), 0) + 1);
            checkerT.put(t.charAt(i), checkerT.getOrDefault(t.charAt(i), 0) + 1);
        }

        return checkerS.equals(checkerT);
    }
}
