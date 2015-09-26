<?php 

define("HOST", "localhost"); // The host you want to connect to.
define("USER", "second_user"); // The database username.
define("PASSWORD", "V0!.]7RA[eVb"); // The database password. 
define("DATABASE", "mysignoff_db"); // The database name.
 
$mysqli = new mysqli(HOST, USER, PASSWORD, DATABASE);
// If you are connecting via TCP/IP rather than a UNIX socket remember to add the port number as a parameter.

;?>