grammar ChatGrammar;

program: expression;

expression:  
    verbs index_number  
    | verbs status_filter? objects (time)?                         
    | TITLE_STRING; 

time: start_time end_time? (today | date) | today | date | duration;

date: INT '/' INT '/' INT ;

today: 'today';

// Status filter for tasks 
status_filter: 'incompleted' | 'completed' | 'pending' | 'done';

start_time: INT ':' INT;

end_time: INT ':' INT;

duration: INT;

index_number: INT;

objects: STRING;

verbs: ('set' | 
        'show' | 'check'| 'tell' | 
        'start' | 'reset' | 
        'complete' | 'finish' | 
        'undo' | 'unfinish' |
        'delete' | 'remove' | 'cancel');


TITLE_STRING: '"' (~[\r\n])* '"';

STRING: [a-zA-Z]+;  

INT: [0-9]+;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines