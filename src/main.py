requirements = """
The system should implement an AI-powered code-commenting and backend-design generator called "comment_adder".

The primary purpose of the system is to accept raw source code and/or high-level project requirements and automatically generate:
    - Clean, contextual, and language-appropriate inline comments throughout the code.
    - A detailed backend design document suitable for implementation by a backend developer

The system should be capable of:
    - Understanding code across multiple languages including (but not limited to) Python, JavaScript,
      Java, C++, Go, and TypeScript.
    - Adding different comment styles such as brief comments, detailed comments, docstring-level explanations,
      and TODO-style suggestions based on the user’s selection.
    - Detecting logical errors, missing validations, potential security issues, and architectural inconsistencies,
      then reflecting them in comments where appropriate.
    - Reading high-level requirements and converting them into a complete design specification containing:
        * API endpoints with request/response schemas.
        * Database schema and table structures.
        * Flow diagrams (text-based).
        * Authentication and authorization rules.
        * Error handling and edge-case definitions.
        * Implementation checklist with priorities.

The system must support multiple output formats:
    - Inline commented code.
    - Annotated full code copy.
    - Detailed backend design document.
    - A combined output including comments, design, explanations, and developer task lists.

The system must validate user input and must gracefully handle:
    - Missing language specifiers.
    - Large code blocks.
    - Requirements with ambiguous statements.

Non-functional expectations:
    - Outputs must be deterministic and readable.
    - Comments should follow the conventional style of the detected language.
    - The system should remain performant even for large files by chunking code intelligently.
"""