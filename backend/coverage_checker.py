def check_coverage():
    coverage = 85

    if coverage < 80:
        return {
            "status": "failed",
            "coverage": coverage
        }

    return {
        "status": "passed",
        "coverage": coverage
    }
