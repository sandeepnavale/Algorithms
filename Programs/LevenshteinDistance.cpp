#include <algorithm>
#include <iostream>
using namespace std;

// len_s and len_t are the number of characters in string s and t respectively
int LevenshteinDistance(const char *s, int len_s, const char *t, int len_t) {
  int cost;

  /* base case: empty strings */
  if (len_s == 0)
    return len_t;
  if (len_t == 0)
    return len_s;

  /* test if last characters of the strings match */
  if (s[len_s - 1] == t[len_t - 1])
    cost = 0;
  else
    cost = 1;

  /* return minimum of delete char from s, delete char from t, and delete char
   * from both */
  return min(min(LevenshteinDistance(s, len_s - 1, t, len_t) + 1,
                 LevenshteinDistance(s, len_s, t, len_t - 1) + 1),
             LevenshteinDistance(s, len_s - 1, t, len_t - 1) + cost);
};

int main() {
  char *s, *t;
  int slen, tlen;

  s = "ABC";
  slen = strlen(s);
  t = "ABDDD";
  tlen = strlen(t);
  cout <<"This needs  "<< LevenshteinDistance(s, slen, t, tlen)<<" Changes";

}
