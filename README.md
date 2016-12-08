# ipa_check_consistency
The script checks consistency across FreeIPA servers.

It can now be used as a Nagios/Opsview plug-in (check -n, -w and -c  options).

Please note, it has only been tested in FreeIPA 4.2 (Centos 7.2) environment.

Requirements:
* FreeIPA 4.2 or higher
* Bash 4.0 or higher

Any comments and improvement ideas are welcome.

## Usage
```
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
    all     - all checks (-w and -c only relevant if -na used), default if incorrect value is passed
    users   - Active Users
    ustage  - Stage Users
    upres   - Preserved Users
    ugroups - User Groups
    hosts   - Hosts
    hgroups - Host Groups
    hbac    - HBAC Rules
    sudo    - SUDO Rules
    zones   - DNS Zones
    ldap    - LDAP Conflicts
    bind    - Anonymous BIND
-w  Warning threshold (0-11), number of failed checks before alerting (default: 1)
-c  Critical threshold (0-11), number of failed checks before alerting (default: 2)
-h  Print this help summary page
```

## Example
```
$ ./ipa_check_consistency -H "shdc01 shdc02 ashb01 ashb02 frem01 vadmz01" -d ipa.wandisco.com -W '********'
FreeIPA servers:    shdc01     shdc02     ashb01     ashb02     frem01     vadmz01    STATE
===========================================================================================
Active Users        169        169        169        169        169        169        OK
Stage Users         0          0          0          0          0          0          OK
Preserved Users     0          0          0          0          0          0          OK
User Groups         50         50         50         50         50         50         OK
Hosts               22         22         22         22         22         22         OK
Host Groups         2          2          2          2          2          2          OK
HBAC Rules          3          3          3          3          3          3          OK
SUDO Rules          2          2          2          2          2          2          OK
DNS Zones           46         46         46         46         46         46         OK
LDAP Conflicts      NO         NO         NO         NO         NO         NO         OK
Anonymous BIND      on         on         on         on         on         on         OK
Replication Status  shdc02 0   ashb01 0   shdc02 0   shdc02 0   shdc02 -1  ashb02 0
                               ashb02 0              vadmz01 0
                               frem01 0
                               shdc01 0
===========================================================================================
```

## Nagios/Opsview plug-in mode
```
$ ./ipa_check_consistency -H "shdc01 shdc02 ashb01 ashb02 frem01" -d ipa.wandisco.com -W '********' -n all
OK - 11/11 checks passed
$ echo $?
0
```
```
$ ./ipa_check_consistency -H "shdc01 shdc02 ashb01 ashb02 frem01" -d ipa.wandisco.com -W '********' -n users
OK - Active User consistency
$ echo $?
0
```
