TEST_PAYLOAD = [
    (
        {"repos_url": "https://api.github.com/orgs/google/repos"},
        [
            {"name": "firmata.py", "license": {"key": "apache-2.0"}},
            {"name": "traceur-compiler", "license": {"key": "apache-2.0"}},
            {"name": "cpp-netlib", "license": {"key": "mit"}}
        ],
        ["firmata.py", "traceur-compiler", "cpp-netlib"],
        ["firmata.py", "traceur-compiler"]
    )
]
