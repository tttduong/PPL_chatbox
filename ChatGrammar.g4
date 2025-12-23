grammar ChatGrammar;

program: expression;

expression:  
    verbs index_number  
    | verbs status_filter? objects (location)? (time)? (query)?                           
    | TITLE_STRING; 

time: start_time end_time? (today | date) | today | date | duration;

date: INT '/' INT '/' INT ;

today: 'today';

// Weather queries
query: ('sunny' | 'cloudy' | 'rainy' | 'windy' | 'snowy' | 'clear' | 'foggy');

// Status filter for tasks (separate from verbs)
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

location: STRING+;

TITLE_STRING: '"' (~[\r\n])* '"';

STRING: [a-zA-Z]+;  

INT: [0-9]+;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines