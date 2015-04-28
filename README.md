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

## installation ##

1. copy plugin `check_bacula_log.pl` as `/usr/lib/nagios/plugins/check_bacula_log`
2. copy command definition and service template definition `check_bacula_log.cfg`  to `/etc/nagios/plugins`.
3. create check definition like this:
```
define service {
    use                     bacula_log
    host_name               localhost
}       
```

**NOTE**: the paths may vary, depending on your Nagios/Icinga installation.
