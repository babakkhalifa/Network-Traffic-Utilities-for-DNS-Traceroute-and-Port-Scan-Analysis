
---


```md
# Security Considerations

This project performs network utility and reconnaissance-style operations.

## Rules of Use

- Only scan systems you own or are explicitly authorized to test.
- Do not use this tool against public or third-party infrastructure without permission.
- Use only in controlled lab environments for learning and demonstration.

## Known Risks

- `os.system()` is used with raw user input in some functions.
- This can create command injection risk.
- Port scanning and banner grabbing may generate visible network traffic.
- Some functions may require elevated privileges depending on the operating system.

## Recommended Hardening

- Replace shell command execution with safer APIs
- Validate and sanitize all user input
- Restrict allowed host formats
- Add rate limiting
- Add structured logging
- Separate scanning logic from user interface
