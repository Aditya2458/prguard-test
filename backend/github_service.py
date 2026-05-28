from ai_reviewer import review_code
from coverage_checker import check_coverage

def process_pull_request(payload):
    pr = payload.get("pull_request", {})

    title = pr.get("title")
    author = pr.get("user", {}).get("login")

    print(f"Processing PR: {title}")
    print(f"Author: {author}")

    ai_result = review_code("sample diff")
    coverage_result = check_coverage()

    print(ai_result)
    print(coverage_result)
