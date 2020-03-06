# Run the role/playbook with ansible-playbook
ansible-playbook test.yml -i inventory

# Run the role/playbook again, checking to make sure it is idempotent
ansible-playbook test.yml -i inventory | tee ansible_test.output

result=0

if grep -q "centos7\s*:\s*ok=19\s*changed=0\s*unreachable=0\s*failed=0" ansible_test.output; then
	echo "[centos7] Idempotence test: pass"
else
	echo "[centos7] Idempotence test: fail"
	result=100
fi

if grep -q "debian8\s*:\s*ok=17\s*changed=0\s*unreachable=0\s*failed=0" ansible_test.output; then
	echo "[debian8] Idempotence test: pass"
else
	echo "[debian8] Idempotence test: fail"
	result=100
fi

# Stop docker images
ansible-playbook test.yml -i inventory -e "docker_dynamic_inventory_provisioner_stop=True" -l "localhost"

exit $result
