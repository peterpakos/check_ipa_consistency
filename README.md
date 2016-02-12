# ipa_check_consistency
The script checks consistency across FreeIPA servers.

It can now be used as a Nagios/Opsview plug-in (check -n, -w and -c  options).

Please note, it's been only tested in FreeIPA 4.2 (Centos 7.2) environment.

Any comments and improvement ideas are welcome.

## Usage
```
ipa_check_consistency version 16.2.12a
Usage: ipa_check_consistency [OPTIONS]
AVAILABLE OPTIONS:
-H  List of IPA servers (e.g.: "server1 server2.domain server3")
    Both short names and FQDNs are supported (FQDN if not within IPA domain)
-d  IPA domain (e.g.: "ipa.domain.com")
-s  LDAP root suffix, if not domain based (default: "dc=ipa,dc=domain,dc=com")
-D  BIND DN (default: cn=Directory Manager)
-W  BIND password (prompt for one if not supplied)
-p  Password file (default: ipa_check_consistency.passwd)
-n  Nagios plugin mode
-w  Warning threshold (0-11), number of failed checks before alerting (default: 1)
-c  Critical threshold (0-11), number of failed checks before alerting (default: 2)
-h  Print this help summary page
-v  Print version number
```

## Example
```
FreeIPA servers:    shdc01    shdc02    ashb01    ashb02    frem01    STATE
===========================================================================
Active Users        223       223       223       223       223       OK
Stage Users         1         1         1         1         1         OK
Preserved Users     0         0         0         0         0         OK
User Groups         50        50        50        50        50        OK
Hosts               6         6         6         6         6         OK
Host Groups         1         1         1         1         1         OK
HBAC Rules          2         2         2         2         2         OK
SUDO Rules          2         2         2         2         2         OK
DNS Zones           4         4         4         4         4         OK
LDAP Conflicts      NO        NO        NO        NO        NO        OK
Anonymous BIND      on        on        on        on        on        OK
Replication Status  ashb01 0  ashb02 0  ashb02 0  ashb01 0  ashb01 -1
                    frem01 0  shdc01 0  frem01 0  shdc02 -1 shdc01 -1
                    shdc02 0            shdc01 -1
===========================================================================
```

## Nagios/Opsview plug-in mode
```
$ ./ipa_check_consistency -H "shdc01 shdc02 ashb01 ashb02 frem01" -d ipa.wandisco.com -W '********' -n
OK - 11/11 checks passed
$ echo $?
0
```
