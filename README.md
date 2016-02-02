# ipa_check_consistency

The script checks consistency across FreeIPA servers.

Put bind password into ipa_check_consistency.passwd file to stop password prompts.

Please note, it's been only tested in FreeIPA 4.2 (Centos 7.2) environment.

Any comments and/or improvement ideas are welcome.

Sample output:
```
FreeIPA servers:    shdc01     shdc02     ashb01     ashb02     frem01     Consistent?
======================================================================================
Users               224        224        224        224        224        YES
Groups              50         50         50         50         50         YES
Hosts               6          6          6          6          6          YES
Hostgroups          1          1          1          1          1          YES
HBAC rules          1          1          1          1          1          YES
SUDO rules          1          1          1          1          1          YES
LDAP conflicts      NO         NO         NO         NO         NO         YES
Anonymous bind      rootdse    rootdse    rootdse    rootdse    rootdse    YES
Replication status  ashb01 0   ashb02 0   ashb02 0   ashb01 0   ashb01 0
                    frem01 0   shdc01 0   frem01 0   shdc02 0   shdc01 0
                    shdc02 0              shdc01 0
======================================================================================
```
