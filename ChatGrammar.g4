grammar ChatGrammar;

program: expression;

expression:  
    verbs index_number  
    | verbs objects (location)? (time)? (query)?                           
    | TITLE_STRING; 

time: start_time end_time? (today | date) | today | date | duration;

date: INT '/' INT '/' INT ;

today: 'today';

query: ('sunny' | 'cloudy' | 'rainy' | 'windy' | 'snowy' | 'clear' | 'foggy');

start_time: INT ':' INT;

end_time: INT ':' INT;

duration: INT;

index_number: INT;

objects: STRING;

verbs: ('set' | 
        'show' | 'check'| 'tell' | 
        'start' | 'reset' | 
        'complete' | 'finish' | 'done' |
        'incomplete' | 'unfinished' | 'undo');

location: STRING+;

TITLE_STRING: '"' (~[\r\n])* '"';

STRING: [a-zA-Z]+;  

INT: [0-9]+;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines