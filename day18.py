#Day 18 - Pull Request Practice 
# This file was added via a Pull Request on GitHub demonstrating the professional engineering workflow of branching, committing, pushing, and creating a pull request for code review and merging.

def pr_summary():
    steps = [
        "1. Create a feature branch.",
        "2. Make your changes.",
        "3. Commit and push the branch.",
        "4. Open a Pull Request on GitHub.",
        "5. Review the diff.",
        "6. Merge the PR.",
        "7. Delete the branch.",
        "8. Pull changes locally."
    ]
    print ("=" * 40)
    print ("   PULL REQUEST WORKFLOW   ")
    print ("=" * 40)
    for step in steps: 
        print (f"{step}")
    print("=" * 40)
pr_summary()