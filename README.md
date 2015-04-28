# check_bacula_log

Nagios/Icinga plugin that checks Bacula logs for last status run.

`check_bacula_log` is a Nagios plugin that checks whether the backups made for today
with the Bacula backup system were succesful. 

This requires the Nagios user to have read access to the bacula log file. 

Make sure that the user that runs Nagios has read access to the Bacula logs,
make sure it also has the right to enter the directory where the log is stored. 

Requirements: 
- Nagios or Icinga
- Perl
