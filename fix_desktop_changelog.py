with open("docs/desktop-changelog.md", "r") as f:
    text = f.read()

# Let's fix ALL files backticks safely, because I just saw the review said "The agent's processing script appears to have used a naive string replacement to add language tags to code blocks"
