# ipa_check_consistency
The script checks consistency across FreeIPA servers.

Please note, it's been only tested in FreeIPA 4.2 (Centos 7.2) environment.

Any comments and/or improvement ideas are welcome.

## Usage
```
$ ./ipa_check_consistency -h
ipa_check_consistency version 16.2.2
Usage: ipa_check_consistency [OPTIONS]
AVAILABLE OPTIONS:
-H  List of hosts (e.g. "server1 server2 server3")
-d  IPA domain (e.g. "ipa.domain.com")
-s  LDAP root suffix, if not domain based (default: "dc=ipa,dc=domain,dc=com")
-D  BIND DN (default: cn=Directory Manager)
-W  BIND password (prompt for one if not supplied)
-p  Password file (default: ipa_check_consistency.passwd)
-h  Print this help summary page
-v  Print version number
```

## Example
```
$ ./ipa_check_consistency -d ipa.wandisco.com -H "shdc01 shdc02 ashb01 ashb02 frem01"
Directory Manager password:

FreeIPA servers:    shdc01     shdc02     ashb01     ashb02     frem01     Consistent?
======================================================================================
Users               224        224        224        224        224        YES
Groups              50         50         50         50         50         YES
Hosts               6          6          6          6          6          YES
Hostgroups          1          1          1          1          1          YES
HBAC rules          1          1          1          1          1          YES
SUDO rules          1          1          1          1          1          YES
LDAP conflicts      NO         NO         NO         NO         NO         YES
Anonymous BIND      rootdse    rootdse    rootdse    rootdse    rootdse    YES
Replication status  ashb01 0   ashb02 0   ashb02 0   ashb01 0   ashb01 0
                    frem01 0   shdc01 0   frem01 0   shdc02 0   shdc01 0
                    shdc02 0              shdc01 0
======================================================================================
```
