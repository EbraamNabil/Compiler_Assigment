import re

# Define token types
TOKEN_TYPES = {
    'COMMENT': r'//.*|/\*[\s\S]*?\*/',  # Single-line or multi-line comments
    'KEYWORD': r'\b(if|else|while|for|break|continue|return|def|class|import|from|as|try|except|with|lambda|async|await|global|nonlocal|pass|raise|True|False|None)\b',  # Keywords
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',  # Identifiers (variables)
    'NUMBER': r'\b\d+(\.\d+)?\b',  # Numbers (integer and float)
    'STRING': r'"([^"\\]*(\\.[^"\\]*)*)"|\'([^\'\\]*(\\.[^\'\\]*)*)\'',  # Strings
    'CHARACTER': r"'([^'\\]*(\\.[^'\\]*)*)'",  # Characters
    'OPERATOR': r'[\+\-\*/=<>!&|]+',  # Operators
    'PUNCTUATION': r'[(){}[\];,]',  # Punctuation
    'WHITESPACE': r'\s+',  # Whitespace
}

# Combine all patterns into one regex
TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES.items())

def tokenize(code):
    tokens = []
    for line in code.splitlines():
        line = line.strip()  
        if not line:  # Skip empty lines
            continue
        for match in re.finditer(TOKEN_REGEX, line):
            token_type = match.lastgroup
            token_value = match.group(token_type)
            # Avoid adding whitespace
            if token_type != 'WHITESPACE':
                tokens.append((token_type, token_value))
    return tokens

# Run the program
if __name__ == '__main__':
   
    code_input = input("Enter your code: ")
    tokens = tokenize(code_input)
    
    
    for token_type, token_value in tokens:
        print(f'Token type: {token_type}, value: {token_value}')
