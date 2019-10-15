Role Name
=========

Easy-install for tinc vpn and tinc-boot.

Requirements
------------

* tar + gzip: for binary installation

Role Variables
--------------


| Variable | Default value | Description |
| -------- | ------------- | ----------- |
| tinc_boot_network |  dnet |  network name (also interface name) |
| tinc_boot_tinc_dir |  /etc/tinc |  location for configuration files (do not change if not sure) |
| tinc_boot_bin_dir |  /usr/local/bin/ |  installation directory for the binary |
| tinc_boot_port |  0 |  port for connections (tinc-boot will check availability; 0 means random) |
| tinc_boot_name |  "{{ansible_hostname}}" |  node name |
| tinc_boot_mask |  16 |  routing IP mask (do not change if not sure) |
| tinc_boot_prefix |  172.173 |  IP address prefix (should be same in mask) |
| tinc_boot_public |  [] |  public node addresses |
| tinc_boot_services |  yes |  enable tinc service? |
| tinc_boot_entry_group |  '' |  entry nodes - ansible inventory roles that can be used as point of key distribution |
| tinc_boot_bootnode |  no |  setup node as a boot node |
| tinc_boot_binding |  "0.0.0.0:8655" |  bootnode bindin address |
| tinc_boot_token |  "{{lookup('password', '/dev/null chars=ascii_letters,digits')}}" |  bootnode token |
| tinc_boot_tls_key |  '' |   (optional) bootnode TLS path to key on local host |
| tinc_boot_tlscert |  '' |   (optional) bootnode TLS path to certificate on local host |
| tinc_boot_certs_location |  "/etc/ssl/certs/tinc-boot/{{tinc_boot_network}}" |  location to store TLS files on host |

* `tinc_boot_network`, `tinc_boot_name` should contains only alphanumeric letters in lowercase.
* To enable TLS for bootnode in addition to flag `tinc_boot_bootnode=yes`, `tinc_boot_tls_key` AND `tinc_boot_tls_cert` should be defined as pathes to local files. Files will be copied to `tinc_boot_certs_location`
* If `tinc_boot_entry_group` defined Ansible will make keys exchange with all hosts in the group and rely on hostvars `tinc_boot_tinc_dir` (default: `/etc/tinc`) and `tinc_boot_network` (default: role `tinc_boot_network`).


Example Playbook
----------------

Public node:

    - hosts: servers
      roles:
         - tinc_boot
      vars:
        tinc_boot_public:
          - 11.22.33.44
          - 55.66.77.88

Private node:

    - hosts: servers
      roles:
         - tinc_boot

Join to existent network (role - 'tinc'):

    - hosts: servers
      roles:
         - tinc_boot       
      vars:
        tinc_boot_entry_group: tinc

License
-------

MPL-2.0

Author Information
------------------

Made by author of tinc-boot itself