#!/bin/bash

. ./unimelb-comp90024-2020-grp-31-openrc.sh; ansible-playbook -i hosts --ask-become-pass ansible_script.yaml
