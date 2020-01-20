###### 1、403 (ACCESS_REFUSED)
Queue names starting with "amq." are reserved for internal use by the broker. 
Attempts to declare a queue with a name that violates this rule 
will result in a channel-level exception with reply code `403 (ACCESS_REFUSED)`.

###### 2、406 (PRECONDITION_FAILED)
Before a queue can be used it has to be declared. 
Declaring a queue will cause it to be created if it does not already exist.  
The declaration will have no effect if the queue does already exist and 
its attributes are the same as those in the declaration.  
When the existing queue attributes are not the same as those in the declaration 
a channel-level exception with code 
`406 (PRECONDITION_FAILED)` will be raised.

###### 3、RESOURCE_LOCKED
An exclusive queue can only be used (consumed from, purged, deleted, etc) by its declaring connection.  
An attempt to use an exclusive queue from a different connection will 
result in a channel-level exception `RESOURCE_LOCKED` with an error message  
that says `cannot obtain exclusive access to locked queue`.







