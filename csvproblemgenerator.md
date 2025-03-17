create a python script for the following usecase
use streamlit for the interface
The user will upload a csv file containing these fields:
Title, Frequency, Acceptance Rate. Slug, Company
the "Slug" field will contain the slug of the leetcode problem
You have to read the csv and then call the api:
https://alfa-leetcode-api.onrender.com/select?titleSlug={slug}

It will return data in the following format:
For example if we fetch:
https://alfa-leetcode-api.onrender.com/select?titleSlug=trapping-rain-water
The json response data will be:
{
"link": "https://leetcode.com/problems/trapping-rain-water",
"questionId": "42",
"questionFrontendId": "42",
"questionTitle": "Trapping Rain Water",
"titleSlug": "trapping-rain-water",
"difficulty": "Hard",
"isPaidOnly": false,
"question": "some string(html)",
"exampleTestcases": "[0,1,0,2,1,0,1,3,2,1,2,1]\n[4,2,0,3,2,5]",
"topicTags": [
{
"name": "Array",
"slug": "array",
"translatedName": null
},
{
"name": "Two Pointers",
"slug": "two-pointers",
"translatedName": null
},
{
"name": "Dynamic Programming",
"slug": "dynamic-programming",
"translatedName": null
},
{
"name": "Stack",
"slug": "stack",
"translatedName": null
},
{
"name": "Monotonic Stack",
"slug": "monotonic-stack",
"translatedName": null
}
],
"hints": [],
"solution": {
"id": "150",
"canSeeDetail": false,
"paidOnly": true,
"hasVideoSolution": false,
"paidOnlyVideo": true
},
"companyTagStats": null,
"likes": 33619,
"dislikes": 587,
"similarQuestions": "[{\"title\": \"Container With Most Water\", \"titleSlug\": \"container-with-most-water\", \"difficulty\": \"Medium\", \"translatedTitle\": null}, {\"title\": \"Product of Array Except Self\", \"titleSlug\": \"product-of-array-except-self\", \"difficulty\": \"Medium\", \"translatedTitle\": null}, {\"title\": \"Trapping Rain Water II\", \"titleSlug\": \"trapping-rain-water-ii\", \"difficulty\": \"Hard\", \"translatedTitle\": null}, {\"title\": \"Pour Water\", \"titleSlug\": \"pour-water\", \"difficulty\": \"Medium\", \"translatedTitle\": null}, {\"title\": \"Maximum Value of an Ordered Triplet II\", \"titleSlug\": \"maximum-value-of-an-ordered-triplet-ii\", \"difficulty\": \"Medium\", \"translatedTitle\": null}]"
}

Then you have to utilize this data to convert it to the following data format:

"title": "", // string
  "slug": "", // string (take from csv data)
  "description": "", // string type: html format containing problem description, input, output format, example testcases with explanation, constraints
  "difficulty": "E", // Enum type: E-> Easy, M-> Medium, H-> Hard
  "time_limit": 1000, // time limit in milliseconds (integer)
  "memory_limit": 256,
  "likes": 0, // keep this as 0
  "dislikes": 0, // keep this a 0
  "is_premium": false, // keep this as false
  "acceptance_rate": 0.0, //  (take from csv data)
  "related_problems": [], // keep it empty for now
  "solution": "", // solution  is of string type in markdown format, containing a structured solution to the problem with approach, code, complexity keep this empty
  "topicTags": ["",""], // array of strings
  "hints": [""], // array of strings
  "default_code_templates": {
    "py": "", // default starting code with function declaration and main function with stdin/stdout,
    "cpp": "", // default starting code with function declaration and main function with stdin/stdout
  }

In the output data here are some key points
keep the default_code_templates as empty string for every problem which will be added later
for topicTags refer to the API data but only take name of the topicTags and also insert one more mandatory tag which will be taken from CSV data : Company

The python script must perform these operations for all the rows of the csv and in return must provide a full json of the problems data
Use any library if it would be needed, keep in mind the api rate limits
The data structure must be 100% accurate

Ask me any follow up questions if you have before proceeding to code