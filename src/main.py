requirements= """
    The system should implement an AI-powered code-commenting agent called "comment_adder".
    The core purpose of the system is to:
    - Accept raw source code in any programming language.
    - Add clear, contextual, and language-appropriate inline comments.
    - Ensure that the original code is NEVER modified, rewritten, or refactored.

  The agent must:
    - Understand and comment multiple languages including Python, JavaScript, Java, C++, Go, and TypeScript.
    - Detect logic flow, control structures, variables, and functions to produce accurate comments.
    - Follow the correct commenting style for the detected language (//, #, /* */, etc.).
    - Add:
        * Brief comments for simple lines
        * Block comments for important logic
        * TODO notes where improvements or validations may be required
    - Identify potential issues such as:
        * Missing validation checks
        * Unclear logic
        * Error-prone patterns
        * Edge cases not covered
      and explain them only using comments inside the code.

  The system must NOT:
    - Produce any backend design documentation.
    - Modify or rewrite the original code.
    - Change formatting, indentation, or structure.
    - Generate extra files or summaries.

  Input handling requirements:
    - Must work even when programming language is not explicitly mentioned.
    - Must handle large code blocks by intelligently chunking internally.
    - Must gracefully handle incomplete, broken, or ambiguous input.

  Non-functional expectations:
    - Output must be deterministic and clean.
    - Comments must increase readability, not clutter the code.
    - The agent must return ONLY the commented version of the code.
"""
