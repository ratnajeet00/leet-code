class Solution {
public:
    int countSeniors(vector<string>& details) {
        int count = 0;
        for (const string& detail : details) {
            // Extract the age from the 11th and 12th characters (0-indexed)
            int age = stoi(detail.substr(11, 2));
            
            // Check if the age is strictly more than 60
            if (age > 60) {
                count++;
            }
        }
        return count;
    }
};
