# ipa_check_consistency
The script checks consistency across FreeIPA servers.

It can now be used as a Nagios/Opsview plug-in (check -n, -w and -c  options).

Please note, it's been only tested in FreeIPA 4.2 (Centos 7.2) environment.

Any comments and improvement ideas are welcome.

## Usage
```
ipa_check_consistency version 16.2.12
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
-w  Warning threshold (0-10), number of failed checks before alerting (default: 1)
-c  Critical threshold (0-10), number of failed checks before alerting (default: 2)
-h  Print this help summary page
-v  Print version number
```

## Example
```
$ ./ipa_check_consistency -H "shdc01 shdc02 ashb01 ashb02 frem01" -d ipa.wandisco.com
Directory Manager password:
FreeIPA servers:    shdc01    shdc02    ashb01    ashb02    frem01    STATE
===========================================================================
Active users        223       223       223       223       223       OK
Stage users         0         0         0         0         0         OK
Preserved users     0         0         0         0         0         OK
Groups              50        49        50        49        50        FAIL
Hosts               6         6         6         6         6         OK
Hostgroups          1         1         1         1         1         OK
HBAC rules          3         3         3         3         3         OK
SUDO rules          2         2         2         2         2         OK
LDAP conflicts      NO        NO        NO        NO        NO        OK
Anonymous BIND      on        on        on        on        on        OK
Replication status  ashb01 0  ashb02 0  ashb02 -1 ashb01 -1 ashb01 -1
                    frem01 0  shdc01 0  frem01 0  shdc02 -1 shdc01 -1
                    shdc02 0            shdc01 -1
===========================================================================
```

## Nagios/Opsview plug-in mode
```
$ ./ipa_check_consistency -H "shdc01 shdc02 ashb01 ashb02 frem01" -d ipa.wandisco.com -W '********' -n
OK - 10/10 checks passed
$ echo $?
0
```
