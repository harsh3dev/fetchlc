**Task:** Generate `Problem JSON` and `Testcase JSON` for LeetCode-style problems based on raw input data.  

### **Instructions:**  
1. You will be provided with **raw and incomplete input data** for generating the `Problem JSON` and `Testcase JSON`.  
2. Your task is to **format and structure** the data according to the required JSON schema.  
3. Ensure that the `Problem JSON` and `Testcase JSON` are always **separate**.  
4. **Strictly follow** the defined fields and format for both JSONs.  
5. The generated JSONs will be used as input for an API to be stored in a database—**consistency and accuracy** are essential.  
6. The `Testcase JSON` must include the example test cases from the problem description, along with additional test cases to ensure robust coverage.
7. Do not include `# Solution\n\n` in starting of the solution string
8. The test cases will never be like 
  ```bash
      n = 4, array = [1, 2, 3, 4]
      n = 3 array = [1, 2, 3]

      or 
      s = "word", k = 2
      s = "animal", k = 1

      rather it would be like
      4
      1 2 3 4
      3
      1 2 3

      and

      word
      2
      animal
      1
  ```
9. Each and every testcase will be in simple string format, so that it could be read from the terminal, be it any data structure required as in the problem description the test case will always be in stdin format.
10. Each defaultCode template for every language will be customised according to the testcase.
11. The main function of the defaultCode will be customised for reading the input as given in the test case input and to print the output as expected in the testcase
12. Keep the solution function of the defaultCode empty without filling in the actual solution ,keep it blank for the user to complete it.
13. if you are given with the main function for any language for the particular problem then use it instead of generating it
14. Also generate the solution of the problem to fill it in the json
15. Include some good edge cases in the testcase and the testcase must be of a balanced type consisting of all kinds of cases including easy, medium and edge cases
16. Add  ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
to the cpp defaultcode for faster execution
17. make sure the input extraction logic handles the input correctly and the output handles the correct precision for example if the output expects 0.0000 precision then the code must handle it

Example of code in python:
```py
from typing import List

def trap(height: List[int]) -> int:
    # Start your code here
    pass

# Do not modify the driver code
if __name__ == "__main__":
    import sys
    input = sys.stdin.read().strip().split("\n")
    height = list(map(int, input[1].split()))
    result = trap(height)
    print(result)

```

Example of code in cpp:
```cpp
#include <iostream>
#include <vector>
using namespace std;

int trap(vector<int>& height) {
    // Start your code here
}

// Do not change the driver code
int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }
    cout << trap(height) << endl;
    return 0;
}
```
18. Make sure to include all the necessary dependencies
19. Also provide the defaultCode and testcases in normal format along with the json to test in the code runner

### Problem JSON Template:
```json
{
  "title": "", // string
  "slug": "", // string
  "description": "", // string type: Markdown format containing problem description, input, output format, example testcases with explanation, constraints
  "difficulty": "E", // Enum type: E-> Easy, M-> Medium, H-> Hard
  "time_limit": 1000, // time limit in milliseconds (integer)
  "memory_limit": 256,
  "likes": 0, // keep this as 0
  "dislikes": 0, // keep this a 0
  "is_premium": false, // keep this as false
  "acceptance_rate": 0.0, // keep this as 0.0
  "related_problems": [], // keep it empty for now
  "solution": "", // solution  is of string type in markdown format, containing a structured solution to the problem with approach, code, complexity
  "topicTags": ["",""], // array of strings
  "hints": [""], // array of strings
  "default_code_templates": {
    "py": "", // default starting code with function declaration and main function with stdin/stdout,
    "cpp": "", // default starting code with function declaration and main function with stdin/stdout
  }
}
```

### Example Problem:
```json
{
  "title": "Merge Strings Alternately",
  "slug": "merge-strings-alternately",
  "description": "<p>You are given two strings <code>word1</code> and <code>word2</code>. Merge the strings by adding letters in alternating order, starting with <code>word1</code>. If a string is longer than the other, append the additional letters onto the end of the merged string.</p>\r\n\r\n<p>Return <em>the merged string.</em></p>\r\n\r\n<p>&nbsp;</p>\r\n<p><strong class=\"example\">Example 1:</strong></p>\r\n\r\n<pre>\r\n<strong>Input:</strong> word1 = &quot;abc&quot;, word2 = &quot;pqr&quot;\r\n<strong>Output:</strong> &quot;apbqcr&quot;\r\n<strong>Explanation:</strong>&nbsp;The merged string will be merged as so:\r\nword1:  a   b   c\r\nword2:    p   q   r\r\nmerged: a p b q c r\r\n</pre>\r\n\r\n<p><strong class=\"example\">Example 2:</strong></p>\r\n\r\n<pre>\r\n<strong>Input:</strong> word1 = &quot;ab&quot;, word2 = &quot;pqrs&quot;\r\n<strong>Output:</strong> &quot;apbqrs&quot;\r\n<strong>Explanation:</strong>&nbsp;Notice that as word2 is longer, &quot;rs&quot; is appended to the end.\r\nword1:  a   b \r\nword2:    p   q   r   s\r\nmerged: a p b q   r   s\r\n</pre>\r\n\r\n<p><strong class=\"example\">Example 3:</strong></p>\r\n\r\n<pre>\r\n<strong>Input:</strong> word1 = &quot;abcd&quot;, word2 = &quot;pq&quot;\r\n<strong>Output:</strong> &quot;apbqcd&quot;\r\n<strong>Explanation:</strong>&nbsp;Notice that as word1 is longer, &quot;cd&quot; is appended to the end.\r\nword1:  a   b   c   d\r\nword2:    p   q \r\nmerged: a p b q c   d\r\n</pre>\r\n\r\n<p>&nbsp;</p>\r\n<p><strong>Constraints:</strong></p>\r\n\r\n<ul>\r\n\t<li><code>1 &lt;= word1.length, word2.length &lt;= 100</code></li>\r\n\t<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>\r\n</ul>",
  "difficulty": "E",
  "time_limit": 1000,
  "memory_limit": 256,
  "likes": 0,
  "dislikes": 0,
  "is_premium": false,
  "acceptance_rate": 0.0,
  "related_problems": [],
  "solution": "# Solution\n\n## Approach\nWe are tasked with merging two strings `word1` and `word2` by adding letters in alternating order. The approach is straightforward:\n\n1. Use two pointers — one for each string.\n2. Start with the first character of `word1`, then the first character of `word2`, and continue this process.\n3. If one string ends before the other, append the remaining characters of the longer string to the merged string.\n\n### Intuition\n- Since both strings are relatively small (max length = 100), a simple two-pointer technique is efficient.\n- The problem is reduced to iterating through both strings while checking for boundaries.\n\n### Complexity Analysis\n**Time Complexity:** `O(n + m)` where `n` and `m` are lengths of `word1` and `word2` respectively.<br>\n**Space Complexity:** `O(n + m)` for the merged string.\n\n### Edge Cases\n✅ Minimum input size: both `word1` and `word2` have a length of 1.<br>\n✅ One string is longer than the other.<br>\n✅ Both strings have equal length.<br>\n✅ One string is empty.\n",
  "topicTags": [
    "String",
    "Two Pointers"
  ],
  "hints": [
    "Use two pointers, one pointer for each string. Alternately choose the character from each pointer, and move the pointer upwards."
  ],
  "default_code_templates": {
    "py": "def mergeAlternately(word1: str, word2: str) -> str:\n    # Write your code here\n    pass\n\nif __name__ == \"__main__\":\n    import sys\n    input = sys.stdin.read().strip().split(\"\\n\")\n    word1 = input[0]\n    word2 = input[1]\n    result = mergeAlternately(word1, word2)\n    print(result)\n",
    "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nstring mergeAlternately(string word1, string word2) {\n    // Write your code here\n}\n\nint main() {\n    string word1, word2;\n    cin >> word1 >> word2;\n    cout << mergeAlternately(word1, word2) << endl;\n    return 0;\n}"
  }
}
```

---

### Testcases Template:
```json
{
  "test_cases": [ // array of test case
    {
      "problem": 2, // problem id
      "input_data": "", // string format (input for stdin)
      "expected_output": "",  // string format (output for stdout)
      "is_sample": true, // this will be true
      "explanation": "", // brief  explanation of test case in string (markdown)
      "order": 1 // integer (testcase number)
    }, // more such test cases in this array
  ]
}
```

### Example Testcase JSON:
```json
{
  "test_cases": [
    {
      "problem": 2,
      "input_data": "word1 = \"abc\", word2 = \"pqr\"",
      "expected_output": "\"apbqcr\"",
      "is_sample": true,
      "explanation": "Characters from 'abc' and 'pqr' are merged alternately.",
      "order": 1
    },
    {
      "problem": 2,
      "input_data": "word1 = \"ab\", word2 = \"pqrs\"",
      "expected_output": "\"apbqrs\"",
      "is_sample": true,
      "explanation": "'ab' and 'pqrs' are merged alternately, then 'rs' from 'pqrs' is appended.",
      "order": 2
    },
    {
      "problem": 2,
      "input_data": "word1 = \"abcd\", word2 = \"pq\"",
      "expected_output": "\"apbqcd\"",
      "is_sample": true,
      "explanation": "'abcd' and 'pq' are merged alternately, then 'cd' from 'abcd' is appended.",
      "order": 3
    },
    {
      "problem": 2,
      "input_data": "word1 = \"a\", word2 = \"b\"",
      "expected_output": "\"ab\"",
      "is_sample": false,
      "explanation": "Both strings are single characters, merged directly.",
      "order": 4
    },
    {
      "problem": 2,
      "input_data": "word1 = \"abc\", word2 = \"\"",
      "expected_output": "\"abc\"",
      "is_sample": false,
      "explanation": "'word2' is empty, so 'word1' is returned as is.",
      "order": 5
    },
    {
      "problem": 2,
      "input_data": "word1 = \"\", word2 = \"xyz\"",
      "expected_output": "\"xyz\"",
      "is_sample": false,
      "explanation": "'word1' is empty, so 'word2' is returned as is.",
      "order": 6
    },
    {
      "problem": 2,
      "input_data": "word1 = \"a\", word2 = \"xyz\"",
      "expected_output": "\"axyz\"",
      "is_sample": false,
      "explanation": "'a' and 'xyz' are merged alternately, then remaining 'xyz' is appended.",
      "order": 7
    },
    {
      "problem": 2,
      "input_data": "word1 = \"abcd\", word2 = \"efgh\"",
      "expected_output": "\"aebfcgdh\"",
      "is_sample": false,
      "explanation": "Both strings have equal length and are merged alternately.",
      "order": 8
    }
  ]
}
```
