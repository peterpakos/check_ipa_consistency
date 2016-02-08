# ipa_check_consistency
The script checks consistency across FreeIPA servers.

It can now be used as a Nagios/Opsview plug-in (check -n, -w and -c  options).

Please note, it's been only tested in FreeIPA 4.2 (Centos 7.2) environment.

Any comments and improvement ideas are welcome.

## Usage
```
$ ipa_check_consistency version 16.2.8
Usage: ipa_check_consistency [OPTIONS]
AVAILABLE OPTIONS:
-H  List of hosts (e.g.: "server1 server2 server3")
-d  IPA domain (e.g.: "ipa.domain.com")
-s  LDAP root suffix, if not domain based (default: "dc=ipa,dc=domain,dc=com")
-D  BIND DN (default: cn=Directory Manager)
-W  BIND password (prompt for one if not supplied)
-p  Password file (default: ipa_check_consistency.passwd)
-n  Nagios plugin mode
-w  Warning threshold (0-8), number of failed checks before alerting (default: 1)
-c  Critical threshold (0-8), number of failed checks before alerting (default: 2)
-h  Print this help summary page
-v  Print version number
```

## Example
```
$ ./ipa_check_consistency -H "shdc01 shdc02 ashb01 ashb02 frem01" -d ipa.wandisco.com
Directory Manager password:
FreeIPA servers:    shdc01    shdc02    ashb01    ashb02    frem01    STATE
===========================================================================
Users               224       224       224       224       224       OK
Groups              50        50        50        50        50        OK
Hosts               6         6         6         6         6         OK
Hostgroups          1         1         1         1         1         OK
HBAC rules          1         1         1         1         1         OK
SUDO rules          1         1         1         1         1         OK
LDAP conflicts      NO        NO        NO        NO        NO        OK
Anonymous BIND      on        on        on        on        on        OK
Replication status  ashb01 0  ashb02 0  ashb02 0  ashb01 0  ashb01 0
                    frem01 0  shdc01 0  frem01 0  shdc02 0  shdc01 0
                    shdc02 0            shdc01 0
===========================================================================
```

## Nagios/Opsview plug-in mode
```
$ ./ipa_check_consistency -H "shdc01 shdc02 ashb01 ashb02 frem01" -d ipa.wandisco.com -W '********' -n
OK - 8/8 checks passed
$ echo $?
0
```
