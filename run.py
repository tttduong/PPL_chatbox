# python run.py
import sys, os
import subprocess
from antlr4 import *

ANTLR_JAR = 'antlr/antlr4-4.9.2-complete.jar'
CPL_Dest = 'CompiledFiles'
SRC = 'ChatGrammar.g4'

def printUsage():
    print('python run.py gen')  
    print('python run.py test')  

def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-visitor', '-Dlanguage=Python3', SRC])
    print('Generate successfully')

def pre_processing(string):
    from functools import reduce

    def compose(*func):
        def h(args):
            return reduce(lambda x,y: y(x), reversed(func), args)
        return h
    
    punctuation = ['.', ',', '?', '!', ':', ';', '\'', '\"', '(', ')', '_', '-', '[', ']' ]
    redundant_words = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will', 'with', 'me' , 'I', 'he', 'she', 'it', 'we', 'them' , 'us', 'week']

    def removed_punctuation(string_x):
        removed_punctuation = list(filter(lambda x: '' if x in punctuation else x, string_x))
        removed_punctuation = "".join(removed_punctuation)
        return removed_punctuation

    def split_words(string_x):
        return list(map(lambda x: x, string_x.split()))
    
    def converted_lowercase(list_x):
        week_date = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        converted_lowercase = list(map(lambda x: x.lower() if x not in week_date else x ,list_x))
        return converted_lowercase

    def filter_redundant_words(list_x):
            filter_stop_words = list(filter(lambda x: '' if x in redundant_words else x, list_x))
            return " ".join(filter_stop_words)
    
    proc_pipeline = compose(filter_redundant_words, converted_lowercase, split_words,  removed_punctuation)
    return proc_pipeline(string)


def test_input():
    from CompiledFiles.ChatGrammarLexer import ChatGrammarLexer
    from CompiledFiles.ChatGrammarParser import ChatGrammarParser
    from antlr4.error.ErrorListener import ErrorListener
    from ExtractorVisitor import ExtractorVisitor
    
    # input = 'show me the meeting on 20/12/2025'
    # input = 'show weather Thanh pho Ho Chi Minh'  -- hiện chỉ test calendar thoi nha
    # set meeting 06:00 07:00 18/11/2025
    # input = 'set meeting at 3:00 pm on 30/12/2024'
    input = 'complete 1'
    pre_processed = pre_processing(input)
    print(pre_processed)
    input_stream = InputStream(pre_processed)
    lexer = ChatGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ChatGrammarParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))
    visitor = ExtractorVisitor()
    elements = visitor.visit(tree)
    print(elements)

def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()
    elif argv[0] == 'test':
        test_input()
    else: 
        printUsage()   

if __name__ == '__main__':
    main(sys.argv[1:]) 