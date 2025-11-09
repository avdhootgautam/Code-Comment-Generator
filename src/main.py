from crew import CodeCommentCrew
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
def run():
    """
    Run the comment adder crew
    """
    inputs={
        'requirements':requirements,
        'code':'''
        from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler,MaxAbsScaler
        def preprocessing_scaling(df,set_of_standard_scaling_column,set_of_min_max_scaling_column,set_of_robust_scaling_columns,set_of_max_absolute_scaling_columns):
            #Now i will make the object of all the scaling features
                standard_scaler=StandardScaler()
                min_max_scaler=MinMaxScaler()
                robust_scaler=RobustScaler()
                max_abs_scaler=MaxAbsScaler()
                if set_of_standard_scaling_column:
                    df[list(set_of_standard_scaling_column)]=standard_scaler.fit_transform(df[list(set_of_standard_scaling_column)])
                if set_of_min_max_scaling_column:
                    df[list(set_of_min_max_scaling_column)]=standard_scaler.fit_transform(df[list(set_of_min_max_scaling_column)])
                if set_of_robust_scaling_columns:
                    df[list(set_of_robust_scaling_columns)]=standard_scaler.fit_transform(df[list(set_of_robust_scaling_columns)])
                if set_of_max_absolute_scaling_columns:
                    df[list(set_of_max_absolute_scaling_columns)]=standard_scaler.fit_transform(df[list(set_of_max_absolute_scaling_columns)])

                return df
        '''
    }

    #Create and run the crew
    result=CodeCommentCrew().crew().kickoff(inputs=inputs)
    print(f"This is the result::{result}")

if __name__=="__main__":
    print(f"In a run")
    run()
