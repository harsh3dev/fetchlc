import streamlit as st
import pandas as pd
import requests
import json
import time
import logging

API_URL = "https://alfa-leetcode-api.onrender.com/select?titleSlug={}"
RATE_LIMIT_DELAY = 61  # 61 seconds to avoid rate limit
MAX_REQUESTS_PER_HOUR = 60

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cache to avoid redundant requests within the same session
cache = {}

def fetch_problem_data(slug):
    if slug in cache:
        logging.info(f"🔁 Using cached data for slug: {slug}")
        return cache[slug]

    try:
        logging.info(f"🌐 Fetching data for slug: {slug}")
        response = requests.get(API_URL.format(slug), timeout=10)
        if response.status_code == 200:
            data = response.json()
            cache[slug] = data
            logging.info(f"✅ Successfully fetched data for slug: {slug}")
            return data
        elif response.status_code == 429:
            logging.warning(f"🚨 Rate limit hit for slug '{slug}', backing off...")
            return None
        else:
            logging.error(f"❌ Failed to fetch data for slug '{slug}': {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"❌ Error fetching data for slug '{slug}': {e}")
        return None

def process_csv(file):
    df = pd.read_csv(file)
    problems = []
    processed_slugs = set()
    request_count = 0

    for index, row in df.iterrows():
        slug = row['Slug']
        company = row['Company']
        acceptance_rate = row['Acceptance Rate']

        if slug in processed_slugs:
            logging.info(f"🔁 Skipping duplicate for slug: {slug}")
            data = cache.get(slug)
            if data and company not in data.get('topicTags', []):
                data['topicTags'].insert(0, company)
            continue

        if request_count >= MAX_REQUESTS_PER_HOUR:
            logging.warning("🚨 API rate limit reached. Stopping further requests.")
            break

        data = fetch_problem_data(slug)
        if data:
            # Add company name to topicTags
            if company not in data.get('topicTags', []):
                data['topicTags'] = [company] + [tag['name'] for tag in data.get('topicTags', [])]

            processed_slugs.add(slug)
            request_count += 1

            problem = {
                "title": data.get("questionTitle", ""),
                "slug": slug,
                "description": data.get("question", ""),
                "difficulty": data.get("difficulty", "")[0].upper(),
                "time_limit": 1000,
                "memory_limit": 256,
                "likes": 0,
                "dislikes": 0,
                "is_premium": False,
                "acceptance_rate": acceptance_rate,
                "related_problems": [],
                "solution": "",
                "topicTags": data.get("topicTags", []),
                "hints": data.get("hints", []) or [""],
                "default_code_templates": {
                    "py": "",
                    "cpp": ""
                }
            }

            problems.append(problem)
            logging.info(f"✅ Processed problem: {slug}")

            # Respect rate limit
            if request_count < MAX_REQUESTS_PER_HOUR:
                logging.info(f"⏳ Waiting for {RATE_LIMIT_DELAY} seconds before next request...")
                time.sleep(RATE_LIMIT_DELAY)

    return problems

def fetch_single_problem(slug):
    data = fetch_problem_data(slug)
    if data:
        problem = {
            "title": data.get("questionTitle", ""),
            "slug": slug,
            "description": data.get("question", ""),
            "difficulty": data.get("difficulty", "")[0].upper(),
            "time_limit": 1000,
            "memory_limit": 256,
            "likes": 0,
            "dislikes": 0,
            "is_premium": False,
            "acceptance_rate": "",
            "related_problems": [],
            "solution": "",
            "topicTags": data.get("topicTags", []),
            "hints": data.get("hints", []) or [""],
            "default_code_templates": {
                "py": "",
                "cpp": ""
            }
        }
        return problem
    return None

def main():
    st.title("LeetCode Problem Processor")

    # Single problem fetching option
    st.header("📌 Fetch Single Problem")
    slug = st.text_input("Enter Problem Slug")
    if st.button("Fetch Problem"):
        if slug:
            st.info("Fetching problem data...")
            problem = fetch_single_problem(slug)
            if problem:
                st.success("✅ Problem fetched successfully!")
                json_output = json.dumps(problem, indent=4)
                st.json(problem)  # Display JSON in readable format
                st.download_button("Download JSON", json_output, f"{slug}.json", "application/json")
            else:
                st.error("❌ Failed to fetch problem data.")
        else:
            st.warning("⚠️ Please enter a valid slug.")

    st.markdown("---")

    # CSV Processing Option
    st.header("📥 Process CSV File")
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        st.info("Processing file...")
        problems = process_csv(uploaded_file)

        if problems:
            st.success(f"✅ Processed {len(problems)} problems!")
            json_output = json.dumps(problems, indent=4)
            st.json(problems)  # Display JSON in readable format
            st.download_button("Download JSON", json_output, "problems.json", "application/json")

if __name__ == "__main__":
    main()
