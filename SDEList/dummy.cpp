#include <vector>
#include <unordered_set>
using namespace std;
class Solution {
public:
    vector<pair<int, int>> directions = {
        {1, 0},
        {0, 1},
        {-1, 0},
        {0, -1},
    };
    long long prime =31;
    long long mod =1e9+7; 
    long long hash_word(string &s){
        long long sum=0;
        long long p=1;
        for(int i=0;i<s.length();i++){
            sum=(sum+s[i]*p)%mod;
            p=(p*prime)%mod;
        }
        return sum;
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        int n=board.size();
        int m=board[0].size();
        set<int> store;
        unordered_set<long long> wanted_words;
        unordered_set<long long> possible_prefixes;
        unordered_map<long long, string> rev_map;
        unordered_set<long long> found_words;
        for(auto &word : words){
            wanted_words.insert(hash_word(word));
            rev_map[hash_word(word)]=word;
            string prefix;
            for(int i=0;i<word.length();i++){
                prefix+=word[i];
                possible_prefixes.insert(hash_word(prefix));
            }
        }
        vector<vector<bool>> visited(n, vector<bool>(m));
        function<void(int, int, long long, long long, string)> dfs = [&](int i, int j, long long val, long long prime_mul, string pp){
            cout<<i<<" "<<j<<" "<<val<<" "<<prime_mul<<" "<<pp<<endl;
            visited[i][j]=true;
            if(wanted_words.find(val)!=wanted_words.end()){
                cout<< rev_map[val] <<endl;
                found_words.insert(val);
            }
            if(possible_prefixes.find(val)==possible_prefixes.end()){
                cout<<"gotcha "<<val<<" "<<pp<<endl;
                return;
            }
            for(auto d : directions){
                int new_i = d.first+i;
                int new_j = d.second+j;
                if(new_i>=0 and new_i<n and new_j>=0 and new_j<m and !visited[new_i][new_j]){
                    cout<<"inside "<<val<<" "<<" "<<board[i][j]*prime_mul<<" "<<(val+1ll*board[i][j]*prime_mul)%mod<<" "<<pp+board[new_i][new_j]<<endl;
                    dfs(new_i, new_j, (val+1ll*board[i][j]*prime_mul)%mod, (1ll*prime_mul*prime)%mod, pp+board[new_i][new_j]);
                }
            }
            visited[i][j]=false;
        };
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                string s;
                s+=board[i][j];
                cout<<"start "<<(int)board[i][j]<<" "<<prime<<" "<<(board[i][j])%mod<<endl;
                dfs(i, j, (1ll*board[i][j])%mod, (1ll*prime)%mod, s);
            }
        }
        vector<string> answer;
        for(auto &word : words){
            long long h = hash_word(word);
            if(found_words.find(h)!=found_words.end()){
                answer.push_back(word);
            }
        }
        return answer;
    }
};